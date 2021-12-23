# import csv
#
# outfile1 = open("student_name.csv", "w")
# outfile2 = open("student_name2.csv", "w")
# outfile_header1 = "student First Name,Student Last Name\n"
# outfile_header2 = "Total student score is\n"
# outfile1.write(outfile_header1)
# outfile2.write(outfile_header2)
# with open("majestic_million.csv") as infile:
#     reader = csv.reader(infile, delimiter=",")
#     title = next(reader)
#     total = 0
#     try:
#         for row in reader:
#             student = row[0]
#             total += int(student)
#
#             line1 = "{}\n".format(student)
#             line2 = "{}\n".format(total)
#             outfile1.write(line1)
#
#
#     except Exception as e:
#         print("error")
# outfile2.write(line2)
# outfile1.close()

# import csv
#
# with open('majestic_million.csv', 'r') as infile:
#     reader = csv.reader(infile, delimiter=",")
#     title = next(reader)
#
#
# def searchByCity(csv_file=None, row=None):
#     city = input('Enter city name\n')
#     for row in title:
#         # if city in row[3]:
#             print(row)
#
#
# def searchByDate():
#     year = input('Enter city name\n')
#     csv_file = csv.reader(open("majestic_million.csv", 'r'))
#     for row in csv_file:
#         if year in row[0]:
#             print(row)
#
#
# print("Enter 1 to search by city names")
# print('Enter 2 to search by date')
# src = int(input('Enter here: '))
# if src == 1:
#     searchByCity()
# elif src == 2:
#     searchByDate()
# else:
#     print("Chcose another number")


import csv
with open('majestic_million.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)