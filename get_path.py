import os


def create_download_relative_way(name_class, number):
    return f"dataset/download_data/{name_class}/{str(number).zfill(4)}.jpg"


def create_changed_relative_way(name_class, number):
    return f"dataset/dataset_another/{name_class}_{str(number).zfill(4)}.jpg"


def create_random_relative_way(number):
    return f"dataset/dataset_number/{str(number).zfill(4)}.jpg"


def get_absolute_way(name_class, number, mode):
    if mode == "download":
        return os.path.abspath(create_download_relative_way(name_class, number))
    if mode == "changed":
        return os.path.abspath(create_changed_relative_way(name_class, number))
    if mode == "random":
        return os.path.abspath(create_random_relative_way(number))