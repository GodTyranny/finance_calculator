#Import
import math


#Variable declaration
#Input from user
string_input = ""

#Investment and Bond - user input
float_money = 0 #Get value in index 0
float_interest_rate = 0 #Get value in index 1
float_investment_time = 0 #Get value in index 2
bool_is_compound = False #Get value in index 3 - Only investment
float_total_after = 0 #Money after investment





#Index to use in if else statement to prevent reqeusting again confirmed value
int_index = 0

#Loop until break after calculation
while True:
    #Ask user what kind of investment they want to do
    print("Choose between \'INVESTMENT\' or \'BOND' from the typing selection below to proceed\n") #Spacing to improve readability
    print("Short eplaination:")
    print("Investment\t-  To calculate the amount of interest you'll earn on your investment")
    print("Bond\t\t-  To calculate the amount you'll have to pay on a home loan")
    print() #Spacing to improve readability
    string_input = input("Please type what calculation you need to select.\nINVESTMENT - BOND: ")

    #Clean and prepare user input to be check
    string_input = string_input.strip() #Remove all the side space
    string_input = string_input.replace(".","") #Remove the point, may be used as end of phrase
    string_input = string_input.upper() #Prevent case sensitive error
    print() #Spacing to improve readability

    if string_input == "INVESTMENT":

        print("Great you choose INVESTMENT! Let's go on")
        print() #Spacing to improve readability

        #Loop until break
        while True:
            try:
                #Using index inside else if statement to prevent from asking again correct value if one is not
                if int_index == 0:
                    print("How much is the amount you want to deposit?") 
                    #User input about deposit amount
                    float_money = float(input("Deposit in $: "))
                    print() #Spacing to improve readability
                    int_index += 1 #Next index
                elif int_index == 1:
                    print("How much is the interest rate you have?")
                    #User input about interest rate
                    float_interest_rate = float(input("Interest rate each year in %: "))
                    print() #Spacing to improve readability
                    int_index += 1 #Next index
                elif int_index == 2:
                    print("How many years you plan to let them invested?")
                    #User input about investment time
                    float_investment_time = float(input("Investment time in years: "))
                    print() #Spacing to improve readability
                    int_index += 1 #Next index
                elif int_index == 3:
                    #Ask user what kind of investment rate they want
                    print("Choose between \'SIMPLE\' or \'COMPOUND' from the typing selection below to proceed\n") #Spacing to improve readability
                    print("Short eplaination:")
                    print("Simple\t\t-  Interest based on the starting amount")
                    print("Compound\t-  Interest based on the current amount")
                    print() #Spacing to improve readability
                    string_input = input("Please type what interest you desire.\nSIMPLE - COMPOUND: ")

                    #Clean and prepare user input to be check
                    string_input = string_input.strip() #Remove all the side space
                    string_input = string_input.replace(".","") #Remove the point, may be used as end of phrase
                    string_input = string_input.upper() #Prevent case sensitive error
                    print() #Spacing to improve readability

                    #Get which kind of interest rate user select
                    if string_input == "SIMPLE":
                        bool_is_compound = False
                        int_index += 1 #Next index
                    elif string_input == "COMPOUND":
                        bool_is_compound = True
                        int_index += 1 #Next index
                    else:
                        #Print error
                        print("You didn't insert one of the option, please try again!")
                    print() #Spacing to improve readability                  
                else:
                    #Confirmation about insert dettails
                    print("That's everything we need for the calculation, please just confirm that you insert correct value.\n") #Spacing to improve readability
                    print("That's a recap about insert details.")
                    print(f"Deposit amount:\t\t{float_money}$")
                    print(f"Interest rate per year:\t{float_interest_rate}%")
                    print(f"Years invested:\t\t{float_investment_time} years")
                    print(f"Compound interest:\t{bool_is_compound}")
                    print() #Spacing to improve readability

                    string_input = input("Is everything correct? Answer with YES or NO.\nKeep in mind that answering NO will ask you to insert them again: ")

                    #Clean and prepare user input to be check
                    string_input = string_input.strip() #Remove all the side space
                    string_input = string_input.replace(".","") #Remove the point, may be used as end of phrase
                    string_input = string_input.upper() #Prevent case sensitive error
                    print() #Spacing to improve readability

                    #Yes to start all the end calculation required
                    if string_input == "YES":
                        #Adjust interest value for calulation as is a percentage
                        float_interest_rate /= 100

                        #Calculation for compound interest or not
                        if bool_is_compound:
                            float_total_after = float_money * math.pow((1 + float_interest_rate), float_investment_time)
                        else:
                            float_total_after = float_money * (1 + (float_interest_rate * float_investment_time))
                        #Round the amount
                        float_total_after = round(float_total_after, 2)
                        
                        print(f"Congratulation your money have become: {float_total_after}$")
                        #Stop current loop
                        break
                    #No to restart inserting all the value
                    elif string_input == "NO":
                        int_index = 0 #Index to restart
                    else:
                        #Print error message
                        print("You didn't insert one of the option, please try again!")
                        print() #Spacing to improve readability
            except:
                #Print error message
                print("You are pleased to insert a real number")
                print() #Spacing to improve readability

        #Stop out statement loop
        break
    elif string_input == "BOND":

        print("Great you choose BOND! Let's go on")
        print() #Spacing to improve readability

        #Loop until break
        while True:
            try:
                #Using index inside else if statement to prevent from asking again correct value if one is not
                if int_index == 0:
                    print("How much is the amount you withdraw for the bond?") 
                    #User input about bond amount
                    float_money = float(input("Bond amount in $: "))
                    print() #Spacing to improve readability
                    int_index += 1 #Next index
                elif int_index == 1:
                    print("How much is the interest rate you have?")
                    #User input about interest rate
                    float_interest_rate = float(input("Interest rate each year in %: "))
                    print() #Spacing to improve readability
                    int_index += 1 #Next index
                elif int_index == 2:
                    print("How many month you plan to take to repay the bond?")
                    #User input about time
                    float_investment_time = float(input("Time to repay in month: "))
                    print() #Spacing to improve readability
                    int_index += 1 #Next index                
                else:
                    #Confirmation about insert dettails
                    print("That's everything we need for the calculation, please just confirm that you insert correct value.\n") #Spacing to improve readability
                    print("That's a recap about insert details.")
                    print(f"Bond amount:\t\t{float_money}$")
                    print(f"Interest rate per year:\t{float_interest_rate}%")
                    print(f"Month to repay:\t\t{float_investment_time} month")
                    print() #Spacing to improve readability

                    string_input = input("Is everything correct? Answer with YES or NO.\nKeep in mind that answering NO will ask you to insert them again: ")

                    #Clean and prepare user input to be check
                    string_input = string_input.strip() #Remove all the side space
                    string_input = string_input.replace(".","") #Remove the point, may be used as end of phrase
                    string_input = string_input.upper() #Prevent case sensitive error
                    print() #Spacing to improve readability

                    #Yes to start all the end calculation required
                    if string_input == "YES":
                        #Adjust interest value for calulation as is a percentage
                        float_interest_rate /= 100
                        #Montly interest
                        float_interest_rate /= 12

                        #Calculation for bond interest and round
                        float_total_after = (float_interest_rate * float_money) / (1 - math.pow((1 + float_interest_rate), -float_investment_time))
                        float_total_after = round(float_total_after, 2)
                        #Get all the information
                        print(f"Money you have to repay are:\t{float_total_after}$")
                        print(f"Each month per:\t\t\t{float_investment_time} month")
                        print(f"For a total of:\t\t\t{round(float_total_after * float_investment_time, 2)}$") #Add extra round for misterious decimal issue
                        #Stop current loop
                        break
                    #No to restart inserting all the value
                    elif string_input == "NO":
                        int_index = 0 #Index to restart
                    else:
                        #Print error message
                        print("You didn't insert one of the option, please try again!")
                        print() #Spacing to improve readability
            except:
                #Print error message
                print("You are pleased to insert a real number")
                print() #Spacing to improve readability

        #Stop out statement loop
        break
    else:
        #Print error
        print("You didn't insert one of the option, please try again!")


