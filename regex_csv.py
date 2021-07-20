import csv

rows = []
header = []

with open("employees.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        rows.append(row)

    print("Total no. of rows in csv: %d"%(reader.line_num))

print("The headers name are: "+ ",".join(header))

print("\nFirst 5 rows are: \n")
for row in rows[:5]:
    print(row)
    



    





