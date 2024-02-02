# Creating a function for cash on hand
def Cash_On_Hand_function(Records):
    """
    - Function will compute the difference in cash on hand
    - Function will show the day and amount where highest increment or decrement occured
    if cash on hand is always increasing or decreasing respectively
    - Function will show the top 3 highest deficit amount and the days it happened
    if cash on hand is always fluctuating
    - Function only requires 1 paramter
    """
    # Initisalising and assigning the boolean values to the variables
    increase = False
    decrease = False
    # Creating a variable for the day which highest increment occured
    increment_day = 0
    # Creating a variable for the highest increment amount
    highest_increment = 0
    # Creating a variable for the day where the highest decrement occured
    decrement_day = 0
    # Creating a variable for the highest decrement amount
    highest_decrement = 0
    # Creating an empty deficits list to store the respective deficits if needed
    deficits_list = []
    # Creating an empty sorted list to store data for sorting if needed
    sorted_list = []

    # Using a list to create the label for the top 3 deficits
    prefix = ["[HIGHEST CASH DEFICIT]", "[2ND HIGHEST CASH DEFICIT]", "[3RD HIGHEST CASH DEFICIT]"]

    # Creating a for loop to iterate over the Records list, starting from the second element to the last element. 
    for variables in range(1, len(Records)):
        # Unpacking values from the list and assigning it to the respective variables 
        current_day, current_cash_on_hand = Records[variables]
        previous_day, previous_cash_on_hand = Records[variables-1]

        # Calculating the difference through using current value minusing previous value 
        # to find if value is a deficit or a surplus
        difference = int(current_cash_on_hand)-int(previous_cash_on_hand)

        # Setting if statements to differentiate the different possible patterns
        if difference > 0:
            # If difference always bigger than 0, it means its always increasing, 
            # hence boolean value assigned to increased needs to be changed to True
            increase = True
            # Making sure that if the increment being processed is higher than the increment assigned
            # to the highest increment variable, the increment being processed will replace that value
            # ensuring that the value assigned to highest_increment is indeed the highest increment 
            if difference > highest_increment:
                # Making sure the the day displayed is the day where highest increment occured
                increment_day = current_day
                highest_increment = difference

        if difference < 0:
            # If difference always smaller than 0, it means its always decreasing,
            # hence boolean value assigned to decrease needs to be changed to True
            decrease = True
            # Making sure that if the decrement being processed is higher than the decrement assigned
            # to the highest decrement variable, the decrement being processed will replace that value
            # ensuring that the value assigned to highest_decrement is indeed the highest decrement 
            if difference > highest_decrement:
                # Making sure the the day displayed is the day where highest decrement occured
                decrement_day = current_day
                highest_decrement = difference

        # Setting an if statement if both increase and decrease is true, which should have already been set 
        # above if conditions are satisfied together with a difference < 0 as we only want the deficit
        if increase and decrease and difference < 0:
            # Appending the deficit and day deficit occured to a list
            deficits_list.append((difference, current_day))
            # Appending the deficit and day deficit occured to a list meant for sorting as we also want
            # the top 3 highest cash deficit and the days it happened
            sorted_list.append((difference, current_day))
    
    # Sorting the data to find the 3 highest deficit
    sorted_list.sort() 

    # If increase is true but decrease is false, statement for always increasing will be returned
    if increase == True and decrease == False:
        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST CASH SURPLUS] DAY: {increment_day}, AMOUNT: SGD{highest_increment}"
    # If increase is false but decrease is true, statement for always decreasing will be returned
    elif increase == False and decrease == True:
        return f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n[HIGHEST CASH DEFICIT] DAY: {decrement_day}, AMOUNT: SGD{highest_decrement}"
    # If increase and decrease both true, statement for fluctuation will be returned
    elif increase == True and decrease == True:
        # Formatting the string such that it displays the same as the expected output
        return_string = '\n'.join([f"[CASH DEFICIT] DAY: {day} AMOUNT: SGD{abs(deficits)}" for deficits, day in deficits_list])

        # Creating a for loop to iterate 3 times to get the top 3 deficits and appending it back to the variable 
        for i in range(3):
            return_string = return_string + f"\n{prefix[i]} DAY: {sorted_list[i][1]} AMOUNT: SGD {abs(sorted_list[i][0])}"

        # Returning all the days and amounts where deficit occured, together with the top 3 highest deficit day and amount
        return return_string
