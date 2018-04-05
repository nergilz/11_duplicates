import os
import argparse


def get_files_size_and_path(path):
    files_size_and_path = {}

    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            path_file = os.path.join(dir_path, file_name)
            size_file = os.path.getsize(path_file)
            path_file = os.path.split(path_file)
            inform_file = (path_file[0], (path_file[1], str(size_file)))
            files_size_and_path.setdefault(inform_file[1], []).append(inform_file[0])

    return files_size_and_path


def get_duplicates(files_size_and_path):
    duplicates_files = {}

    for name_size_file, paths_file in files_size_and_path.items():
        if len(paths_file) > 1:
            for path in paths_file:
                duplicates_files.setdefault(name_size_file, []).append(path)
    return duplicates_files


def pprint_duplicates(duplicates_files):

    for name_size_file, paths_file in duplicates_files.items():
        for path in paths_file:
            name = name_size_file[0]
            size = name_size_file[1]
            path_file = os.path.join(path, name)
            print(' PATH: {0}  SIZE: {1}'.format(path_file, size))


def get_parser_args():
    parser = argparse.ArgumentParser(
        description='Path to check for duplication'
    )
    parser.add_argument(
        'path',
        help='input path to check'
    )
    return parser.parse_args()


if __name__ == '__main__':

    arguments = get_parser_args()
    if os.path.isdir(arguments.path):
        files_size_and_path = get_files_size_and_path(arguments.path)
        duplicates_files = get_duplicates(files_size_and_path)
        pprint_duplicates(duplicates_files)
    else:
        print(' ERROR: this is a file, or directory not found')
