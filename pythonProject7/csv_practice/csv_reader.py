import csv

outfile = open("student_name.csv", "w")
outfile_header="student First Name,Student Last Name\n"
outfile.write(outfile_header)
with open("test_csv_DB.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    try:
        for row in reader:
            student_first_name = row[0]
            student_last_name = row[1]
            student_last_year = row[2]
            student_grade1 = row[3]
            student_grade2 = row[4]
            line = "{},{}\n".format(student_first_name, student_last_name)
            outfile.write(line)
    except StopIteration:
        print(error)
outfile.close()
