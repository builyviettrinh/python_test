import csv
import codecs
import os

def remove_invalid_characters(text, encoding):
    cleaned_text = ''
    for char in text:
        try:
            char.encode(encoding)
            cleaned_text += char
        except UnicodeEncodeError:
            pass
    return cleaned_text

def convert_csv_encoding(input_file, output_directory, from_encoding, to_encoding):
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        with codecs.open(input_file, 'r', encoding=from_encoding) as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        
        # Loại bỏ ký tự không hợp lệ trước khi chuyển đổi
        cleaned_data = []
        for row in data:
            cleaned_row = [remove_invalid_characters(cell, to_encoding) for cell in row]
            cleaned_data.append(cleaned_row)
        
        output_file = os.path.join(output_directory, os.path.basename(input_file))
        with codecs.open(output_file, 'w', encoding=to_encoding) as file:
            writer = csv.writer(file)
            writer.writerows(cleaned_data)
        
        print(f"Successfully converted and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Config tham số
input_file = 'staffs-utf8.csv'
output_directory = 'output'
from_encoding = 'utf-8'  # Encoding
to_encoding = 'shift_jis'  # Encoding

# Chuyển đổi từ UTF-8 sang Shift JIS
convert_csv_encoding(input_file, output_directory, from_encoding, to_encoding)

# Chuyển đổi từ Shift JIS sang UTF-8
# convert_csv_encoding(input_file, output_directory, to_encoding, from_encoding)
