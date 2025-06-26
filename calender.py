# importing calendar module
# for calendar operations
import calendar
a=int(input("Which year calendar do you want :"))
print(f"The calender of year {a} is : ")
print(calendar.calendar(a,2,1,6))
input()