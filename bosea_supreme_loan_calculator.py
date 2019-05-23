#This project is to test the Bosea Supreme loan computation
#formula is ((l*1.i)-r)+(outstanding*1.i)
loanAmount = 0
repaymentAmount = 0

loanAmount = input("How much do you wish to secure ")
loanAmount = float(loanAmount)
repaymentAmount = input ("State repayment for the first month ")
repaymentAmount = float(repaymentAmount)
#Loan durtation from supreme should be within 31 to 62 days 
loanDuration = input("How long do you want the loan for ")
loanDuration = int(loanDuration)
#Convert the duration into days
duration_perday = loanDuration/31
#find the interest on the loan using the duration per day
interest = duration_perday*(loanAmount*.20)

outstanding = (loanAmount+interest)-repaymentAmount
interestOnOustanding = outstanding*.20

repaymentSecMonth = outstanding+interestOnOustanding
totalInterestPaid = interest+interestOnOustanding
totalRepayment = loanAmount+interest+interestOnOustanding

print("Loan amount is {0:0.2f}".format(loanAmount))
print("Total Interest for the two months is {0:0.2f}".format(totalInterestPaid))
print("Total repayment at the end of two months {0:0.2f}".format(totalRepayment))
