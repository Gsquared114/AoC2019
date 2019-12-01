import math

Total_Fuel = 0
count = 1
print("Enter 0 if done adding modules")
    
while True:
        
    try:
        x = float((input("Enter the mass of the module: ")))
        
        if x == 0:
            print("The total amount of fuel needed is: " + str(Total_Fuel))
            break
        else:
            Fuel_Needed = (int((math.floor(x/3)-2)))
            Total_Fuel = Total_Fuel + Fuel_Needed
        print("Fuel needed for module #" + str(count) +": " + str(Fuel_Needed))
        print()
        count = count + 1
        
    except:
        print("Please enter a valid number, or 0 if done adding modules")
        print()
        continue

    
    
