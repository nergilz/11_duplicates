import os
import argparse


def get_size_paths_files(path):
    name_size_paths_for_files = {}

    for dir_path, dir_names, files_names in os.walk(path):
        for file_name in files_names:
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            name_size_paths_for_files.setdefault(
                (file_name, file_size),
                []
            ).append(file_path)

    return name_size_paths_for_files


def get_duplicates(size_and_paths_for_files):
    duplicate_files = {}

    for name_size_file, paths_files in size_and_paths_for_files.items():
        if len(paths_files) > 1:
            duplicate_files.setdefault(name_size_file, paths_files)

    return duplicate_files


def pprint_duplicate(duplicate_files):

    for (name_file, size_file), paths_files in duplicate_files.items():
        for path_file in paths_files:
            print(' PATH: {0}  SIZE: {1}'.format(path_file, size_file))


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
        name_size_paths_for_files = get_size_paths_files(arguments.path)
        duplicate_files = get_duplicates(name_size_paths_for_files)
        pprint_duplicate(duplicate_files)
    else:
        print(' ERROR: this is a file or directory not found!')
