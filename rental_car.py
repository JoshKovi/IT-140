import sys
'''
Section 1: Collect customer input
'''

#Input Section, This area takes all user input and assigns it to the appropriate variable
#rentalCode can be 'B', 'D' or 'W'. The rentalPeriod is an interger, and goes through an if 
#statement in order to display the appropriate prompt. odoStart and odoEnd are the begining and
#ending odometer readings respectively, they are converted into an interger before being assigned
#to a variable.
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
if rentalCode == "D" or rentalCode == "B":
    rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == "W":
    rentalPeriod = input("Number of Weeks Rented:\n")
odoStart = int(input('Starting Odometer Reading:\n'))
odoEnd = int(input('Ending Odometer Reading:\n'))

#This section calculates totalMiles driven (by subtracting odoEnd from odoStart)
#and assigns three variables for the three different charge rates depending on the rental code
#while this could be hardcoded into the next conditionals this is a cleaner way
totalMiles = odoEnd - odoStart
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00


#This section uses a conditional to determine the appropriate action, regardless of which 
#conditional is true this determines the baseCharge and mileCharge variables for each unique condition
#the base charge is immediately determinedm then the average number of miles per rental period.
#Finally the nested conditionals determine if an additional mile charge is required, in the case of 
#the budget rental, the mileCharge is a flat rate regardless of average miles per rental period
if rentalCode == "D":
    baseCharge = dailyCharge * float(rentalPeriod)
    averageDayMiles = int(totalMiles)/int(rentalPeriod)
    if averageDayMiles <= 100:
      mileCharge = 0.00
    else:
      mileCharge = float(averageDayMiles-100) * 0.25
elif rentalCode == "W":
    baseCharge = weeklyCharge * float(rentalPeriod)
    averageWeekMiles = int(totalMiles)/int(rentalPeriod)
    if averageWeekMiles <= 900:
      mileCharge = 0.00
    else:
      mileCharge = float(rentalPeriod) * 100
elif rentalCode == "B":
    baseCharge = budgetCharge * float(rentalPeriod)
    mileCharge = float(totalMiles) * 0.25

#This section calculates the total amount due and then outputs(prints) all of the relavent data
#to the customer, the "\t"'s and"\n"'s are purely for formating and an attempt to align the values
# in a cleaner way.
amtDue = float(baseCharge) + float(mileCharge)
print("Rental Summary")
print("Rental Code: \t\t" + str(rentalCode))
print("Rental Period: \t\t" + str(rentalPeriod))
print("Starting Odometer: \t" + str(odoStart))
print("Ending Odometer: \t" + str(odoEnd))
print("Miles Driven: \t\t" + str(totalMiles))
print("Amount Due: \t\t$" + format(amtDue, '.2f'))

