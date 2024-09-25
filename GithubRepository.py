SlryAmt = float(250000)
AmtMin = float(30000)

LoanLim = SlryAmt*10

AmtLoan = float(2500000)

MosToPay = 7
LoanInt = 0.10
InsTotal = AmtLoan+(AmtLoan*LoanInt)
MthlyPay = InsTotal / MosToPay

if(SlryAmt>=AmtMin):
    if(AmtLoan<=LoanLim):
        print("For how many Months would you like to pay?")
        print(MosToPay) 
        print("Great! Your monthly instalment total would be" , MthlyPay)
    else:
        print("I'm sorry, your Loan Request exceeds the limit amount. Your Max loan amount is only" , LoanLim)
else:
    print("I'm sorry, you are not eligible for a loan. Enter an amount greater than or equal to" , AmtMin)
   
   
 
     
