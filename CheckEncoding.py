import chardet

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

file_path = 'A:/data/python.txt'

encoding = detect_file_encoding(file_path)
print(f'The encoding of file {file_path} is {encoding}')

