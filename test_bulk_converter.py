# path/filename: test_bulk_converter.py

import unittest
from bulk_converter import bulk_convert_xlsx_to_text
import os
        

class TestBulkConverter(unittest.TestCase):

    def test_single_file_conversion(self):
        # Test converting a single file
        file_list = ['file1.xlsx']
        output_dir = 'output_directory'
        delimiter = ';'
        max_threads = 4

        bulk_convert_xlsx_to_text(file_list, output_dir, delimiter, max_threads)

        # Add assertions to verify the conversion results
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'file1.txt')))
        # Add more assertions as needed

    def test_multiple_file_conversion(self):
        # Test converting multiple files
        file_list = ['file1.xlsx', 'file2.xlsx']
        output_dir = 'output_directory'
        delimiter = ','
        max_threads = 2

        bulk_convert_xlsx_to_text(file_list, output_dir, delimiter, max_threads)

        # Add assertions to verify the conversion results
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'file2.txt')))
        # Add more assertions as needed

    def test_invalid_file_handling(self):
        # Test handling of invalid file paths
        file_list = ['invalid_file.xlsx']
        output_dir = 'output_directory'
        delimiter = ','
        max_threads = 2

        bulk_convert_xlsx_to_text(file_list, output_dir, delimiter, max_threads)

        # Add assertions to verify the handling of invalid file paths
        self.assertFalse(os.path.exists(os.path.join(output_dir, 'invalid_file.txt')))
        # Add more assertions as needed

    def test_delimiter_handling(self):
        # Test the application of different delimiters
        file_list = ['file1.xlsx', 'file2.xlsx']
        output_dir = 'output_directory'
        delimiter = '|'
        max_threads = 2

        bulk_convert_xlsx_to_text(file_list, output_dir, delimiter, max_threads)

        # Add assertions to verify the conversion results with different delimiters
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'file2.txt')))
        # Add more assertions as needed

    def test_thread_count_handling(self):
        # Test the function with different thread counts
        file_list = ['file1.xlsx', 'file2.xlsx']
        output_dir = 'output_directory'
        delimiter = ','
        max_threads = 1

        bulk_convert_xlsx_to_text(file_list, output_dir, delimiter, max_threads)

        # Add assertions to verify the conversion results with different thread counts
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'file2.txt')))
        # Add more assertions as needed

# Example usage
if __name__ == '__main__':
    unittest.main()
