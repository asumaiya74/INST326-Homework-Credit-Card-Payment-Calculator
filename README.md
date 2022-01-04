# Instructions
For this homework you will write a script to do some useful calculations for credit card payments. Use the template provided below. At a minimum, your script should contain the functions get_min_payment(), interest_charged(), remaining_payments(), and main(), each of which is described below. Be sure to include a docstring in each function.

_Note_:  The  resulting  script  is  only  an  example  of  a  remaining  payments  calculator  and  may  not accurately reflect the same calculation methods as your personal credit card. This script should not be used to make financial decisions.

# get_min_payment()
**Parameters**
- The  total  amount  of  the  balance  in  an  account  that  is  left  to  pay  (called  the  balance;  you  can assume this is a positive number)
- The  fees  associated  with  the  credit  card  account  (you  can  assume  this  is  a  positive  integer; assign this parameter a default value of 0)

**Functionality**
1. Compute the minimum credit card payment. (**min_payment**). You should use the formula **min_payment = ((b * m) + f)** where
    -  b is the balance in the account
    -  m  is  the  percent  of  the  balance  that  needs  to  be  paid  (represented  as  a  float  where  2%  is represented as .02). Make the constant value of this variable .02. Note: This is not the same thing as the APR.
    -  f is the amount of fees that will be paid per month.
2. Determine  if  the  minimum  payment  that  was  computed  using  the  formula  is  below  25.  If  is  is, we should set the minimum payment to 25 instead. Return this number.

> Note : This  function  takes  into  account  only  balance,  the  minimum  payment  percentage, and  fees.  In  the  real  world,  minimum  credit  card  payments  may  take  more  factors into account.

# interest_charged()
# remaining_payments()
# main()
# Running your program
Your program is designed to run from the terminal. To run it, open a terminal and ensure you are
in the directory where your script is saved.

The  program  takes  three  required  command-line  arguments:  a  balance  amount,  an  APR  integer (expressed  as  a  number  between  0  and  100)  and  a  credit  line  amount  (expressed  as  a  positive integer). It also allows the following optional arguments: --payment (the desired monthly payment) and --fees (the amount of monthly fees that the credit card requires). Below are some examples of how  to  use  the  program.  The  examples  assume  you  are  using  macOS  and  your  program  is  called credit_card.py.  If  you  are  using  Windows,  replace  python3  with  python.  If  your  program  has  a different name, replace credit_card.py with the name of your program.

> Basic usage: python3 credit_card.py 15_000 10 17_000
