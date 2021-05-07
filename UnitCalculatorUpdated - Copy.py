import sys

# Greet and welcome the user
def greet_user():
    user_name = ()
    
    user_name = input("Please Enter your Name Here: ")
    print("Hello " + user_name.title() + "!, Welcome to my program.") 
greet_user()


# Imperial system is equal to 1 unit of the metric system
# Metric system is being used for the base units
imperial_system_to_metric = {
    "kilometer": "mile", 
    "millimeter": "inches", 
    "meter": "yard", 
    "centimeter": "feet"
    }

# Dictionary with the corresponding imperial units to metric
imperial_units = {
    "1 kilometer": 0.6213712,
    "1 millimeter": 0.03937008,
    "1 meter": 1.093613,
    "1 centimeter": 0.0328084
}


# Empty dictionary to store the data in
stored_data = {}


# Converting Kilometers to miles
kilometer_mile = input("Kilometers To Miles: ")
user_input1 = ((float(kilometer_mile) * 0.6213712))
print(f"{kilometer_mile} Kilometers = {user_input1} Miles")
stored_data[kilometer_mile + ' Kilometers'] = (f'{user_input1} Miles')


# Converting millimeters to inches
millimeter_inches = input("Millimeters To Inches: ")
user_input2 = (float(millimeter_inches) * 0.03937008)
print(f"{millimeter_inches} Millimeters = {user_input2} Inches")
stored_data[millimeter_inches + ' Millimeters'] = (f'{user_input2} Inches')


# Converting meters to yards
meter_yards = input("Meters To Yards: ")
user_input3 = (float(meter_yards) * 1.093613)
print(f"{meter_yards} Meters = {user_input3} Yards")
stored_data[meter_yards + ' Meters'] = (f'{user_input3} Yards')


# Converting centimeters to feet
centimeters_feet = input("Centimeters To Feet: ")
user_input4 = (float(centimeters_feet) * 0.0328084)
print(f"{centimeters_feet} Centimeters = {user_input4} Feet")
stored_data[centimeters_feet + ' Centimeters'] = (f'{user_input4} Feet')


# Creating a txt file and stroing the data in it
store_values = open('stored_data.txt', 'w')
store_values.write(str(stored_data))
store_values.close()


# Finishing output  
end_input = input("Do you want to see what values you entered, Yes or No: ")
if end_input == "yes":
    for key, value in stored_data.items():
        print(key, ' = ', value)
elif end_input == "no":
    sys.exit()
