import requests
import sys

def search_name():
    name = input("Enter Name: \n-")
    response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}".format(name),
      headers={
        "X-Mashape-Key": "svNpqNZzwnmshPVTx0vZ6RJ6iAZfp10a9XhjsnwVFHdA5R1Q1i"}).json()
    try:
        cats = ["name", "cardSet", "cost", "attack", "health", "rarity", "text"]
        for x in cats:
            print(x.title(),":", str(response[0].get(x)).replace("<b>", "").replace("</b>", ""))
    except KeyError:
        print("We couldn't find that name")
        again = input("Do you want to try again? Y/n?\n-").lower()
        if again == "y":
            search_name()
        else:
            pass

def ask_info():
    cat = input("(C)lasses, (R)aces, or (S)ets?\n").lower()
    if cat == "c":
        return "classes"
    elif cat == "r":
        return "races"
    elif cat == "s":
        return "sets"
    else:
        print("oops\n")
        ask_info()

def ask_value(info):
    if info == "classes":
        value = input("Which class?\n-")
        return info, value
    elif info == "races":
        value = input("Which race?\n-")
        return info, value
    elif info == "sets":
        value = input("Which set?\n-")
        return info, value
    else:
        print("Try again\n")
        ask_value()

def search(area, value):
    response = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/{}/{}".format(area, value),
      headers={
        "X-Mashape-Key": "svNpqNZzwnmshPVTx0vZ6RJ6iAZfp10a9XhjsnwVFHdA5R1Q1i"}).json()
    try:
        for x in response:
            print(x['name'])
    except TypeError:
        print("Couldn't find that one")
        again = input("Do you want to try again? Y/n?\n-").lower()
        if again == "y":
            stuff = ask_value(ask_info())
            search(stuff[0], stuff[1])
        else:
            pass

def info(category):
    response = requests.get('https://omgvamp-hearthstone-v1.p.mashape.com/info',
      headers={
        "X-Mashape-Key": "svNpqNZzwnmshPVTx0vZ6RJ6iAZfp10a9XhjsnwVFHdA5R1Q1i" }).json()
    print(category.title())
    for x in response[category]:
        print(x,end=", ")
    print("\n")
