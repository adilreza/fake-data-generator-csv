import random
import string
import csv

all_unique = []
header = ["FullName", "UserName", "Email", "Password"]

def genberate_date(times):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num
    Email=FullName=UserName=Password=""
    temp_ar = []
    for i in range(times):
        rn = "".join(random.sample(all,15))
        temp_ar.append(rn)
    temp2_ar = set(temp_ar)
    temp3_ar = list(temp2_ar)
    ll= len(temp3_ar)
    for i in range(ll):
        rn = temp3_ar[i]
        Email = rn+"@gmail.com"
        FullName = rn
        UserName = rn
        Password = rn
        single_data = [FullName, UserName, Email, Password]
        all_unique.append(single_data)
    with open('/home/adil/Desktop/spiga/loadtest/user-data100.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(all_unique)

genberate_date(100)

