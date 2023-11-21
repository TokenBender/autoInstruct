
# Project Documentation

## Overview
This project includes scripts for data formatting and conversion between different file formats. The main script, `autoFormatter.py`, processes JSONL or JSON files based on user-specified parameters. Additionally, the `parquet_to_json.py` script supports converting data between JSONL and Parquet formats.

## Installation
To use these scripts, you need to have Python installed on your system along with a few dependencies.

1. Clone this repository.
2. Navigate to the repository directory.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### autoFormatter.py
This is the primary script for processing JSONL or JSON files. It takes several command-line arguments for input and output file specifications, processing options, and conversion settings.

#### Extended Command Example
```
python autoFormatter.py datasets/Evol-Instruction-66k-modified.json datasets/Evol-Instruction-66k-chatml.jsonl instruction output --format chatml --split_ratio 0.9 --to_parquet true
```
- `datasets/Evol-Instruction-66k-modified.json`: The input JSON file.
- `datasets/Evol-Instruction-66k-chatml.jsonl`: The output JSONL file.
- `instruction`: Name of the instruction column in the input file.
- `output`: Name of the response column in the input file.
- `--format chatml`: Specifies the format for the output file.
- `--split_ratio 0.9`: Determines the ratio for splitting the dataset.
- `--to_parquet true`: Converts the output to Parquet format if set to true.

### parquet_to_json.py
This script converts data between JSONL and Parquet formats.

#### Commands
- To convert JSONL to Parquet:
  ```
  python parquet_to_json.py jsonl_to_parquet <jsonl_file> <parquet_file>
  ```
- To convert Parquet to JSONL:
  ```
  python parquet_to_json.py parquet_to_jsonl <parquet_file> <jsonl_file>
  ```
