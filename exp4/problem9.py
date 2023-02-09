
# IX. The monthly payment for the given loan pays the principal and the interest. The monthly interest is computed by multiplying the monthly 
# interest rate and the balance (the remaining principal). The principal paid for the month is therefore the monthly payment minus the monthly 
# interest. Write a program that lets the user enter the loan amount, number of years, and interest rate, and then displays the amortization 
# schedule for the loan. 

def get_inputs():
    loan_amount = float(input("Enter loan amount: "))
    years = int(input("Enter number of years: "))
    interest_rate = float(input("Enter interest rate: ")) / 100
    return loan_amount, years, interest_rate

def calculate_monthly_payment(loan_amount, years, interest_rate):
    monthly_payment = loan_amount * interest_rate / (1 - (1 / (1 + interest_rate) ** (years * 12)))
    return monthly_payment

def main():
    loan_amount, years, interest_rate = get_inputs()
    monthly_payment = calculate_monthly_payment(loan_amount, years, interest_rate / 12)
    balance = loan_amount
    for i in range(1, years * 12 + 1):
        interest = balance * interest_rate / 12
        principal = monthly_payment - interest
        balance -= principal
        print("Month {0}:, interest={1:.2f}, principal={2:.2f}, balance={3:.2f}".format(i, interest, principal, balance))
main()