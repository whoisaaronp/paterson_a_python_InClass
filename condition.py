# print a message to the terminal window
print("Rules that govern the state of water")

# set up a variable to hodl the temperature we input
current_temp = False


while current_temp is False:
	# make this a number and clean the code up (DRY and Out)
    current_temp = input("Enter a temperature:\n")
    # see what current temp is
    print("your input:", current_temp)


    # if the current temp is a freezing or below, water  is a solid
    if (int(current_temp) < 0 or (int(current_temp) == 0)):
        print("water is solid cuz it's at or below freezing")
        current_temp = False
    # else chech another condition. if it's not freezing, is below boiling?
    elif (int(current_temp) < 100):
        print("water is a liquid, because it's above freezing and below boiling")
        current_temp = False

    elif(int(current_temp) > 100 or (int(current_temp) == 100 )):
        print("water is a gas. cuz it's like really wet")
        current_temp = False