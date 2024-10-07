print("What is your monthly salary? ")
SlryAmt = float(input())
AmtMin = 30000

LoanLim = SlryAmt*10

if(SlryAmt>=AmtMin):
    print("How much loan would you like to request? ")
    AmtLoan = float(input())
    if(AmtLoan<=LoanLim):
        print("For how many months would you like to pay? ")
        input()

        MosToPay = 50
        LoanInt = 0.10
        InsTotal = AmtLoan+(AmtLoan*LoanInt)
        MthlyPay = InsTotal / MosToPay
        
        print("Great! Your monthly instalment total would be" , MthlyPay)
    else:
        print("I'm sorry, your Loan Request exceeds the limit amount. Your Max loan amount is only" , LoanLim)
else:
    print("I'm sorry, you are not eligible for a loan. Enter an amount greater than or equal to" , AmtMin)
   
   
 
     