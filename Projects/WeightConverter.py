print("Welcome to the weight converter")
weight = int(input("enter in your weight: "))
unit_of_measure = input("enter (L)bs or (K)g: ").lower()
converted_weight = 0
kg = 0.45


if unit_of_measure == "l":
    converted_weight = weight * kg
    unit_of_measure = "kilograms"
else:
    converted_weight = weight / kg
    unit_of_measure = "pounds"

print(f"you weigh {converted_weight} {unit_of_measure}")
