import unittest
import parquet_to_json

class ParquetToJsonTestCase(unittest.TestCase):
    def test_convert_parquet_to_jsonl(self):
        parquet_file = 'test.parquet'
        jsonl_file = 'test.jsonl'
        result = parquet_to_json.convert_parquet_to_jsonl(parquet_file, jsonl_file)
        self.assertEqual(result, 0)
        # Add additional assertions to validate the generated JSONL file

    def test_convert_jsonl_to_parquet(self):
        jsonl_file = 'test.jsonl'
        parquet_file = 'test.parquet'
        result = parquet_to_json.convert_jsonl_to_parquet(jsonl_file, parquet_file)
        self.assertEqual(result, 0)
        # Add additional assertions to validate the generated Parquet file

if __name__ == "__main__":
    unittest.main()