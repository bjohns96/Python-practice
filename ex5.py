_name = 'Zed A. Shaw'
_age = 35 # not a lie
_height = 74 # inches
_weight = 180 #lbs
_eyes = 'Blue'
_teeth = 'White'
_hair = 'Brown'
new_height = _height*2.54
new_weight = 180/2.205

print(f"Let's talk about {_name}.")
print(f"He's {new_height} centimeters tall.")
print(f"He's {new_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {_eyes} eyes and {_hair} hair.")
print(f"His teeth are usually {_teeth} depending on the coffee.")


#this line is tricky, try to get it exactly right
total = _age + _height + _weight
print(f"If I add {_age}, {_height}, and {_weight} I get {total}.")
