import csv
out = open('sample_1.csv', 'w')
for y in range(1,6):
    with open('sample.csv', 'r', encoding="utf-8") as f:
        content = csv.reader(f)
        counter = 0
        z_counter = 0
        for x in content: # retrieve all row info within results
            print(counter)
            counter += 1
            # print(len(x))

            for z in range(len(x)): # loop within row for column info
                # print(z)
                z_counter += 1
                if z == 0: # split tweet from user ID / date
                    out.write(x[z].split()[0])
                    out.write(',')
                elif z == 93: # reached end of info, make new line
                    out.write(x[z])
                    out.write('\n')
                else: # all data in the middle
                    out.write(x[z])
                    out.write(',')
            z_counter = 0 # reset column counter so it doesn't continue to increase and go out of index
out.close()
