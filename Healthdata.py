def getdate():
    import datetime
    return datetime.datetime.now()


n = int(input("Press '1' for lock or press '2' for retrieve: "))
if n == 1:
    m = int(input("Select whose data you want lock Aditya(1), Harry(2) or Karan(3): "))
    if m == 1:
        print("You have selected Aditya.")
        l = int(input("What do you want to update- Exercise(1) or Diet(2): "))
        if l ==1:
            with open("Aditya1.txt", "a") as f:
                a= input("Enter exercise: ")
                f.write("["+str(getdate())+"]  " + a)

        elif l ==2:
            with open("Aditya1.txt", "a") as f:
                a= input("Enter diet: ")
                f.write("["+str(getdate())+"]  " + a)

        else:
            print("Type right input")

    elif m == 2:
        print("You have selected Harry.")
        l = int(input("What do you want to update- Exercise(1) or Diet(2): "))
        if l == 1:
            with open("Harry1.txt", "a") as f:
                a = input("Enter exercise: ")
                f.write("[" + str(getdate()) + "]  " + a)

        elif l == 2:
            with open("Harry1.txt", "a") as f:
                a = input("Enter diet: ")
                f.write("[" + str(getdate()) + "]  " + a)

        else:
            print("Type right input")

    elif m == 3:
        print("You have selected Karan.")
        l = int(input("What do you want to update- Exercise(1) or Diet(2): "))
        if l == 1:
            with open("Karan1.txt", "a") as f:
                a = input("Enter exercise: ")
                f.write("[" + str(getdate()) + "]  " + a)

        elif l == 2:
            with open("Karan1.txt", "a") as f:
                a = input("Enter diet: ")
                f.write("[" + str(getdate()) + "]  " + a)

        else:
            print("Type right input")

    else:
        print("Type right input")

elif n ==2:
    m = int(input("Select whose data you want retrieve Aditya(1), Harry(2) or Karan(3): "))
    if m == 1:
        print("You have selected Aditya.")
        l = int(input("What do you want to check- Exercise(1) or Diet(2): "))
        if l == 1:
            with open("Aditya1.txt", "r") as f:
                a = f.read()
                print(a)


        elif l == 2:
            with open("Aditya1.txt", "r") as f:
                a = f.read()
                print(a)


        else:
            print("Type right input")

    elif m == 2:
        print("You have selected Harry.")
        l = int(input("What do you want to check- Exercise(1) or Diet(2): "))
        if l == 1:
            with open("Harry1.txt", "r") as f:
                a = f.read()
                print(a)

        elif l == 2:
            with open("Harry1.txt", "r") as f:
                a = f.read()
                print(a)

        else:
            print("Type right input")

    elif m == 3:
        print("You have selected Karan.")
        l = int(input("What do you want to check- Exercise(1) or Diet(2): "))
        if l == 1:
            with open("Karan1.txt", "r") as f:
                a = f.read()
                print(a)

        elif l == 2:
            with open("Karan1.txt", "r") as f:
                a = f.read()
                print(a)

        else:
            print("Type right input")

    else:
        print("Type right input")




