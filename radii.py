# Jack Daniel Kinne CIS 5.  Prompt "r", display area/circum/volume/radii
print ("This Tool will help discover valuable information about Circles.")
print ("...Or at least that's the idea, anyway.  \n Try it!")

done = False
while not done:

    print ("Type a Radius.")
    r = eval(input("Radii:"))

    if r > 0:

        pi = 3.14

        print ("Your Radius is:", r)
    
        area = pi * (r**2) 
        print ("Your Area is:", area)
    
        circum = 2 * pi * r
        print ("Your Circumference is:", circum)
    
        vol = (4 * pi * r**3) / 3
        print ("Your Volume is:", vol)
    
        surface_area = 4 * pi * (r**2)
        print ("Your Surface area is:", surface_area)
    
        print ("Littera Scripta Manet \n Jack Daniel Kinne, CIS 5")
        done = True

    elif r == 0:
        print ("Your circle is a Point!  Nice try, circle.  You lose!")

    elif r < 0:
        print ("I want you to try and picture this:  Take a circle.")
        print ("Make it so small that it becomes a dot.  Invert that dot.")
        print ("Make the inversion larger.  What is this negative thing?")
        print ("It is a hole to nothingness which you have opened.")
        print ("What have you done?")
        print ("Your mad quest for numbers has ruined everything.")
        
    else:
        print ("I don't know how you did this, but i'm pretty sure...")
        print ("That's not a number.")
