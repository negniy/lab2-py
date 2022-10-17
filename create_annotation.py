import csv
import os
from iterator import Count

def cteate_annotation(class_name, file_path):
    with open("annotation.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Абсолютный путь", "Относительный путь", "Класс"])
        count=Count()
        while ( count.num != 1050 ) :
            file_writer.writerow([os.path.abspath (file_path), file_path, class_name])
        
    
    def main():
        print("Start")
        
    
    if __name__ == "__main__":
        main()