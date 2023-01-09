order = input('Welcome to The Bistro! What would you like to do?\n Check the menu, Place an order, Make a reservation ')

#----------------------------------------------------------
while order == "Check the menu":
    if "Check the menu" in order:
      print("Here are the options")
  
      options = input('Salad, Sandwhich, or Panini ')
      another = input('Would you like to do something else? Yes or No ')
      if "Yes" in another:
          break
        
      if "No" in another:
        if "Salad" in options:
         print("Our Salad is a combination of various green vegetables like cabbage and spinach and is sprinkled in cheese. It comes with a side of dressing.")
      
        if "Sandwhich" in options:
          print("Our Sandwhich is made with fresly made bread and contains ham, mayonaise, mustard, cheese, lettuce and a special sauce.")
    
        if "Panini" in options:
          print("Our Panini is like a sandwhich but grilled and made with delicious italian bread.")
  
  #----------------------------------------------------------
while order == "Place an order":
    if "Place an order" in order:
      print("Alright, what would you like to order?")
    
      options = input('Salad, Sandwhich, or Panini ')
      another = input('Would you like to do something else? Yes or No ')
      if "Yes" in another:
        break
        
      if "No" in another:
        if "Salad" in options:
          print("A healthy option, it will be ready quickly.")
      
        if "Sandwhich" in options:
          print("Okay, your order will arrive soon!")
      
        if "Panini" in options:
         print("It will take more time to prepare but the wait will be worth it!")
  
  #----------------------------------------------------------
if "Make a reservation" in order:
      print("At what time and day would you like to reserve?")
      print("Please write the month, day, and time")
      month_day = input('What month and day would that be? ')
      time = input ('At what time? ')
    
      print("Fortunately, " + month_day + " at " + time + " will be available. We hope to see you then. " )

#------------------------------------------------------------
