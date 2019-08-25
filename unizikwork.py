import math
cheta_height = 5
cheta_mass = 50
chidera_height = 3
chidera_mass = 30
cheta_BMI = (cheta_mass/math.pow(cheta_height,2))
print(cheta_BMI)
chidera_BMI= (chidera_mass/math.pow(chidera_height,2))
print(chidera_BMI)
print("Is cheta's BMI higher than chidera's BMI")
if cheta_BMI > chidera_BMI:
    print("Yes")
else:
    print("No")