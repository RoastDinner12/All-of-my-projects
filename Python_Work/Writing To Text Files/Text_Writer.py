

yy = input("Enter File Name")
mm = input("Write To your file here: ")


with open(yy , 'w') as f:
    f.write(mm)