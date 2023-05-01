print('''
         
            ______  __  __   ______       ______   __  __   ______       ______   ______  ______   ______  
            /\__  _\/\ \_\ \ /\  ___\     /\  == \ /\ \/\ \ /\  ___\     /\  ___\ /\__  _\/\  __ \ /\  == \ 
            \/_/\ \/\ \  __ \\\ \  __\     \ \  __< \ \ \_\ \\\ \___  \    \ \___  \\\\/_/\ \/\ \ \/\ \\\\ \  _-/ 
               \ \_\ \ \_\ \_\\\ \_____\    \ \_____\\\ \_____\\\\/\_____\    \/\_____\  \ \_\ \ \_____\\\\ \_\   
                \/_/  \/_/\/_/ \/_____/     \/_____/ \/_____/ \/_____/     \/_____/   \/_/  \/_____/ \/_/   
                                                                                                

    
                                                           ''')
_continue = input("Welcome, press enter to continue" )

print("\nYou find yourself at a bus stop, late at night, when a **FROG** suddenly interrupts your routine.")
print("It is big and unlike any you've seen before. You are bored. Despite feeling bored,\nyou can't help but sense that this is a special night.\n However, you also feel a bit afraid.")
print("Kiss it? (type: 'yes' or 'no')")
kiss_frog = input().lower()
print('''
         o-o
        /,_,\\
      ,Mm/_\\mM,
''')

if kiss_frog == 'yes':
    print('It was poisonous.\nGame over.')
else:
  print("The frog hops aways... ... ...")
  print("An odd orange bus arrives.")
  print("It has the identification of your bus in It")
  print("weird... The door opens.. its 5 min early, a voice calls you")
  bus_decision =  input("What do you do? run? do nothing ? get on the bus? ")
  if bus_decision.lower() == 'run':
    print("You get to a safe place. Call an uber. You're back home to your boring routine\nGame over")
  elif bus_decision.lower() == 'do nothing':
    print("The strange bus drives away...")
    print("Your bus arrives. your are back to your boring routine\nGame over")
  elif bus_decision.lower() != 'get on the bus':
    print('Game over.')
  else:
      print("The driver apologizes for being a little late.")
      print("Somthing is strange. The Bus' design seems from 40 years ago")
      print("but the vehicle itself looks brand new.")  
      input("press enter to continue")
      print("It's your bus!! but it appears to be lost in time.")
      print('''
            As it drops you off at your destination, \nyou take a look around and realize that you have traveled through time.
            People are dressed differently and have different hairstyles 
            Awesome! Don't tell anyone! 
            Go win the lottery and buy some stocks.
            You win!
           ''') 
    