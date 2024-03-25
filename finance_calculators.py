# =================================================================== #
# Copyright (c) 2023. Roni Reis (RR23110011802) - All rights reserved #
# =================================================================== #

# ===================== T05 - Capstone Project ====================== #
import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n")
# Investment or bond selection
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
selection = selection.lower().strip()

if (selection == "investment"):
    #
    # Interest calculation
    #
    principal = float(input("\nEnter the amount of money that your are depositing: "))
    rate = int(input("Enter the interest rate (without the '%' symbol): "))
    time = int(input("Enter the number of years you plan to invest: "))
    interest = input("What type of interest (simple, compound)? ")

    r = rate/100 # Convert rate to decimal

    if (interest.strip().lower() == "compound"):
        # Formula for the total amount when compound interest is applied:
        # A = P(1 + r)^t
        total_amount = principal * math.pow((1 + r), time)

        print("\n-----------------------------------")
        print(f"Investment:    £{principal:,.2f}")
        print(f"Interest Rate: {rate}%")
        print("Interest:      Compound interest")
        print(f"Time:          {time} years")
        print(f"Total Amount:  £{total_amount:,.2f}")
        print("-----------------------------------")
    else:
        # Formula for the total amount when simple interest is applied:
        # A = P(1 + r x t)
        total_amount = principal * (1 + r*time)

        print("\n-----------------------------------")
        print(f"Investment:    £{principal:,.2f}")
        print(f"Interest Rate: {rate}%")
        print("Interest:      Simple interest")
        print(f"Time:          {time} years")
        print(f"Total Amount:  £{total_amount:,.2f}")
        print("-----------------------------------")

elif (selection == "bond"):
    #
    # Bond repayment calculation
    #
    house_value = float(input("\nEnter the value of the house: "))
    rate = int(input("Enter the interest rate (without the '%' symbol): "))
    years = int(input("Enter the number of years you plan to repay the bond: "))

    time = years * 12 # Total number of months
    monthly_rate = (rate/100) / 12 # Monthly interest rate (in decimal)

    # Bond repayment formula:
    # R = i x P / 1 - (1+i)^-n
    repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate)**(-time))

    print("\n-----------------------------------------")
    print(f"House Value:            £{house_value:,.2f}")
    print(f"Interest Rate:          {rate}%")
    print(f"Repayment (each month): £{repayment:,.2f}")
    print(f"Time:                   {time} months")
    print("-----------------------------------------")

else:
    #
    # Selection error
    #
    print(f"\nYou should enter 'investment' or 'bond'. {'(' + selection + ')'}")