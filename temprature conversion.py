#temprature conversion



temprature = float(input("enter your temprature: "))
unit  = input("degree celsius or farhenite(dc or f):")
if unit == "dc":
    temprature = round((9 * temprature) / 5 + 32, 1)
    print(f"The temprature in farenite is {temprature}")
elif unit == "f":
    temprature = round((temprature - 32) * 5/9, 1)
    print(f"The temprature in  degree celsius is {temprature} ")

