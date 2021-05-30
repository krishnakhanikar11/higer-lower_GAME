print(logo)
  print(f"your Current score is {score}")
  random_a=random_b
  random_b = random.choice(data)
  if random_a == random_b:
    random_b=random.choice(data)
  
  a_follower= random_a["follower_count"]
  b_follower= random_b["follower_count"]

  def details(random_ab):
    a_name=random_ab["name"]
    a_desc=random_ab["description"]
    a_country=random_ab["country"]
    return f"{a_name}, a {a_desc}, from {a_country}"

 
  print(details(random_a))
  print(vs)
  print(details(random_b))
  guess = input("Who has more followers? Type 'A' or 'B':")
  if (guess=="a" and a_follower > b_follower) or (guess=="b" and b_follower > a_follower):
    
    score = score +1

  else:
    clear()
    ans_correct=False
    print(f"Game over. Your score is{score}")
