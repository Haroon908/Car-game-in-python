get_help = input("> ")
print("start: to start the car")
print("stop: to stop the car")
print("quit: to quit ")

functions_of_car = ""
started = False
while True:
    functions_of_car = input("> ").upper()
    if functions_of_car.upper() == "START":
        if started:
            print("Already started")
        else:
            started = True
            print("Car is started")
    elif functions_of_car.upper() == "STOP":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car is stopped")
    elif functions_of_car.upper() == "QUIT":
        print("You exited")
        break
    else:
        print("I don't understand that....")
