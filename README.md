# APLN590

- How to set up Conda environment:
```bash
mamba create -p ./myenv --file requirements.txt -y
./myenv/bin/pip install -e .
```

- How to run experiments:
```bash
export PATH=$PWD/myenv/bin:$PATH
run_cs_experiment --input_file_name Fruitfly.tsv --train_sample_size 0.8 --output_dir model1
```

- How to run a FastAPI application serving our model:
```
export PATH=$PWD/myenv/bin:$PATH
gunicorn firstmodel.app:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

- How to make requests:
```shell
$ curl -X 'GET' '0.0.0.0:80/info' -H 'accept: application/json'
"0.1.0"

$ curl -X 'POST' '0.0.0.0:80/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"text": ""}'
2.1073153083074065
```
