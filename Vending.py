#Vending machine utility app.

#Vending machine stock and prize

#Snacks

#Cookies = 3
#Croissant = 5
#Saltine Crackers = 2
#Biscuits = 3
#Sandwich = 7

#Hot Drinks
#Coffee = 2
#Black Tea = 1
#Karak Tea = 2

#Cold Drinks
#Bottled Water = 1
#Iced Tea = 5
#Iced Coffee = 5
#Chocolate drink = 3
#Soda = 3
#Mixed Fruit Juice = 5

#This part shows the user the snack type, name, price, the remaining quantity left, and the code for in the machine, basically this is the first thing that a user would see
print ("""Welcome! Written below is the list of snacks and drinks available.
Type in the code of your order to confirm""")

vending_machine_stock = """
Snacks:
Name:                Price:                    Code:
Cookies---------------3DHS----------------------s1
Croissant-------------5DHS----------------------s2
Saltine Crackers------2DHS----------------------s3
Biscuits--------------3DHS----------------------s4
Sandwich--------------7DHS----------------------s5

Hot Drinks:
Name:                Price:                    Code:
Coffee----------------2DHS----------------------h1
Black Tea-------------1DHS----------------------h2
Karak Tea-------------2DHS----------------------h3

Cold Drinks:
Name:                Price:                    Code:
Bottled Water---------1DH-----------------------c1
Iced Tea--------------5DHS----------------------c2
Iced Coffee-----------5DHS----------------------c3
Chocolate Drink-------3DHS----------------------c4
Soda------------------3DHS----------------------c5
Mixed Fruits Juice----5DHS----------------------c6
"""
print(vending_machine_stock)
#User interface(where the user would interact with the machine)
money = (int(input("Insert money (minimum of 2DHS) ")))
print("==Processing==")
print("==Please wait==")
if money > 1:
   print("You have inserted", money, "DHS")
else:
   print("the amount you have input is insufficient")
   money = (int(input("Insert money (minimum of 2DHS) ")))
   print("==Processing==")
   print("==Please wait==")
   print("You have inserted", money, "DHS")

answer = (input("""would you like to proceed?(type in "yes" or "no") """))
if answer == "yes":
  product_code = (input("Please input the code of the product you wish to buy: "))

elif answer == "no":
  print("""==Processing Request==
Refunding amount of""", money, """DHS
 Have a great day!""")


#Price
#Snacks
Cookies = 3
Croissant = 5
Saltine_crackers = 2
Biscuits = 3
Sandwich = 7
#Hot drinks
Coffee = 2
Black_Tea = 1
Karak_Tea = 2
#Cold drinks
Bottled_water = 1
Iced_Tea = 5
Iced_Coffee = 5
Chocolate_drink = 3
Soda = 3
Mixed_fruit_juice = 5


#this part is where the whole system or unit of the code process the request/s of the user


#Snacks
def s1():
  if money >= Cookies:
     money_to_return = money - Cookies
     print("""Your order of Cookies is being processed
     Please wait
     dispensing Cookies
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def s2():
  if money >= Croissant:
     money_to_return = money - Croissant
     print("""Your order of Croissant is being processed
     Please wait
     dispensing Croissant
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def s3():
  if money >= Saltine_crackers:
     money_to_return = money - Saltine_crackers
     print("""Your order of Saltine crackers is being processed
     Please wait
     Dispensing Saltine Crackers
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def s4():
  if money >= Biscuits:
     money_to_return = money - Biscuits
     print("""Your order of Biscuits is being processed
     Please wait
     Dispensing Biscuits
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def s5():
  if money >= Sandwich:
     money_to_return = money - Sandwich
     print("""Your order of Sandwich is being processed
     Please wait
     Dispensing Sandwich
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

#hot drinks
#in the hot drinks section have a longer line of code to accommodate suggestions that for me are appropriate from the snacks section
def h1():
  if money >= Coffee:
     money_to_return = money - Coffee
     print("""Your order of Coffee is being processed
     Please wait
     Dispensing Coffee
     You have a change of""", money_to_return, "DHS")
     offer = input("""Would you like a Croissant to go with your Coffee? (input "yes" or "no" ) """)
  if offer == "yes":
     offer_price = money_to_return - Croissant
     print("""your additional order of Croissant is being processed
     Please wait
     Dispensing Croissant
     You have a change of""", offer_price, "DHS")
  elif offer == "no":
    print("""You have a change of""", money_to_return, """DHS
    Thank you for using this vending machine""")
  
  else:
     print("The amount you have input is insufficient for the chosen product")

def h2():
  if money >= Black_Tea:
     money_to_return = money - Black_Tea
     print("""Your order of Black Tea is being processed
     Please wait
     Dispensing Black Tea
     You have a change of""", money_to_return, "DHS")
     offer = input("""Would you like Saltine Crackers to go with your Black Tea? (input "yes" or "no" ) """)
  if offer == "yes":
     offer_price = money_to_return - Saltine_crackers
     print("""your additional order of Saltine Crackers is being processed
     Please wait
     Dispensing Saltine Crackers
     You have a change of""", offer_price, "DHS")
  elif offer == "no":
    print("""You have a change of""", money_to_return, """DHS
    Thank you for using this vending machine""")
  
  else:
     print("The amount you have input is insufficient for the chosen product")

def h3():
  if money >= Karak_Tea:
     money_to_return = money - Karak_Tea
     print("""Your order of Karak Tea is being processed
     Please wait
     Dispensing Karak Tea
     You have a change of""", money_to_return, "DHS")
     offer = input("""Would you like a biscuit to go with your Karak Tea? (input "yes" or "no" ) """)
  if offer == "yes":
     offer_price = money_to_return - Biscuits
     print("""your additional order of Biscuits is being processed
     Please wait
     Dispensing Biscuits
     You have a change of""", offer_price, "DHS")
  elif offer == "no":
    print("""You have a change of""", money_to_return, """DHS
    Thank you for using this vending machine""")
  
  else:
     print("The amount you have input is insufficient for the chosen product")

#cold drinks

def c1():
  if money >= Bottled_water:
     money_to_return = money - Bottled_water
     print("""Your order of a bottled water is being processed
     Please wait
     dispensing Bottled water
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def c2():
  if money >= Iced_Tea:
     money_to_return = money - Iced_Tea
     print("""Your order of an Iced Tea is being processed
     Please wait
     dispensing Iced Tea
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def c3():
  if money >= Iced_Coffee:
     money_to_return = money - Iced_Coffee
     print("""Your order of an Iced Coffee is being processed
     Please wait
     dispensing Iced Coffee
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def c4():
  if money >= Chocolate_drink:
     money_to_return = money - Chocolate_drink
     print("""Your order of Chocolate drink is being processed
     Please wait
     dispensing Chocolate drink
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def c5():
  if money >= Soda:
     money_to_return = money - Soda
     print("""Your order of Soda is being processed
     Please wait
     dispensing Soda
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

def c6():
  if money >= Mixed_fruit_juice:
     money_to_return = money - Mixed_fruit_juice
     print("""Your order of Mixed Fruit Juice is being processed
     Please wait
     dispensing Mixed Fruit Juice
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have input is insufficient for the chosen product")

#snacks
if product_code == "s1":
   s1()
elif product_code == "s2":
   s2()
elif product_code == "s3":
   s3()
elif product_code == "s4":
   s4()
elif product_code == "s5":
   s5()
#hot drinks
elif product_code == "h1":
   h1()
elif product_code == "h2":
   h2()
elif product_code == "h3":
   h3()
#cold drinks
elif product_code == "c1":
   c1()
elif product_code == "c2":
   c2()
elif product_code == "c3":
   c3()
elif product_code == "c4":
   c4()
elif product_code == "c5":
   c5()
elif product_code == "c6":
  c6()
else:
  print("Error! Invalid Code")

#additional info, note the difference between the line of code for a product without a recommendation and with a recommendation

#Code without recommendation

#def c1():
  #if money >= Bottled_water:
     #money_to_return = money - Bottled_water
     #print("""Your order of a bottled water is being processed
     #Please wait
     #dispensing Bottled water
     #You have a change of""", money_to_return, """DHS
     #Thank you for using this vending machine""")
  #else:
     #print("The amount you have input is insufficient for the chosen product")

#Code with recommendation

#def c2():
#if money >= Iced_Tea:
     #money_to_return = money - Iced_Tea
     #print("""Your order of Iced Tea is being processed
     #Please wait
     #Dispensing Iced Tea
     #You have a change of""", money_to_return, "DHS")
     #offer = input("""Would you like a Sandwich to go with your Iced Tea? (input "yes" or "no" ) """)
  #if offer == "yes":
     #offer_price = money_to_return - Sandwich
     #print("""your additional order of Sandwich is being processed
     #Please wait
     #Dispensing Sandwich
     #You have a change of""", offer_price, "DHS")
  #elif offer == "no":
    #print("""You have a change of""", money_to_return, """DHS
    #Thank you for using this vending machine""")
  
  #else:
     #print("The amount you have input is insufficient for the chosen product")
     