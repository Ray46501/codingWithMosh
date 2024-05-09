command =  ""
started = False

while command.lower() != 'quit':
    command = input('> ')
    if command.lower() == 'start':
        print(" Car started ...")
        if started:
            print("car is already started!")

    elif command.lower() == "stop":
        print('car stopped.')
        if not started:
            print('car is already stopped!')

    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    
    else:
        print('sorry, i dont understand that!')