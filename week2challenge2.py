
balance = 4773	
annualInterestRate = 0.2
monthlyInterestRate 	= annualInterestRate / 12
minMonthPayment = 0

previousBalance = balance
while previousBalance > 0:
	previousBalance = balance
	minMonthPayment += 10

	counter = 12
	while counter > 0:	

		monthlyUnpaidBalance = previousBalance - minMonthPayment
		previousBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

		counter -= 1

print('Lowest Payment: ', minMonthPayment)

