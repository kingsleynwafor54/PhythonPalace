import csv

with open("majestic_million.csv","r")as infile:
    reader=csv.reader(infile,delimiter=",")
    title=next(reader)
    found_section=False
    header=None
    alloy_index=None
    alloy_sum=0.0
    try:
     for row in reader:
        if not found_section:
            if len(row)>0:
                if row[0]=="Phase":
                    header=next(reader)
                    alloy_index=header.index('alloy=solid_0')
                    found_section=True
            else:
                if len(row)>0:
                    alloy_sum+=float(row[alloy_index])
                else:
                    break
    except StopIteration as s:
        print(s.value)