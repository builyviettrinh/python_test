#pip3 install chardet
import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
    return result['encoding']

# Config file
file_path = 'output/staffs-shiftJIS.csv'
encoding = detect_file_encoding(file_path)
print(f"The file is encoded as {encoding}")