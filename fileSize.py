import os
import queryFileSize
import sys

path_from_user = sys.argv[2]

def get_dir_size(path):
    size_in_bytes = 0

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            size_in_bytes += os.path.getsize(full_path)

    size_in_megabytes = str(round(size_in_bytes/1000000, 2))+" MB"
    name_of_file = path.rsplit('/', 1)[1]
    return name_of_file, size_in_megabytes

file = get_dir_size(path_from_user)
name_of_file = file[0]
size_of_file = file[1]

queryFileSize.create_table()
queryFileSize.insert(name_of_file, size_of_file)

print("The data was sent to the database")