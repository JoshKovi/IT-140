
#def grocery(grocery_item = {}, grocery_history = []):
#    #grocery_item {'name': XXXX, 'number': int(#), 'price':float(#.##)}
#    #grocery_list [{grocery_item}, {grocery_item},{grocery_item}, {grocery_item}]
#    #grocery_history = [{'name':'carl', 'number':int(5), 'price': float(5.99)},
#    #{'name':'sinbad', 'number':int(1), 'price': float(1000.11)},
#    #{'name':'joe Rogan', 'number':int(4), 'price': float(800.32)}]

#    #stop while loop condition True is 'go', otherwise False
#    stop = 'go'
#    if grocery_history == []:
#        while stop == 'go':

#            item_name = input("Item name:\n")
#            quantity = input("Quantity purchased:\n")
#            cost = input("Price per item:\n")
#            grocery_item = {'name':item_name, 'number':int(quantity), 'price': float(cost)}
#            grocery_history.append(grocery_item)
#            cont = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
        
#            if cont == 'q':
#                stop = 'quit'
#            #print(grocery_item, grocery_history, sep='\n')

#    grand_total = 0.00

#    for grocery_item in grocery_history:
#        #print(i['name'])
#        #print(i['number'],' ', i['name'], "\t@ $",i['price'],
#        #      " ea\t$",  round(float(i['number'])*float(i['price']), 2),
#        #                                           sep = '', flush=True)
#        #grand_total +=  round(float(i['number'])*float(i['price']), 2)
#        item_total = round(float(grocery_item['number'])*float(grocery_item['price']), 2)
#        grand_total+=item_total
#        print(grocery_item['number'],' ', grocery_item['name'], "\t@ $",format(grocery_item['price'], '.2f'),
#              " ea\t$",  format(item_total, '.2f'), sep = '', flush=True)
#        item_total = 0
#    print("Grand total: $", format(grand_total, '.2f'), sep="")
#---------------------------------------------------------------------------------------------------------

# This initializes 3 variables, grocery_item as an empty dictionary, grocery_history as an empty list
# and stop as a conditional variable for the while loop. grocery_item is only created here to satisfy the
# project requirements and is not actually required to be initialized here as it is effectively used as a
# local, independent variable in both the for and while loop in my code

grocery_item = {}
grocery_history = []
stop = 'go'

while stop == 'go':
    #This while loop will continue to be executed until the variable stop is not equal to 'go'
    #This area assigns three seperate user inputs to the appropriately named variables
    item_name = input("Item name:\n")
    quantity = input("Quantity purchased:\n")
    cost = input("Price per item:\n")

    # This is the most effecient way to assign the previously collected variables to the previously empty
    # dictionary grocery_item. Another (less efficient) method would be: grocery['key'] = value/variable
    #grocery_history then has the dictionary grocery_item appended to it. 
    grocery_item = {'name':item_name, 'number':int(quantity), 'price': float(cost)}
    grocery_history.append(grocery_item)

    # This retrieves a string of user input and checks if it is 'q', anything else is treated as if the user
    # would like to continue. if the input is 'q' then the conditional assigns 'quit' to stop, it could assign
    #any value to stop besides 'go' and the result would still result in the while loop being exited.
    response = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    if response == 'q':
      stop = 'quit'
      
#This initialized the grand_total variable as a float variable
grand_total = 0.00


for grocery_item in grocery_history:
  # This for loop goes through every item in the grocery_history list. using a range(len(grocery_history))
  # would also work but would require more code then this method.
   
  #This calculates a float value of quantity(number) multiplied by price(cost), rounds the number to 2 decimal
  #places (I had problems with a dozen plus decimal digits in some testing cases) and then adds that value to 
  #the grand_total variable
  item_total = round(float(grocery_item['number'])*float(grocery_item['price']), 2)
  grand_total+=item_total

  #This prints out the quantity, name, '@ $' price(formated to 2 decimal places), and item_total (also to 2 decimal
  #places) in a user friendly format as required by the code tests.
  print(grocery_item['number'],' ', grocery_item['name'], "\t@ $",format(grocery_item['price'], '.2f'),
        " ea\t$",  format(item_total, '.2f'), sep = '', flush=True)
  #This clears the value of item_total, or rather sets the value to zero, while not necessary, it does make the code
  #slightly more readable 

  item_total = 0

#This prints out the previously calculated grand_total variable in a user friendly, 2 decimal format
print("Grand total: $", format(grand_total, '.2f'), sep="")


#While I see no added value to modifying the values of the dictionary beyond converting them from user input
#To the appropriate data type I can do so if required for the Final version of this script with the line:
# grocery_history[grocery_history.index(grocery_item)]['total'] = item_total
# I believe this would satisfy the criteria of modifying a list and a dictionary in one line 