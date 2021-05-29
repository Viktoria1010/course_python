import csv

with open(r"C:\Users\Виктория\Downloads\stage3_test.csv", 'r', encoding='utf-8') as csv_file:
    with open('task_3.csv', 'w', encoding='utf-8') as to_write:
        spamreader = csv.reader(csv_file)
        spamwriter = csv.writer(to_write)
        for row in spamreader:
            spamwriter.writerow([row[0], row[2], row[4]])
