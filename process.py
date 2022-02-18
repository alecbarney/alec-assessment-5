log_file = open("um-server-01.txt")
# this is opening up our file where some data is held, and saving it to a variable so we can access it in our code.

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)
#this is a function.  It runs a for in loop that goes over the data in the log_file.  First we strip the information to get a copy with any trailing characters removed.  And then we set the first part of the line and the next 3 characters equal to day.  If that variable is equal to tue.  We print the whole line.  This function basically is checking all the deliveries made on tuesday and provides the whole line for those. 

# sales_reports(log_file)
#this is running our function.


def sales_totals(log_file):
    for line in log_file:
        row = line.split(' ')
        ans = row[0:4]
        melon = int(ans[2])
        if melon > 10:
            print(' '.join(row))

sales_totals(log_file)

log_file.close()