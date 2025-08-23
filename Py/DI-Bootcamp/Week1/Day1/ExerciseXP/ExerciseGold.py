#Exercise1
print("\n---Exercise 1 : Hello World-I Love Python---")
print(" Hello World " * 4, " I Love Python " * 4)

#Exercise2
print("\n---Exercise 2 : What Is The Season ?---")
'''Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)'''
month = int(input("Enter the number of the month (from 1 to 12, where 1 is January, 2 is Februay ect.)"))
if month < 1 or month > 12:
    print("This is the wrong number, try again")
elif month == 12 or month <= 2:
    print("This month is Winter")
elif month >=3 and month <= 5:
    print ("This month is Spring")
elif month >= 6 and month <= 8:
    print("This month is Summer")
else:
    print("This month is Autumn")
month_names = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_name = month_names[month]
print(f"It was {month_name}, isn't it?")