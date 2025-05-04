import zipfile as zip

# create a ZIP archive
with zip.ZipFile('../files/archive.zip', 'w') as zip_file:
    zip_file.write('file1.txt')
    zip_file.write('file2.txt')

# Extract files form a ZIP archive
with zip.ZipFile('../files/archive.zip', 'r') as zip_file:
    zip_file.extractall('target_directory')