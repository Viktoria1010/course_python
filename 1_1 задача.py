import csv

with open(r"C:\Users\Виктория\Downloads\stage3_test.csv", 'r', encoding='utf-8') as csv_file:
    with open('task_1.csv', 'w', encoding='utf-8') as to_write:
        reader = csv.DictReader(csv_file)
        fieldnames = ["Id", "Images", "Title", "Description", "Price"]
        writer = csv.DictWriter(to_write, fieldnames)
        writer.writeheader()
        for row in reader:
            if row['Images'].count(',') >= 2:
                writer.writerow(row)


