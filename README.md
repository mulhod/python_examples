# APLN590

- How to set up Conda environment:
```bash
mamba create -p ./myenv --file requirements.txt -y
./myenv/bin/pip install -e .
```

- How to run `run_experiment.py`:
```bash
myenv/bin/python run_experiment.py --input_file_name Fruitfly.tsv --train_sample_size 0.8 --output_dir 2
```
