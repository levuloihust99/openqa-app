from flask import jsonify, Flask, request
from flask_cors import CORS
from transformers import TFBertModel, BertTokenizer
import tensorflow as tf
from indexer import DenseFlatIndexer
import time
import glob
import pandas as pd


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/get_answers', methods=['POST'])
def home():
    data = request.get_json()
    question = data
    retrieved_docs = retrieve(question, top_docs=10)
    response = jsonify(retrieved_docs)
    return response


def predict(question):
    input_ids = get_question_tensor(question)
    attention_mask = tf.cast(input_ids > 0, dtype=tf.int32)

    q_outputs = question_encoder(
        input_ids=input_ids,
        attention_mask=attention_mask,
        training=False
    )

    q_pooled = q_outputs[0][:, 0, :]


def load_ctx_sources(ctx_source_path):
    print("Loading all documents into memory... ")
    start_time = time.perf_counter()
    all_docs_df = pd.read_csv(ctx_source_path, sep='\t', header=0)
    all_ids = all_docs_df.id.tolist()
    all_ids = ["wiki:{}".format(id) for id in all_ids]
    all_docs = dict(zip(all_ids, zip(all_docs_df.text, all_docs_df.title)))
    print("done in {}s".format(time.perf_counter() - start_time))
    print("----------------------------------------------------------------")

    return all_docs


def retrieve(input_question, top_docs):
    query_vectors = predict(input_question)

    top_ids_and_scores = indexer.search_knn(query_vectors, top_docs=top_docs)
    top_ids = top_ids_and_scores[0][0]
    retrieved_docs = [all_docs[id] for id in top_ids]
    retrieved_docs = [{
        'title': doc[1],
        'text': doc[0]
    } for doc in retrieved_docs]

    return retrieved_docs


def get_question_tensor(question):
    tokens = tokenizer.tokenize(question)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    token_ids = [tokenizer.cls_token_id] + token_ids + [tokenizer.sep_token_id]
    token_ids = token_ids[:64]
    token_ids = token_ids + [tokenizer.pad_token_id] * (64 - len(token_ids))
    token_ids[-1] = tokenizer.sep_token_id

    return tf.convert_to_tensor([token_ids], dtype=tf.int32)


if __name__ == "__main__":
    print("Loading encoder...")
    question_encoder = TFBertModel.from_pretrained("pretrained/NlpHUST/vibert4news-base-cased")
    context_encoder = TFBertModel.from_pretrained("pretrained/NlpHUST/vibert4news-base-cased")

    retriever = tf.train.Checkpoint(question_model=question_encoder, ctx_encoder=context_encoder)
    ckpt = tf.train.Checkpoint(model=retriever)
    ckpt.restore("checkpoints/ckpt-20")

    tokenizer = BertTokenizer.from_pretrained("pretrained/NlpHUST/vibert4news-base-cased")
    all_docs  = load_ctx_sources(ctx_source_path="data/vicovid_ctx_sources.tsv")

    index_path = "indexer/vicovid_inbatch_batch8_query64_gradnorm3"
    indexer = DenseFlatIndexer(buffer_size=50000)
    print("Deserializing indexer from disk... ")
    indexer.deserialize(index_path)

    app.run()