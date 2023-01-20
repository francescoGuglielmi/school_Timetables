 #Python first program

#I want to study at the campus which is opened from 7 to 17 but during the night the I can enter only if the guard is present.

hour = int(input("Enter the hour of the time you want to study at the campus: "))
  
if 7 < hour < 17:
    guard = True
    print("You're in!")
   #Let's add a random 1/2 probability to study at the Campus.
elif 0 < hour < 7 or 7 < hour < 23:
    print("You gotta be lucky!")
    import random
    t_or_f = random.randint(0,1)
    if t_or_f == 1: 
      guard = True
      print("You're in this time!") 
    else: 
      guard = False
      print("I need to go home...")
else:
    print ("invalid time, try again.")