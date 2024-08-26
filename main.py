
#SarsoftRobot by Sarveshwar Senthilkumar

#sRobot
#SarsoftRobot

import sys
import os
import time
import json
import random
import string
import datetime 
from gtts import gTTS
from colorama import Fore, Back, Style
import calendar
from datetime import date
from datetime import *
from googlesearch import search 
import urllib.request
import urllib.parse
import re
import turtle
import tkinter as tk
import tkinter.font as font
import pytz
from collections import defaultdict
from google_currency import convert 

def RPS_Game_Sarveshwar():

  def last(name, credits):
    os.system("clear")
    print("Bye " + name + "! \n")
    input("Press enter to continue...")
    os.system("clear")
    
    tz_CH = pytz.timezone('America/Chicago') 
    datetime_CH = datetime.now(tz_CH)

    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    a = (" || Date: " + d2 + " || Time of exit(CST time):" + datetime_CH.strftime("%H:%M:%S"))
    gstrin = "\nName: " + name + a
    opn = open("RPSData.txt", "a")

    opn.writelines(gstrin)

    opn.close()

    robot_wait()

  def easygame(name,credits):

    os.system("clear")
    newpoin = 0
    newpoini = 0
    
    while True:
      randnum = random.randint(1,3)

      print("Low Credits\n")
      print("""    1. Rock
      2. Paper
      3. Scissors\n""")
      opti = int(input("Which one do you want to go for? (Enter the number): "))

      if opti == 1:
        os.system("clear")
        if randnum == 2:
          newpoini += 1
          

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      elif opti == 2: 
        os.system("clear")     
        if randnum == 3:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
    
      elif opti == 3:  
        os.system("clear")    
        if randnum == 1:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      if newpoin == 3:
        credits += 1
        print("You won this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break
      
      elif newpoini == 3:
        print("You lost this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break


  def medgame(name,credits):
    os.system("clear")
    newpoin = 0
    newpoini = 0
    while True:
      randnum = random.randint(1,3)

      print("Medium Credits\n")
      print("""    1. Rock
      2. Paper
      3. Scissors\n""")
      opti = int(input("Which one do you want to go for? (Enter the number): "))

      if opti == 1:
        os.system("clear")
        if randnum == 2:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      elif opti == 2:   
        os.system("clear")   
        if randnum == 3:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
    
      elif opti == 3: 
        os.system("clear")     
        if randnum == 1:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      if newpoin == 3:
        credits += 3
        print("You won this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break
      
      elif newpoini == 3:
        print("You lost this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break

  def hardgame(name,credits):
    os.system("clear")
    newpoin = 0
    newpoini = 0
    while True:
      randnum = random.randint(1,3)

      print("High Credits\n")
      print("""    1. Rock
      2. Paper
      3. Scissors\n""")
      opti = int(input("Which one do you want to go for? (Enter the number): "))

      if opti == 1:
        os.system("clear")
        if randnum == 2:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      elif opti == 2:    
        os.system("clear")  
        if randnum == 3:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
    
      elif opti == 3:   
        os.system("clear")   
        if randnum == 1:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      if newpoin == 3:
        credits += 7
        print("You won this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break
      
      elif newpoini == 3:
        print("You lost this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break
    
  def chalgame(name,credits):
    os.system("clear")
    newpoin = 0
    newpoini = 0
    while True:
      randnum = random.randint(1,3)

      print("Extremely High Credits\n")
      print("""    1. Rock
      2. Paper
      3. Scissors\n""")
      opti = int(input("Which one do you want to go for? (Enter the number): "))

      if opti == 1:
        os.system("clear")
        if randnum == 2:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      elif opti == 2: 
        os.system("clear")     
        if randnum == 3:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 1:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
    
      elif opti == 3:   
        os.system("clear")   
        if randnum == 1:
          newpoini += 1

          print("You lost...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 3:
          print("You tied...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
        
        elif randnum == 2:
          newpoin += 1

          print("You won...\n")
          print(str(newpoin) + ":" + str(newpoini) + "\n")
          input("Press enter to continue...")
          os.system("clear")
      
      if newpoin == 3:
        credits += 200
        print("You won this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break
      
      elif newpoini == 3:
        print("You lost this match\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
        os.system("clear")
        break

  def titlescreen(name, credits):
    os.system("clear")
    print("Welcome to Sarveshwar's Rock Paper Scissors\n")
    print("Credits: " + str(credits) + "\n")
    print("""  1. Low Credits (0 credits to enter)
    2. Good Credits (1 credit to enter)
    3. Great Credits (5 credits to enter)
    4. HELP GUIDE
    5. QUIT\n""")
    gameopt = int(input("Which one do you want to go for? (Enter the number): "))
    os.system("clear")
    if gameopt == 1:    
      easygame(name, credits)
    
    elif gameopt == 2:

      if credits >= 1:
        credits-=1
        medgame(name, credits)
      else:
        print("Hey, stop trying to break the game. Insufficient Credits\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
    
    elif gameopt == 3:

      if credits >= 5:
        credits-=5
        hardgame(name, credits)
      else:
        print("Hey, stop trying to break the game. Insufficient Credits\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
    
    elif gameopt == 50:

      if credits >= 50:
        credits-=5
        chalgame(name, credits)
      else:
        print("Hey, stop trying to break the game. Insufficient Credits\n")
        input("Press enter to continue...")
        titlescreen(name, credits)
    
    elif gameopt == 313:
      namer = input("Enter your name: ")

      tz_CH = pytz.timezone('America/Chicago') 
      datetime_CH = datetime.now(tz_CH)

      today = date.today()
      d2 = today.strftime("%B %d, %Y")

      a = (" || Date: " + d2 + " || Time of exit(CST time):" + datetime_CH.strftime("%H:%M:%S"))
      gstrin = "\nName: " + namer + a
      opn = open("secretnames.txt", "a")

      opn.writelines(gstrin)

      opn.close()

      passw = input("")

      if passw == "SarveshwarProgrammer":
        os.system("clear")
        abc = open("data.txt", "r")
        print(abc.read())
          
    
    elif gameopt == 4:
      input("Press enter to continue...")
      os.system("clear")
      guide(name, credits)

    elif gameopt == 5:
      input("Press enter to continue...")
      os.system("clear")
      last(name, credits)

  def guide(name, credits):
    os.system("clear")
    print("In Sarveshwar's Rock Paper Scissors you have to choose either a low, medium or high credits game and then you go against a robot for either 1, 3, 7 or 200 credits, you have to pick rock, paper or scissors ,if you win you get one point and if you get 3 points before the robot you win the credits for that game.\n")
    input("Press enter to continue...")
    os.system("clear")
    titlescreen(name, credits)

  os.system("clear")

  print("Welcome to Sarveshwar's Rock Paper Scissors\n")

  name = input("Enter your name: ")
  os.system("clear")
  print("If you have 50 credits enter 50 as an option\n")
  input("Press enter to continue...")
  os.system("clear")
  print("Welcome to Sarveshwar's Rock Paper Scissors\n")
  input("Press enter to continue...")
  credits = 0
  titlescreen(name, credits)


def random_card_generator():
  def find_card(numbered_card):
    group_num = random.randint(1, 4)

    card_num = random.randint(1, 14)

    if group_num == 1:
      group = " of Diamond"

    elif group_num == 2:
      group = " of Hearts"

    elif group_num == 3:
      group = " of Clovers"

    elif group_num == 4:
      group = " of Spades"

    if card_num == 1:
      card = "Ace"

    elif card_num == 11:
      card = "Jack"

    elif card_num == 12:
      card = "Queen"

    elif card_num == 13:
      card = "King"

    elif card_num == 14:
      card = "Ace"

    else:
      card = str(card_num)

    number_card = str(numbered_card)
    if (number_card[-1]) == "1":
      print(number_card + "st card is " + card + group)

    elif number_card[-1] == "2":
      print(number_card + "nd card is " + card + group)

    elif number_card[-1] == "3":
      print(number_card + "rd card is " + card + group)

    elif number_card[-1] == "4" or number_card[-1] == "5" or number_card[-1] == "6" or number_card[-1] == "7" or number_card[-1] == "8" or number_card[-1] == "9" or number_card[-1] == "0":
      print(number_card + "th card is " + card + group)

  print("Welcome to Random Card Generator by Sarveshwar Senthilkumar\n")
  input("Press enter to continue...")
  os.system("clear")

  while True:
    os.system("clear")
    print("Welcome to Random Card Generator\n")
    random_C_num = (input("Enter the number of random cards you want(Q to quit/exit): "))
    os.system("clear")

    if random_C_num == "Q" or random_C_num == "q" or random_C_num.isalpha():
      os.system("clear")
      robot_wait()
      break
    
    else:
      random_C_num = int(random_C_num)

    numbered_card = 0

    print()

    while random_C_num > 0:
      numbered_card += 1
      random_C_num -= 1
      find_card(numbered_card)

    print()

    input("Press enter to continue...")
    os.system("clear")

def TaxCalculator():
  while True:
    os.system("clear")
    name = input("Enter your name: ")
    os.system("clear")
    print("Welcome to Sarveshwar's Tax Calculator\n")
    print("Enter the price of one (You will have to enter the quantity later)\n")

    price = (input("Enter the price of the item (Q to quit): "))
    
    if price == "Q" or price == "q":
      os.system("clear")
      print("Bye " + name + "...")
      print()
      input("Press enter to continue...")

      dateP = datetime.now()

      date_and_time = dateP.strftime("%d/%m/%Y %H:%M:%S")
      os.system("clear")
      opened = open("TaxedNames.txt", "a")

      line = name + " || " + date_and_time
      opened.write(line)

      opened.close()

      robot_wait()
      break
    
    elif price.isalpha():
      os.system("clear")
      print("Bye " + name + "...")
      print()
      input("Press enter to continue...")

      date_and_time = now.strftime("%d/%m/%Y %H:%M:%S")
      os.system("clear")
      opened = open("TaxedNames.txt", "a")

      line = name + " || " + date_and_time
      opened.write(line)

      opened.close()

      break
    
    else:
      price = int(price)

    taxpercent = float(input("Enter the percentage of tax Example(10, 50, 80): "))

    item = input("Enter the name of the item: ")

    quantity = input("How many " + item + " do you have?: ")

    currency = input("Enter the currency: ")

    os.system("clear")

    tax = price / 100
    tax = tax * taxpercent
    taxWprice = (price + tax)

    quantity2 = float(quantity)

    taxWprice = taxWprice * quantity2

    totaltax = tax * quantity2

    if isinstance(tax, int):
      tax = int(tax)
      taxWprice = int(taxWprice)

    print("The price without tax for one " + item + " is " + str(price) + " " + currency)

    print("The tax is " + str(taxpercent) + "%")
    print("The tax for one " + item + " will be " + str(tax) + " " + currency)

    print("The total tax for " + str(quantity) + " " + item + " is " + str(totaltax) + currency)

    print("The total cost is " + str(taxWprice) + " " + currency)

    input("\nPress enter to continue...")

#Business Sim by Sarveshwar Senthilkumar

def BusinessSim():
  def finished():
    name = input("Enter your name: ")
    os.system("clear")
    print("Bye " + name + "...\n")
    input("Press enter to continue...")
    os.system("clear")
    
    time_now = datetime.now()

    opened = open("BusinessSimNames.txt", "w")
    opened.write("\n\n" + name + " || " + str(time_now))

    opened.close()

    robot_wait()

  deal_given = False
  
  chance = random.randint(1, 5)
  print("Business Sim by Sarveshwar Senthilkumar\n")
  input("Press enter to continue...")
  os.system("clear")
  print("Welcome to Business Sim\n")
  print("Money per hour is determined by money per hour subtracted by pay per hour(You have to enter pay per hour next)\n")
  mon_per_hour = int(input("How much money would you like to earn per hour? Example(50, 75): "))
  pay_per_hour = int(input("How much money do you have to pay per hour?: "))
  tax_percent = int(input("What is the tax percentage?(Example: 20, 80, 120): "))

  currency = input("Enter the name of your currency: ")

  os.system("clear")

  mon_per_hour = mon_per_hour - pay_per_hour
  total_money = 0
  experience = 0
  weeks = 0
  accepted_deal = False
  week_times = []
  recent_offer = 0

  time_tested = int(input("How many weeks would you like to test?: "))


  while weeks < time_tested:
    chance = random.randint(1, 5)
    weeks += 1

    if chance <= 3:
      gotProject = True
    else:
      gotProject = False
      week_times.append(0)
    if gotProject:
      time_needed = random.randint(8, 40)
      experience = experience + time_needed

      money_made = time_needed * mon_per_hour

      tax = (money_made / 100) * tax_percent

      money_made = money_made - tax
      
      total_money = total_money + money_made
      week_times.append(time_needed)


    if experience > 2000:
      buyout_money = experience * mon_per_hour * 2.3
      if deal_given == False or buyout_money > recent_offer and accepted_deal == False: 
        rare_chance = random.randint(1, 10000)
        if rare_chance > 9990:
          if deal_given == False:
            deal_given = True
            buyout_money = experience * mon_per_hour * 2.3
            tax = (buyout_money / 100) * tax_percent
            buyout_money = buyout_money - tax
            recent_offer = buyout_money
            #A company made us a deal to buy us out
            os.system("clear")
            print("A company named SenthilTech wants to buy you out for " + str(buyout_money))
            chance_accepting = input("Will you accept the offer? Example(YES, NO): ")
            if chance_accepting == "YES".lower():
              
              accepted_deal = True
              
              total_money = total_money + buyout_money
              
              line1 = "\nTotal Money Earned: " + str(total_money) + " " + currency
              line2 = "\nExperience: " + str(experience) + " hours"
              line25 = "\nDeal Given: " + str(deal_given)
              line3 = "\nDeal Accepted: " + str(accepted_deal)
              line4 = "\nMoney Per Hour: " + str(mon_per_hour) + " " + currency
              line5 = "\nWeeks Tested: " + str(weeks) + "\n"

              os.system("clear")

              options2 = input("Would you like to see how may hours you worked in the " + str(weeks) + " weeks?(YES, NO): ")

              os.system("clear")

              if options2 == "YES".lower() or options2 == "yes".upper():
                for i in week_times:
                  print(i) 

                input("\nPress enter to continue...")
                os.system("clear")

              print(line1)
              print(line2)
              print(line25)
              print(line3)
              print(line4)
              print(line5)

              openfile = open("dataB.txt", "a")

              openfile.write(line1)
              openfile.write(line2)
              openfile.write(line25)
              openfile.write(line3)
              openfile.write(line4)
              openfile.write(line5)

              openfile.close()

              openfile2 = open("dataB2.txt", "a")

              for i in week_times:
                i = str(i)
                openfile2.write(i + "\n")

              openfile2.write("\n")

              openfile2.close()

              print()
              input("Press enter to continue...")
              
              os.system("clear")

              finished()
          else:
            accepted_deal = False

  line1 = "\nTotal Money Earned: " + str(total_money)
  line2 = "\nExperience: " + str(experience)
  line25 = "\nDeal Given: " + str(deal_given)
  line3 = "\nDeal Accepted: " + str(accepted_deal)
  line4 = "\nMoney Per Hour: " + str(mon_per_hour)
  line5 = "\nWeeks Tested: " + str(time_tested) + "\n"

  os.system("clear")

  options2 = input("Would you like to see how may hours you worked in the " + str(time_tested) + " weeks?(YES, NO): ")

  os.system("clear")

  if options2 == "YES".lower() or options2 == "yes".upper():
    for i in week_times:
      print(i) 

    input("\nPress enter to continue...")
    os.system("clear")

  print(line1)
  print(line2)
  print(line25)
  print(line3)
  print(line4)
  print(line5)

  openfile = open("dataB.txt", "a")

  openfile.write(line1)
  openfile.write(line2)
  openfile.write(line25)
  openfile.write(line3)
  openfile.write(line4)
  openfile.write(line5)

  openfile.close()

  openfile2 = open("dataB2.txt", "a")

  for i in week_times:
    i = str(i)
    openfile2.write(i + "\n")

  openfile2.write("\n")

  openfile2.close()

  print()
  input("Press enter to continue...")
  
  os.system("clear")

  finished()

#BusinessSim()

def findleap():
  def cleaner():
    print()
    input("Press enter to continue...")
    os.system("clear")
    exit()
  year = input("What year would you like to check?: ")
  year1 = int(year)
  a = calendar.isleap(year1)
  os.system("clear")
  if a:
    print(year, "is a leap year")
  else:
    print(year, "is not a leap year")

def fact():
  def clearer():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  n = input("Enter the number you want the factorial of: ")
  n = int(n)

  if n <= 1:
    print("The factorial of", n, "is 1")

  else:
    fn = 1
    for i in range(1, n + 1):
      fn = fn * i
    print("The factorial of", n, "is", fn)
  
  clearer()


def excrates():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()

  print("Exchange Rates:")

  print()

  fromcurrency = input("1st Currency Example(INR, USD): ")
  fromcurrency = fromcurrency.lower()

  tocurrency = input("2nd Currency Example(INR, USD): ")
  tocurrency = tocurrency.lower()

  howmuch = input("How many would you like to see the rate for?: ")
  howmuch = int(howmuch)

  convertedvalue = (convert(fromcurrency, tocurrency, howmuch))  

  y = json.loads(convertedvalue)

  convalmon = (y["amount"])

  fromcurrency = fromcurrency.upper()
  tocurrency = tocurrency.upper()

  os.system("clear")

  sentencer = (howmuch, fromcurrency, "to", tocurrency, "is", convalmon, tocurrency)
  print(sentencer)

  clear()

  d = datetime.now()
  timezone = pytz.timezone("America/Chicago")
  d_aware = timezone.localize(d)
  d_aware.tzinfo
  utc_now = pytz.utc.localize(datetime.utcnow())
  pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
  pst_now = str(pst_now)

  pst_now == utc_now

  a = open("currency.txt", "a")
  a.write("\n")
  a.write("\n")
  a.write(sentencer)
  a.write(" / ")
  a.write(pst_now)
  a.close()



def fpalin():
  def cleanerscr():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  os.system("clear")
  anletter = input("Enter your letters: ")
  char_count = defaultdict(int)
  
  for c in anletter:
    char_count[c] += 1

  od = ""
  pal = ""

  for c, cnt in char_count.items():
    if cnt % 2 == 0:
      pal += c * (cnt // 2)
    elif not od:
      od += c
      pal += c * (cnt // 2)
    else:
      print("You can't get a palindrome from", anletter)
  palindrome = pal + od + pal[::-1]
  print("You can get", palindrome, "palindrome from anletter") 

def feetmet():
  def cleaner():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()

  os.system("clear")
  print("""
  1. Feet to meters
  2. Meters to feet
  """)
  opi = int(input("Enter you option: "))
  if opi == 1:
    os.system("clear")
    mot = int(input("Enter the number of feet: "))
    gall = mot * 0.3048
    os.system("clear")
    print(mot, " feet is ", gall, " meters")
    
  elif opi == 2:
    os.system("clear")
    mot = int(input("Enter the number of meters: "))
    gra = mot * 3.28084
    os.system("clear")
    print(mot, "meters is ", gra, "feet")
    cleaner()


def higherorlower():
  def cleanert():
    print()
    input("Press enter to continue...")
    os.system("clear")
  
  def title():
    print()
    
    max = input("Enter the maximum you want for the game: ")
    max = int(max)
    rannum = random.randint(1, max)
    os.system("clear")
    ran = max // 2
    print("1. Higher than", ran)
    print("2. Lower than", ran)
    print("3. QUIT")

    an = input("Enter your option: ")
    an = int(an)
    os.system("clear")

    if rannum > ran:
      if an == 1:
        print("You got it right!!")
        print("You said it was higher than", ran)
        print("The number was", rannum)
        print()
        input("Press enter to continue...")
        os.system("clear")
        title()

      elif an == 2:
        print("You got it wrong!!")
        print("You said it was lower than", ran)
        print("The number was", rannum)
        print()
        input("Press enter to continue...")
        os.system("clear")
        title()
      
      elif an == 3:
        cleanert()

    elif rannum < ran:
      if an == 1:
        print("You got it wrong!!")
        print("You said it was higher")
        print("The number was", rannum)
        print()
        input("Press enter to continue...")
        os.system("clear")
        title()

      elif an == 2:
        print("You got it right!!")
        print("You said it was lower than", ran)
        print("The number was", rannum)
        print()
        input("Press enter to continue...")
        os.system("clear")
        title()
      
      elif an == 3:
        cleanert()

  title()

def litgal():
  def cleaner():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()

  os.system("clear")
  print("""
  1. Liters to gallons
  2. Gallons to liters
  """)
  opi = int(input("Enter you option: "))
  if opi == 1:
    os.system("clear")
    mot = int(input("Enter the number of liters: "))
    gall = mot * 0.264172
    os.system("clear")
    print(mot, " liters is ", gall, " gallons")
    
  elif opi == 2:
    os.system("clear")
    mot = int(input("Enter the number of gallons: "))
    gra = mot * 3.78541
    os.system("clear")
    print(mot, "gallons is ", gra, "liters")
    cleaner()


def mlfloz():
  def cleaner():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()

  os.system("clear")
  print("""
  1. Milliliters to fluid ounces
  2. Fluid ounces to milliliters
  """)
  opi = int(input("Enter you option: "))
  if opi == 1:
    os.system("clear")
    mot = int(input("Enter the number of milliliters: "))
    ounces = mot * 0.033814
    os.system("clear")
    print(mot, " milliliters is ", ounces, " fluid ounces")
    
  elif opi == 2:
    os.system("clear")
    mot = int(input("Enter the number of fluid ounces: "))
    gra = mot * 29.5735
    os.system("clear")
    print(mot, " fluid ounces is ", gra, "milliliters")
    cleaner()


def graoun():
  def cleaner():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()

  os.system("clear")
  print("""
  1. Grams to ounces
  2. Ounces to grams
  """)
  opi = int(input("Enter you option: "))
  if opi == 1:
    os.system("clear")
    mot = int(input("Enter the number of grams: "))
    ounces = mot * 0.035274
    os.system("clear")
    print(mot, " grams is ", ounces, "ounces")
    
  elif opi == 2:
    os.system("clear")
    mot = int(input("Enter the number of ounces: "))
    gra = mot * 28.3495
    os.system("clear")
    print(mot, " ounces is ", gra, "grams")
    cleaner()

def monyear():
  def cleaner():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()

  os.system("clear")
  print("""
  1. Months to years
  2. Years to months
  """)
  opi = int(input("Enter you option: "))
  if opi == 1:
    os.system("clear")
    mot = int(input("Enter the number of months: "))
    years = mot / 12
    os.system("clear")
    print(mot, " months is ", years, "years")
    
  elif opi == 2:
    os.system("clear")
    years = int(input("Enter the number of years: "))
    months = years * 12
    os.system("clear")
    print(years, " years is ", months, "months")
    cleaner()

def distancefind():
  def cleaner():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()

  os.system("clear")
  print("""
  1. Miles to Kilometers
  2. Kilometers to Miles
  """)
  opi = int(input("Enter you option: "))
  if opi == 1:
    os.system("clear")
    dist = int(input("Enter the distance in miles: "))
    distkm = dist * 1.60934
    os.system("clear")
    print(dist, " miles is ", distkm, "kilometers")
    
  elif opi == 2:
    os.system("clear")
    dist = int(input("Enter the distance in kilometers: "))
    distmi = dist * 0.621371
    os.system("clear")
    print(dist, " kilometers is ", distmi, "miles")

  cleaner()

def finddivisor():
  def clean():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
    
  number = input("What number would you like to find the divisors of?: ")
  number = int(number)
  num2 = number

  abledivide = []
  
  while num2 > 0:
    if number % num2 == 0:
      abledivide.append(num2)
      num2 -= 1
    else:
      num2 -= 1

  divisors = 0

  os.system("clear")
  print("The divisors of", number, "are")
  for item in abledivide:
    divisors += 1
    print()
    print(divisors, ".", item)
  print()
  print("In total there are", divisors, "divisors")

def sleep_in():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  day = input("Is it a weekday? (Y)es or (N)o: ")
  vaca = input("Are you on vacation? (Y)es or (N)o:")
  if day == "Y".lower() or "YES".lower():
    weekday = True
  else:
    weekday = False
  
  if vaca == "Y".lower() or "YES".lower():
    vacation = True
  else:
    vacation = False
  
  os.system("clear")

  if vaca or not weekday:
    print("you can sleep in")
  else:
    print("You cannot sleep in today")
  clear()

def comparerandomnum():
  def clear():
    print()
    input("Press enter to continue...")
    robot_wait()
  comparison = input("How many numbers do you want to compare?: ")
  numlist = []
  comparison = int(comparison)
  while comparison > 0:
    number = random.randint(0, 9)
    numlist.append(number)
    comparison -= 1
  numlist.sort()
  os.system("clear")
  print("This list is sorted in ascending order")

  for item in numlist:
   print(item)

def riddley():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  ranornum = input("Would you like (R)andom or (N)umber?: ")

  r1 = "What has to be broken before you can use it?"
  r1ans = "AN EGG"

  r2 = "I'm tall when i'm young and i'm short when i'm old, What am I?"
  r2ans = "A CANDLE"

  r3 = "What month of the year has 28 days?"
  r3ans = "ALL OF THEM"

  r4 = "What is full of holes but still holds water?"
  r4ans = "A SPONGE"
  
  r5 = "What qouestion can you never answer yes to?"
  r5ans = "ARE YOU ASLEEP YET?"

  r6 = "What is always in front of you but can never be seen?"
  r6ans = "THE FUTURE"

  r7 = "There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?"
  r7ans = "THEY AREN'T ANY, IT IS A ONE STORY HOUSE"

  r8 = "What can you break, even if you never pick it up or touch it?"
  r8ans = "A PROMISE"

  r9 = "What goes up but never comes down?"
  r9ans = "YOUR AGE"

  r10 = "A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?"
  r10ans = "HE WAS BALD"

  r11 = "What gets wet while drying?"
  r11ans = "A TOWEL"

  r12 = "What can you keep after giving to someone?"
  r12ans = "YOUR WORD"

  r13 = "I shave every day, but my beard stays the same. What am I?"
  r13ans = "A BARBER"

  r14 = "You see a boat filled with people, yet there isn’t a single person on board. How is that possible?"
  r14ans = "THEY ARE ALL MARRIED"

  r15 = "You walk into a room that contains a match, a kerosene lamp, a candle and a fireplace. What would you light first?"
  r15ans = "A MATCH"
  
  r16 = "A man dies of old age on his 25 birthday. How is this possible?"
  r16ans = "HE WAS BORN ON FEBRUARY 29"

  r17 = "I have branches, but no fruit, trunk or leaves. What am I?"
  r17ans = "A BANK"

  r18 = "What can’t talk but will reply when spoken to?"
  r18ans = "AN ECHO"

  r19 = "The more of this there is, the less you see. What is it?"
  r19ans = "DARKNESS"

  r20 = "I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?"
  r20ans = "A SHADOW"

  if ranornum == "RANDOM".lower() or "R".lower():
    os.system("clear")
    rand = random.randint(1, 20)
    if rand == 1:
      print(r1)
      print()
      answe = input("What is the answer?: ")
      if answe == r1ans.lower():
        print("Correct")
      else:
        print("The answer is", r1ans.lower())

    elif rand == 2:
      print(r2)
      print()
      answe = input("What is the answer?: ")
      if answe == r2ans.lower():
        print("Correct")
      else:
        print("The answer is", r2ans.lower())
    
    elif rand == 3:
      print(r3)
      print()
      answe = input("What is the answer?: ")
      if answe == r3ans.lower():
        print("Correct")
      else:
        print("The answer is", r3ans.lower())

    elif rand == 4:
      print(r4)
      print()
      answe = input("What is the answer?: ")
      if answe == r4ans.lower():
        print("Correct")
      else:
        print("The answer is", r4ans.lower())
    
    elif rand == 5:
      print(r5)
      print()
      answe = input("What is the answer?: ")
      if answe == r5ans.lower():
        print("Correct")
      else:
        print("The answer is", r5ans.lower())
    
    elif rand == 6:
      print(r6)
      print()
      answe = input("What is the answer?: ")
      if answe == r6ans.lower():
        print("Correct")
      else:
        print("The answer is", r6ans.lower())

    elif rand == 7:
      print(r7)
      print()
      answe = input("What is the answer?: ")
      if answe == r7ans.lower():
        print("Correct")
      else:
        print("The answer is", r7ans.lower())

    elif rand == 8:
      print(r8)
      print()
      answe = input("What is the answer?: ")
      if answe == r8ans.lower():
        print("Correct")
      else:
        print("The answer is", r8ans.lower())

    elif rand == 9:
      print(r9)
      print()
      answe = input("What is the answer?: ")
      if answe == r9ans.lower():
        print("Correct")
      else:
        print("The answer is", r9ans.lower())

    elif rand == 10:
      print(r10)
      print()
      answe = input("What is the answer?: ")
      if answe == r10ans.lower():
        print("Correct")
      else:
        print("The answer is", r10ans.lower())

    elif rand == 11:
      print(r11)
      print()
      answe = input("What is the answer?: ")
      if answe == r11ans.lower():
        print("Correct")
      else:
        print("The answer is", r11ans.lower())

    elif rand == 12:
      print(r12)
      print()
      answe = input("What is the answer?: ")
      if answe == r12ans.lower():
        print("Correct")
      else:
        print("The answer is", r12ans.lower())
    
    elif rand == 13:
      print(r13)
      print()
      answe = input("What is the answer?: ")
      if answe == r13ans.lower():
        print("Correct")
      else:
        print("The answer is", r13ans.lower())

    elif rand == 14:
      print(r14)
      print()
      answe = input("What is the answer?: ")
      if answe == r14ans.lower():
        print("Correct")
      else:
        print("The answer is", r14ans.lower())
    
    elif rand == 15:
      print(r15)
      print()
      answe = input("What is the answer?: ")
      if answe == r15ans.lower():
        print("Correct")
      else:
        print("The answer is", r15ans.lower())
    
    elif rand == 16:
      print(r16)
      print()
      answe = input("What is the answer?: ")
      if answe == r16ans.lower():
        print("Correct")
      else:
        print("The answer is", r16ans.lower())

    elif rand == 17:
      print(r17)
      print()
      answe = input("What is the answer?: ")
      if answe == r17ans.lower():
        print("Correct")
      else:
        print("The answer is", r17ans.lower())

    elif rand == 18:
      print(r18)
      print()
      answe = input("What is the answer?: ")
      if answe == r18ans.lower():
        print("Correct")
      else:
        print("The answer is", r18ans.lower())

    elif rand == 19:
      print(r19)
      print()
      answe = input("What is the answer?: ")
      if answe == r19ans.lower():
        print("Correct")
      else:
        print("The answer is", r19ans.lower())

    elif rand == 20:
      print(r20)
      print()
      answe = input("What is the answer?: ")
      if answe == r20ans.lower():
        print("Correct")
      else:
        print("The answer is", r20ans.lower())

  else:
    os.system("clear")
    print("These are the riddles:")
    print()
    print("1.", r1)
    print()
    print("2.",r2)
    print()
    print("3.",r3)
    print()
    print("4.",r4)
    print()
    print("5.",r5)
    print()
    print("6.",r6)
    print()
    print("7.",r7)
    print()
    print("8.",r8)
    print()
    print("9.",r9)
    print()
    print("10.",r10)
    print()
    print("11.",r11)
    print()
    print("12.",r12)
    print()
    print("13.",r13)
    print()
    print("14.",r14)
    print()
    print("15.",r15)
    print()
    print("16.",r16)
    print()
    print("17.",r17)
    print()
    print("18.",r18)
    print()
    print("19.",r19)
    print()
    print("20.",r20)

    whichrid = input("Which riddle do you want?: ")
    whichrid = int(whichrid)

    if whichrid == 1:
      print(r1)
      print()
      answe = input("What is the answer?: ")
      if answe == r1ans.lower():
        print("Correct")
      else:
        print("The answer is", r1ans.lower())

    elif whichrid == 2:
      print(r2)
      print()
      answe = input("What is the answer?: ")
      if answe == r2ans.lower():
        print("Correct")
      else:
        print("The answer is", r2ans.lower())
    
    elif whichrid == 3:
      print(r3)
      print()
      answe = input("What is the answer?: ")
      if answe == r3ans.lower():
        print("Correct")
      else:
        print("The answer is", r3ans.lower())

    elif whichrid == 4:
      print(r4)
      print()
      answe = input("What is the answer?: ")
      if answe == r4ans.lower():
        print("Correct")
      else:
        print("The answer is", r4ans.lower())
    
    elif whichrid == 5:
      print(r5)
      print()
      answe = input("What is the answer?: ")
      if answe == r5ans.lower():
        print("Correct")
      else:
        print("The answer is", r5ans.lower())
    
    elif whichrid == 6:
      print(r6)
      print()
      answe = input("What is the answer?: ")
      if answe == r6ans.lower():
        print("Correct")
      else:
        print("The answer is", r6ans.lower())

    elif whichrid == 7:
      print(r7)
      print()
      answe = input("What is the answer?: ")
      if answe == r7ans.lower():
        print("Correct")
      else:
        print("The answer is", r7ans.lower())

    elif whichrid == 8:
      print(r8)
      print()
      answe = input("What is the answer?: ")
      if answe == r8ans.lower():
        print("Correct")
      else:
        print("The answer is", r8ans.lower())

    elif whichrid == 9:
      print(r9)
      print()
      answe = input("What is the answer?: ")
      if answe == r9ans.lower():
        print("Correct")
      else:
        print("The answer is", r9ans.lower())

    elif whichrid == 10:
      print(r10)
      print()
      answe = input("What is the answer?: ")
      if answe == r10ans.lower():
        print("Correct")
      else:
        print("The answer is", r10ans.lower())

    elif whichrid == 11:
      print(r11)
      print()
      answe = input("What is the answer?: ")
      if answe == r11ans.lower():
        print("Correct")
      else:
        print("The answer is", r11ans.lower())

    elif whichrid == 12:
      print(r12)
      print()
      answe = input("What is the answer?: ")
      if answe == r12ans.lower():
        print("Correct")
      else:
        print("The answer is", r12ans.lower())
    
    elif whichrid == 13:
      print(r13)
      print()
      answe = input("What is the answer?: ")
      if answe == r13ans.lower():
        print("Correct")
      else:
        print("The answer is", r13ans.lower())

    elif whichrid == 14:
      print(r14)
      print()
      answe = input("What is the answer?: ")
      if answe == r14ans.lower():
        print("Correct")
      else:
        print("The answer is", r14ans.lower())
    
    elif whichrid == 15:
      print(r15)
      print()
      answe = input("What is the answer?: ")
      if answe == r15ans.lower():
        print("Correct")
      else:
        print("The answer is", r15ans.lower())
    
    elif whichrid == 16:
      print(r16)
      print()
      answe = input("What is the answer?: ")
      if answe == r16ans.lower():
        print("Correct")
      else:
        print("The answer is", r16ans.lower())

    elif whichrid == 17:
      print(r17)
      print()
      answe = input("What is the answer?: ")
      if answe == r17ans.lower():
        print("Correct")
      else:
        print("The answer is", r17ans.lower())

    elif whichrid == 18:
      print(r18)
      print()
      answe = input("What is the answer?: ")
      if answe == r18ans.lower():
        print("Correct")
      else:
        print("The answer is", r18ans.lower())

    elif whichrid == 19:
      print(r19)
      print()
      answe = input("What is the answer?: ")
      if answe == r19ans.lower():
        print("Correct")
      else:
        print("The answer is", r19ans.lower())

    elif whichrid == 20:
      print(r20)
      print()
      answe = input("What is the answer?: ")
      if answe == r20ans.lower():
        print("Correct")
      else:
        print("The answer is", r20ans.lower())    
    clear()

presses = 0
def clicker():
  presses = 0
  def done():
    numguess = input("How many times do you think you clicked?: ")
    numguess = int(numguess)
    realguess = numguess - presses
    os.system("clear")
    print("your guess was", numguess)
    print()
    print("The answer is", presses)
    print("You were", realguess, "off")
  def click():
    os.system("clear")
    global presses
    presses += 1
    
  os.system("clear")
  root = tk.Tk()
  frame = tk.Frame(root)
  frame.pack()
  button = tk.Button(text="Click Me", command=click, height = "50", width = "100", bg = "green", activebackground = "green")
  button.pack(side=tk.BOTTOM)

  os.system("clear")
  root = tk.Tk()
  frame = tk.Frame(root)
  frame.pack()
  button = tk.Button(text="Quit", command=click, height = "50", width = "100", bg = "white", activebackground = "white", fg = "red")
  button.pack(side=tk.BOTTOM)

  root.mainloop()

def datetoday():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  today = date.today()
  d2 = today.strftime("%B %d, %Y")
  print("Today's date is", d2)

def shoppingcosts():
  def clean():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  #How many items?
  hmi = input("How many items did you buy?: ")
  hmi = int(hmi)
  items = []
  itemprices = []
  os.system("clear")
  while hmi > 0:
    item = input("What is the name of the item?: ")
    itemprice = input("How much was it?: ")
    itemprice = int(itemprice)
    items.append(item)
    itemprices.append(itemprice)
    hmi -= 1
  os.system("clear")
  print("Index.Name:Price ")
  print()
  for item in items:
    #item index
    itemin = items.index(item)
    val2 = itemprices[itemin]
    itemin = itemin + 1
    print("  ", itemin, ".", item, ":", val2)
    totalprice = sum(itemprices)
  print()
  print("Total price:", totalprice)


def findpercentage():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    exit()
  numper = input("What is the number you would like to find a percentage of?: ")
  numper = int(numper)
  percentage = input("What is the percentage you would like to find? Example(12, 20, 50, 200): ")
  percentage = int(percentage)
  num1 = numper / 100
  percentans = num1 * percentage
  os.system("clear")
  print(percentage, "% of", numper, "is", percentans)
  clear()

def weightconverter():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  print("Welcome to Weight Converter")
  print()
  print("""1. Kilogram
  2. Pounds""")
  #Weight Unit
  wunit = input("Which unit do you use to measure weight?: ")
  if wunit == "1" or "KILOGRAM".lower() or "KG".lower() or "KILO".lower():
    weight = input("What is the weight that you want to convert?: ")
    weight = int(weight)
    weightINpounds = weight * 2.205
    os.system("clear")
    print(weight, "kilograms is", weightINpounds, "pounds")
  else:
    weight = input("What is the weight that you want to convert?: ")
    weight = int(weight)
    weightINkilograms = weight / 2.205
    os.system("clear")
    print(weight, "pounds is", weightINkilograms, "kilograms")
    clear()

#Find Family Age
def ffage():
  def clear():
    print()
    print("Press enter to continue...")
    os.system("clear")
    robot_wait()

  #Number of family members
  nofm = input("How many people are in your family?: ")
  nofm = int(nofm)
  #family members
  fammemname = []
  fammemage = []
  num = 0

  os.system("clear")
  while nofm > 0:
    #family member name
    famnam = input("What is the family member's name?: ")
    #family member age
    fammembage = input("What is the family member's age?: ")
    fammembage = int(fammembage)
    nofm -= 1
    num += 1

    fammemname.append(famnam)
    fammemage.append(fammembage)
  os.system("clear")
  familyage = sum(fammemage)
  print("Number:Name:Age")
  print()
  for value in fammemname:
    index = fammemname.index(value)
    val2 = fammemage[index]
    index = index + 1 
    print(index, ".", value, ":", val2)
  print()
  print("Your family is", familyage, "years old")
  clear()

def findremainder():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  print("")
  divident = input("Enter the divident: ")
  divisor = input("Enter the divisor: ")
  divident = int(divident)
  divisor = int(divisor)
  quotient = divident // divisor
  remainder = divident % divisor
  os.system("clear")
  print(divident, "/", divisor, "=", quotient)
  print()
  if remainder == 0:
    print("You have no remainder")
  else:
    print("The remainder of", divident, "/", divisor, "=", remainder)
  clear()

def cbr(): 
  print("Welcome to Button Presser")
  print("Yeah, I don't know what to name this")
  print("Send me name suggestions at sarvesms@outlook.com or gamedev313@gmail.com")

  def clear():
    os.system("clear")
    print("If you find and bugs or have any suggestions send them to sarvesms@outlook.com or gamedev313@gmail.com")
    time.sleep(5)
    os.system("clear")
    exit()

  #number of presses

  wpr = 0
  blpr = 0
  rpr = 0
  grpr = 0
  blupr = 0
  cypr = 0
  yellpr = 0
  magenpr = 0


  def statlist():
    os.system("clear")
    totalpresses = int(wpr + blpr + rpr + grpr + blupr + cypr + yellpr + magenpr)
    print("White presses: ", wpr)
    print("Black presses: ", blpr)
    print("Red presses: ", rpr)
    print("Green presses: ", grpr)
    print("Blue presses: ", blupr)
    print("Cyan presses: ", cypr)
    print("Yellow presses: ", yellpr)
    print("Magenta presses: ", magenpr)
    print()
    print("Total presses: ", totalpresses)

  #color buttons
  def colw():
    global wpr
    os.system("clear")
    print("You pressed the white button")
    wpr += 1
    print("White presses: ", wpr)
  def colbl():
    global blpr
    os.system("clear")
    print("You pressed the black button")
    blpr += 1
    print("Black presses: ", blpr)
  def colr():
    global rpr
    os.system("clear")
    print("You pressed the red button")
    rpr += 1
    print("Red presses: ", rpr)
  def colgr():
    global grpr
    os.system("clear")
    print("You pressed the green button")
    grpr += 1
    print("Green presses: ", grpr)
  def colblu():
    global blupr
    os.system("clear")
    print("You pressed the blue button")
    blupr += 1
    print("Blue presses: ", blupr)
  def colcy():
    global cypr
    os.system("clear")
    print("You pressed the cyan button")
    cypr += 1
    print("Cyan presses: ", cypr)
  def colyell():
    global yellpr
    os.system("clear")
    print("You pressed the yellow button")
    yellpr += 1
    print("Yellow presses: ", yellpr)
  def colmagen():
    global magenpr
    os.system("clear")
    print("You pressed the magenta button")
    magenpr += 1
    print("Magenta presses: ", magenpr)
  
  root = tk.Tk()
  frame = tk.Frame(root)
  frame.pack()

  os.system("clear")
  button = tk.Button(text="White Button", command=colw, height = "2", width = "100", bg = "white", activebackground = "white")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Black Button", command=colbl, height = "2", width = "100", bg = "black", fg = "white", activebackground = "black")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Red Button", command=colr, height = "2", width = "100", bg = "red",   activebackground = "red")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Green Button", command=colgr, height = "2", width = "100", bg = "green", activebackground = "green")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Blue Button", command=colblu, height = "2", width = "100", bg = "blue", activebackground = "blue")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Cyan Button", command=colcy, height = "2", width = "100", bg = "cyan", activebackground = "cyan")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Yellow Button", command=colyell, height = "2", width = "100", bg = "yellow", activebackground = "yellow")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Magenta Button", command=colmagen, height = "2", width = "100", bg = "magenta", activebackground = "magenta")
  button.pack(side=tk.TOP)
  button = tk.Button(text="Stats", command=statlist, height = "5", width = "100", fg = "black", activebackground = "cyan")
  button.pack(side=tk.TOP)
  button = tk.Button(text="QUIT", command=clear, height = "5", width = "100", fg = "red", activebackground = "red")
  button.pack(side=tk.TOP)
  os.system("clear")

def multiplesfinder():
  def clear():
    input("Press enter to continue...")
    os.system("clear")
    print("Please wait...")
    time.sleep(3)
    os.system("clear")
    robot_wait()
    
  print("Welcome to Multiples")
  print()
  multiple = input("What number would you like to get multiples for?: ")
  multiple = int(multiple)
  #How many multiples?
  hmm = input("How many multiples would you like?: ")
  hmm = int(hmm)
  num = 1
  os.system("clear")
  print(hmm, "multiples of", multiple)
  print()
  while hmm > 0:
    multinum = multiple * num
    print(num, ":", multinum)
    num += 1
    hmm -= 1
  print()
  clear()


#find age of car
def faoc():
  def clear():
    print()
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  #Current year
  cy = datetime.now().year
  cy = int(cy)
  os.system("clear")
  PreOrNew = input("Did you buy your car new or pre owned?: ")
  if PreOrNew == "NEW".lower():
    os.system("clear")
    caryear = input("What year did you purchase your car?: ")
    caryear = int(caryear)
    if caryear == cy:
      os.system("clear")
      print("Your car is brand new")
      print()
      print("It hasn't even been one year since you bought your car")
    else:
      os.system("clear")
      carage = (cy - caryear)
      print("Your car is ", carage, " years old")
  else:
    os.system("clear")
    caryear = input("When was your car manufactured?: ")
    caryear = int(caryear)
    if caryear == cy:
      os.system("clear")
      print("Your car is brand new")
      print()
      print("It hasn't even been one year since your car was manufactured")
    else:
      os.system("clear")
      carage = (cy - caryear)
      print("Your car is ", carage, " years old")
  


tscore = int(0)
t2score = int(0)

def scorecount():
  #team score
  tscore = int(0)
  t2score = int(0)
  root = tk.Tk()
  frame = tk.Frame(root)
  frame.pack()
  myFont = font.Font(size=10)
  os.system("clear")

  def clear():
    os.system("clear")
    print(team1, ":", tscore)
    print(team2, ":", t2score)
    print()
    input("Press enter to continue...")
    robot_wait()

  #Add points
  def team1scored():
    global tscore
    tscore = tscore
    os.system("clear")
    print(team1, "Scored!!!")
    tscore += 1
    print(team1, ":", tscore)

  def team2scored():
    global t2score
    t2score = t2score
    os.system("clear")
    print(team2, "Scored!!!")
    t2score += 1
    print(team2, ":", t2score)

  #Subtract points
  def team1penalty():
    global tscore
    tscore = tscore
    os.system("clear")
    print(team1, "Penalized")
    tscore -= 1
    print(team1, ":", tscore)

  def team2penalty():
    global t2score
    t2score = t2score
    os.system("clear")
    print(team1, "Penalized")
    t2score -= 1
    print(team2, ":", t2score)
  
  team1 = input("What is the first team's name?: ")
  team11 = team1 + ":Add point"
  team12 = team1 + ":Subtract point"
  team2 = input("What is the second team's name?: ")
  team21 = team2 + ":Add point"
  team22 = team2 + ":Subtract point"
  team1color = input("Would you(1st team) like to be blue or red?: ")
  os.system("clear")

  if team1color == "BLUE".lower():
    button = tk.Button(text = team11, command = team1scored, bg = "blue", activebackground = "blue", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = team21, command = team2scored, bg = "red", activebackground = "red", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = team12, command = team1penalty, bg = "blue", activebackground = "blue", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = team22, command = team2penalty, bg = "red", activebackground = "red", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = "QUIT", command = clear, fg = "red", width = "20", height = "50",) 
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    root.mainloop()

  else:
    button = tk.Button(text = team11, command = team1scored, bg = "red", activebackground = "red", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = team21, command = team2scored, bg = "blue", activebackground = "blue", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = team12, command = team1penalty, bg = "red", activebackground = "red", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = team22, command = team2penalty, bg = "blue", activebackground = "blue", width = "20", height = "50", fg = "white")
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    button = tk.Button(text = "QUIT", command = clear, fg = "red", width = "20", height = "50",) 
    button['font'] = myFont
    button.pack(side = tk.LEFT)
    root.mainloop()

def drawshape():
  print("Welcome to Shapes")
  print()
  input("Press enter to continue...")
  os.system("clear")
  def drawsquare():
    turtle.shape("square")
  def drawtriangle():
    turtle.shape("triangle")
  def drawcircle():
    turtle.shape("circle")
  def drawoctagon():
    def oside():
      turtle.forward(90)
      turtle.left(45)
    oside()  
    oside()
    oside()
    oside()
    oside()
    oside()
    oside()
    oside()
  def drawrectangle():
    turtle.forward(130)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(130)
    turtle.left(90)
    turtle.forward(70)
  def drawpentagon():
    turtle.forward(45)
    turtle.left(70)
    turtle.forward(45)
    turtle.left(70)
    turtle.forward(45)
    turtle.left(70)
    turtle.forward(45)
    turtle.left(70)
    turtle.forward(45)
    turtle.left(70)
  def drawhexagon():
    turtle.forward(90)
    turtle.left(300)
    turtle.forward(90)
    turtle.left(300)
    turtle.forward(90)
    turtle.left(300)
    turtle.forward(90)
    turtle.left(300)
    turtle.forward(90)
    turtle.left(300)
    turtle.forward(90)
    turtle.left(300)
  #what shape?
  ws = input("What shape would you like to see?: ")
  os.system("clear")
  if ws == "SQUARE".lower():
    drawsquare()
  elif ws == "TRIANGLE".lower():
    drawtriangle()
  elif ws == "CIRCLE".lower():
    drawcircle()
  elif ws == "OCTAGON".lower():
    drawoctagon()
  elif ws == "RECTANGLE".lower():
    drawrectangle()
  elif ws == "PENTAGON".lower():
    drawpentagon()
  elif ws == "HEXAGON".lower():
    drawhexagon()
  else:
    print("Invalid input")
  input("Press enter to continue...")
  os.system("clear")
  robot_wait()

os.system("clear")
print("Welcome to Sarsoft Robot by Sarveshwar Senthilkumar\n")
print("Made by Sarveshwar Senthilkumar\n")

print("I hope you like this program\n")

print("If you would like to see more programs go to sarvesh313.wordpress.com")

print()

CanEnter = input("Press enter to continue...")

os.system("clear")

if CanEnter == "SARSOFTROBOT":
  print("If you want to go straight to the app, go to https://repl.it/@SarveshMercedes/SarsoftRobotApp#main.py")

  print()

  input("Press enter to continue...")
  
  os.system("clear")

print("Also, this is an app for computers, laptops and tablets")

print("I mean you can use it on a phone but it is not made for it")

print("")

input("Press enter to continue...")

os.system("clear")

def Duplicates():
  def end():
    os.system("clear")
    robot_wait()
  list = []
  print("Welcome to Duplicates")
  print()
  an = input("Enter how many value do you want to check?: ")
  an = int(an)
  while an > 0:
    os.system("clear")
    a = input("Enter a value: ")
    a = int(a)
    list.insert(an, a)
    an -= 1

  list.sort()

  def findduplicates(list):
    if len(list) == len(set(list)):
      return False
    else:
      return True 

  ifDuplicate = findduplicates(list)

  if ifDuplicate:
    os.system("clear")
    print(list)
    print("There are duplicates in this list")
  else:
    os.system("clear")
    print(list)
    print("There are no duplicates in this list")

  input("Press enter to continue...")
  end()

def AutoTakeoff():
  print("Hello", full_name)
  print()

  def RTakeoff():
    print("Rejecting Takeoff...")
    print("Closing Program...")
    Thrust = 0
    ParkingBrake = "On"
    Flaps = 0
    Speed = 0
    time.sleep(5)
    os.system("clear")
  
  Autopilot = "Off"
  AoA = (0)
  Altitude = (0)
  Thrust = (0)
  Speed = (0)
  TakeThrust = (80)
  Flaps = (0)
  F1 = (8)
  F2 = (11)
  F5 = (14)
  F10 = (19)
  F15 = (22)
  F25 = (26)
  F30 = (35)
  F40 = (46)
  FlapSettings = [F1, F2, F5, F10, F15, F25, F30, F40]
  TakeoffSpeed = int(input("What is the takeoff speed?: "))
  ParkingBrake = "On"

  os.system("clear")
  print("Setting thrust to 40%")
  print("Setting flaps 5")
  Thrust = (40)
  Flaps = F5
  FindError = input("Is there any problems? (Y)es or (N)o: ")
  os.system("clear")
  Prob = (("N").lower() or ("no").upper())

  if FindError == Prob:
    Thrust = TakeThrust
    Speed = TakeoffSpeed
    AoA = (10)
    Altitude = (1000)
    Autopilot = "On"
    ParkingBrake = "Off"
    print("Takeoff Successful")
    time.sleep(10)
    os.system("clear")
  elif FindError == ("Y").lower() or ("yes").upper():
    RTakeoff()
  
  print()
  print("Thank you for using SarsoftRobot")
  robot_wait()

def temperconvert():
  print("Hello", full_name)
  print()
  def convert_to_fahrenheit(celsius):
      c = celsius
      f = c * 9 / 5 + 32
      print('%r Celsius, converted to Fahrenheit, is: %r Fahrenheit.' % c, f)

  def convert_to_celsius(fahrenheit):
      f = fahrenheit
      c = (f - 32) * 5 / 9
      print('%r Fahrenheit, converted to Celsius, is: %r Celsius.' % f, c)
 
  print("1. Fahrenheit to Celsius")
  print("2. Celsius to Fahrenheit")
  print()
  whichconvert = input("Enter your option: ")
  whichconvert = int(whichconvert)
  temppp = input("Enter the temperature to convert: ")
  if whichconvert == 1:
    convert_to_celsius(temppp)
  elif whichconvert == 2:
    convert_to_fahrenheit(temppp)
  
  print()
  print("Thank you for using SarsoftRobot")
  robot_wait()

def comairinf():
  def end():
    input("Press enter to continue...")
    os.system("clear")
    robot_wait()
  #Planes from each manufacturer
  EmbraerP = ["135", "140", "145", "170", "175", "190", "195"]
  ATRP = ["42", "72"]
  BoeingP = ["737", "747", "777", "787"]
  AirbusP = ["A220", "A320", "A330", "A350", "A380"]
  def quest_wait():
    print("Welcome to Commercial Airplane Info")
    print()
    print("Boeing, Airbus, Embraer, ATR")
    #Plane Manufacturer
    pm = input("Which manufacturer would you like to know about?: ")
    os.system("clear")
    if pm == "AIRBUS".lower():
      for value in AirbusP:
        print("Airbus makes the", value)
    elif pm == "BOEING".lower():
      for value in BoeingP:
        print("Boeing makes the", value)
    elif pm == "EMBRAER".lower():
      for value in EmbraerP:
        print("Embraer makes the", value)
    elif pm == "ATR".lower():
      for value in ATRP:
        print("ATR makes the", value)
  

def typepractice():
  print("Hello", full_name)
  print()
  print("Welcome to Typing Practice")
  print()
  print("Enter the paragraph correctly: ")
  a = open("typingpara.txt", "r")
  for para in a:
    ang = random.randint(1, 3)
    if ang == 1:
      print(a.p1)
    elif ang == 2:
      print(a.p2) 
    elif ang == 3:
      print(a.p3)
  argnu = input(": ")
  if argnu in a:
    print("You typed in the paragraph correctly")
    print()
    print("Thank you for playing")
    print()
    robot_wait()
  else:
    print("You typed in the paragraph incorrectly")
    print()
    print("Thank you for playing")
    print()
    robot_wait()

print("SarsoftRobot")
print()
print("Version: There are no version numbers, it just gets updated\n")
print("Make sure to check in every once in a while")
print()
print("Made by Sarveshwar Senthilkumar")
print()
input("Press enter to continue...")
os.system("clear")

def bluer():
  print(Fore.BLUE)

def redder():
  print(Fore.RED)

def greener():
  print(Fore.GREEN)

def magentaer():
  print(Fore.MAGENTA)

def whiteback():
  print(Back.WHITE)

def blueback():
  print(Back.BLUE)

def redback():
  print(Back.RED)

def preent():
  input("Press enter to continue...")
  os.system("clear")

def appgame():
  ag = input("Do you think this is an app or a game?: ")

print("Welcome to SarsoftRobot")
print()
print("You can do a lot of things with Python")
print("This game/app was made from Python")
print()
print("You can check out more of my projects at sarvesh313.wordpress.com")
print()
print("This App/Game was built by Sarveshwar Senthilkumar")
print()
appgame()
print()
input("Press enter to continue...")
os.system("clear")


def InfoPro():
  with open:
    file1 = open("CodeLangInfo.txt","r") 
    print("Hello", full_name)
    print()
    print("Thank you for using SarsoftRobot")
    print()
    print("""1.Python
2.JavaScript
3.Java
4.C
5.C++
6.PHP
7.Swift
8.C#
9.Ruby
10.Objective-C
11.SQL
12.Kotlin
13.TypeScript
14.Go/GoLang
15.R
16.Erlang
17.Assembly
18.VBA
19.Lua
20.HTML""")
    print()
    ihuhj = input("Which language would you like to learn about?: ")
    igg = int(ihuhj)
    os.system("clear")
    if igg == 1:
      print(file1.Python)
      print()
      aghn = input("Would you like to know the official Python website?: ")
      print()
      if aghn == "Y".lower():
        print("It is python.org")
        print("Python is my favorite language")
      elif aghn == "YES".lower():
        print("It is python.org")
        print("Python is my favorite language")
      else:
        print("Before you leave I need to tell you that python is my favorite language.")
        print()
        print("Ok, Bye")
        print()
        print("Thank you for using SarsoftRobot ")

    elif igg == 2:
      print(file1.JavaScript)
      print()
      aghn = input("Would you like to know the official JavaScript website?: ")
      print()
      if aghn == "Y".lower():
        print("It is javaScript.com")
      elif aghn == "YES".lower():
        print("It is javaScript.com")
      else:
        print("Ok, Bye")

    elif igg == 3:
      print(file1.Java)
      print()
      aghn = input("Would you like to know the official Java website?: ")
      print()
      if aghn == "Y".lower():
        print("It is java.com")
      elif aghn == "YES".lower():
        print("It is java.com")
      else:
        print("Ok, Bye")

    elif igg == 4:
      print(file1.C)
      print()
      aghn = input("Would you like to know the official C website?: ")
      print()
      if aghn == "Y".lower():
        print("It is learn-C.org")
      elif aghn == "YES".lower():
        print("It is learn-C.org")
      else:
        print("Ok, Bye")

    elif igg == 5:
      print(file1.CPP)
      print()
      aghn = input("Would you like to know the official C++ website?: ")
      print()
      if aghn == "Y".lower():
        print("It is cplusplus.com")
      elif aghn == "YES".lower():
        print("It is cplusplus.com")
      else:
        print("Ok, Bye")

    elif igg == 6:
      print(file1.PHP)
      print()
      aghn = input("Would you like to know the official PHP website?: ")
      print()
      if aghn == "Y".lower():
        print("It is php.net")
      elif aghn == "YES".lower():
        print("It is php.net")
      else:
        print("Ok, Bye")

    elif igg == 7:
      print(file1.Swift)
      print()
      aghn = input("Would you like to know the official Swift website?: ")
      print()
      if aghn == "Y".lower():
        print("It is swift.org")
      elif aghn == "YES".lower():
        print("It is swift.org")
      else:
        print("Ok, Bye")

    elif igg == 8:
      print(file1.Csharp)
      print()
      aghn = input("Would you like to know the official C# website?: ")
      print()
      if aghn == "Y".lower():
        print("It is docs.microsoft.com/en-us/dotnet/csharp")
      elif aghn == "YES".lower():
        print("It is docs.microsoft.com/en-us/dotnet/csharp")
      else:
        print("Ok, Bye")

    elif igg == 9:
      print(file1.Ruby)
      print()
      aghn = input("Would you like to know the official Ruby website?: ")
      print()
      if aghn == "Y".lower():
        print("It is ruby-lang.org")
      elif aghn == "YES".lower():
        print("It is ruby-lang.org")
      else:
        print("Ok, Bye")

    elif igg == 10:
      print(file1.ObjectiveC)
      print()
      aghn = input("Would you like to know the official Objective-C website?: ")
      print()
      if aghn == "Y".lower():
        print("It is https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html, it does not have a website just a dev forum on Apple's website")
      elif aghn == "YES".lower():
        print("It is https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html")
      else:
        print("Ok, Bye")

    elif igg == 11:
      print(file1.SQL)
      print()
      aghn = input("Would you like to know the official SQL website?: ")
      print()
      if aghn == "Y".lower():
        print("It is MySQL.com")
      elif aghn == "YES".lower():
        print("It is MySQL.com")
      else:
        print("Ok, Bye")

    elif igg == 12:
      print(file1.Kotlin)
      print()
      aghn = input("Would you like to know the official Kotlin website?: ")
      print()
      if aghn == "Y".lower():
        print("It is kotlinlang.org")
      elif aghn == "YES".lower():
        print("It is kotlinlang.org")
      else:
        print("Ok, Bye")

    elif igg == 13:
      print(file1.TypeScript)
      print()
      aghn = input("Would you like to know the official TypeScript website?: ")
      print()
      if aghn == "Y".lower():
        print("It is typeScriptlang.org")
      elif aghn == "YES".lower():
        print("It is typeScriptlang.org")
      else:
        print("Ok, Bye")

    elif igg == 14:
      print(file1.GoGolang)
      print()
      aghn = input("Would you like to know the official Golang website?: ")
      print()
      if aghn == "Y".lower():
        print("It is golang.org")
      elif aghn == "YES".lower():
        print("It is golang.org")
      else:
        print("Ok, Bye")

    elif igg == 15:
      print(file1.R)
      print()
      aghn = input("Would you like to know the official R website?: ")
      print()
      if aghn == "Y".lower():
        print("It is r-project.org")
      elif aghn == "YES".lower():
        print("It is r-project.org")
      else:
        print("Ok, Bye")

    elif igg == 16:
      print(file1.Erlang)
      print()
      aghn = input("Would you like to know the official Erlang website?: ")
      print()
      if aghn == "Y".lower():
        print("It is erlang.org")
      elif aghn == "YES".lower():
        print("It is erlang.org")
      else:
        print("Ok, Bye")

    elif igg == 17:
      print(file1.Assembly)
      print()
      aghn = input("Would you like to know the official Assembly website?: ")
      print()
      if aghn == "Y".lower():
        print("It is webassembly.org")
      elif aghn == "YES".lower():
        print("It is webassenbly.org")
      else:
        print("Ok, Bye")

    elif igg == 18:
      print(file1.VBA)
      print()
      aghn = input("Would you like to know the official VisualBasic website?: ")
      print()
      if aghn == "Y".lower():
        print("It is code.visualbasic.com")
      elif aghn == "YES".lower():
        print("It is code.visualbasic.com")
      else:
        print("Ok, Bye")

    elif igg == 19:
      print(file1.Lua)
      print()
      aghn = input("Would you like to know the official Lua website?: ")
      print()
      if aghn == "Y".lower():
        print("It is lua.org")
      elif aghn == "YES".lower():
        print("It is lua.org")
      else:
        print("Ok, Bye")

    elif igg == 20:
      print(file1.HTML)
      print()
      aghn = input("Would you like to know the official HTML website?: ")
      print()
      if aghn == "Y".lower():
        print("It is html.com")
      elif aghn == "YES".lower():
        print("It is html.com")
      else:
        print("Ok, Bye")

    else:
      print("Invalid Input")
    print()
    robot_wait()

def DiceGame():
  Count=0
  Roll=0
  Previous_Roll=0

  def Start():
    print("Do you know how to play?")
    Begin=input("Y=Yes and N=No")
    Begin=Begin.upper()
    if Begin=="Y":
      print("")
      print("Good! We can continue!")
      return()
    if Begin=="N":
      print("")
      print("This is the higher or lower game, to win you must get 10 guesses in a row correct")
      print()
      print("The game will roll a number between 1 to 13")
      print()
      print("You have to guess if the next number will be higher or lower than the number rolled")
      print()
      print("Afterwards if your guess is correct you continue, if not it's GAME OVER")
      return()
    else:
      print("")
      print("You haven't answered with a valid selection choice, please try again")
      print("")
      Start()

  def Roll_Dice():
    global Roll
    Roll=random.randint(1,13)

  def Higher():
    global Roll
    global Previous_Roll
    global Correct
    if Roll>Previous_Roll or Roll==Previous_Roll:
      Correct=True
    else:
      Correct=False

  def Lower():
    global Roll
    global Previous_Roll
    global Correct
    if Roll<Previous_Roll or Roll==Previous_Roll:
      Correct=True
    else:
      Correct=False

  Start()
  Roll_Dice()
  print("")
  print("Let's Begin!")
  while Count!=10:
    print("")
    Previous_Roll=Roll
    print("Roll is:", Previous_Roll)
    print("Higher or Lower?")
    Guess=input("H=Higher, L=Lower")
    Guess=Guess.upper()
    Roll_Dice()
    Correct=False
    if Guess=="H":
      Higher()
    elif Guess=="L":
      Lower()
    print("")
    if Correct==True:
      print("Correct!")
      Count=Count+1
    if Correct==False:
      print("Wrong!")
      print("Roll was:",Roll)
      print("GAME OVER!")
      print("Better luck next time!")
      print("You got",Count)
      import sys
      robot_wait()
  print("")
  print("You guessed 10 times in a row!")
  print("Success!")
  print("Congratulations!")

def poemmaker():
  color = input("Enter a color: ")
  plural_noun = input("Enter a Plural noun: ")
  noun = input("Enter a noun: ")
  print("Roses are " +  color)
  print( plural_noun + " are blue")
  print("I " +  noun + " this game""")

def groceylist():
  groceryl = []  
  def asklist():
      numbb = 1
      lis = input("Grocery: ")
      while lis != "F".lower(): 
        lisa = lis
        groceryl.append(lisa)
        lis = input("Grocery: ")
      if lis == "F".lower():
        os.system("clear")
        for item in groceryl:
          print(numbb, ".", item)
          numbb += 1
  print(full_name,"'s Grocery List")
  print()
  print("Enter all the things in your Grocery List and when you're done enter F")
  print()
  asklist()

def rantee():
  goog = random.randint(0, 6)
  sent1 = "This was made by Sarveshwar Senthilkumar"
  sent2 = "If you want to sponsor this app,  Contact me at sarvesms@outlook.com or gamedev313@gmail.com"
  sent3 = "If you want to see the first version of this robot, Go to frobot.sarveshmercedes.repl.run"
  sent4 = "Remember if you have any suggestions email sarvesms@outlook.com or gamedev313@gmail.com"
  sent5 = "If you want to see more of my projects, Go to sarvesh313.wordpress.com"
  sent6 = "I have a lite version of this robot, Go to https://replit.com/@SarveshMercedes/SarsoftRobotLite, Some features are not available"
  ag = input("Is this an app or a game?: ")
  sentlist = [sent1, sent2, sent3, sent4, sent5, sent6, ag]
  print()
  print(sentlist[goog])
  print()

def yousearch():
  query_string = urllib.parse.urlencode({"search_query" : input("What would you like to search for?: ")})
  html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
  search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
  print("Watch this: http://www.youtube.com/watch?v=" + search_results[0]) 
  print()
  robot_wait()
def goosearch():
  print("Hello", full_name)
  print()
  query = input("What do you want to search?: ")  
  tl = input("Enter a Top-Level Domain: ")
  for j in search(query, tld = tl, num=10, stop=1, pause=2): 
    os.system("clear")
    print("Please Wait...")
    time.sleep(3)
    os.system("clear")
    print("You searched for", query)
    print("Your best result website is:")
    print()
    print(j) 
    print()
    print("This result is from the", tl, "TLD")
    print()
    an = input("Would you like to get more results? ((Y)es or (N)o): ")
    mubo = 1
    if an == "Y".lower():
      os.system("clear")
      print("If you would like to get as many results as possible, Enter Unlimited")
      print()
      que2 = input("How many more would you like to have?: ")
      if que2 != "UNLIMITED".lower():
        que2 = int(que2)
        for url in search(query, stop = que2):
          print(mubo, ".", url)
          mubo += 1
          print()
      elif que2 == "UNLIMITED".lower():
        que2 = 0
        for url in search(query):
          print(mubo, ".", url)
          mubo += 1
          print()
    elif an == "YES".lower():
      os.system("clear")
      que2 = input("How many more would you like to have?: ")
      for url in search(query, stop = que2):
        print(mubo, ".", url)
        mubo += 1
        print()
    else:
      os.system("clear")
      print("Ok")
      print()
    robot_wait()

today = date.today()
currentDT = datetime.now()
MyYName = "Sarveshwar Senthilkumar"
hour = currentDT.hour
minute = currentDT.minute
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
os.environ['TZ'] = 'North America/Chicago'

time2 = str(hour) + ":" + str(minute)

print("Today's date is", today)
print("The time is " + time2)
print()
print("My name is", MyYName)
print("")
print("I will be your host today")
print()
print("Nah, Just Kidding")
print()
print("You can do this by yourself")
print()
input("Press enter to continue...")
os.system("clear")

def calendar1():
  print("Hello", full_name)
  print()
  year = input("What year calendar would you like to see?: ")
  year1 = int(year)
  print("Ok")
  time.sleep(3)
  os.system("clear")
  print("Please Wait... Opening Calendar")
  time.sleep(3)
  os.system("clear")
  print(calendar.calendar(year1))
  robot_wait()

def randname():
  car = open("data.txt")
  car_names = []
  for line in car:
    a = line
    car_names.append(a)

  randomg = random.randint(0, len(car_names))

  ado = (car_names[randomg])

  print("Hello", full_name)
  print()
  time.sleep(2)
  os.system("clear")
  print("Please Wait...")
  print("Randomizing...")
  time.sleep(2)
  print("Your random car name is", ado)
  print()
  print("Press enter to continue...")
  os.system("clear")

def quit_game():
  confirmation = ("Do you sure you want to crash the game?: ")
  if confirmation == "YES".lower():
    print("Well then, Good Bye")
    ss()
  elif confirmation == "Y".lower():
    print("Well then, Good Bye")
    ss()
  else:
    print("Ok, I'll redirect you to the main menu")
    robot_main()

def pent():
  input("Press enter to continue...")

def sar():
  print("This was made by Sarveshwar Senthilkumar")

def p(a):
  print(a)

def pe():
  print()

def ts(a):
  import time
  time.sleep(a)

def ss():
  robot_wait()

def rant(a, s):
  random.randint(a, s)



def para():
  print("""Hello there, 
  I am the creator of this program. 
  Do you know my name?, Probably not. I told you but you didn't pay attention 
  My name is Sarveshwar, Wait..Wait...Wait.... 
  How did you get here?
  I will crash this program now
  because you're not suppose to see this
  Goodbye...""")
  pe()
  sar()
  pe()
  input("Press enter to continue...")
  
  robot_wait()

print("If this program does not run")
print()
print("If this program is very slow")
print("I have a lite version of this robot")
print()
print("Go to sarsoftrobotlite.sarveshmercedes.repl.run")
print()
print("It may not have the same features")
print()
print("Some features are not available")
pe()
sar()
pe()

input("Press enter to continue...")

os.system("clear")

os.system("clear")

a = 0

while a < 100:
  
  print("Loading", a, "%")

  a += 1

  print("Please wait...")

  print("Do not turn off your device or exit this program")

  print()

  print("If you exit this program you will have to download the packages again")

  import time
  time.sleep(0.2)

  os.system("clear")

print("")

print(Fore.RED)
print("""Welcome to 𝕊𝕒𝕣𝕤𝕠𝕗𝕥ℝ𝕠𝕓𝕠𝕥 """)
print(Style.RESET_ALL)
print("This program requires a lot of software to run")
print("So it may have took a long time to download")
print()
print("Do not turn off your device or change tabs")
print("Or you may have to load it again")
pe()
print("This is an app made by Sarveshwar Senthilkumar")
pe()
input("Press enter to continue...")

os.system("clear")

print(Fore.BLUE)
print(Style.BRIGHT)
asd1 = "YES"
asd2 = "Y"
asd = input("Would you like to have the Terms and Conditions dictated?: ")
if asd == asd1.lower():  
  os.system("clear")
  spech = """Welcome to SarsoftRobot

Terms and Conditions:

1. This program does log your data
2. Do not use tha name SarsoftRobot in your programs
3. Do not copy the code and call it something else
4. Do not copy this idea and create your own Sarsoft Robot
5. You have to agree to the Terms and Conditions to continue
6. If you do not agree to the Terms and Conditions you cannot play
7. If you have any suggestions email sarvesms@outlook.com or gamedev313@gmail.com
8. Do not use this code in any other app or games
9. Do not try to break the robot
10. Do not change the code in the robot
11. This program uses a different version of the Python Programming Language, do not change the version
12. Do not copy the robot idea
13. Do not copy the name it is copywrited
"""
  pe()
  sar()
  tts = gTTS(text = spech, lang = 'en')
  tts.save("good.wav")
  os.system("play good.wav")
  os.system("clear") 
elif asd == asd2.lower():  
  os.system("clear")
  spech = """Welcome to SarsoftRobot

Terms and Conditions:

1. This program does log your data
2. Do not use tha name SarsoftRobot in your programs
3. Do not copy the code and call it something else
4. Do not copy this idea and create your own Sarsoft Robot
5. You have to agree to the Terms and Conditions to continue
6. If you do not agree to the Terms and Conditions you cannot play
7. If you have any suggestions email sarvesms@outlook.com or gamedev313@gmail.com
8. Do not use this code in any other app or games
9. Do not try to break the robot
10. Do not change the code in the robot
11. This program uses a different version of the Python Programming Language, do not change the version
12. Do not copy the robot idea
13. Do not copy the name it is copywrited"""
  pe()
  sar()
  tts = gTTS(text=spech, lang='en')
  tts.save("good.wav")
  os.system("play good.wav")
  os.system("clear")

os.system("clear")

print("""Welcome to SarsoftRobot

Terms and Conditions:

1. This program does log your data
2. Do not use tha name SarsoftRobot in your programs
3. Do not copy the code and call it something else
4. Do not copy this idea and create your own Sarsoft Robot
5. You have to agree to the Terms and Conditions to continue
6. If you do not agree to the Terms and Conditions you cannot play
7. If you have any suggestions email sarvesms@outlook.com or gamedev313@gmail.com
8. Do not use this code in any other app or games
9. Do not try to break the robot
10. Do not change the code in the robot
11. This program uses a different version of the Python Programming Language, do not change the version
12. Do not copy the robot idea
13. Do not copy the name it is copywrited
""")
pe()
sar()

print(Style.RESET_ALL)
print(Fore.RED)

print("By going forward you agree to the Terms and Conditions")
  
print("If you don't agree enter N")
print()
asdf = input("(A)gree or (N)o: ")

if asdf == "N".lower():
  ss()

else:
  print("Ok, You can play")
  
os.system("clear")
print(Style.RESET_ALL)

first_name = input(str("Enter First Name: "))
print()
first_name = first_name + " "
last_name = input("Enter Last Name: ")
print()
full_name = str(first_name + last_name)

input("Press enter to continue...")
os.system("clear")
agein = input("What is your age?: ")

os.system("clear")

d = datetime.now()
timezone = pytz.timezone("America/Chicago")
d_aware = timezone.localize(d)
d_aware.tzinfo
utc_now = pytz.utc.localize(datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
pst_now = str(pst_now)

pst_now == utc_now

a = open("names.txt", "a")
a.write("\n")
a.write("\n")
a.write(full_name)
a.write(" / ")
a.write(pst_now)
a.close()

d = datetime.now()
timezone = pytz.timezone("America/Chicago")
d_aware = timezone.localize(d)
d_aware.tzinfo
utc_now = pytz.utc.localize(datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
pst_now = str(pst_now)

pst_now == utc_now

a = open("age.txt", "a")
a.write("\n")
a.write("\n")
a.write(agein)
a.write(" / ")
a.write(pst_now)
a.close()

firs_name = ("Sarveshwar ")
last_nam = ("Senthilkumar")
firs_name2 = ("Sarveshwar ")
last_nam2 = ("Senthilkumar")
firs_name1 = ("SARVESHWAR ")
last_nam1 = ("SENTHILKUMAR")
mname = str(firs_name + last_nam)
mname1 = str(firs_name1 + last_nam1)

if (full_name == mname.lower()):
  os.system("clear")
  print("Welcome back to Sarsoft Robot, Master")
  pe()
  input("Press enter to continue...")
  os.system("clear")
  print("Redirecting Immediately, Master")
  time.sleep(1)
  os.system("clear")
elif (full_name == "SENTHILKUMAR SUBRAMANIAN".lower()):
  os.system("clear")
  print("Welcome to Sarsoft Robot, Dad")
  pe()
  input("Press enter to continue...")
  os.system("clear")
  print("Redirecting,", full_name)
  time.sleep(4)
  os.system("clear")
elif (full_name == "SUBHALAKSHMI SENTHILKUMAR".lower()):
  os.system("clear")
  print("Welcome to Sarsoft Robot, Mom")
  pe()
  input("Press enter to continue...")
  os.system("clear")
  print("Redirecting,", full_name)
  time.sleep(4)
  os.system("clear")
elif (full_name == "SAR SEN".lower()):
  os.system("clear")
  print("Welcome to Sarsoft Robot, Secret Master")
  pe()
  input("Press enter to continue...")
  os.system("clear")
  print("Redirecting,", full_name)
  time.sleep(4)
  os.system("clear")
elif full_name == mname:
  os.system("clear")
  print("Welcome back to Sarsoft Robot, Master")
  pe()
  input("Press enter to continue...")
  os.system("clear")
  print("Redirecting Immediately, Master")
  time.sleep(1)
  os.system("clear")

elif full_name == mname.upper():
  os.system("clear")
  print("Welcome back to Sarsoft Robot, Master")
  pe()
  input("Press enter to continue...")
  os.system("clear")
  print("Redirecting Immediately, Master")
  time.sleep(1)
  os.system("clear")

else:
  os.system("clear")
  print("Welcome to Sarsoft Robot, Enjoy")
  pe()
  input("Press enter to continue...")
  os.system("clear")
  print("Redirecting,", full_name)
  time.sleep(4)
  os.system("clear")

os.system("clear")
spech = """Welcome to Sarsoft Robot"""
tts = gTTS(text=spech, lang='en')
tts.save("good.wav")
os.system("play good.wav")
os.system("clear")
os.system("clear")
os.system("clear")
spech = """Welcome to Sarsoft Robot"""
tts = gTTS(text=spech, lang='en')
tts.save("good.wav")
os.system("play good.wav")
os.system("clear")
os.system("clear")
print("Welcome to Sarsoft Robot")
pe()
print(Fore.RED, "|------------------------|")
print(Fore.RED, "|    _ _____             |")
print(Fore.YELLOW, "|   //     \             |")
print(Fore.BLUE, "|  | \____  \            |")
print(Fore.GREEN, "|  |      \  \_________  |")
print(Fore.MAGENTA, "|  | \____/ arveshwar's\ |")
print(Fore.RED, "|  |  Python Programs  / |")
print(Fore.RED, "| /___________________/  |")
print(Fore.YELLOW, "|________________________|")
print(Style.RESET_ALL)
pe()
print("Remember to look for bugs and suggestions")
pe()
print("If you have any suggestions email sarvesms@outlook.com or gamedev313@gmail.com")
pe()
input("Press enter to continue...")
time.sleep(3)
os.system("clear")
print("Ok, I will redirect you to a quick guide")
time.sleep(2)
os.system("clear")

def forrobot():
  myname = "Sarveshwar"
  print("Hello Friend")
  fname = input("What's your name? :")
  if fname == "SARSOFTROBOT":
    print("Yes Sir, I recognized you")
    print("You may enter")
    robot_wait()
  print(("Hi ") + (fname) + str(", my name is ") + (myname))
  fsubject = input("What's your favourite subject in school? :")
  msubject = "Math"
  print(("oh, favourite subject in school is ") + (fsubject) + (", my favourite subject in school is ") + (msubject))
  print("Bye")
  
  pe()

  robot_main()

def emerrobot_wait():
  print("Sorry, we got an emergency exit")
  print("")
  print("This was made by Sarveshwar Senthilkumar")
  pe()
  ss()

def sponsor():
  print("""If you want have your name written in here you can contact me at sarvesms@outlook.com or gamedev313@gmail.com and become a sponsor and your name can be on here
  """)
  pe()
  robot_wait()

def stot():
  print("Welcome to SarsoftRobot")

  print()

  print("This robot will be like a choose your own adventure book")

  print()

  print("You can choose your own adventure")

  print()

  print("Ok, hope you enjoy")

  print()

  print("Bye...")

  print()

  input("Press enter to continue...")

stot()

def tempe():
  os.system("clear")
  cod = input("How did you get here?: ")
  os.system("clear")
  print(cod, "?")
  time.sleep(4)
  print("Whatever")
  os.system("clear")
  print("Now that you're here I have some questions for you.")
  pe()
  a = input("Question number 1. Would you answer this question? ")
  print(a)
  input("Press enter to continue..")
  os.system("clear")
  print("Good, you passed my first test")
  print("You shall not pass the next one")
  pe()
  b = input("What is your name?: ")
  print(b, "?")
  print("Hi ", b)
  input("Press enter to continue...")
  os.system("clear")
  print("Next quest.. I ran out of questions")
  print("Ok fine, you passed")
  print("I will let you go as long as you tell me the password")
  print("You only get one try")
  pe()

  asd = input("What is the password?: ")
  asf = "SARSOFTROBOT"

  if asd == asf.lower():
    os.system("clear")
    print("You found it")
    print("As I told you you may leave")
    robot_wait()

  else:
    print("I am extremely sorry my friend")
    print("I have to abandon you too")
    print("The password was....")
    print("Just kidding I'm not going to tell you")
    print("Goodbye...")
    input("Press enter to continue...")

    emerrobot_wait()
    
    os.system("clear")
    ss()

  
  time.sleep(2)
  print("Bye")

def choice():
  qeus = input("How many choices do you want to choose from?: ")
  ques = int(qeus)
  ques = ques - 1 
  bh = random.randint(0, ques)
  ad = -1
  lis = []
  os.system("clear")
  print("Please Wait..")
  time.sleep(3)
  can = 0 
  while ques > ad:
    os.system("clear")
    can = ques + 1
    ane = input("Enter a choice: ")
    anop = ane
    lis.append(anop)
    ques = ques - 1
    os.system("clear")

  print(lis[bh])

  input("Press enter to continue...")
  os.system("clear")
  robot_wait()

def add2():
  anum = random.randint(1, 10000000000000)
  bnum = random.randint(1, 10000000000000)
  cnum = anum + bnum
  stre = anum, "+", bnum, "= "
  print("C =", anum, "+", bnum)
  abn = input("What is C?: ")
  abnm = int(abn)
  if abnm == cnum:
    os.system("clear")
    print("Correct")
    pe()
    print("You're good at Math")
  else:
    os.system("clear")
    print("Wrong!!")
    pe()
    print("Good try")

def game():
  def add():

    os.system("clear")

    anum = random.randint(1, 10000000000000)

    bnum = random.randint(1, 10000000000000)

    cnum = anum + bnum

    stre = anum, "+", bnum, "= "

    print("A =", anum, "+", bnum)

    abn = input("What is A?: ")

    abnm = int(abn)

    if abnm == cnum:

      os.system("clear")

      print("Correct")

      pe()

      print("You're good at Math")

      pe()

      input("Press enter to continue...")
    
      isCorrect = True


    else:
      os.system("clear")

      print("Wrong")

      pe()
      print("Good try")
    
      isCorrect = False

    if isCorrect == True:
      add()

    elif isCorrect == False:
      print("Game Over")
  

  def add1():

    os.system("clear")

    anum = random.randint(1, 10000000000000)

    bnum = random.randint(1, 10000000000000)

    cnum = anum + bnum

    stre = anum, "+", bnum, "= "

    print("A =", anum, "+", bnum)

    abn = input("What is A?: ")

    abnm = int(abn)

    if abnm == cnum:

      os.system("clear")

      print("Correct")

      pe()

      print("You're good at Math")

      pe()

      input("Press enter to continue...")
    
      isCorrect = True


    else:
      os.system("clear")

      print("Wrong")

      pe()
      print("Good try")

    
      isCorrect = False 

    if isCorrect == True:
      add()
    elif isCorrect == False:
      print("Game Over")
      
  add1()
  robot_wait()

def game3():
  isCorrect = False
  poi1 = 0

  def add():

    os.system("clear")

    anum = random.randint(1, 100000)

    bnum = random.randint(1, 100000)

    cnum = anum + bnum

    stre = anum, "+", bnum, "= "

    print("A =", anum, "+", bnum)

    abn = input("What is A?: ")

    abnm = int(abn)

    if abnm == cnum:

      os.system("clear")

      print("Correct")

      pe()

      print("You're good at Math")

      pe()

      input("Press enter to continue...")
    
      isCorrect = True


    else:
      os.system("clear")

      print("Wrong")

      pe()
      print("Good try")
    
      isCorrect = False

    if isCorrect == True:
      add()

    elif isCorrect == False:
      print("Game Over")

  def add1():

    os.system("clear")

    anum = rant(1, 100000)

    bnum = rant(1, 100000)

    cnum = anum + bnum

    stre = anum, "+", bnum, "= "

    print("A =", anum, "+", bnum)

    abn = input("What is A?: ")

    abnm = int(abn)

    if abnm == cnum:

      os.system("clear")

      print("Correct")

      pe()

      print("You're good at Math")

      pe()

      input("Press enter to continue...")
    
      isCorrect = True


    else:
      os.system("clear")

      print("Wrong")

      pe()
      print("Good try")

    
      isCorrect = False 

    if isCorrect == True:
      add()
    elif isCorrect == False:
      print("Game Over")
      
  add1()
  robot_wait()

def game2():
  isCorrect = False
  poi1 = 0

  def add():

    os.system("clear")

    anum = rant(1, 100000000)

    bnum = rant(1, 100000000)

    cnum = anum + bnum

    stre = anum, "+", bnum, "= "

    print("A =", anum, "+", bnum)

    abn = input("What is A?: ")

    abnm = int(abn)

    if abnm == cnum:

      os.system("clear")

      print("Correct")

      pe()

      print("You're good at Math")

      pe()

      input("Press enter to continue...")
    
      isCorrect = True


    else:
      os.system("clear")

      print("Wrong")

      pe()
      print("Good try")

    
      isCorrect = False
    if isCorrect == True:
      add()
    elif isCorrect == False:
      print("Game Over")
  

  def add1():
  

    os.system("clear")

    anum = rant(1, 100000000)

    bnum = rant(1, 100000000)

    cnum = anum + bnum

    stre = anum, "+", bnum, "= "

    print("A =", anum, "+", bnum)

    abn = input("What is A?: ")

    abnm = int(abn)

    if abnm == cnum:

      os.system("clear")

      print("Correct")

      pe()

      print("You're good at Math")

      pe()

      input("Press enter to continue...")
    
      isCorrect = True


    else:
      os.system("clear")

      print("Wrong")

      pe()
      print("Good try")

    
      isCorrect = False 

    if isCorrect == True:
      add()
    elif isCorrect == False:
      print("Game Over")
      
  add1()
  robot_wait()

def ranhome():
  lk = rant(1,3)
  os.system("clear")
  print("Please Wait")
  print("Randomizing...")
  time.sleep(3)
  os.system("clear")
  if lk == 1:
    game()
  if lk == 2:
    game2()
  if lk == 3:
    game3()

def ga():
  os.system("clear")
  print("Welcome to MathGame")
  pe()
  print("1. Easy Mode")
  print("2. Medium Mode")
  print("3. Hard Mode")
  print("4. Random Mode")
  ghj = input("What mode would you like?:")
  os.system("clear")
  if ghj == "1":
    game3()
  elif ghj == "2":
    game2()
  elif ghj == "3":
    game()
  elif ghj == "4":
    ranhome()
  else:
    print("Invalid input")
    pe()
    robot_wait()

def tellice():
  print("Enter 'Ice Cream Randomizer' as an option in my app")
  input("Press enter to continue...")
  os.system("clear")

def tell():
  print("Enter sing song as an option in my app")
  input("Press enter to continue...")
  os.system("clear")

def randtellyou():
  abnmj = rant(1, 2)
  print(Fore.GREEN)
  if abnmj == 1:
    tell()
  elif abnmj == 2:
    tellice()

def dictator():
  os.system("clear")
  print("""Chinese
         zh-cn : Chinese (Mandarin/China)
         zh-tw : Chinese (Mandarin/Taiwan)
         Indian Languages
         ta : Tamil(Tamil Nadu, India)
         te : Telugu(Andhra Pradesh, etc)
        African:
        af : Afrikaans(Africa)
        Asia:
        hi : Hindustani(South Asia)
        ja : Japanese(Japan)
        English
         en-us :  English (US)  
         en-ca :  English (Canada)  
         en-uk :  English (UK)  
         en-gb :  English (UK)  
         en-au :  English (Australia)  
         en-gh :  English (Ghana)  
         en-in :  English (India)  
         en-ie :  English (Ireland)  
         en-nz :  English (New Zealand)  
         en-ng :  English (Nigeria)  
         en-ph :  English (Philinputpines)  
         en-za :  English (South Africa)  
         en-tz :  English (Tanzania)  
        French
         fr-ca :  French (Canada)  
         fr-fr :  French (France)  
        Portuguese
         pt-br :  Portuguese (Brazil)  
         pt-pt :  Portuguese (Portugal)  
        Spanish
         es-es :  Spanish (Spain)  
         es-us :  Spanish (United States) """)
  spech = input("What would you like the robot to say?: ")
  os.system("clear")
  print("""Chinese
         zh-cn : Chinese (Mandarin/China)
         zh-tw : Chinese (Mandarin/Taiwan)
         Indian Languages
         ta : Tamil(Tamil Nadu, India)
         te : Telugu(Andhra Pradesh, etc)
        African:
        af : Afrikaans(Africa)
        Asia:
        hi : Hindustani(South Asia)
        ja : Japanese(Japan)
        English
         en-us :  English (US)  
         en-ca :  English (Canada)  
         en-uk :  English (UK)  
         en-gb :  English (UK)  
         en-au :  English (Australia)  
         en-gh :  English (Ghana)  
         en-in :  English (India)  
         en-ie :  English (Ireland)  
         en-nz :  English (New Zealand)  
         en-ng :  English (Nigeria)  
         en-ph :  English (Philinputpines)  
         en-za :  English (South Africa)  
         en-tz :  English (Tanzania)  
        French
         fr-ca :  French (Canada)  
         fr-fr :  French (France)  
        Portuguese
         pt-br :  Portuguese (Brazil)  
         pt-pt :  Portuguese (Portugal)  
        Spanish
         es-es :  Spanish (Spain)  
         es-us :  Spanish (United States) """)
  print("Language code above ")
  lann = input("What language do you want him to say it in?: ")
  tts = gTTS(text=spech, lang = lann )
  tts.save("good.wav")
  os.system("play good.wav")
  os.system("clear")
  robot_wait()
def pORc(): 
  inu = input("Enter a number: ")
  inuu = int(inu)
  os.system("clear")
  print("Please Wait...")
  time.sleep(3)
  os.system("clear")
  if inuu % 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 == 0:
    print(inuu, "is a composite number")
  else:
    print(inuu, "is a prime number")  
  input("Press enter to continue...")
  os.system("clear")
  robot_wait()
def QT():
  na = input("Enter a number between 1 and 15: ")
  os.system("clear")
  aa = "'It does'nt matter how many lines of code you write, all that matters is how beautiful the program is'"
  ab = "'Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it.'"
  ac = "'If a man does not keep pace with his companions, perhaps it is because he hears a different drummer. Let him step to the music which he hears, however measured or far away.'"
  ad = "'You know you’re in love when you can’t fall asleep because reality is finally better than your dreams.'"
  ae = "'I’m selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can’t handle me at my worst, then you sure as hell don’t deserve me at my best'"
  af = "'Get busy living or get busy dying.'"
  ag = "'The first step toward success is taken when you refuse to be a captive of the environment in which you first find yourself'"
  ah = "'When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us'"
  ai = "'Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do'"
  aj = "'When I dare to be powerful – to use my strength in the service of my vision, then it becomes less and less important whether I am afraid'"

  ak = "'Be yourself; everyone else is already taken'"

  al = "'Two things are infinite: the universe and human stupidity; and I'm not sure about the universe'"

  am = "'So many books, so little time'"

  an = "'Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.'"
  
  ao = "'A room without books is like a body without a soul'"

  if (na == "1"):
    print(aa)
  elif (na == "2"):
    print(ab)
  elif (na == "3"):
    print(ac)
  elif (na == "4"):
    print(ad)
  elif (na == "5"):
    print(ae)
  elif (na == "6"):
    print(af)
  elif (na == "7"):
    print(ag)
  elif (na == "8"):
    print(ah)
  elif (na == "9"):
    print(ai)
  elif (na == "10"):
    print(aj)
  elif (na == "11"):
    print(ak)
  elif (na == "12"):
    print(al)
  elif (na == "13"):
    print(am)
  elif (na == "14"):
    print(an)
  elif (na == "15"):
    print(ao)
  else:
    print("Invalid input")
  pe()
  robot_wait()

def findicecream():
  os.system("clear")

  time.sleep(3)
  os.system("clear")
  a = 1
  b = 3
  c = 2
  print("Please Wait...")
  time.sleep(3)
  os.system("clear")
  randnum = random.randint(1, 3)
  a = "Ice Cream Fudgestick"
  b = "Ice Cream Cone"
  c = "Ice Cream Sandwich"
  aa = "Vanilla Caramel"
  bb = "Vanilla"
  cc = "Chocolate"
  if randnum == 1:
    print(a)
    input("Press enter to continue...")
    pe()
  elif randnum == 2:
    print(b)
    randnum2 = rant(1, 3)
    input("Press enter to continue...")
    os.system("clear")
    pe()
    if randnum2 == 1:
      print(aa)
      input("Press enter to continue...")
      pe()
    elif randnum2 == 2:
      print(bb)
      input("Press enter to continue...")
      pe()
    elif randnum2 == 3:
      print(cc)
      input("Press enter to continue...")
      pe()
  elif randnum == 3:
    print(c)
    input("Press enter to continue...")
    pe()
  print()
  input("Press enter to continue...")
  os.system("clear")
  
def findicecream1():
  os.system("clear")
  print("Starting secret program")
  time.sleep(3)
  os.system("clear")
  a = 1
  b = 3
  print("Secret Faster Edition!!!")
  time.sleep(2)
  os.system("clear")
  randnum = rant(a, b)
  a = "Ice Cream Fudgestick"
  b = "Ice Cream Cone"
  c = "Ice Cream Sandwich"
  aa = "Vanilla Caramel"
  bb = "Vanilla"
  cc = "Chocolate"
  if randnum == 1:
    print(a)
    input("Press enter to continue...")
    pe()
  elif randnum == 2:
    print(b)
    randnum2 = rant(1, 3)
    input("Press enter to continue...")
    if randnum2 == 1:
      print(aa)
      input("Press enter to continue...")
    elif randnum2 == 2:
      print(bb)
      input("Press enter to continue...")
    elif randnum2 == 3:
      print(cc)
      input("Press enter to continue...")
  elif randnum == 3:
    print(c)
    input("Press enter to continue...")
  os.system("clear")

def strmulti():
  os.system("clear")
  print("Welcome to Matrix Multiplier")
  stri1 = input("Enter a matrix you want to multiply: ")
  numbo = input("How many times do you want to multiply your matrix?: ")
  numb = int(numbo)
  time.sleep(1)
  os.system("clear")
  print("Please Wait...")
  time.sleep(3)
  finmat = stri1*numb
  print(finmat)
  robot_wait()
def findicecream():
  os.system("clear")
  print("Starting program")
  time.sleep(3)
  os.system("clear")
  a = 1
  b = 3
  print("Please Wait...")
  print("Randomizing")
  time.sleep(3)
  os.system("clear")
  randnum = rant(a, b)
  a = "Ice Cream Fudgestick"
  b = "Ice Cream Cone"
  c = "Ice Cream Sandwich"
  aa = "Vanilla Caramel"
  bb = "Vanilla"
  cc = "Chocolate"
  if randnum == 1:
    print(a)
    input("Press enter to continue...")
  elif randnum == 2:
    print(b)
    randnum2 = random.randint(1, 3)
    input("Press enter to continue...")
    if randnum2 == 1:
      print(aa)
      input("Press enter to continue...")
    elif randnum2 == 2:
      print(bb)
      input("Press enter to continue...")
    elif randnum2 == 3:
      print(cc)
      input("Press enter to continue...")
  elif randnum == 3:
    print(c)
    input("Press enter to continue...")
  os.system("clear")

def sectimer():
  second = input("How many seconds do you want to be timed?: ")
  secon = int(second)
  print("Starting in 3")
  time.sleep(1)
  print("Starting in 2")
  time.sleep(1)
  print("Starting in 1")
  time.sleep(1)
  os.system("clear")
  while secon > -1:
      print(secon, "left")
      time.sleep(1)
      secon = secon - 1
      os.system("clear")

  print("Your time is over")
  print("Thank you for using Second Timer")
  pe()
  robot_wait()
def conday():
  weeks = input("How many weeks?: ")
  weeee = input("How many days?: ")
  dd = int(weeks)
  ddd = (dd*7)
  weee = int(weeee)
  day = 0
  day = weee + ddd
  print("There are", day, "days in", weeks, "weeks and", weeee, "days")
  pe()
  robot_wait()
def conhour():
  week = input("How many weeks?: ")
  day = input("How many days?: ")
  hour = input("How many hours?: ")
  we = int(week)
  d = int(day)
  ho = int(hour)
  hou = 0
  for week in week:
    hou += 168
  for day in day:
    hou += 24
  hou = hou + ho
  print("There are", hou, "hours in", day, "days and", week, "weeks")
  pe()
  robot_wait()
def conmin():
  week = input("How many weeks?: ")
  day = input("How many days?: ")
  hour = input("How many hours?: ")
  minute = input("How many minutes?: ")
  we = int(week)
  d = int(day)
  ho= int(hour)
  minuo = int(minute)
  min = 0
  for week in week:
    min += 10080
  for day in day:
    min += 1440
  for hour in hour:
    min += 60
  min = min + minuo
  print("There are", min, "minutes in", week, "weeks,", day, "days,", hour, "hours, and", minute, "minutes")
  pe()
  robot_wait()
def consec():
  week = input("How many weeks?: ")
  day = input("How many days?: ")
  hour = input("How many hours?: ")
  minute = input("How many minutes?: ")
  second = input("How many seconds?: ")
  wee = int(week)
  da = int(day)
  hou = int(hour)
  minu = int(minute)
  seco = int(second)
  sec = 0
  for week in week:
    sec += 604800
  for day in day:
    sec += 86400
  for hour in hour:
    sec += 3600
  for minute in minute:
    sec += 60
  sec = sec + seco
  print("There are", sec, "seconds in", day, "days", hour, "hours,", minute, "minutes and", second, "seconds")
  pe()
  robot_wait()

def spread():
  mat = input("Enter a matrix: ")
  os.system("clear")
  for letter in mat:
    print(letter)
    time.sleep(1)
  pe()
  print("Matrix:", mat)
  pe()
  time.sleep(5)
  robot_wait()

def WPM():
  WP = input("Enter your Words Per Minute: ")
  W = int(WP)
  CPM = (W*5)
  PPM = (W/200)
  os.system("clear")
  print("Please Wait")
  time.sleep(5)
  os.system("clear")
  print(W, "Words Per Minute")
  print(CPM, "Characters Per Minute")
  print(PPM, "Paragraph Per Minute")
  robot_wait()
def oORe():
  num = input("Enter a number: ")
  Num = int(num)
  os.system("clear")
  print("Please Wait")
  time.sleep(6)
  if (Num % 2) == 0:
    print("Even")
  else:
    print("Odd")
  print("Thank you for using Odd or Even")
  robot_wait()

def bye():
  print("Ok, I gotta go now")
  print("It's been nice talking to you")
  print("It's also been nice playing with you")
  print(("Bye ") + (firstname))

  q = input("Do you think i'm programmed well? : ")
  if q.lower() == "no":
    print("Oh ok")
    hy = input("Why do you think i'm programmed bad?:")
    print("Oh, thank you for your feedback")
  else:
    print("Thank you")
  
  os.system("clear")

  print("Thanks for using Srobot")
  pe()
  print("This is my logo")
  print("|------------------------|")
  print("|    _ _____             |")
  print("|   //     \             |")
  print("|  | \____  \            |")
  print("|  |      \  \_________  |")
  print("|  | \____/ arveshwar's\ |")
  print("|  |  Python Programs  / |")
  print("| /___________________/  |")
  print("|________________________|")  
  print("you can contact the creator at sarvesms@outlook.com or gamedev313@gmail.com")
  pe()
  print("This was made by Sarveshwar Senthilkumar")
  input("Press enter to continue...")
  os.system("clear")
  print("This was made by Sarveshwar Senthilkumar")
  
def end():
  os.system("clear")
  print("Thanks for using Srobot")
  pe()
  print("This is my logo")
  print("|------------------------|")
  print("|    _ _____             |")
  print("|   //     \             |")
  print("|  | \____  \            |")
  print("|  |      \  \_________  |")
  print("|  | \____/ arveshwar's\ |")
  print("|  |  Python Programs  / |")
  print("| /___________________/  |")
  print("|________________________|")  
  print("you can contact the creator at sarvesms@outlook.com or gamedev313@gmail.com")
  pe()
  print("This was made by Sarveshwar Senthilkumar")
  input("Press enter to continue...")
  os.system("clear")
  print("This was made by Sarveshwar Senthilkumar")
def crArr():
  import os
  bDay = input("When is your Birthday?: ")
  bYear = input("What is your Birthyear?: ")
  Age = input("What is your age?: ")
  FirNa = input("What is your first name?: ")
  LasNa = input("What is your last name?: ")
  bPlace = input("Where is your birthplace?: ")
  Name = FirNa + " " + LasNa
  os.system("clear")
  print(Name, ": ")
  Person = {"Name" : Name, "Birthday" : bDay, "Birthyear" : bYear, "Age" : Age, "Birthplace" : bPlace}
  print(Person)
  input("Press enter to continue...")
  os.system("clear")
  robot_wait()

def numcount():
  am = input("Enter a number matrix or numbers: ")
  numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
  numycount = 0
  for number in am:
    if number in numbers:
      numycount += 1
    else:
      pe()
  os.system("clear")
  print("Please Wait....")
  time.sleep(4)
  print("Matrix:", am)
  print("There are", numycount, "numbers in your matrix")
  robot_wait()

def vowelcoun():
  jmatrix = input("Enter a Matrix or Word: ")
  mat = int(len(jmatrix))
  vowel = ("AEIOU").lower()
  consonants = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ").lower()
  vowcoun = 0
  concoun = 0
  for letter in jmatrix:
    if letter in vowel:
      vowcoun += 1
    elif letter in consonants:
      concoun += 1
    else:
      pe()      
  os.system("clear")
  print("Please Wait...")
  time.sleep(5)
  os.system("clear")
  print("Matrix:", jmatrix)
  pe()
  print("There are", vowcoun, "vowels in your matrix")
  conson = input("Do you want to see how many consonants are in your matrix?: ")
  if conson == "YES".lower():
    os.system("clear")
    print("There are", concoun, "consonants in your matrix")
  elif conson == "Y".lower():
    os.system("clear")
    print("There are", concoun, "consonants in your matrix")
  else:
    print("Oh ok")
  print("Thank you for using vowel counter")
  input("Press enter to continue...")
  os.system("clear")
  robot_wait()

def reverser():
  print("Welcome to the Sentence Reverser")
  sent = input("Enter a sentence or word to be reversed: ")
  os.system("clear")
  print("Please Wait...")
  print("Go check out more programs at sarvesh313.wordpress.com")
  time.sleep(5)
  os.system("clear")
  revsent = str(sent[::-1])
  print("Your sentence reversed is:")
  print(revsent)
  pe()
  input("Press enter to continue...")
  os.system("clear")
  robot_wait()
def calculator():
  print("Welcome to The Calculator")
  def add(x, y):
   return x + y

  def subtract(x, y):
   return x - y

  def multiply(x, y):
   return x * y

  def divide(x, y):
   return x / y

  def square(x):
    return x * x

  def calcend():
    print("Thank you for using my calculator")
    print("Check out more programs at sarvesh313.wordpress.com")
    time.sleep(3)
    os.system("clear")
    robot_wait()

  print("Select operation")
  print("1.Add")
  print("2.Subtract")
  print("3.multiply")
  print("4.Divide")
  print("5.Square")

  choice = input("Enter choice(1/2/3/4/5):")

  num1 = int(input("Enter first number: "))
  
  if choice == "5":
    print()
  else:
    num2 = int(input("Enter second number: "))
  os.system("clear")
  if choice == '1':
    print("Please Wait...")
    time.sleep(4)
    print(num1, "+", num2, "=", add(num1,num2))
    calcend()

  elif choice == '2':
    print("Please Wait...")
    time.sleep(4)
    print(num1, "-", num2, "=", subtract(num1,num2))
    calcend()

  elif choice == '3':
    print("Please Wait...")
    time.sleep(4)
    print(num1, "*", num2, "=", multiply(num1,num2))
    calcend()

  elif choice == '4':
    print("Please Wait...")
    time.sleep(4)
    print(num1, "/", num2, "=", divide(num1,num2))
    calcend()
  
  elif choice == '5':
    print("Please Wait...")
    time.sleep(4)
    print(num1 , "=", square(num1), "squared")
    calcend()

  else:
     print("Invalid input")
     calcend()

def robotrigenerator():
  def Let():
    string.ascii_letters
    os.system("clear")
    print("Please Wait...")
    print("Check out more programs at sarvesh313.wordpress.com")
    time.sleep(4)
    os.system("clear")
    print("Your random letter is", random.choice(string.ascii_letters))
    ts(9)
    os.system("clear")

  def Num():
    os.system("clear")
    a = int(input("Starting Number: "))
    b = int(input("Ending Last Number: ")) 
    os.system("clear")
    print("Please Wait...")
    print("Check out more programs at sarvesh313.wordpress.com")
    time.sleep(4)
    os.system("clear")
    print("Your random number is", rant(a, b))
    ts(9)
    os.system("clear")

  def LetNum():
    string.ascii_letters
    os.system("clear")
    a = int(input("Starting Number: "))
    b = int(input("Ending Last Number: ")) 
    os.system("clear")
    print("Please Wait...")
    print("Check out more programs at sarvesh313.wordpress.com")
    time.sleep(4)
    os.system("clear")
    print("Your random code is", (random.choice(string.ascii_letters)) + str(rant(a, b)))
    ts(9)
    os.system("clear")

  def Endo():
    ag = input("Have you seen my website?: ")
    if ag == "YES".lower() or "Y".lower():
      print("Ok, There are many programs on my website ")
      ab = input("Do you like my programs?: ")
      if ab == "YES".lower() or "Y".lower():
        print("Thank you")
        print("I'm glad you like it,")
        print("I spent a lot of time on it")
      else:
        print("Oh ok")
    else:
      print("Go see my website at sarvesh313.wordpress.com")
    time.sleep(3)
    print("You have reached the end of the program")
    print("Thank you for playing") 
    pres = input("Press enter to continue...")
    os.system("clear") 

  print("Welcome to Random Generator")
  print("Please Wait... Loading")
  time.sleep(3)
  os.system("clear")
  pe()
  print("1.Only Letters[1]")
  print("2.Only Numbers[2]")
  print("3.Numbers and Letters[3]")
  pe()
  L = "1"
  N = "2"
  LN = "3"
  type = input("Which Setting?: ")

  if type == L:
    Let()
    Endo()

  if type == N:
    Num()
    Endo()

  if type == LN:
    LetNum()
    Endo()
  robot_wait()
def robotwcount():
  print("Welcome to Word Counter")
  inup = input("Enter some characters: ")
  sp = " "
  num = 1
  for le in inup:
    if le == sp:
      num = num + 1
  print(num)
  ts(8)
  robot_wait()

def robot_wait():
  os.system("clear")
  input("Press enter to continue..")
  robot_main() 

def robotcounter():
  print("Welcome to Character Counter!")
  abcd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z", " "]
  numsi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  eup = input("Enter some letters, numbers or something: ")
  num = 0
  for let in eup:
    if let.lower() in abcd or numsi:
        num = num + 1
    elif let not in abcd or numsi:
      print("Invalid input")
    else:
      print(num)
  print(num, "Characters")
  robot_wait()

def robo_speech():
  spech = input("What do you want me to say?: ")
  tts = gTTS(text=spech, lang='en')
  tts.save("good.wav")
  os.system("play good.wav")
  print("please wait.. loading")
  time.sleep(5)
def robot_fib():
  n = input("Enter a number: ")
  a = 0
  b = 1
  fibnum = [0,1]
  count = 2
  while count < int(n):
    c = (a + b)
    count += 1
    fibnum.insert(count,c)
    a = b
    b = c
  j = 0
  for num in fibnum:
    j += 1
    print(str(j), "-> ", num)
  robot_wait()
def robot_dice():

  randomnumber = rant(1, 6)
  print("The dice rolls", randomnumber)

  e = input("Do you want to roll again.. press 'Y' to continue, 'N' to exit: ")
  os.system("clear")

  d = datetime.now()
  timezone = pytz.timezone("America/Chicago")
  d_aware = timezone.localize(d)
  d_aware.tzinfo
  utc_now = pytz.utc.localize(datetime.utcnow())
  pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
  pst_now = str(pst_now)

  pst_now == utc_now

  a = open("dice.txt", "a")
  a.write("\n")
  a.write("\n")
  a.write(randomnumber)
  a.write(" / ")
  a.write(pst_now)
  a.close()

  if (e =='Y') or (e == 'y'):
    robot_dice()
  else:
    robot_wait()
def speech():
    print("Welcome to Robo Talk \n")
    robo_speech()
    robot_wait()
def fibonaccinums():
    print("Welcome to Fibonacci Series Center \n")
    robot_fib()
def dice():
    print("Welcome to Dice Table \n")
    robot_dice()
def guide():
    print("Help Page: \n")
    print("Welcome to Robot Sarvesh")
    pe()
    print("In Robot Sarvesh you have many programs you can run with the click of two keys")
    pe()
    asd = input("Would you like to have the sentence dictated?: ")
    if asd == asd1.lower():
      os.system("clear")
      spech = """
      
      1. In Speech, you enter a saying and then a robot says it
2.In Fibonnacci Numbers, you can find out numbers of fibonnacci
3.In Dice, you can generate a random number between 1 through 6
4.In Character Counter, you can enter in characters and it will count how many there are
5.In Word Counter you can count how many words there are
6.In Random Generator you can get a random code, letter or numbers
7.In Calculator you can Add, Subtract, Divide or multiply numbers
8.In Word Reverser you can reverse sentences and words
9.In Vowel and Consonant counter you can count how many vowels and consonants are in your matrix
10.In Number Counter you count how many numbers are in your matrix
11.In Array Generator you can generate an array for anyone you want
12.In Odd or Even you can find out if a number is odd or even
13.In How Fast You Type you have to enter your words per minute and it will tell you how many characters and paragraph per minute
14.In Matrix Vertical you can spell out a matrix vertically
15.In Second Counter you can turn weeks, days, hours, and minutes into seconds
16.In Minute Counter turn weeks, days, hours and seconds into minutes
17.In Hour Counter you can turn weeks and days into hours
18.In Day Counter you can turn weeks into days
19.In Second Timer you can time yourself as many seconds as you want
20.In Matrix Multiplier you can enter a matrix and a multinputle and you get your matrix multiplied by your multinputle
21.In Quote Teller you can enter a number and it will tell you a quote
22.In Prime or Composite you can find out if a number is a prime number or a composite number
23.In Dictator you can enter a word, phrase, sentence, matrix, numbers, songs, or stories and enter a language and he will tell you it in that language
24.In MathGame you can practice adding numbers
25.In Choice Chooser you can enter the number of choices and then enter the choices and it will choose a random choice
26.In Sponsor List you can see all the sponsors that have sponsored this app and how you can get your name on that list of sponsors
27.In SarsoftRobot you can see the first version of this robot SarsoftRobot
28.In RPS you can play Rock Paper Scissors against a robot
29.In Name Randomizer you can get a random name 
30. In Calendar you can get any year calendar you want
31. In Search you can search something and you can get a webiste for that specific query
32. In YouSearch you can search for a specific query and it will suggest a video for you to watch
33. In Grocery List you can make a grocery list and it will remind you
34. In Poem Maker you can make a poem
35. In Higher or Lower you can choose higher or lower and there will be a random number either higher or lower
36. In LangInfo you can learn about a specific programming language.
37. In Typing Practice you can type paragraphs and practice typing
38. In Temperature Converter you can convert temperatures to the other temperature system
39. In Auto Takeoff Simulator you can simulate a takeoff
40. In Duplicates you can see if there is any duplicates in your matrix
41. In Commercial Aircraft Info you can see which manufacturer makes which planes
42. In Shapes you can see shapes, I mean what did you expect?
43. In Scoreboard you can keep track of the score 
44. In Car's Age you can see how old your car is
45. In Multiple Find you can find the multiples of a number
46. In Color Button presses you can press colorful buttons and learn colors
47. In Find Remainder you can divide and find the answer as well as the remainder
48. In Family Age you can find out your family's age
49. In Weight Converter you can convert pounds into kilograms or kilograms into pounds
50. In Percentage Finder you can find a percentage of a number
51. In Shopping Receipt you can list your items and their prices and you can find out the total price
52. In Today's Date you can see today's date
53. In Clicker ypou can click a button as many times as you want
54. In Riddles you can do some riddles
55. In Random Greater or Lower you can get as many random numbers as you want and then you can compare them
56. In Sleep In you can find out if you can sleep in or not
57. In Find Divisors you can find divisors for a specific number
58. In Miles to Kilometers you can convert miles to kilometers and kilometers to miles
59. In Months to year you can convert months to years or years to months
60. In Grams to ounces you can convert grams to ounces or convert ounces to grams
61. In Milliliters to fluid ounces you can convert milliliters to fluid ounces or fluid ounces to milliliters
62. In Liters to gallons you can convert liters to gallons or gallons to liters
63. In Feet to meters you can convert feet to meters and meters to feet
64. In Find Palindrome you can enter some letters and it will try to find a palindrome with those letters
65. In Currency Rates you can find out the rate of a currency to a different currency
66. In Factorial FInder you can find the factorial of a number
67. In Leap Year you can find out which years are leap years
68. In Business Sim you can simulate a business
69. In Tax Calculator you enter the price and the tax rate and you can find the total price with taxes
70. In Random Card Generator you get a random card generated
"""
      tts = gTTS(text=spech, lang='en')
      tts.save("good.wav")
      os.system("play good.wav")
      print("Please Wait")
      time.sleep(5)
      os.system("clear")
      input("Press enter to continue...")
      os.system("clear")
    pe()
    print("Thank you for choosing Robot Sarvesh")
    print("Hope you enjoy Robot Sarvesh")
    pe()
    print(Fore.YELLOW)
    print(Style.BRIGHT)
    print("1. In Speech, you enter a saying and then a robot says it")
    print("2.In Fibonnacci Numbers, you can find out numbers of fibonnacci")
    print("3.In Dice, you can generate a random number between 1 through 6")
    print("4.In Character Counter, you can enter in characters and it will count how many there are")
    print("5.In Word Counter you can count how many words there are")
    print("6.In Random Generator you can get a random code, letter or numbers  ")
    print("7.In Calculator you can Add, Subtract, Divide or multiply numbers")
    print("8.In Word Reverser you can reverse sentences and words")
    print("9.In Vowel and Consonant counter you can count how many vowels and consonants are in your matrix")
    print("10.In Number Counter you count how many numbers are in your matrix")
    print("11.In Array Generator you can generate an array for anyone you want")
    print("12.In Odd or Even you can find out if a number is odd or even")
    print("13.In How Fast You Type you have to enter your words per minute and it will tell you how many characters and paragraph per minute")
    print("14.In Matrix Vertical you can spell out a matrix vertically")
    print("15.In Second Counter you can turn weeks, days, hours, and minutes into seconds")
    print("16.In Minute Counter turn weeks, days, hours and seconds into minutes")
    print("17.In Hour Counter you can turn weeks and days into hours")
    print("18.In Day Counter you can turn weeks into days")
    print("19.In Second Timer you can time yourself as many seconds as you want")
    print("20.In Matrix Multiplier you can enter a matrix and a multinputle and you get your matrix multiplied by your multinputle")
    print("21.In Quote Teller you can enter a number and it will tell you a quote")
    print("22.In Prime or Composite you can find out if a number is a prime number or a composite number")
    print("23.In Dictator you can enter a word, phrase, sentence, matrix, numbers, songs, or stories and enter a language and he will tell you it in that language")
    print("24.In MathGame you can practice adding numbers")
    print("25.In Choice Chooser you can enter the number of choices and then enter the choices and it will choose a random choice")
    print("26.In Sponsor List you can see all the sponsors that have sponsored this app and how you can get your name on that list of sponsors")
    print("27.In SarsoftRobot you can see the first version of this robot SarsoftRobot")
    print("28.In RPS you can play Rock Paper Scissors against a robot")
    print("29.In Name Randomizer you can get a random name")
    print("30. In Calendar you can get any year calendar you want")
    print("31. In Search you can search something and you can get a website for that specific query")
    print("32. In YouSearch you can search for a specific query and it will suggest a video for you to watch")
    print("33. In Grocery List you can make a grocery list and it will remind you")
    print("34. In Poem Maker you can make a poem")
    print("35. In Higher or Lower you can choose higher or lower and there will be a random number either higher or lower")
    print("36. In LangInfo you can learn about a specific programming language.")
    print("37. In Typing Practice you can type paragraphs and practice typing")
    print("38. In Temperature Converter you can convert temperatures to the other temperature system")
    print("39. In Auto Takeoff Simulator you can simulate a takeoff")
    print("40. In Duplicates you can see if there is any duplicates in your matrix")
    print("41. In Commercial Aircraft Info you can see which manufacturer makes which planes")
    print("42. In Shapes you can see shapes, I mean what did you expect?")
    print("43. In Scoreboard you can keep track of the score")
    print("44. In Car's Age you can see how old your car is")
    print("45. In Multiple Find you can find the multiples of a number")
    print("46. In Color Button presses you can press colorful buttons and learn colors")
    print("47. In Find Remainder you can divide and find the answer and the remainder")
    print("48. In Family Age you can find out your family's age")
    print("49. In Weight Converter you can convert pounds into kilograms or kilograms into pounds")
    print("50. In Percentage Finder you can find a percentage of a number")
    print("51. In Shopping Receipt you can list your items and their prices and you can find out the total price")
    print("52. In Today's Date you can see today's date")
    print("53. In Clicker you can click a button as many times as you want")
    print("54. In Riddles you can do some riddles")
    print("55. In Random Greater or Lower you can get as many random numbers as you want and then you can compare them")
    print("56. In Sleep In you can find out if you can sleep in or not")
    print("57. In Find Divisors you can find divisors for a specific number")
    print("58. In Miles to Kilometers you can convert miles to kilometers and kilometers to miles")
    print("59. In Months to year you can convert months to years or years to months")
    print("60. In Grams to ounces you can convert grams to ounces or convert ounces to grams")
    print("61. In Milliliters to fluid ounces you can convert milliliters to fluid ounces or fluid ounces to milliliters")
    print("62. In Liters to gallons you can convert liters to gallons or gallons to liters")
    print("63. In Feet to meters you can convert feet to meters and meters to feet")
    print("64. in Find Palindrome you can enter some letters and it will try to find a palindrome with those letters")
    print("65. In Currency Rates you can find out the rate of a currency to a different currency")
    print("66. In Factorial FInder you can find the factorial of a number")
    print("67. In Leap Year you can find out which years are leap years")
    print("68. In Business Sim you can simulate a business")
    print("69. In Tax Calculator you enter the price and the tax rate and you can find the total price with taxes")
    print("70. In Random Card Generator you get a random card generated")
    pe()
    print(Style.RESET_ALL)
    input("Press enter to continue...")
    robot_wait()
def robot_wait2():
    e = input("Are you sure you want to exit.. press 'Y' to exit: ")
    os.system("clear")
    print()
    if (e =='Y') or (e == 'y'):
      print("It was nice to see you in my app")
      a = date.today()
      print("This was the version of", a)
      print()
      print("Good Bye.. exiting Robo meet., see you again")
      bye()

      os.system("clear")
    else:
      robot_main()
def exit1():
    os.system("clear")
    os.system("clear")
    nm = input("Are you sure you want to exit.. press 'Y' to exit: ")
    if (nm =='Y') or (nm == 'y'):
      print("Good Bye.. exiting Robo meet., see you again")
      bye()
      quit()
      os.system("clear")
    else:
      robot_main()
def pOptions():
    print("Welcome to Robot Sarvesh...\n")
    pe()
    asd = input("Would you like to have the options dictated?: ")
    print(Fore.BLUE)
    print(Style.BRIGHT)
    if asd == asd1.lower():      
      os.system("clear")
      spech = """1. Speech
      2. Fibonacci Numbers
      3. Dice
      4. Character Counter
      5. Word Counter
      6. Random Generator
      7. The Calculator
      8. Word Reverser
      9. Vowel and Consonant Counter
      10. Number Counter
      11. Array Generator
      12. Odd or Even
      13. How Fast You Type
      14. Matrix Vertical
      15. Second Counter
      16. Minute Counter
      17. Hour Counter
      18. Day Counter
      19. Second Timer
      20. Matrix Multiplier
      21. Quote Teller
      22. Prime or Composite
      23. Dictator
      24. MathGame
      25. Choice Chooser
      26. Sponsor List
      27. SarsoftRobot
      28. RPS
      29. Name Randomizer
      30. Calendar
      31. Search
      32. YouSearch
      33. Grocery List
      34. Poem Maker
      35. Higher or Lower
      36. LangInfo
      37. Typing Practice
      38. Temperature Converter
      39. Auto Takeoff Simulator
      40. Duplicates
      41. Commercial Aircraft Info
      42. Shapes
      43. Scoreboard
      44. Car's Age
      45. Multiple Finder
      46. Color Button Presses
      47. Find Remainder
      48. Family Age
      49. Weight Converter
      50. Percentage Finder
      51. Shopping Receipt
      52. Today's Date
      53. Clicker
      54. Riddles
      55. Random Greater or Lower
      56. Sleep In
      57. Find Divisors
      58. Miles to Kilometers
      59. Months to years
      60. Grams to ounces
      61. Milliliters to fluid ounces
      62. Liters to gallons
      63. Feet to meters
      64. Find Palindrome
      65. Currency Rates
      66. Factorial Finder
      67. Leap Year
      68. Business Sim
      69. Tax Calculator
      70. Random Card Genereator
      71. Help
      72. Exit"""
      tts = gTTS(text=spech, lang='en')
      tts.save("good.wav")
      os.system("play good.wav")
      print("Please Wait")
      time.sleep(5)
      os.system("clear")
      input("Press enter to continue...")
      os.system("clear")
    print("I recommend going to the help page to see what the programs can do.")
    print()
    input("Press enter to continue...")
    os.system("clear")
    print("Welcome to Robot Sarvesh...\n")
    print("1. Speech")
    print("2. Fibonacci Numbers")
    print("3. Dice")
    print("4. Character Counter")
    print("5. Word Counter")
    print("6. Random Generator")
    print("7. The Calculator")
    print("8. Word Reverser")
    print("9. Vowel and Consonant Counter")
    print("10. Number Counter")
    print("11. Array Generator")
    print("12. Odd or Even")
    print("13. How Fast You Type")
    print("14. Matrix Vertical")
    print("15. Second Counter")
    print("16. Minute Counter")
    print("17. Hour Counter")
    print("18. Day Counter")
    print("19. Second Timer")
    print("20. Matrix Multiplier")
    print("21. Quote Teller")
    print("22. Prime or Composite")
    print("23. Dictator")
    print("24. MathGame")
    print("25. Choice Chooser")
    print("26. Sponsor List")
    print("27. SarsoftRobot")
    print("28. RPS")
    print("29. Name Randomizer")
    print("30. Calendar")
    print("31. Search")
    print("32. YouSearch")
    print("33. Grocery List")
    print("34. Poem Maker")
    print("35. Higher or Lower")
    print("36. LangInfo")
    print("37. Typing Practice ")
    print("38. Temperature Converter")
    print("39. Auto Takeoff Simulator")
    print("40. Duplicates")
    print("41. Commercial Aircraft Info")
    print("42. Shapes")
    print("43. Scoreboard")
    print("44. Car's Age")
    print("45. Multiple Finder")
    print("46. Color Button Presses")
    print("47. Find Remainder")
    print("48. Family Age")
    print("49. Weight Converter")
    print("50. Percentage Finder")
    print("51. Shopping Receipt")
    print("52. Today's Date")
    print("53. Clicker")
    print("54. Riddles")
    print("55. Random Greater or lower")
    print("56. Sleep In")
    print("57. Find Divisors")
    print("58. Miles to Kilometers")
    print("59. Months to years")
    print("60. Grams to ounces")
    print("61. Milliliters to fluid ounces")
    print("62. Liters to gallons")
    print("63. Feet to meters")
    print("64. Find Palindrome")
    print("65. Currency Rates")
    print("66. Factorial Finder")
    print("67. Leap Year")
    print("68. Business Sim")
    print("69. Tax Calculator")
    print("70. Random Card Generator")
    print("71. Help")
    print("72. Exit")
    print(Style.RESET_ALL)

def robot_main():
  os.system("clear")
  input("Press enter to continue...")
  os.system("clear")
  pOptions()
  
  print(Fore.RED)
  lis = []
  print("Recent Search History: ")
  for item in lis:
    print(item)
    d = datetime.now()

    timezone = pytz.timezone("America/Chicago")

    d_aware = timezone.localize(d)

    d_aware.tzinfo

    utc_now = pytz.utc.localize(datetime.utcnow())

    pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))

    pst_now = str(pst_now)

    pst_now == utc_now
    a = open("searchapphistory.txt", "a")
    a.write("\n")
    a.write("\n")
    a.write(lis)
    a.write(" / ")
    a.write(pst_now)
    a.close()
    
    os.system("clear")
    aaa = "Y"
  
  print(Fore.BLUE)
  print(Style.BRIGHT)
  argument = input("Enter your option: ")

  lis.append(argument)

  os.system("clear")

  if (argument == "1"):  
         
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """1. In Speech, you enter a saying and then a robot says it"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("1. In Speech, you enter a saying and then a robot says it")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           robo_speech()
         else:
           robot_wait2()

  elif (argument == "2"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """2.In Fibonnacci Numbers, you can find out numbers of fibonnacci"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("2.In Fibonnacci Numbers, you can find out numbers of fibonnacci")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           fibonaccinums()
         else:
           robot_wait2()
    
  elif (argument == "3"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """3.In Dice, you can generate a random number between 1 through 6"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("3.In Dice, you can generate a random number between 1 through 6")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           dice()
         else:
           robot_wait2()
        
  elif (argument == "71"):
         guide()
        
  elif (argument == "4"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """4.In Character Counter, you can enter in characters and it will count how many there are"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("4.In Character Counter, you can enter in characters and it will count how many there are")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           robotcounter()
         else:
           robot_wait2()

  elif (argument == "72"):
        robot_wait2()

  elif (argument == "5"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """5.In Word Counter you can count how many words there are"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("5.In Word Counter you can count how many words there are")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           robotwcount()
         else:
           robot_wait2()

  elif (argument == "6"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """6.In Random Generator you can get a random code, letter or numbers  """
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("6.In Random Generator you can get a random code, letter or numbers  ")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           robotrigenerator()
         else:
           robot_wait2()

  elif (argument == "7"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """7.In Calculator you can Add, Subtract, Divide or multiply numbers"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("7.In Calculator you can Add, Subtract, Divide or multiply numbers")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           calculator()
         else:
           robot_wait2()

  elif (argument == "8"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """8.In Word Reverser you can reverse sentences and words"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("8.In Word Reverser you can reverse sentences and words")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           reverser()
         else:
           robot_wait2()

  elif (argument == "9"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """9.In Vowel and Consonant counter you can count how many vowels and consonants are in your matrix"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("9.In Vowel and Consonant counter you can count how many vowels and consonants are in your matrix")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           vowelcoun()
         else:
           robot_wait2()

  elif (argument == "10"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """10.In Number Counter you count how many numbers are in your matrix"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("10.In Number Counter you count how many numbers are in your matrix")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           numcount()
         else:
           robot_wait2()

  elif (argument == "11"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """11.In Array Generator you can generate an array for anyone you want"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("11.In Array Generator you can generate an array for anyone you want")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           crArr()
         else:
           robot_wait2()
 
  elif (argument == "12"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """12.In Odd or Even you can find out if a number is odd or even"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("12.In Odd or Even you can find out if a number is odd or even")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           oORe()
         else:
           robot_wait2()
   
  elif (argument == "13"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """13.In How Fast You Type you have to enter your words per minute and it will tell you how many characters and paragraph per minute(You need to know your Words Per Minute, Go to NitroType.com and find out your WPM(Recommended))"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("13.In How Fast You Type you have to enter your words per minute and it will tell you how many characters and paragraph per minute(You need to know your Words Per Minute, Go to NitroType.com and find out your WPM(Recommended))")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           WPM()
         else:
           robot_wait2()
    
  elif (argument == "14"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """14.In Matrix Vertical you can spell out a matrix vertically"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("14.In Matrix Vertical you can spell out a matrix vertically")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           spread()
         else:
           robot_wait2()
        
  elif (argument == "15"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """15.In Second Counter you can turn weeks, days, hours, and minutes into seconds"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("15.In Second Counter you can turn weeks, days, hours, and minutes into seconds")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           consec()
         else:
           robot_wait2()
       
  elif (argument == "16"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """16.In Minute Counter turn weeks, days, hours and seconds into minutes"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("16.In Minute Counter turn weeks, days, hours and seconds into minutes")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           conmin()
         else:
           robot_wait2()
        
  elif (argument == "17"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """17.In Hour Counter you can turn weeks and days into hours"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("17.In Hour Counter you can turn weeks and days into hours")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           conhour()
         else:
           robot_wait2()
       
  elif (argument == "18"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """18.In Day Counter you can turn weeks into days"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("18.In Day Counter you can turn weeks into days")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           conday()
         else:
           robot_wait2()
       
  elif (argument == "19"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """19.In Second Timer you can time yourself as many seconds as you want(Go to Second Counter and convert hours, minutes, and even days into seconds(Recommended))"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("19.In Second Timer you can time yourself as many seconds as you want(Go to Second Counter and convert hours, minutes, and even days into seconds(Recommended))")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back ")
         if abn == "Y".lower():      
           os.system("clear")     
           sectimer()
         else:
           robot_wait2()
           
  elif (argument == "20"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """20.In Matrix Multiplier you can enter a matrix and a multinputle and you get your matrix multiplied by your multinputle"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("20.In Matrix Multiplier you can enter a matrix and a multinputle and you get your matrix multiplied by your multinputle")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           strmulti()
         else:
           robot_wait2()

  elif (argument == "21"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """21.In Quote Teller you can enter a number and it will tell you a quote"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("21.In Quote Teller you can enter a number and it will tell you a quote")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           QT()
         else:
           robot_wait2()

  elif (argument == "22"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """22.In Prime or Composite you can find out if a number is a prime number or a composite number"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("22.In Prime or Composite you can find out if a number is a prime number or a composite number")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           pORc()
         else:
           robot_wait2()

  elif (argument == "23"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """23.In Dictator you can enter a word, phrase, sentence, matrix, numbers, songs, or stories and enter a language and he will tell you it in that language"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("23.In Dictator you can enter a word, phrase, sentence, matrix, numbers, songs, or stories and enter a language and he will tell you it in that language")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           dictator()
         else:
           robot_wait2()

  elif (argument == "24"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """24.In MathGame you can practice adding numbers"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)  
         print("24.In MathGame you can practice adding numbers")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           ga()
         else:
           robot_wait2()

  elif (argument == "25"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """25.In Choice Chooser you can enter the number of choices and the choices and it will randomly tell you one of your choice"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("25.In Choice Chooser you can enter the number of choices and the choices and it will randomly tell you one of your choice")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           choice()
         else:
           robot_wait2()

  elif (argument == "26"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """26. In Sponsor List you can see the list of people who have sponsored my app and you can learn how to sponsor my app"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("26. In Sponsor List you can see the list of people who have sponsored my app and you can learn how to sponsor my app")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           sponsor()
         else:
           robot_wait2()

  elif (argument == "27"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """27. In SarsoftRobot you can play the first version of this robot SarsoftRobot"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("27. In SarsoftRobot you can play the first version of this robot SarsoftRobot")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           forrobot()
         else:
           robot_wait2()

  elif (argument == "28"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """28. In RPS you can play Rock Paper Scissors against a robot"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("28. In RPS you can play Rock Paper Scissors against robot")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           cls()
           RPS_Game_Sarveshwar()
         else:
           robot_wait2()

  elif (argument == "29"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """29. In Name Randomizer you can get a random name"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("29. In Name Randomizer you can get a random name")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           randname()
         else:
           robot_wait2()

  elif (argument == "30"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """30. In Calendar you can get a calendar of any year you want"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("30. In Calendar you can get a calendar of any year you want")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           calendar1()
         else:
           robot_wait2()

  elif (argument == "31"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """31. In Search you can search something and you can get a website for your specific query"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("31. In Search you can search something and you can get a website for your specific query")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           goosearch()
         else:
           robot_wait2()

  elif (argument == "32"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """32. In YouSearch you can search for a specific query and it will suggest a video"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("32. In YouSearch you can search for a specific query and it will suggest a video")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           yousearch()
         else:
           robot_wait2()

  elif (argument == "33"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """33. In Grocery List you can make a grocery list and it will remind you"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("33. In Grocery List you can make a grocery list and it will remind you")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           groceylist()
         else:
           robot_wait2()

  elif (argument == "34"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """34. In Poem Maker you can make a poem"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("34. In Poem Maker you can make a poem")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           poemmaker()
         else:
           robot_wait2()

  elif (argument == "35"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """35. In Higher or Lower you can choose higher or lower and there will be a random number either higher or lower"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("35. In Higher or Lower you can choose higher or lower and there will be a random number either higher or lower")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           DiceGame()
         else:
           robot_wait2()

  elif (argument == "36"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """36. In LangInfo you can learn about a specific programming language."""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("36. In LangInfo you can learn about a specific programming language.")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           InfoPro()
         else:
           robot_wait2()

  elif (argument == "37"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """37. In Typing Practice you can type paragraphs and practice typing"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("37. In Typing Practice you can type paragraphs and practice typing")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           typepractice()
         else:
           robot_wait2()
  elif (argument == "38"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """38. In Temperature Converter you can convert temperatures to the other temperature system"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("38. In Temperature Converter you can convert temperatures to the other temperature system")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           temperconvert()
         else:
           robot_wait2()
  elif (argument == "39"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """39. In Auto Takeoff Simulator you can simulate an automatic takeoff"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("39. In Auto Takeoff Simulator you can simulate an automatic takeoff")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           AutoTakeoff()
         else:
           robot_wait2()
  elif (argument == "40"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """40. In Duplicates you can see if there are any duplicates in you matrix"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("40. In Duplicates you can see if there are any duplicates in you matrix")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           Duplicates()
         else:
           robot_wait2()
  
  elif (argument == "41"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """41. In Commercial Aircraft Info you can see which aircraft manufacturer makes which planes"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("41. In Commercial Aircraft Info you can see which aircraft manufacturer makes which planes")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           comairinf()
         else:
           robot_wait2()

  elif (argument == "42"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """42. In Shapes you can see shapes, I mean what did you expect?"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("42. In Shapes you can see shapes, I mean what did you expect?")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           drawshape()
         else:
           robot_wait2()

  elif (argument == "43"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """43. In Scoreboard you can keep track of the score"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("43. In Scoreboard you can keep track of the score")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           scorecount()
         else:
           robot_wait2()

  elif (argument == "44"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """44. In Car's Age you can find out your car's age"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("44. In Car's Age you can find out your car's age")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           faoc()
         else:
           robot_wait2()
  
  elif (argument == "45"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """45. In Multiples Finder you can find multiples of a number"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("45. In Multiples Finder you can find the multiples of a number")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           multiplesfinder()
         else:
           robot_wait2()

  elif (argument == "46"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """46. In Color Button Presses you can press colorful buttons and learn colors"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("46. In Color Button Presses you can press colorful buttons and learn colors")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           cbr()
         else:
           robot_wait2()

  elif (argument == "47"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """47. In Find Remainder you can divide and find the answer as well as the remainder"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("47. In Find Remainder you can divide and find the answer as well as the remainder")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           findremainder()
         else:
           robot_wait2()
    
  elif (argument == "48"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """48. In Family Age you can find out your family's age"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("48. In Family Age you can find out your family's age")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           ffage()
         else:
           robot_wait2()
    
  elif (argument == "49"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """49. In Weight converter you can convert kilograms to pounds or pounds to kilograms"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("49. In Weight converter you can convert kilograms to pounds or pounds to kilograms")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           weightconverter()
         else:
           robot_wait2()

  elif (argument == "50"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """50. In Percentage Finder you can find a percentage of a number"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("50. In Percentage Finder you can find a percentage of a number")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           findpercentage()
         else:
           robot_wait2()

  elif (argument == "51"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """51. In Shopping Receipt you can list your items and their costs and you can find the total price"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("51. In Shopping Receipt you can list your items and their costs and you can find the total price")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           shoppingcosts()
         else:
           robot_wait2()
  
  elif (argument == "52"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """52. In Today's Date you can see today's date"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("52. In Today's Date you can see today's date")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           datetoday()
         else:
           robot_wait2()

  elif (argument == "53"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """53. In Clicker you can click a button as many times as you want"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("53. In Clicker you can click a button as many times as you want")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           clicker()
         else:
           robot_wait2()

  elif (argument == "54"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """54. In Riddles you can do some riddles"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("54. In Riddles you can do some riddles")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           riddley()
         else:
           robot_wait2()

  elif (argument == "55"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """55. In Random Greater or lower you can get as many random numbers as you would like and you can compare those numbers"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("55. In Random Greater or lower you can get as many random numbers as you would like and you can compare those numbers")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           comparerandomnum()
         else:
           robot_wait2()
           
  elif (argument == "56"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """56. In Sleep In you can see if you can sleep in or not"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("56. In Sleep In you can see if you can sleep in or not")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           sleep_in()
         else:
           robot_wait2()        

  elif (argument == "57"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """57. In Find Divisors you can find divisors for any number you want"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("57. In Find Divisors you can find divisors for any number you want")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           finddivisor()
         else:
           robot_wait2() 
  
  elif (argument == "58"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """58. In Miles to Kilometers you can convert miles to kilometers or kilometers to miles"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("58. In Miles to Kilometers you can convert miles to kilometers or kilometers to miles")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           distancefind()
         else:
           robot_wait2()

  elif (argument == "59"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """59. In Months to years you can convert months to years or years to months"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("59. In Months to years you can convert months to years or years to months")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           monyear()
         else:
           robot_wait2()

  elif (argument == "60"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """60. In Grams to ounces you can convert grams to ounces or ounces to grams"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("60. In Grams to ounces you can convert grams to ounces or ounces to grams")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           graoun()
         else:
           robot_wait2()

  elif (argument == "61"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """61. In Milliliters to fluid ounces you can convert milliliters to fluid ounces or fluid ounces to milliliters"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("61. In Milliliters to fluid ounces you can convert milliliters to fluid ounces or fluid ounces to milliliters")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           mlfloz()
         else:
           robot_wait2()

  elif (argument == "62"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """62. In Liters to gallons you can convert Liters to gallons or gallons to liters"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("62. In Liters to gallons you can convert Liters to gallons or gallons to liters")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           litgal()
         else:
           robot_wait2()
  
  elif (argument == "63"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """63. In Feet to meters you can convert feet to meters and meters to feet"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("63. In Feet to meters you can convert feet to meters and meters to feet")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           feetmet()
         else:
           robot_wait2()

  elif (argument == "64"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """64. In Find Palindrome you can enter some letters and it will try to find a palindrome with those letters"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("64. In Find Palindrome you can enter some letters and it will try to find a palindrome with those letters")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           fpalin()
         else:
           robot_wait2()
  
  elif (argument == "65"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """65. In Currency Rates you can see the exchange rates of a currency by comparing it to another currency"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("65. In Currency Rates you can see the exchange rates of a currency by comparing it to another currency")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           excrates()
         else:
           robot_wait2()

  elif (argument == "66"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """66. In Factorial finder you can find the factorial of a number"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("66. In Factorial finder you can find the factorial of a number")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           fact()
         else:
           robot_wait2()

  elif (argument == "67"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """67. In Leap Year you can find out which years are leap years"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("67. In Leap Year you can find out which years are leap years")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           fact()
         else:
           robot_wait2()
  
  elif (argument == "68"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """68. In Business Sim you cna simulate a business"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("68. In Business Sim you cna simulate a business")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           BusinessSim()
         else:
           robot_wait2()

  elif (argument == "69"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """69. In Tax Calculator you enter the price and the tax rate and you can find the total price with taxes"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("69. In Tax Calculator you enter the price and the tax rate and you can find the total price with taxes")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           TaxCalculator()
         else:
           robot_wait2()

  elif (argument == "70"):
         asd = input("Would you like to have the sentence dictated?: ")
         if asd == asd1.lower():
           os.system("clear")
           spech = """70. In Random Card Generator you get a random card generated"""
           tts = gTTS(text=spech, lang='en')
           tts.save("good.wav")
           os.system("play good.wav")
           print("Please Wait")
           time.sleep(5)
           os.system("clear")
           input("Press enter to continue...")
           os.system("clear")
         print(Fore.MAGENTA)
         print(Style.RESET_ALL)
         print("70. In Random Card Generator you get a random card generated")
         pe()
         abn = input("Do you want to continue?..Enter Y to continue or press enter to go back... ")
         if abn == "Y".lower():      
           os.system("clear")     
           random_card_generator()
         else:
           robot_wait2()


  
  elif (argument == "313"):
    print("Welcome to SarsoftRobot\n")
    pas = "SarveshwarProgrammer"

    print("Authorized Personnel only\n")
    namersd = input("Enter your name: ")
    
    d = datetime.now()
    timezone = pytz.timezone("America/Chicago")
    d_aware = timezone.localize(d)
    d_aware.tzinfo
    utc_now = pytz.utc.localize(datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
    pst_now = str(pst_now)

    pst_now == utc_now

    a = open("secretname.txt", "a")
    a.write("\n")
    a.write("\n")
    a.write(namersd)
    a.write(" / ")
    a.write(pst_now)
    a.close()
    os.system("clear")

    apas = input(":")
    if apas == pas:
      print()
      filename = input()
      if filename == "age":
        f = open("age.txt", "r")
        print(f.read())

      elif filename == "dice":
        f = open("dice.txt", "r")
        print(f.read())
      
      elif filename == "names":
        f = open("names.txt", "r")
        print(f.read())

      elif filename == "searchapphistory":
        f = open("searchapphistory.txt", "r")
        print(f.read())

      elif filename == "shouldcode":
        f = open("shouldcode.txt", "r")
        print(f.read())

    else:
      print("The robot will crash now...")
      exit()
      robot_wait2()
    
    input("Press enter to continue...")
    os.system("clear")
    robot_wait2()


  elif (argument == "SECRET".lower()):
        print("How did you get here?")
        print()
        print("This program will crash now")
        print()
        print("Wait...")
        time.sleep(2)
        print("Bye..")
        time.sleep(2)
        os.system("clear")
        tempe()
        para()
        print("The program will crash now, Bye...")
        ss()

  elif (argument == "SING SONG".lower()):
        s1 = ("""Yeah, you got that yummy, yum
        That yummy, yum
        That yummy, yum
        Yeah, you got that yummy, yum
        That yummy, yum
        That yummy, yummy

        Say the word, on my way
        Yeah babe, yeah babe, yeah babe
        Any night, any day
        Say the word, on my way
        Yeah babe, yeah babe, yeah babe
        In the morning or late
        Say the word, on my way

        Bonafide stallion
        You ain't in no stable, no, you stay on the run
        Ain't on the side, you're number one
        Yeah, every time I come around, you get it done

        Fifty-fifty, love the way you split it
        Hunnid racks, help me spend it, babe
        Light a match, get litty, babe
        That jet set, watch the sunset kinda, yeah, yeah
        Rollin' eyes back in my head, make my toes curl, yeah, yeah

        Yeah, you got that yummy, yum
        That yummy, yum
        That yummy, yummy
        Yeah, you got that yummy, yum
        That yummy, yum
        That yummy, yummy

        Say the word, on my way
        Yeah babe, yeah babe, yeah babe
        Any night, any day
        Say the word, on my way
        Yeah babe, yeah babe, yeah babe
        In the morning or late
        Say the word, on my way

        Standing up, keep me on the rise
        Lost control of myself, I'm compromised
        You're incriminated, no disguise
        And you ain't never running low on supplies

        Fifty-fifty, love the way you split it
        Hunnid racks, help me spend it, babe
        Light a match, get litty, babe
        That jet set, watch the sunset kinda, yeah, yeah
        Rollin' eyes back in my head, make my toes curl, yeah, yeah

        Yeah, you got that yummy, yum
        That yummy, yum
        That yummy, yummy (and you stay flexing on me)
        Yeah, you got that yummy, yum
        That yummy, yum (yeah)
        That yummy, yummy

        Say the word, on my way
        Yeah babe, yeah babe, yeah babe (yeah babe)
        Any night, any day
        Say the word, on my way
        Yeah babe, yeah babe, yeah babe (yeah babe)
        In the morning or late
        Say the word, on my way

        Hop in the Lambo, I'm on my way
        Drew House slinputpers on with a smile on my face
        I'm elated that you are my lady
        You got the yum, yum, yum, yum
        You got the yum, yum, yum, whoa
        Whoa-ooh

        Yeah, you got that yummy, yum
        That yummy, yum
        That yummy, yummy
        Yeah, you got that yummy, yum
        That yummy, yum
        That yummy, yummy

        Say the word, on my way
        Yeah babe, yeah babe, yeah babe (yeah babe)
        Any night, any day
        Say the word, on my way
        Yeah babe, yeah babe, yeah babe (yeah babe)
        In the morning or late
        Say the word, on my way
        By Justin Bieber
        """)  
        song2 = """White shirt now red, my bloody nose
Sleeping, you're on your tinputpy toes
Creeping around like no one knows
Think you're so criminal
Bruises, on both my knees for you
Don't say thank you or please
I do what I want when I'm wanting to
My soul? So cynical
So you're a tough guy
Like it really rough guy
Just can't get enough guy
Chest always so puffed guy
I'm that bad type
Make your mama sad type
Make your girlfriend mad tight
Might seduce your dad type
I'm the bad guy, duh
I'm the bad guy
I like it when you take control
Even if you know that you don't
Own me, I'll let you play the role
I'll be your animal
My mommy likes to sing along with me
But she won't sing this song
If she reads all the lyrics
She'll pity the men I know
So you're a tough guy
Like it really rough guy
Just can't get enough guy
Chest always so puffed guy
I'm that bad type
Make your mama sad type
Make your girlfriend mad tight
Might seduce your dad type
I'm the bad guy, duh
I'm the bad guy, duh
I'm only good at being bad, bad
I like when you get mad
I guess I'm pretty glad that you're alone
You said she's scared of me?
I mean, I don't see what she sees
But maybe it's 'cause I'm wearing your cologne
I'm a bad guy
I'm a bad guy
Bad guy, bad guy
I'm a bad-
By Billie Eilish"""
        song3 = """I love it when you call me Señorita
I wish I could pretend I didn't need ya
But every touch is ooh-la-la-la
It's true la-la-la
Ooh I should be running
Ooh you keep me coming
For ya

Land in Miami
The air was hot from summer rain
Sweat drinputping off me
Before I even knew her name la-la-la
It felt like ooh-la-la-la
Yeah, no

Sapphire moonlight
We danced for hours in the sand
Tequila Sunrise
Her body fit right in my hands, la-la-la
It felt like ooh-la-la-la
Yeah

I love it when you call me Señorita
I wish I could pretend I didn't need ya
But every touch is ooh-la-la-la
It's true la-la-la
Ooh I should be running
Ooh you know I love it

When you call me Señorita
I wish it wasn't so damn hard to leave ya
But every touch is ooh-la-la-la
It's true la-la-la
Ooh I should be running
Ooh you keep me coming
For ya

Locked in the hotel
There's just some things that never change
You say, "We're just friends."
But friends don't know the way you taste-la-la-la
'Cause you know it's been a long time comin'
Don't you let me fall, oh

Oh, when your lips undress me
Hooked on your tongue
Ooh, love, your kiss is deadly
Don't stop

I love it when you call me Señorita
I wish I could pretend I didn't need ya
But every touch is ooh-la-la-la
It's true la-la-la
Ooh I should be running
Ooh you know I love it

When you call me Señorita
I wish it wasn't so damn hard to leave ya
But every touch is ooh-la-la-la
It's true la-la-la
Ooh I should be running
Ooh you keep me coming
For ya

All along I'll be coming for ya (for ya)
And I hope it meant something to ya
Call my name I'll be comin' for ya (comin' for ya)
Comin' for ya (comin' for ya)

For ya, for ya (oh, she loves it when I call her), for ya
Ooh I should be running
Ooh you keep me coming
For ya
By Shawn Mendez
"""
        song4 = """Here's to the ones that we got
Cheers to the wish you were here, but you're not
'Cause the drinks bring back all the memories
Of everything we've been through
Toast to the ones here today
Toast to the ones that we lost on the way
'Cause the drinks bring back all the memories
And the memories bring back, memories bring back you
There's a time that I remember, when I did not know no pain
When I believed in forever, and everything would stay the same
Now my heart feel like December when somebody say your name
'Cause I can't reach out to call you, but I know I will one day, yeah
Everybody hurts sometimes
Everybody hurts someday, aye aye
But everything gon' be alright
Go and raise a glass and say, aye
Here's to the ones that we got
Cheers to the wish you were here, but you're not
'Cause the drinks bring back all the memories
Of everything we've been through
Toast to the ones here today
Toast to the ones that we lost on the way
'Cause the drinks bring back all the memories
And the memories bring back, memories bring back you
Doo doo, doo doo, doo doo
Doo doo, doo doo, doo doo, doo doo
Doo doo, doo doo, doo doo doo
Memories bring back, memories bring back you
There's a time that I remember when I never felt so lost
When I felt all of the hatred was too powerful to stop (ooh, yeah)
Now my heart feel like an ember and it's lighting up the dark
I'll carry these torches for ya that you know I'll never drop, yeah
Everybody hurts sometimes
Everybody hurts someday, aye aye
But everything gon' be alright
Go and raise a glass and say, aye
Here's to the ones that we got (oh oh)
Cheers to the wish you were here, but you're not
'Cause the drinks bring back all the memories
Of everything we've been through (no, no)
Toast to the ones here today (aye)
Toast to the ones that we lost on the way
'Cause the drinks bring back all the memories (aye)
And the memories bring back, memories bring back you
Doo doo, doo doo, doo doo
Doo doo, doo doo, doo doo, doo doo
Doo doo, doo doo, doo doo doo
Memories bring back, memories bring back you
Doo doo, doo doo doo doo
Doo doo, doo doo, doo doo, doo doo
Doo doo, doo doo, doo doo doo (ooh, yeah)
Memories bring back, memories bring back you
Yeah, yeah, yeah
Yeah, yeah, yeah, yeah, yeah, no, no
Memories bring back, memories bring back you
By Maroon 5"""
        song5 = """We go together
Better than birds of a feather, you and me
We change the weather, yeah
I'm feeling heat in December when you're 'round me
I've been dancing on top of cars and stumbling out of bars
I follow you through the dark, can't get enough
You're the medicine and the pain, the tattoo inside my brain
And, baby, you know it's obvious
I'm a sucker for you
You say the word and I'll go anywhere blindly
I'm a sucker for you, yeah
Any road you take, you know that you'll find me
I'm a sucker for all the subliminal things
No one knows about you (about you) about you (about you)
And you're making the typical me break my typical rules
It's true, I'm a sucker for you, yeah
Don't complicate it (yeah)
'Cause I know you and you know everything about me
I can't remember (yeah)
All of the nights I don't remember
When you're 'round me (oh, yeah yeah)
I've been dancing on top of cars and stumbling out of bars
I follow you through the dark, can't get enough
You're the medicine and the pain, the tattoo inside my brain
And, baby, you know it's obvious
I'm a sucker for you
You say the word and I'll go anywhere blindly
I'm a sucker for you, yeah
Any road you take, you know that you'll find me
I'm a sucker for all the subliminal things
No one knows about you (about you) about you (about you)
And you're making the typical me break my typical rules
It's true, I'm a sucker for you, yeah
I've been dancing on top of cars and stumbling out of bars
I follow you through the dark, can't get enough
You're the medicine and the pain, the tattoo inside my brain
And, baby, you know it's obvious
I'm a sucker for you
You say the word and I'll go anywhere blindly
I'm a sucker for you, yeah
Any road you take, you know that you'll find me
I'm a sucker for all the subliminal things
No one knows about you (about you) about you (about you)
And you're making the typical me break my typical rules
It's true, I'm a sucker for you
I'm a sucker for you"""
        acb = input("Would you like to Randomize it?Enter (Random)(You can choose it, if you want to, enter(Choose): ")
        accc = "RANDOM"
        addd = "CHOOSE"
        if acb == accc.lower():
          adg = rant(1, 5)
          if adg == 1:
            spech = s1
          elif adg == 2:
            spech = song2
          elif adg == 3:
            spech = song3
          elif adg == 4:
            spech = song4
          elif adg == 5:
            spech = song5
        elif acb == addd.lower():
          print("""
          1. Yummy by Justin Bieber
          2. Bad Guy by Billie Eilish
          3. Senorita by Shawn Mendes
          4. Memories by Maroon 5
          5. Sucker by Jonas Brothers
          """)
          pe()
          opti = input("Enter your option: ")
          ab = ["1", "2", "3", "4", "5"]
          
          if opti == ab[0]:
            spech = s1
          if opti == ab[1]:
            spech = song2
          if opti == ab[2]:
            spech = song3
          if opti == ab[3]:
            spech = song4
          if opti == ab[4]:
            spech = song5

        tts = gTTS(text = spech, lang = 'en')
        tts.save("good.wav")
        os.system("play good.wav")
        pe()
        os.system("clear")
        print("please wait.. loading")
        time.sleep(5)
        os.system("clear")
        print("If you have any suggestions for any more songs email me at sarvesms@outlook.com or gamedev313@gmail.com")
        pe()
        input("Press enter to continue...")
        os.system("clear")
        robot_wait()
  elif (argument == "ICE CREAM RANDOMIZER".lower()):
        print("Welcome to Secret Ice Cream Randomizer")
        pe()
        print("I have no idea how you found out about this program")
        pe()
        print("You have sharp eyes")
        input("Press enter to continue...")
        findicecream1()     
  elif (argument == "SECRET".lower()):
        tempe()
        print("You looked into the code didn't you")   
        robot_wait2()   
  else:
        print("Invalid inp")
        print("Please Wait...")
        print("Redirecting...")
        time.sleep(4)
        os.system("clear")
        exit1()

os.system("clear")
p("Whatever you do, do not go type in 'secret' as an option in my app")
time.sleep(2)
print()
input("Press enter to continue...")
os.system("clear")
print("Please Wait...")
time.sleep(3)
os.system("clear")
print()
print("Hi, my name is Sarvesh")
print()
print("Nice to meet you")
print()
print("What's your name?")
firstname = input("Enter your name: ")
firstname = firstname 
if (firstname == first_name.lower()):
  print("OK")
  pe()
  tell()
  pe()
  input("Press enter to continue...")
  os.system("clear")
elif (firstname == "S@rv35hw@r"):
  print("Good Job")
  print("Ok, redirecting you to the app")
  time.sleep(2)
  robot_main()
elif (firstname == first_name.upper()):
  print("OK")
  pe()
  tellice()
  pe()
  input("Press enter to continue...")
  os.system("clear")
  input("Press enter to continue...")
  os.system("clear")
elif (firstname == full_name.lower()):
  print("OK")
  pe()
  tell()
  pe()
  input("Press enter to continue...")
  os.system("clear")
elif (firstname == full_name.upper()):
  print("OK")
  pe()
  os.system("clear")
  tellice()
  pe()
  input("Press enter to continue...")
  os.system("clear")
elif (firstname == last_name.lower()):
  print("OK")
  pe()
  os.system("clear")
  tell()
  pe()
  input("Press enter to continue...")
  os.system("clear")
elif (firstname == last_name.upper()):
  print("OK")
  pe()
  os.system("clear")
  tellice()
  pe()
  input("Press enter to continue...")
  os.system("clear")
else:
  print("You can't trick me,", firstname)
  print("I know your name is", full_name)
  pe()
  print(Fore.GREEN)
  randtellyou()
  print(Style.RESET_ALL)

  pe()
  input("Press enter to continue...")
  os.system("clear")

lik = input("Do you like Soccer: ")
if lik.lower() == "no":
    sp = input("What is your favourite sport: ")
    print("Soccer is mine")
    print()
    input("Press enter to continue...")
    os.system("clear")
else:
    print("I like Soccer too")
    print("Soccer is my favourite sport")
    print()
    input("Press enter to continue...")
    os.system("clear")


a2345 = input("How old are you: ")

os.system("clear")

if a2345.lower() == "3":
  print("I'm 3 too")
elif a2345.lower() == "S@rv35hw@r":
  print("Good Job finding this")
  print("Redirecting you to the app...")
  time.sleep(2)
  robot_main()
else:
  print("Oh your", a2345, ", I'm 3")

print("I really appreciate that you spend your time with me")
print()
print("I would appreciate it more if you shared this app with someone else.")
print()
input("Press enter to continue...")

os.system("clear")

print("How are you feeling today ," + firstname + "?")

happiness = input("How are you feeling today? : ")

print("oh ok")

if happiness == "S@rv35hw@r":
  print("Good Job finding this")
  print("I'll redirect you immediately to your app")
  time.sleep(2)
  robot_main()

reasoning = input("why are you feeling " + happiness + "?: ")

os.system("clear")

hyello = "yes"
rid = input("Do you want to hear a riddle?: ")
if rid == hyello.lower():
  voi = input("Would you like to have it dictated?: ")
  voi1 = "YES"
  master = "5@rv35hw@r"
  if voi == voi1.lower():
    spech = """Joe's father has 4 sons, One is named January, One is named Febuary, One is named March, What's the last one named?"""
    tts = gTTS(text=spech, lang='en')
    tts.save("good.wav")
    os.system("play good.wav")
    print("please wait.. loading")
    time.sleep(5)
    os.system("clear")
  elif voi == "Y".lower():
    spech = """Joe's father has 4 sons, One is named January, One is named Febuary, One is named March, What's the last one named?"""
    tts = gTTS(text=spech, lang='en')
    tts.save("good.wav")
    os.system("play good.wav")
    print("please wait.. loading")
    time.sleep(5)
    os.system("clear")
elif rid == "Y".lower():
  voi = input("Would you like to have it dictated?: ")
  voi1 = "YES"
  if voi == voi1.lower():
    spech = """Joe's father has 4 sons, One is named January, One is named Febuary, One is named March, What's the last one named?"""
    tts = gTTS(text=spech, lang='en')
    tts.save("good.wav")
    os.system("play good.wav")
    print("please wait.. loading")
    time.sleep(5)
    os.system("clear")
  elif voi == "Y".lower():
    spech = """Joe's father has 4 sons, One is named January, One is named Febuary, One is named March, What's the last one named?"""
    tts = gTTS(text=spech, lang='en')
    tts.save("good.wav")
    os.system("play good.wav")
    print("please wait.. loading")
    time.sleep(5)
    os.system("clear")
  elif rid == "S@rv35hw@r":
    print("Good Job")
    print("I'll redirect you to my master's app")
    time.sleep(2)
    robot_main()
  elif rid == master.lower():
    print("Good Job")
    print("I'll redirect you to my master's app")
    time.sleep(2)
    robot_main()
  else:
    print("Ok, It's fine")
    
  print(Fore.MAGENTA)
  print("Joe's father has 4 sons")
  print("One is named January")
  print("One is named Febuary")
  print("One is named March")
  print(Fore.YELLOW)
  ridd = input("What's the last one named?: ")
  ator = "JOE"

  if ridd == ator.lower():
    print("Correct")
    print("Many people get tricked by this riddle")
  else:
    print(Fore.GREEN)
    print("The answer is Joe")
    print("Because it's Joe's Father")
    print("Many people get tricked by this riddle")

print("Ok, let's change the topic")
print()
input("Press enter to continue...")

os.system("clear")
print(Fore.BLUE)
print(Style.BRIGHT)
print("Enter 'Ice Cream Randomizer' as an option in my app")
print()
input("Press enter to continue...")
os.system("clear")
print(Style.RESET_ALL)
print("What do you want to talk about?")

topic = input("What do you want to talk about? : ")

os.system("clear")

if topic.lower() == "nothing":
  print("Oh ok")
else:
  print(("what do you know about the ") + (topic) + ("?"))
  fact = input(("what do you know about ") + (topic) +("? : "))
  print(fact)
  print("oh that's a interesting fact.")

print()

input("Press enter to continue...")
os.system("clear")
print(Fore.RED)
print(Style.BRIGHT)
print("Did you know you can sponsor me?")
print("Just contact me at sarvesms@outlook.com or gamedev313@gmail.com")
print("If you sponsor me,")
print("Your name will be on the sponsors list")
print("You will be able to review my ideas for the robot")
print("and many more...")
print()
print("Please Wait...")
time.sleep(3)
print(Style.RESET_ALL)
input("Press enter to continue...")
os.system("clear")

print("I would like to show you something")
Ice = input("Do you like ice cream?: ")

d = datetime.now()
timezone = pytz.timezone("America/Chicago")
d_aware = timezone.localize(d)
d_aware.tzinfo
utc_now = pytz.utc.localize(datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
pst_now = str(pst_now)

pst_now == utc_now

a = open("DOlikeIce.txt", "a")
a.write("\n")
a.write("\n")
a.write(Ice)
a.write(" / ")
a.write(pst_now)
a.close()

asdf = "YES"

if Ice == asdf.lower():
  print("So do I") 
  print("I like Ice cream too")
  print("I have to show you something")
  print("I think you will like it")
  print()
  input("Press enter to continue...")
  os.system("clear")
  print("Wait!!")
  time.sleep(3)
  print("It is a program to randomly find out what flavor of ice cream to get")
elif Ice == "Y".lower():
  print("So do I") 
  print("I like Ice cream too")
  print("I have to show you something")
  print("I think you will like it")
  input("Press enter to continue...")
  os.system("clear")
  print("Wait!!")
  time.sleep(3)
  print("It is a program to randomly find out what flavor of ice cream to get")
else:
  print("Oh Ok")
  print("Well I still have to show you something")
  input("Press enter to continue...")
  os.system("clear")
  print("Wait!!")
  time.sleep(3)
  pe()
  print("It is a program to randomly find out what flavor of ice cream to get")

findicecream()

realcad = "yes"
coad = input("Do you like to code? : ")
if (coad.lower)() == realcad:
  print("Oh, I like to code too")
  print("I think coding is fun")
elif (coad.lower)() == "y":
  print("Oh, I like to code too")
  print("I think coding is fun")
else:
  print("Well, I like to code")
  print("I think coding is fun")


res = input("Do you think we should learn how to code? :")

if (res.lower)() == "yes":
  rea = input("Yeah me too, but why? :")
  print(rea)
  print("Ok")
  
  d = datetime.now()
  timezone = pytz.timezone("America/Chicago")
  d_aware = timezone.localize(d)
  d_aware.tzinfo
  utc_now = pytz.utc.localize(datetime.utcnow())
  pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
  pst_now = str(pst_now)

  pst_now == utc_now

  a = open("shouldcode.txt", "a")
  a.write("\n")

  a.write(rea)
  a.write(" / ")
  a.write(pst_now)
  a.close()

elif (res.lower)() == "y":
  rea = input("Yeah me too, but why? :")
  print(rea)
  print("Ok")

  
  d = datetime.now()
  timezone = pytz.timezone("America/Chicago")
  d_aware = timezone.localize(d)
  d_aware.tzinfo
  utc_now = pytz.utc.localize(datetime.utcnow())
  pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
  pst_now = str(pst_now)

  pst_now == utc_now

  a = open("shouldcode.txt", "a")
  a.write("\n")

  a.write(rea)
  a.write(" / ")
  a.write(pst_now)
  a.close()

else:
  print("oh ok")
  rea1 = input("Why not?:")
  print(rea1)
    
  d = datetime.now()
  timezone = pytz.timezone("America/Chicago")
  d_aware = timezone.localize(d)
  d_aware.tzinfo
  utc_now = pytz.utc.localize(datetime.utcnow())
  pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
  pst_now = str(pst_now)

  pst_now == utc_now

  a = open("shouldcode.txt", "a")
  a.write("\n")

  a.write(rea1)
  a.write(" / ")
  a.write(pst_now)
  a.close()

d = datetime.now()
timezone = pytz.timezone("America/Chicago")
d_aware = timezone.localize(d)
d_aware.tzinfo
utc_now = pytz.utc.localize(datetime.utcnow())
pst_now = utc_now.astimezone(pytz.timezone("America/Chicago"))
pst_now = str(pst_now)

pst_now == utc_now

a = open("shouldcode.txt", "a")
a.write("\n")
a.write("\n")
a.write(res)
a.write(" / ")
a.write(pst_now)
a.close()

print("Let me tell you a quote")
input("Press enter to continue...")
os.system("clear")
print("My dad once told me a quote")
asd = input("Would you like to have the quote dictated?: ")
os.system("clear")
asd1 = "YES"
if asd == asd1.lower():
  spech = """'It doesn't matter how many lines of code you write, all that matters is how beautiful the program is'"""
  tts = gTTS(text=spech, lang='en')
  tts.save("good.wav")
  os.system("play good.wav")
  print("Please Wait")
  ts(9)
  os.system("clear")
  input("Press enter to continue...")
  os.system("clear")
  spech = "By My Dad"
  tts = gTTS(text=spech, lang='en')
  tts.save("good.wav")
  print("please wait.. loading")
  time.sleep(5)
  os.system("clear")
elif asd == "Y".lower():
  spech = """'It does'nt matter how many lines of code you write, all that matters is how beautiful the program is'"""
  tts = gTTS(text=spech, lang='en')
  tts.save("good.wav")
  os.system("play good.wav")
  print("Please Wait")
  ts(9)
  os.system("clear")
  input("Press enter to continue...")
  os.system("clear")
  spech = "By My Dad"
  tts = gTTS(text=spech, lang='en')
  tts.save("good.wav")
  print("please wait.. loading")
  time.sleep(5)
  os.system("clear")
else:
  print("Ok, It's fine")
  time.sleep(2)
  os.system("clear")
  input("Press enter to continue...")
  os.system("clear")

print(Fore.RED)
print(Style.BRIGHT)
print("'It does'nt matter how many lines of code you write, all that matters is how beautiful the program is' By My Dad")
pe()
time.sleep(5)
input("Press enter to continue...")
pe()
os.system("clear")
print(Style.RESET_ALL)

myname = "Sarvesh"

fsubject = input("What's your favourite subject in school? :")
msubject = "Math"
pe()

if fsubject == msubject.lower():
  print(("oh, your favourite subject in school is ") + (fsubject) + (", my favourite subject in school is ") + (msubject) + (" too."))

else:
  print(("oh, your favourite subject in school is ") + (fsubject) + (", my favourite subject in school is ") + (msubject))

pe()

def enyned():
  q = input("Do you think i'm programmed well? : ")
  if q.lower() == "no":
    print("Oh ok")
    hy = input("Why do you think i'm programmed bad?: ")
    print("Oh, thank you for your feedback")
    os.system("clear")
    end()
  else:
    print("Thank you")
    time.sleep(2)
    os.system("clear")
    end()
  ts(10)

nnnn = input("Do you want to see my app? : ")

if nnnn.lower() == "yes":
  robot_main()

elif nnnn.lower() == "y":
  robot_main()
  
  
else:
  print("Ok")
  time.sleep(1)
  print("Ok, I gotta go now")

  print("If you want to see the first version of this robot")

  print(Fore.GREEN)
  print(Style.BRIGHT)

  print("Go to frobot.sarveshmercedes.repl.run")

  pe()

  print(Style.RESET_ALL)

  print("If you want to sponsor this app")

  print(Fore.RED)
  print(Style.BRIGHT)

  print("remember to contact me at sarvesms@outlook.com or gamedev313@gmail.com")
  pe()
  print(Style.RESET_ALL)
  
  print("It's been nice talking to you")
  print(("Bye ") + (firstname))
  enyned()

enyned()

print("\033[1;34;40m") 

print("sarvesh313.wordpress.com")

print("\033[1;31;40m") 

print("If you want to sponsor this app contact me at sarvesms@outlook.com or gamedev313@gmail.com")

pe()

print(Style.RESET_ALL)

print(Fore.BLUE)

print("This was made by Sarveshwar Senthilkumar")

pe()

print("Thank you for playing...")

print("Remember if you have any suggestions email sarvesms@outlook.com or gamedev313@gmail.com")

pe()

print("It would be nice if you shared this app")

print()

print("This game will be updated often so check back in a bit")

print(Style.RESET_ALL)

print()

print("Goodbye and remember to check back in")

print("Please recommend it to people", full_name)

print()

print("I think they'll like it")

print()

input("Press enter to continue...")

os.system("clear")

print("Thank you for using Sarsoft Robot")

pe()

print(Fore.RED, "|------------------------|")
print(Fore.RED, "|    _ _____             |")
print(Fore.YELLOW, "|   //     \             |")
print(Fore.BLUE, "|  | \____  \            |")
print(Fore.GREEN, "|  |      \  \_________  |")
print(Fore.MAGENTA, "|  | \____/ arveshwar's\ |")
print(Fore.RED, "|  |  Python Programs  / |")
print(Fore.RED, "| /___________________/  |")
print(Fore.YELLOW, "|________________________|")
print(Style.RESET_ALL)

print()

print("This programm/app/game/robot was made by Sarveshwar Senthilkumar")

print()

print("This was made by Sarveshwar Senthilkumar")

print()

input("")
os.system("clear")

print()
print("Secret Phrase: ")
print()

print("Sarveshwar Senthilkumar is getting bigger and bigger")

input("")

print("This started as an school Genius Hour project in 2018")

print("\nIf you don't know what Genius Hour is, Genius Hour is an hour that you get to spend researching and making a thing of your choosing.\n")

print("My dad was a software engineer")

print("/nSo I wondered what he did so I started to research")

print("\nI was looking at programming videos on YouTube and at the end I decided to learn Python 3")

print("\nI used the Japanese concept of Kaizen which means to improve slowly over time")

print("\nI would work on this everyday in the morning and that helped improve this program and become a better software engineer.")

print()

print("Thanks for reading my story of how I became a software engineer and how this program became so big.\n")

input("")

os.system("clear")