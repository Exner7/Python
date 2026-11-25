print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1: 
    planet = "Venus"
    relative_gravity = 0.91
elif planet == 2: 
    planet = "Mars"
    relative_gravity = 0.38
elif planet == 3: 
    planet = "Jupiter"
    relative_gravity = 2.34
elif planet == 4: 
    planet = "Saturn"
    relative_gravity = 1.06
elif planet == 5: 
    planet = "Uranus"
    relative_gravity = 0.92
else: 
    planet = "Neptune"
    relative_gravity = 1.19

weight_on_destination_planet = weight * relative_gravity

print("Codey's weight on " + planet + " would be", weight_on_destination_planet)
