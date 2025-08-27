import math

# Give user information.
print("""investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan \n """)

# Store the calculation type as a lower case string. use a while loop to ask for repeated input if invalid
calc_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

while calc_type != "investment" and calc_type != "bond":
    calc_type = input("Invalid input. Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Decision tree if calculation is for an investment.
if calc_type == "investment":
    # Ask for user input for required variables 
    while True:
        try:
            principal = float(input("Enter the amount of money you will be deposting: R"))
        except ValueError:
            print("Please enter only the value in Rand: ")
            continue
        else:
            break
    
    while True:
        try:
            interest_rate = float(input("Enter the interest rate (without the %): ")) / 100
        except ValueError:
            print("Please enter only the value of the interest rate: ")
            continue
        else:
            break
    
    while True:
        try:
            years = int(input("Enter the number of years you will invest for: "))
        except ValueError:
            print("Please enter only the number of years (in digits): ")
            continue
        else:
            break
    

    interest = input("What kind of interest would you like? Enter 'simple' or 'compound': ").lower()

    while interest != "simple" and interest != "compound":
        interest = input("Invalid input: enter 'simple' or 'compound'.").lower()
   
    # Calculate interest based on choice, display error message if neither chosen
    if interest == "simple":
        #calculate simple interest
        total = principal * (1 + (interest_rate * years))

        # Printing total amount earned using entered parameters.
        print("Using the current parameters: ")
        print(f"Interest rate: {interest_rate}%")
        print(f"Years of investment: {years}")
        print(f"Initial deposit: R{principal}")
        print(f"Type of interest: {interest.capitalize()}")
        print(f"You will receive R{format(total, ".2f")}")

    elif interest == "compound":
        # Calulate compund interest
        total = principal * math.pow((1 + interest_rate), years)

        # Print results
        print("Using the current parameters: ")
        print(f"Interest rate: {interest_rate * 100}%")
        print(f"Years of investment: {years}")
        print(f"Initial deposit: R{principal}")
        print(f"Type of interest: {interest.capitalize()}")
        print(f"You will receive R{format(total, ".2f")}")
else:
    # Ask for user input to calculate bond payments
    while True:
        try:
            house_value = float(input("Enter the current value of your home: R"))
        except ValueError:
            print("Please enter only the value in Rands: ")
            continue
        else:
            break
    
    while True:
        try:
            bond_rate = float(input("Enter the current bond interest rate (without the %): ")) / 100
        except ValueError:
            print("Please enter only the value of the bond interest rate: ")
            continue
        else:
            break
    
    while True:
        try:
            months = int(input("Enter the number of months you plan to take to repay the bond: "))
        except ValueError:
            print("Please enter only the number of months: ")
            continue
        else:
            break
    

    # Calculate monthly bond repayment
    repayment = ((bond_rate / 12) * house_value) / (1 - (1 + (bond_rate / 12)) ** (-months))

    # Print details of bond repayments
    print("Using the current parameters: ")
    print(f"Interest rate: {bond_rate * 100}%")
    print(f"Repayment period: {months} months")
    print(f"House value: R{house_value}")
    print(f"You will need to pay R{format(repayment, ".2f")} per month.")