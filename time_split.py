from datetime import datetime
import csv
import pandas as pd
# split all data by time
with open('LIWC_TG_averages/bar_going_before.csv', 'w')as wthird_file:
    with open('LIWC_TG_averages/bar_going_after.csv', 'w') as wfourth_file:
        with open('LIWC-TreatedGroups/LIWC_bar_going.csv', 'r')as rfirst_file:
            with open("TreatedGroup/Bar_Going.txt", 'r') as rsecond_file:
                first_content = csv.reader(rfirst_file)
                headers = next(first_content, None)
                second_content = rsecond_file.read().split('\n')

                # write headers into intermediate file
                for index in range(len(headers)):
                    wthird_file.write(headers[index])
                    wthird_file.write(',')
                    wfourth_file.write(headers[index])
                    wfourth_file.write(',')
                    if index == len(headers) - 1:
                        wthird_file.write(headers[index])
                        wthird_file.write('\n')
                        wfourth_file.write(headers[index])
                        wfourth_file.write('\n')

                # extract time from original Treated Group file
                tg_accts = set()
                for  s_row in range(0, len(second_content) - 1):
                    info = second_content[s_row].strip().split('_')
                    acct_no = info[0]
                    date_int = datetime.strptime(info[1], '%Y-%m-%d')
                    tg_accts.add(acct_no)
                # print(tg_accts)

                    # Find matching account number and time stamps
                for f_row in first_content:
                    # print(tg_accts)
                    if f_row[1] in tg_accts:
                        date = datetime.strptime(f_row[2], '%Y-%m-%d')
                        # print(f_row[1], f_row[2], "MATCH")
                        date_range = date - date_int
                        # print(f_row[1], date_range, date, date_int)

                        # write all lines approximately 2 months prior to interruption in intermediate before file
                        if date_range.days <= 0 and date_range.days >= -60:
                            # print(f_row[1], date_range, date, date_int)
                            for item in range(len(f_row)):
                                wthird_file.write(f_row[item])
                                wthird_file.write(',')
                                if item == len(f_row) - 1 :
                                    wthird_file.write(f_row[item])
                                    wthird_file.write('\n')
                #
                        # write all lines approximately 2 months after interruption in intermediate after file
                        elif date_range.days >= 0 and date_range.days <= 60:
                            # print("AFTER", f_row[1], date_range, date, date_int)
                            for item in range(len(f_row)):
                                wfourth_file.write(f_row[item])
                                wfourth_file.write(',')
                                if item == len(f_row) - 1 :
                                    wfourth_file.write(f_row[item])
                                    wfourth_file.write('\n')

# use PANDAS to group data by month 2 months before and 2 months after
before_data = pd.read_csv("LIWC_TG_averages/sport_leaving_before.csv")
after_data = pd.read_csv("LIWC_TG_averages/sport_leaving_after.csv")

group_before = before_data.groupby(['userID', 'year', 'month']).mean()
group_after = after_data.groupby(['userID', 'year', 'month']).mean()

# print(group_before)
# print(group_after)
group_before.to_csv("LIWC_TG_averages/sport_leaving_before_month.csv")
group_after.to_csv("LIWC_TG_averages/sport_leaving_after_month.csv")
