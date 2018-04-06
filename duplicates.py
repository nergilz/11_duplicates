import os
import argparse


def get_size_path_files(path):
    size_and_path_for_files = {}

    for dir_path, dir_names, names_files in os.walk(path):
        for name_file in names_files:
            path_file = os.path.join(dir_path, name_file)
            size_file = os.path.getsize(path_file)
            size_and_path_for_files.setdefault(
                (name_file, size_file),
                []
            ).append(path_file)

    return size_and_path_for_files


def get_duplicates(size_and_path_for_files):
    duplicate_files = {}

    for name_size_file, paths_files in size_and_path_for_files.items():
        if len(paths_files) > 1:
            for path_file in paths_files:
                duplicate_files.setdefault(name_size_file, []).append(path_file)

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
        size_and_path_for_files = get_size_path_files(arguments.path)
        duplicate_files = get_duplicates(size_and_path_for_files)
        pprint_duplicate(duplicate_files)
    else:
        print(' ERROR: this is a file, or directory not found')
