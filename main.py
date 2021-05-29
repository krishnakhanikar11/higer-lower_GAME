from art import logo 
from art import vs
import random
from game_data import data
from replit import clear

print(logo)

score = 0
game_continue = True
account_b= random.choice(data)

while game_continue:
  account_a= account_b
  account_b= random.choice(data)
  if account_a==account_b:
    account_b=random.choice(data)

  def acc(account):
    account_name=account["name"]
    account_descp=account["description"]    
    account_country=account["country"]
    return f"{account_name},a {account_descp},from {account_country}"


  def ans_check(guess,account_follower_a,account_follower_b):
    if account_follower_a>account_follower_b:
      return guess=="a"
    else:
      return guess=="b"
    

  print("Welcome to Higer Lower game")
  print(f"Compare A:{acc(account_a)}")
  print(vs)
  print(f"Compare B:{acc(account_b)}")
  guess = input("Who has more follower? A or B :").lower()
  account_follower_a=account_a["follower_count"]
  account_follower_b=account_b["follower_count"]

  is_answer=ans_check(guess,account_follower_a,account_follower_b)

  if is_answer:
    clear()
    score+=1
    print(f"you got it right. {score}")
      
  else:
    clear()
    print(f"game over{score}")
    game_continue=False
