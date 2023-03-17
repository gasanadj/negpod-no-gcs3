print("Prepare to enter a Month")
month = input("Enter the Month : ")
if (month == "february"):
    print("28 or 29 days")
elif (month in ("april","june","september","november")):
    print("30 days")
elif (month in ("january","march","may","july","october","august","december")):
    print("31 days")
else:
    print("invalid Month input")            