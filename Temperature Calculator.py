# Temperature Checker Program
temp = float(input("Enter temperature in degree Celsius: "))
if temp < -273.15:
    print("The temperature is invalid because it is below absolute zero.")

elif temp == -273.15:
    print("The temperature is absolute 0.")

elif temp > -273.15 and temp < 0:
    print("The temperature is below freezing.")

elif temp == 0:
    print("The temperature is at the freezing point.")

elif temp > 0 and temp < 100:
    print("The temperature is in the normal range.")

elif temp == 100:
    print("The temperature is at the boiling point.")

else:
    print("The temperature is above boiling point.")
