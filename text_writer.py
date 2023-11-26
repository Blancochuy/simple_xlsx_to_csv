# path/filename: text_writer.py

import csv

class DelimitedFileWriter:
    def __init__(self, output_path, delimiter=','):
        self.output_path = output_path
        self.delimiter = delimiter

    def write_data(self, data):
        with open(self.output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=self.delimiter)
            for row in data:
                writer.writerow(row)

# Example usage
# writer = DelimitedFileWriter('output.csv', delimiter=';')
# writer.write_data(data)
