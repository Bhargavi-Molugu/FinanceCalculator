#=====Capstone Project I-This project is to build two calculators (Investement and Home Loan Repayment) =====
#To Accomplish the Capstone Project, I have used conditional operators and math module.
import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("\nbond\t   - to calculate the amount you'll have to pay on a home loan ")
print("Enter either 'investment' or 'bond' from the menu above to proceed: ")
calculation_var = input("Choose one of the calculation 'investment' or 'bond': ")

#If the input from user is 'Investment' the below logic calculates the total amount
if calculation_var.upper() == 'INVESTMENT':
    deposit_money = float(input("Enter the money you want to deposit: "))
    interest_rate = float(input("Enter the rate of interest(rate is taken as a percentage): "))
    investing_time = float(input("Enter the number of Years you plan to invest: "))
    interest = input("Enter the interest type ('Simple' or 'Compound') " )

    #Calculating the total amount depending on the interest type(simple/compound).
    if interest.upper() == 'SIMPLE':
        total_amount = deposit_money * (1 + ((interest_rate/100) * investing_time))
        print(f"The total amount of an investment when Simple interest is applied is : {total_amount}" )
    elif interest.upper() == 'COMPOUND':
        total_amount = deposit_money * (math.pow((1+ (interest_rate/100)),investing_time))
        print(f"The total amount of an investment when Compound interest is applied is : {total_amount}" )
    else:
        print("Please enter the valid interest type 'Simple" or 'Compound')

#If input value from user is 'BOND' the below logic calculates the amount to be repaid for each month.
elif calculation_var.upper() == 'BOND':
    present_value =float(input("Enter the present value of the house: "))
    rate_of_interest = float(input("Enter the rate of Interest: "))
    repay_months = float(input("Enter the months you plan to take to repay the bond: "))
    monthly_interest_rate = (rate_of_interest/100)/12
    #Bond repayment formula calculation
    amount_repaid = (monthly_interest_rate * present_value)/(1-((1+monthly_interest_rate) ** (-repay_months)))
    print(f"The amount you will have to be repaid for the home loan each month is: {amount_repaid} ")

#if the user input is other than 'investment' or 'bond' returning below error.
else:
    print("Invalid Input, Please enter the type of calculation ('investment' or 'bond').")
