import sqlite3
import time

conn = sqlite3.connect('Mexican_Food.db')
c = conn.cursor()

def food_name_lookup(name):
  line = c.execute("SELECT * FROM Mexican_Food WHERE name IS ?;", (name,)).fetchone()

  if line == None:
    print("Beep boop error")
    create = input("This does not exist, would you like to add it? y/n ")

    


  else:
    print(str(line))

def ask_user():
  print("Hello! \nWelcome to the VERY limited mexican food database.")
 
  time.sleep(1)
  user_food = input("What would you like to search? ")

  food_name_lookup(user_food)

ask_user()

def main():
  while True:
    ask_user()

if __name__ == "__main__":
  main()