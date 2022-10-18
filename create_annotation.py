import csv
import os
from iterator import Count
import get_path

def create_annotation(class_name):
    with open("annotation.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь", "Относительный путь", "Класс"])
        count=Count()
        while ( count.num != 1050 ) :
            if (os.path.isfile(get_path.get_absolute_way(class_name, count.num, "download")) == True ):
                file_writer.writerow([get_path.get_absolute_way(class_name, count.num, "download"), get_path.download_relative_way(class_name, count.num), class_name])
            next(count)
        
    
def main():
        print("Start")
        class_name = "rose"
        create_annotation(class_name)
        class_name = "tulip"
        create_annotation(class_name)
        print("The end")
    
if __name__ == "__main__":
        main()