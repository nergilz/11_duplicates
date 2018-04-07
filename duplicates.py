import os
import argparse


def get_files_size_paths(path):
    files_name_size_paths = {}

    for dir_path, dir_names, files_names in os.walk(path):
        for file_name in files_names:
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            files_name_size_paths.setdefault(
                (file_name, file_size),
                []
            ).append(file_path)

    return files_name_size_paths


def get_duplicates(files_name_size_paths):

    return {
        name_size: file_paths
        for name_size, file_paths in files_name_size_paths.items()
        if len(file_paths) > 1
    }


def pprint_duplicate(duplicate_files):

    for (file_name, file_size), files_paths in duplicate_files.items():
        for file_path in files_paths:
            print(' PATH: {0}  SIZE: {1}'.format(file_path, file_size))


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
        files_name_size_paths = get_files_size_paths(arguments.path)
        duplicate_files = get_duplicates(files_name_size_paths)
        pprint_duplicate(duplicate_files)
    else:
        print(' ERROR: this is a file or directory not found!')
