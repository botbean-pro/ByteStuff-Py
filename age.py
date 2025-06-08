age = int(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are 18 years old, a young adult.")
elif age > 100:
    print("You are a centenarian!")
else:
    print("ur dum")