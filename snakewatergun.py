import random

print("\t\t\tWelcome to SNAKE WATER GUN game\n")
a_point = 0
b_point = 0
tie_point = 0
attempts=1
while attempts<=10:
    a = input("Choose Snake(s) or Water(w) or Gun(g): ").lower()
    b = random.choice(["s", "w", "g"])
    if (b=="s" and a=="s") or (b=="w" and a=="w") or (b=="g" and a=="g"):
         print("Tie")
         tie_point+=1
    elif (b=="s" and a == "w") or (b=="w" and a=="g") or (b=="g" and a=="s"):
         print("Computer won")
         b_point+=1
    elif (b=="s" and a=="g") or (b=="w" and a=="s") or (b=="g" and a=="w"):
         print("You won")
         a_point+=1
    else:
         print("Invalid Input!")
         continue

    print("No. of attempts left {}".format(10-attempts))
    attempts+=1

    if attempts>10:
        print("Game over!\n")

print(f"Your score: {a_point}\nComputer score: {b_point}\nTie: {tie_point}")
if a_point>b_point:
    print("\nYou Won Congratulations:)")
elif b_point>a_point:
    print("\nSo sad you loose:( , Computer Won")
else:
    print("\nNo one won, Its a tie")



















