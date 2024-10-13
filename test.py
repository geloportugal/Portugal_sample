
AmtMin = float(3000)


SlryAmt_str = input("How much is your Monthly Salary? ")
SlryAmt = int(SlryAmt_str)
LoanLim = SlryAmt*10

AmtLoan_str = input("How much is your Loan request? ")
AmtLoan = int(AmtLoan_str)

if(SlryAmt>=AmtMin):
        if(AmtLoan<=LoanLim):
            
            MosToPay_str = input("For how many months would you like to pay?: ")
            MosToPay = int(MosToPay_str)
            LoanInt = 0.10
            InsTotal = AmtLoan+(AmtLoan*LoanInt)
            MthlyPay = InsTotal / MosToPay
            
            MthlyPayR = round(MthlyPay, 2)
            print("Great! Your monthly instalment total would be" , MthlyPayR)
        else:
            print("I'm sorry, your Loan Request exceeds the limit amount. Your Max loan amount is only" , LoanLim)
else:
        print("I'm sorry, you are not eligible for a loan. Enter an amount greater than or equal to" , AmtMin)