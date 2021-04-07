#a program that allows the user to enter an order#
import json

global price
try:
        with open('price.json') as f:
            price = json.load(f)
except FileNotFoundError:
        print("Could not load price.json")
        price = {}


price = {}        

def _save():
    with open('price.json', 'w+') as f:
        json.dump(price, f)
      
print("Welcome to DillBil's Delight")
name = input("Can I get a name for your order? - ")
price[name] = 0
_save()
print(f"Welcome {name}!")
op = input("Would you like a sandwich today? Yes or No? - ")
if op == "No":
    opp = input("Would you like a drink? Yes or No? - ")
    if opp == "No":
        oppp = input("Would you like fries? Yes or No? - ")
        if oppp == "No":
            print("Then stop wasting our time")
            print("You were kicked out.")
        if opp == "Yes":
            fries = input("What kind of fried would you like?  Waffle Fries, Sweet Potatoe Fries, French Fries, or Steak Fries? - ")
            if fries == "Waffle Fries":
                price[name] += 5
                _save()
            if fries == "Sweet Potatoe Fries":
                price[name] += 4
                _save()
            if fries == "Steak Fries":
                price[name] += 4
                _save()
            if fries == "French Fries":
                price[name] += 3
                _save()
            print(f"Ok then, your total will be ${price[name]}!")
    if opp == "Yes":
        drink = input("What would you like to drink? Coke, Pepsi, Water, or Lemonade? - ")
        if drink == "Water":
            price[name] += 1
            _save()
        if drink == "Lemonade":
            price[name] += 3
            _save()
        if drink == "Coke":
            price[name] += 2
            _save()
        if drink == "Pepsi":
            price[name] += 2
            _save()
        opp = input("Would you like fries? Yes or No? - ")
        if opp == "Yes":          
            fries = input("What kind of fried would you like?  Waffle Fries, Sweet Potatoe Fries, French Fries, or Steak Fries? - ")
            if fries == "Waffle Fries":
                price[name] += 5
                _save()
            if fries == "Sweet Potatoe Fries":
                price[name] += 4
                _save()
            if fries == "Steak Fries":
                price[name] += 4
                _save()
            if fries == "French Fries":
                price[name] += 3
                _save()
            print(f"Ok then, your total will be ${price[name]}!")
        if opp == "No":
                    print(f"Ok then, your total will be ${price[name]}!")
                    
if op == "Yes":
    sandwich = input("What kind of sandwich would you like? Ham and Cheese, Turkey and Cheese, Baloney and Cheese, or Peanut Butter and Jelly? - ")
    if sandwich == "Ham and Cheese":
                        price[name] += 4
                        _save()
    if sandwich == "Turkey and Cheese":
                        price[name] += 5
                        _save()
    if sandwich == "Baloney and Cheese":
                        price[name] += 3
                        _save()
    if sandwich == "Peanut Butter and Jelly":
                        price[name] += 2
                        _save()
    opp = input("Would you like a drink? Yes or No? - ")
    if opp == "No":
                    oppp = input("Would you like fries? Yes or No? - ")
                    if oppp == "No":
                            print(f"Ok then, your total will be ${price[name]}!")
                    if oppp == "Yes":
                            fries = input("What kind of fries would you like?  Waffle Fries, Sweet Potatoe Fries, French Fries, or Steak Fries? - ")
                            if fries == "Waffle Fries":
                                price[name] += 5
                                _save()
                            if fries == "Sweet Potatoe Fries":
                                price[name] += 4
                                _save()
                            if fries == "Steak Fries":
                                price[name] += 4
                                _save()
                            if fries == "French Fries":
                                price[name] += 3
                                _save()
                            print(f"Ok then, your total will be ${price[name]}!") 
    if opp == "Yes":
                        drink = input("What would you like to drink? Coke, Pepsi, Water, or Lemonade? - ")
                        if drink == "Water":
                            price[name] += 1
                            _save()
                        if drink == "Lemonade":
                            price[name] += 3
                            _save()
                        if drink == "Coke":
                            price[name] += 2
                            _save()
                        if drink == "Pepsi":
                            price[name] += 2
                            _save()
                        oppp = input("Would you like fries? Yes or No? - ")
                        if oppp == "Yes":          
                            fries = input("What kind of fried would you like?  Waffle Fries, Sweet Potatoe Fries, French Fries, or Steak Fries? - ")
                            if fries == "Waffle Fries":
                                price[name] += 5
                                _save()
                            if fries == "Sweet Potatoe Fries":
                                price[name] += 4
                                _save()
                            if fries == "Steak Fries":
                                price[name] += 4
                                _save()
                            if fries == "French Fries":
                                price[name] += 3
                                _save()
                            print(f"Ok then, your total will be ${price[name]}!")
                        if oppp == "No":
                            print(f"Ok then, your total will be ${price[name]}!")
                    
