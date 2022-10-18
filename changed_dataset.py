import os
from iterator import Count
import get_path
import shutil


def copy_to_another( class_name):
    count = Count()
    while (count.num!=1050):
        if (os.path.isfile(get_path.get_absolute_way(class_name, count.num, "download")) == True ):
            shutil.copyfile(get_path.get_absolute_way(class_name, count.num, "download"), get_path.get_absolute_way(class_name, count.num, "changed"))
        next(count)


def main():
        print("Start changing")
        if not os.path.isdir("dataset/changed_dataset"):
            os.mkdir("dataset/changed_dataset")
        class_name = "rose"
        copy_to_another(class_name)
        class_name = "tulip"
        copy_to_another(class_name)
        print("The end of changing")
    
if __name__ == "__main__":
        main()