temperature = float(input("What is the temperature outside? "))
if temperature < 55:
    clothes = "a warm raincoat" if weather == "raining" else "a fleece"
else:  # 55 or warmer..
    clothes = "an umbrella" if weather == "raining" else "sunglasses"
print("You should bring {0}.".format(clothes))
