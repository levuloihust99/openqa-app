# INSTALLATION GUIDE
## Requirements
- Python 3.8
- Node 14.17.0
- Google Cloud SDK
## Backend setup
### 1. Create virtual environment and install requirements
Go to `backend/` directory and run:
```shell
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt
```

### 2. Download model checkpoints
```shell
$ cd backend
$ mkdir checkpoints
$ cd checkpoints
$ mkdir vicovid_inbatch_batch8_query64_gradnorm3_V3
$ cd vicovid_inbatch_batch8_query64_gradnorm3_V3
$ gsutil cp gs://openqa-dpr/checkpoints/retriever/vicovid/vicovid_inbatch_batch8_query64_gradnorm3_V3/ckpt-20* .
```

### 3. Download pretrained model
```shell
$ gsutil cp -r gs://openqa-dpr/pretrained/ .
```

### 4. Download indexer
```shell
$ cd backend
$ mkdir indexer
$ gsutil cp -r gs://openqa-dpr/indexer/vicovid_inbatch_batch8_query64_gradnorm3_V3/ indexer
```

### 5. Download context source
```shell
$ cd backend
$ mkdir data
$ gsutil cp gs://openqa-dpr/data/wikipedia_split/vicovid/V3/vicovid_ctx_source.tsv
```

### 6. Run backend
```shell
$ python app.py
```

## Frontend setup
### 1. Install node modules
```shell
$ cd frontend
$ npm i
```

### 2. Run frontend
```shell
$ npm start
```

## Run app
- Open `/etc/hosts` and add the following line

    127.0.0.1   qaserver

- Open browser and go to `http://localhost:3000`
- Test app

![VNQA](https://user-images.githubusercontent.com/49064246/123550848-9aae1480-d799-11eb-9ba3-a48566efdb46.png)