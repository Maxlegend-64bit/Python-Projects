#weight converter

weight = float(input("enter your weight:"))
unit  = input("Kilogram or pounds(k or l):")
if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "l":
    weight = weight / 2.205
    unit = "kgs"
else:
    print(f"{unit} was not valid")

print(f"your weight is : {weight} {unit}")
