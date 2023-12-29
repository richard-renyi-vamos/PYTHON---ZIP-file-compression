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
