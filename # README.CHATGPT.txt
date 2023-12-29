

User
create a python app that compresses a file
ChatGPT
Certainly! One effective way to compress files in Python is by using the zipfile module, which allows you to create and extract ZIP files. Here's an example of how you could create a simple Python app to compress a file:

python
Copy code
import zipfile
import os

def compress_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    file_name, file_extension = os.path.splitext(file_path)
    zip_file_path = file_name + '.zip'

    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, os.path.basename(file_path))

    print(f"File compressed successfully: {zip_file_path}")

# Example usage:
file_to_compress = 'example.txt'  # Replace this with the file you want to compress
compress_file(file_to_compress)
This code defines a function compress_file that takes the file path as input and compresses it into a ZIP file using the zipfile module. Replace 'example.txt' with the path of the file you want to compress.

Remember to run this code in a directory where you have write permissions to create the compressed file.

Would you like a detailed breakdown of how this code works?





