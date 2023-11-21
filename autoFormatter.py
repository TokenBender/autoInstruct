# autoFormatter.py
import json
import argparse
import os
import parquet_to_json

# Create the parser
parser = argparse.ArgumentParser(description='Process a jsonl or json file.')

# Add the arguments
parser.add_argument('input_filename', type=str, help='The input jsonl or json file')
parser.add_argument('output_filename', type=str, help='The output file')
parser.add_argument('instruction_column', type=str, help='Name of the instruction column')
parser.add_argument('response_column', type=str, help='Name of the response column')
parser.add_argument('--format', type=str, default='alpaca', choices=['alpaca', 'chatml'], help='Output format: alpaca or chatml (default: alpaca)')
parser.add_argument('--split_ratio', type=float, default=None, help='Ratio of data to use for training (default: None)')
parser.add_argument('--to_parquet', type=bool, default=False, help='Convert JSONL to Parquet.')

# Parse the arguments
args = parser.parse_args()

# Read the input file
with open(args.input_filename, 'r') as input_file:
    transformed_data = []
    # Check the file extension
    file_extension = os.path.splitext(args.input_filename)[1]

    if file_extension in ['.json', '.jsonl']:
        # Load the file line by line for JSONL or as a JSON object/array for JSON
        json_lines = [json.loads(line) for line in input_file] if file_extension == '.jsonl' else json.load(input_file)
        if isinstance(json_lines, dict):
            json_lines = [json_lines]

    else:
        raise ValueError('Unsupported file extension: ' + file_extension)

    for json_data in json_lines:
        instruction = json_data.get(args.instruction_column, 'No instruction found')
        response = json_data.get(args.response_column, 'No response found')

        if args.format == 'alpaca':
            transformed_text = f'''###Instructions: {instruction}\n###Response: {response}'''
        elif args.format == 'chatml':
            transformed_text = f'''<|im_start|>user\n{instruction}<|im_end|>\n<|im_start|>assistant\n{response}<|im_end|>\n'''

        transformed = {
            "instruction": instruction,
            "input": "",
            "output": response,
            "text": transformed_text
        }
        transformed_data.append(transformed)

# Split the data into training and validation sets
if args.split_ratio:
    training_data = transformed_data[:int(len(transformed_data) * args.split_ratio)]
    validation_data = transformed_data[int(len(transformed_data) * args.split_ratio):]
    
    output_file_name = args.output_filename.split('.')[0]
    training_file_name = output_file_name + '_train.jsonl'
    validation_file_name = output_file_name + '_test.jsonl'

    with open(training_file_name, 'w') as training_file:
        for data in training_data:
            training_file.write(json.dumps(data) + '\n')

    with open(validation_file_name, 'w') as validation_file:
        for data in validation_data:
            validation_file.write(json.dumps(data) + '\n')

else:
    with open(args.output_filename, 'w') as output_file:
        for data in transformed_data:
            output_file.write(json.dumps(data) + '\n')

if args.to_parquet and args.split_ratio:
    parquet_to_json.convert_jsonl_to_parquet(training_file_name, training_file_name.replace('.jsonl', '.parquet'))
    parquet_to_json.convert_jsonl_to_parquet(validation_file_name, validation_file_name.replace('.jsonl', '.parquet'))

if args.to_parquet and not args.split_ratio:
    parquet_to_json.convert_jsonl_to_parquet(args.output_filename, args.output_filename.replace('.jsonl', '.parquet'))