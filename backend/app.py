from flask import jsonify, Flask, request
from flask_cors import CORS
# from numpy.core.numeric import False_
# from transformers import TFBertModel, BertTokenizer
# import tensorflow as tf


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/get_answers', methods=['POST'])
def home():
    data = request.get_json()
    print(data)
    response = [
        {
            "title": "Đường lây, cách điều trị và dự phòng bệnh viêm phổi cấp do virus corona mới (nCoV)",
            "text": "Bệnh viêm phổi cấp do virus corona chủng mới, gọi tắt là nCoV-2019, đã được phát hiện đầu tiên tại thành phố Vũ Hán (Trung Quốc) cuối tháng 12, 2019 và đang lây lan nhanh sang các nước chung quanh và các châu lục khác"
        },
        {
            "title": "Đường lây, cách điều trị và dự phòng bệnh viêm phổi cấp do virus corona mới (nCoV)",
            "text": "Bệnh viêm phổi cấp do virus corona chủng mới, gọi tắt là nCoV-2019, đã được phát hiện đầu tiên tại thành phố Vũ Hán (Trung Quốc) cuối tháng 12, 2019 và đang lây lan nhanh sang các nước chung quanh và các châu lục khác"
        },
        {
            "title": "Đường lây, cách điều trị và dự phòng bệnh viêm phổi cấp do virus corona mới (nCoV)",
            "text": "Bệnh viêm phổi cấp do virus corona chủng mới, gọi tắt là nCoV-2019, đã được phát hiện đầu tiên tại thành phố Vũ Hán (Trung Quốc) cuối tháng 12, 2019 và đang lây lan nhanh sang các nước chung quanh và các châu lục khác"
        }
    ]

    response = jsonify(response)
    return response


# def predict(question):
#     input_ids = get_token_tensor(question)
#     attention_mask = tf.cast(input_ids > 0, dtype=tf.int32)

#     q_outputs = question_encoder(
#         input_ids=input_ids,
#         attention_mask=attention_mask,
#         training=False
#     )

#     q_pooled = q_outputs[0][:, 0, :]



# def get_token_tensor(question):
#     tokens = tokenizer.tokenize(question)
#     token_ids = tokenizer.convert_tokens_to_ids(tokens)
#     token_ids = [tokenizer.cls_token_id] + token_ids + [tokenizer.sep_token_id]
#     token_ids = token_ids[:64]
#     token_ids = token_ids + [tokenizer.pad_token_id] * (64 - len(token_ids))
#     token_ids[-1] = tokenizer.sep_token_id

#     return tf.convert_to_tensor([token_ids], dtype=tf.int32)


if __name__ == "__main__":
    # question_encoder = TFBertModel.from_pretrained("pretrained/NlpHUST/vibert4news-base-cased")
    # context_encoder = TFBertModel.from_pretrained("pretrained/NlpHUST/vibert4news-base-cased")

    # retriever = tf.train.Checkpoint(question_model=question_encoder, ctx_encoder=context_encoder)
    # ckpt = tf.train.Checkpoint(model=retriever)
    # ckpt.restore("checkpoints/ckpt-20")

    # tokenizer = BertTokenizer.from_pretrained("pretrained/NlpHUST/vibert4news-base-cased")

    app.run()