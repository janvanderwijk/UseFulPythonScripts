# Python program to display calendar of given month of the year

# import module
import calendar

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# ask user to input month and year
yy = int(input("Enter the Year: "))
mm = int(input("Enter the Month: "))

print("\n")  # Prints empty Line

if (yy % 4) == 0:
   if (yy % 100) == 0:
       if (yy % 400) == 0:
           print("{0} is a leap year".format(yy))
       else:
           print("{0} is not a leap year".format(yy))
   else:
       print("{0} is a leap year".format(yy))
else:
   print("{0} is not a leap year".format(yy))


# display the calendar
print("\n") # Prints empty Line
print(calendar.month(yy, mm))
