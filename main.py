#This project idea is borrowed from Chuck Keith aka NetworkChuck. I have expanded on it and added my own ideas.
#This program is a simple interaction between you and a coffee barista .
#When you run the program the barista generates their menu. You are then prompted for input from the console. 
#The barista wants to know what items you would like to order. The script comes to it's conclusion after you have finished
#ordering and reads back your order. This is a work-in-progress. 

import random
menu = ["Black Coffee", "Green Tea", "Caramel Macchiato", "Americano", "Cookie", "Eggnog", "Expresso", "Chai Latte", "Vanilla Latte", "Chamomile Tea", "Black Tea", "Frappucino", "Mocha", "Toast"]
todaysmenu = random.sample(menu, 4)
name = input("Hello! What is your name? \n")
wholeorder = []
print(f"Hello {name}. Welcome to the barista. What would you like to order? \n")
def order():
  more = "N"
  while more == "N":
    order = input(f"Today we have: {', '.join(todaysmenu)} \n")
    while order != todaysmenu[0] and order != todaysmenu[1] and order != todaysmenu[2] and order != todaysmenu[3]:
      order = input("That's not on today's menu. What would you like to order? \n")
    wholeorder.append(order)
    more = input("Excellent choice! Will this complete your order? ('Y' or 'N') \n")
    if more != "N" and more != "Y":
      more = input("I'm sorry, try again. Please type 'Y' or 'N'")
  else:
    if more == "N":
      print("OK. What else would you like?")
order()
print(f"OK! Your {', '.join(wholeorder)} will be right out!")
