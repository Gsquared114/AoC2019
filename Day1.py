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
            Current_Module = Fuel_Needed
            Fuel_for_Fuel = 0
            
            while Fuel_Needed > 5:
                Fuel_Needed = (int((math.floor(Fuel_Needed/3)-2)))
                Fuel_for_Fuel = Fuel_for_Fuel + Fuel_Needed 
                
            Total_Fuel = Total_Fuel + Fuel_for_Fuel
            
        print("Fuel needed for module #" + str(count) +": " + str(Current_Module + Fuel_for_Fuel))
        print()
        count = count + 1
        
    except:
        print("Please enter a valid number, or 0 if done adding modules")
        print()
        continue

    
    
