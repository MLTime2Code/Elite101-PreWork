order = input('Welcome to The Bistro! What would you like to do?\n Check the menu, Place an order, Make a reservation, or leave ')

#----------------------------------------------------------

if "Check the menu" in order:
  print("Here are the options")

  options = input('Salad, Sandwhich, or Panini ')

  if "Salad" in options:
    print("Our Salad is a combination of various green vegetables like cabbage and spinach and is sprinkled in cheese. It comes with a side of dressing.")
    
  if "Sandwhich" in options:
    print("Our Sandwhich is made with fresly made bread and contains ham, mayonaise, mustard, cheese, lettuce and a special sauce.")
  
  if "Panini" in options:
    print("Our Panini is like a sandwhich but grilled and made with delicious italian bread.")
#----------------------------------------------------------
  elif "Place an order" in order:
    print("Alright, what would you like to order?")
  
    options = input('Salad, Sandwhich, or Panini ')
  
    if "Salad" in options:
      print("A healthy option, it will be ready quickly.")
    
    if "Sandwhich" in options:
      print("Okay, your order will arrive soon!")
    
#----------------------------------------------------------
    elif "Make a reservation" in order:
        print("At what time and day would you like to reserve?")
    print("Please write the month, day, and time")
  
    month_day = input('What month and day would that be? ')
    time = input ('At what time? ')
  
    print("Fortunately, " + month_day + " at " + time + "       will be available. We hope to see you then. " )
  
elif not "Check the menu"or"Place an order"or"Make a reservation"or"leave":
  print("Could you repeat that?")
  order = input('Welcome to The Bistro! What would you like to do?\n Check the menu, Place an order, Make a reservation ')
elif "leave" in order:
  print("Thank you for visiting. We hope that you will come again soon!")
  exit()
#----------------------------------------------------------
