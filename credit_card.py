#Aysha Sumaiya: ayshasumaiya74@gmail.com
#INST 326 - Object-Oriented Programming for Information Science
#Assignment: HOMEWORK #2
#Date: 9_19_21 


"""Perform credit card calculations."""
from argparse import ArgumentParser
import sys

def get_min_payment(b, f=0):
    """
    Caculates credit card payment (minimum) on of credit card

    Args:
    b = the balance in the account
    f = the amount of fees that will be paid per month.
    m = the percent of the balance that needs to be paid
    
    Set minimum payment to 25, if minimum payment was computed using the formula is below 25
    
    Return
    minimum_payment = The minimym card payment 
    """
    m=0.02
    minimum_payment = ((b * m) + f)
    if minimum_payment < 25:
        minimum_payment = 25
    return minimum_payment


def interest_charged(a,b):
    """
    Caculates interest charged on credit card

    Args:
    a = APR expressed as a floating point number
    y = the amount of days in a year
    b = the balance in the account
    d = the number of days in a billing cycle (30 days each time)
    
    Return
    i = the amount of interest accrued in the next payment
    """
    y = 365                  #The amount of days in a year
    d = 30                   #the number of days in a billing cycle 
    i = ((a/100)/y) * b * d
    return i



def remaining_payments(credit_balance, annual_rate, target_payment, credit_line = 5000, a=0):
    """
    Caculates the remaining payment 

    Args:
    credit_balance = The amount in the account that has not been paid off yet
    annual_rate = Annual APR; this is an integer between 0 and 100
    target_payment = The amount the user wants to pay per payment;
    credit_line = The maximum amount of balance that an account holder can keep in their account; defaults to 5000
    a =  amount of fees that will be charged in addition to the minimum payment; positive integer; defaults to 0
    
    Return: counter_payment, counter_target_payment, counter_fees, counter_spend
    """
    counter_payment = 0 
    counter_target_payment = 0 
    counter_fees = 0 
    counter_spend = 0 

    while credit_balance > 0: 
        if target_payment == None:
            payment_amount = get_min_payment(credit_balance, a)
        else:
            payment_amount = target_payment
        payment_toward_balance = payment_amount - interest_charged(annual_rate, credit_balance)
        if payment_toward_balance < 0:
            print("The card balance can not be paid off.")
            return
        
        credit_balance -= payment_toward_balance
        if credit_balance > .75 * credit_line:
            counter_spend += 1
        if credit_balance > .5 * credit_line:
            counter_fees += 1
        if credit_balance > .25 * credit_line:
            counter_target_payment += 1
        counter_payment += 1
    return counter_payment, counter_target_payment, counter_fees, counter_spend



def main (b, apr, credit_line=5000, targetamount = None, fees=0):
    """ 
    Amount in the account that has not been paid off yet; this is a positive number.
    
    Args:
    b = the balance in the account
    apr = Annual APR
    targetamount = The amount the user wants to pay per payment (parameter was passed in as None)
    credit_line = The maximum amount of balance that an account holder can keep in their account; defaults to 5000
    fees =  The amount of fees that will be charged in addition to the minimum payment ; defaults to 0
    
    Returns:
    reco_minimum_payment = Recommended minimum payment
    total_card_payment = Number of payments
    targetamount = Target payment amount

    
    Display another message that will show the user hoe many payment they wull be above 25%, 50%, and 75%
    """
    reco_minimum_payment = get_min_payment(b,fees)        #recommanded mini payment 
    print(f"Your recommended starting minimum payment is $", reco_minimum_payment)
    pays_minimum = False
    if targetamount == None:
        pays_minimum = True
    elif targetamount < reco_minimum_payment:
        print(f"Your target payment is less than the minimum payment for this credit card.")
        return
        
    total_card_payment = remaining_payments(b, apr, targetamount, credit_line, fees)
    if pays_minimum == True:
        print(f"If you pay the minimum payments each month, you will pay off the credit card in {total_card_payment[0]} payments.")
    if pays_minimum == False:
        print(f"If you make payments of $ {targetamount}, you will pay off the credit car in {total_card_payment[0]} payments.")
    return(f"You will spend a total of {total_card_payment[1]} months over 25% of the credit line. \nYou will spend a total of {total_card_payment[2]} months over 50% of the credit line. \nYou will spend a total of {total_card_payment[3]} months over 75% of the credit line.")


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments

    Args:
    args_list (list) : the list of strings from the command prompt

    Returns:
    args (ArgumentParser)
    """
    parser = ArgumentParser()

    parser.add_argument('balance_amount', type = float, help = 'The total amount of balance left on the credit account')
    parser.add_argument('apr', type = int, help = 'The annual APR, should be an int between 1 and 100')
    parser.add_argument('credit_line', type = int, default = 5000, help = 'The maximum amount of balance allowed on the credit line.')
    parser.add_argument('--payment', type = int, default = None, help = 'The amount the user wants to pay per payment, should be a positive number')
    parser.add_argument('--fees', type = float, default = 0, help = 'The fees that are applied monthly.')

    # parse and validate arguments
    args = parser.parse_args(args_list)

    if args.balance_amount < 0:
        raise ValueError("balance amount must be positive")
    if not 0 <= args.apr <= 100:
        raise ValueError("APR must be between 0 and 100")
    if args.credit_line < 1:
        raise ValueError("credit line must be positive")
    if args.payment is not None and args.payment < 0:
        raise ValueError("number of payments per year must be positive")
    if args.fees < 0:
        raise ValueError("fees must be positive")
    
    return args

if __name__ == "__main__":

    try:
        arguments = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    
    print(main(arguments.balance_amount, arguments.apr, credit_line = arguments.credit_line, targetamount = arguments.payment, fees = arguments.fees))