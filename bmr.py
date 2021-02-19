
# Basal Metabolic Rate Calculator (but lets define another variable)
weight =  int(input ("Enter your weight in KG:    \n"))
height = int(input ("Enter your height in cm:    \n"))
age = int(input ("Enter your age in years:    \n"))
isMale = str(input("Are you a male? (y/n)"))

if isMale == "y": 	
    isMale = True 
elif isMale == "n":      
    isMale = False 
else:
    print("Error")	
    quit()

# Mifflin St. Jeor Equation for males

if isMale:
    bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
else:     
    bmr = 655.1 + (9.6* weight) + (1.8 * height) - (4.7 * age)
bar = round(bmr)
print(bmr)
