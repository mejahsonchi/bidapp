from replit import clear
#HINT: You can call clear() to clear the output in the console.\
from art import logo
print(logo)
storage = {}
is_finished = False
while not is_finished:
  name_input = input("what is your name?: ")
  bid_input = input("what is your bid?: $")
    
  storage[name_input] = bid_input
  repeat = input('Are there any other bidders? Type "yes" or "no" ')
  if repeat == "yes":
    clear()
    is_finished = False
    
  elif repeat == "no":
    
    max_value = max(storage.values())
    max_key = max(storage, key=storage.get)
    print(f"the winner is {max_key} with the bid of {max_value}")
    is_finished = True


