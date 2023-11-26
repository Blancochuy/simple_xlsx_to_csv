# path/filename: bulk_converter.py

from concurrent.futures import ThreadPoolExecutor
import os
from xlsx_reader import XlsxReader
from text_writer import DelimitedFileWriter  # Import DelimitedFileWriter class

class BulkConverter:
    def __init__(self, output_dir, delimiter=',', max_threads=2, progress_callback=None):
        self.output_dir = output_dir
        self.delimiter = delimiter
        self.max_threads = max_threads
        self.progress_callback = progress_callback

    def convert_xlsx_to_text(self, file_paths):
        def convert_file(file_path):
            try:
                xlsx_reader = XlsxReader(file_path)
                data, _ = xlsx_reader.read_xlsx()
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                output_file = os.path.join(self.output_dir, base_name + '.csv')
                writer = DelimitedFileWriter(output_file, self.delimiter)
                writer.write_data(data)
                return True
            except Exception as e:
                print(f"Error converting {file_path}: {e}")
                return False
            finally:
                if self.progress_callback:
                    self.progress_callback(1)  # Update progress by 1 unit

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            results = list(executor.map(convert_file, file_paths))

        return results  # Return list of conversion results

# Example usage
# file_list = ['file1.xlsx', 'file2.xlsx']
# converter = BulkConverter('', delimiter='|', max_threads=4, progress_callback=update_progress)
# results = converter.convert_xlsx_to_text(file_list)
