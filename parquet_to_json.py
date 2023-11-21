import argparse
import pandas as pd
import sys

def convert_parquet_to_jsonl(parquet_file, jsonl_file):
    try:
        df = pd.read_parquet(parquet_file)
        df.to_json(jsonl_file, orient='records', lines=True)
        return 0
    except Exception as e:
        print(f"Error converting Parquet to JSONL: {e}")
        return 1

def convert_json_to_parquet(json_file, parquet_file):
    try:
        df = pd.read_json(json_file, lines=True)
        df.to_parquet(parquet_file)
        return 0
    except Exception as e:
        print(f"Error converting JSON to Parquet: {e}")
        return 1
    
def convert_parquet_to_jsonl(parquet_file, jsonl_file):
    try:
        df = pd.read_parquet(parquet_file)
    except Exception as e:
        sys.stderr.write(f"Error reading parquet file: {e}")
        return 1

    try:
        df.to_json(jsonl_file, orient='records', lines=True)
    except Exception as e:
        sys.stderr.write(f"Error writing JSONL file: {e}")
        return 1

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert between Parquet and JSONL')
    parser.add_argument('input_file', type=str, help='Input file')
    parser.add_argument('output_file', type=str, help='Output file')
    parser.add_argument('--to_parquet', action='store_true', help='Convert JSONL to Parquet. Example: python parquet_to_json.py input.jsonl output.parquet --to_parquet')
    parser.add_argument('--to_jsonl', action='store_true', help='Convert Parquet to JSONL. Example: python parquet_to_json.py input.parquet output.jsonl --to_jsonl')
    args = parser.parse_args()

    if args.to_parquet:
        sys.exit(convert_json_to_parquet(args.input_file, args.output_file))
    elif args.to_jsonl:
        sys.exit(convert_parquet_to_jsonl(args.input_file, args.output_file))
    else:
        parser.print_help()