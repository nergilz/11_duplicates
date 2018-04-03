import os
import argparse


def get_files_free(path):
    files_tree = []
    files_size_and_path = {}

    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            path_file = os.path.join(dir_path, file_name)
            size = os.path.getsize(path_file)
            path_file = list(os.path.split(path_file))
            path_file.append(str(size))
            files_tree.append(path_file)
    for path, name, size in files_tree:
        name_and_size = name + ' ' + size
        files_size_and_path.setdefault(name_and_size, []).append(path)

    return files_size_and_path


def get_duplicates(files_size_and_path):
    duplicates_files = []
    for file, paths in files_size_and_path.items():
        if len(paths) > 1:
            for path in paths:
                res = path + '/' + file
                duplicates_files.append(res)
    return duplicates_files


def pprint_duplicates(duplicates_files):
    for file_inform in duplicates_files:
        information = file_inform.split()
        path = information[0]
        size = information[1]
        print(' Path: {0}  Size: {1}'.format(path, size))


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
    try:
        arguments = get_parser_args()
        if os.path.isdir(arguments.path):
            files_tree = get_files_free(arguments.path)
            duplicates_files = get_duplicates(files_tree)
            pprint_duplicates(duplicates_files)
        else:
            print(' ERROR: this is a file, you need a directory')
    except FileNotFoundError as ex:
        print(' ERROR: {}'.format(ex))
