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
