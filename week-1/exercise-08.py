# Exercise 08: Traffic Light Simulator (Case-Insensitive)

signal = input("Enter traffic light color (red/yellow/green): ")

# Convert input to lowercase to avoid case sensitivity issues
signal = signal.lower()

if signal == "red":
    print("STOP!")
elif signal == "yellow":
    print("Prepare to stop")
elif signal == "green":
    print("You can go")
else:
    print("Wrong input!")
