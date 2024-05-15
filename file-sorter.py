import os
import shutil

# Define the directory where the files are located
source_dir = '/home/enigma/google-drive'

# Define the directories for each file type
directories = {
    'img': ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'svg'],
    'documents': ['xdoc', 'doc', 'docx', 'pdf', 'txt', 'odt', 'rtf'],
    'videos': ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv'],
    'audio': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a'],
    'archives': ['zip', 'rar', 'tar', 'gz', '7z', 'bz2'],
    'scripts': ['sh', 'bat', 'py', 'js', 'pl', 'rb'],
    'spreadsheets': ['xls', 'xlsx', 'ods', 'csv'],
    'presentations': ['ppt', 'pptx', 'odp'],
    'ebooks': ['epub', 'mobi', 'azw3', 'fb2'],
    'deb': ['deb'],
    'iso': ['iso'],
    'fonts': ['ttf', 'otf', 'woff', 'woff2']
}

# Create directories if they don't exist
for directory in directories.keys():
    dir_path = os.path.join(source_dir, directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Move files to respective directories
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        file_extension = filename.split('.')[-1].lower()
        for dir_name, extensions in directories.items():
            if file_extension in extensions:
                dest_dir = os.path.join(source_dir, dir_name)
                shutil.move(file_path, os.path.join(dest_dir, filename))
                break

