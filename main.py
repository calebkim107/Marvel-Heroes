Heroes = {
    "AAA" : "Starlord",
    "AAB" : "Drax",
    "ABA" : "Black Panther",
    "ABB" : "Doctor Strange",
    "BAA" : "Winter Soldier",
    "BAB" : "Rocket Raccoon",
    "BBA" : "Captain America",
    "BBB" : "Iron Man",
    "CAA" : "Groot",
    "CAB" : "Hulk",
    "CBA" : "Spiderman",
    "CBB" : "Mantis",
    "DAA" : "Thanos",
    "DAB" : "Thor",
    "DBA" : "Hawkeye",
    "DBB" : "Black Widow"
}

name = input("Hello, what is your name?")
answer = input("Hello" + name + "! Ready to play? Y or N ")

if answer.upper() == "Y":
  question1 = input("What color do you prefer?(Choose A or B) \nA Red \nB) Blue")
  question2 = input("What sport do you prefer?(Choose A or B) \nA Soccer \nB) Basketball")
  question3 = input("What dessert do you prefer?(Choose A or B) \nA Cake \nB) Ice cream")
  choice = question1 + question2 + question3
  wait = input("Are you ready yo know what marvel character you are most like?")
  if wait.upper() == "Y or N":
    print("Your Marvel Hero is " + Heroes [choice.upper()] )
  else:
    print("Okay suit yourself")
else:
  print("Oh that's too bad. Come back again later.")
