order = input('Welcome to The Bistro! What would you like to do?\n Check the menu or Place an order ')


if "Check the menu" in order:
  print("Here are the options")
else:
  print("Could you say that again?")
options = input('Salad, Sandwhich, or Panini ')



if "Salad" in options:
  print("The Salad is a combination of various green vegetables like cabbage and spinach and is sprinkled in cheese. It comes with a side of dressing.")
  
if "Sandwhich" in options:
  print("The Sandwhich is made with fresly made bread and contains ham, mayonaise, mustard, cheese, and a special sauce.")

if "Panini" in options:
  print("Our Panini is like a sandwhich but grilled and made with delicious italian bread.")

order = input('Welcome to The Bistro! What would you like to do?\n Check the menu or Place an order: ')

if "Place an order" in order:
  print("Alright, what would you like to order?")
