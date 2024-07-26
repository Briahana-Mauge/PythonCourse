command = ""
car_started = False

while True:
     
    command = input("Enter a command: ").lower()
    print(' ')
    if command == 'help':
        print("""
These are the following commands you can use:
              
Start - to start the car
Stop - to stop the car
Quit - to exit
        """)
        print(' ') 
    elif command == 'start':
        if car_started:
            print("The car is running already! Try stopping the car first!!")  
            print(' ')
        else:
            car_started = True
            print("Car started... Ready to go!")
            print(' ')  
    elif command == 'stop':
        if not car_started:
            print("The car has already been stopped! Try starting the car first!!") 
            print(' ')
        else:
            car_started = False
            print("Car Stopped.")
            print(' ') 
    elif command == 'quit':
        break 
    else:
        print("I don't understand that...")
        print("Type 'Help' to find a list of command you can enter")
        print(' ')
