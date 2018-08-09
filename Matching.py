from datetime import datetime
import csv
out_file = open('LIWC_bar_going.csv', 'w')

#open Treated Group file and extract user IDs associated
with open("TreatedGroup/Bar_Going.txt") as second_file:
    base = second_file.read().split('\n')
    leaving_accts = set()
    dates = set()
    for i in range(0, len(base)-1):
        info = base[i].strip().split('_')
        acct_no =  info[0]
        time = info[1]
        leaving_accts.add(acct_no)
        dates.add(time)

# open file with all data
with open('LIWC_INFO_organized.csv', 'r') as first_file:
    content = csv.reader(first_file)
    headers = next(content)

    # writing headers into new file
    for index in range(len(headers)):
        out_file.write(headers[index])
        out_file.write(',')
        if index == len(headers)-1:
            out_file.write(headers[index])
            out_file.write('\n')

    # writing matching acct numbers into new file
    for row in content:
        if row[1] in leaving_accts:
            # print(row)
            for col in range(0, len(row)):
                out_file.write(row[col])
                out_file.write(',')
                if col == len(row)-1:
                    out_file.write(row[col])
                    out_file.write('\n')
out_file.close()

