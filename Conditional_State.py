"""
temperature = float(input("What is the temperature outside? "))
weather = input("Is it raining or sunny outside? ")
weather = weather.lower() # change to lower case
if temperature < 55:
    clothes = "a warm raincoat" if weather == "raining" else "a fleece"
else:  # 55 or warmer..
    clothes = "an umbrella" if weather == "raining" else "sunglasses"
print("You should bring {0}.".format(clothes))
"""

temperatures = [12, 46, 24, 67, 80, 26, 64, 24, 45, 40]
howitfeels = ["{0} is Brr!".format(temp) if temp < 50 else temp for temp in temperatures]
print(howitfeels)
#['12 is Brr!', 46, '24 is Brr!', 67, 80, '26 is Brr!', 64, '24 is Brr!', 45, 40]
print(temp)
