year = int(input("Which year you want to check leap year or not?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a Leap Year.")
        else:
            print("It's not a Leap Year.")    
    else:
        print("It's a Leap Year.")     
else:
    print("It's not a Leap Year.")           