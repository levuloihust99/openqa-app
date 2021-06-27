SRC_PATH=`dirname $(pwd)/$0`
echo $SRC_PATH
docker run -d \
    --mount type=bind,src="$SRC_PATH/backend/pretrained",dst=/home/app/pretrained \
    --mount type=bind,src="$SRC_PATH/backend/indexer",dst=/home/app/indexer \
    --mount type=bind,src="$SRC_PATH/backend/data",dst=/home/app/data \
    --mount type=bind,src="$SRC_PATH/backend/checkpoints",dst=/home/app/checkpoints \
    --name backend backend