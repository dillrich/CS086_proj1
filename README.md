# Introduction
In this project, you learn some basic object oriented design in Python.  Python is a powerful interpretive language which has both scripting and object oriented programing features.  This project is inspired by my recent TDY to Tokyo, Japan, where the vending machines which are more sophisticated and complex than the US vending machines.  In Japan, vending machines serve a spectrum of items -- beverages, food, toys, puppies, etc.  

You will create a program that acts as a super vending machine, even better than the ones in Japan.  You will provide a scriptable way to populate the machine, pay for items, dispense change, and record transactions.  

# Project Description

You are going to implement a text driven super vending machine.  The design will be up to you, but will be required to read commandline data:
| Command                            | Example                  | Description                                                    |
| -----------------------------------|--------------------------|----------------------------------------------------------------- 
| balance                            | balance                  | shows the balance                   
| history                            | history                  | prints list of transactions
| inventory                          | inventory                | prints available items with name and ID 
| add item \<str\> \<int\> \<float\> | add item chips 2 \$1.00  | add an item name qty price 
| buy item \<str\> \{5\}\{int\}      | buy item chips 1 2 2 4 3 | buys an item with \# dollars, quarters, dimes, nickles, pennies.  It also shows change given and the remaining balance with currency distribution.  For change, the machine uses the largest denominator of curenncy that is available.   
| help                               | help                     | display help menu with these commands
| exit                               | exit                     | exit the vending machine


## Sample Input

The sample input below is a sequence of correctly formatted commands. Your program should detect and ignore commands that are not correctly formatted.

add item chips 20 $.50
add item coke 5 $.75
inventory
buy item coke 0 3 0 0 0 
inventory
buy item chips 1 0 0 0 0
inventory
history 
balance
