# Paste your code into this box
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

counter = 12
while counter > 0:

	monthlyInterestRate 	= annualInterestRate / 12

	minMonthPayment 		= monthlyPaymentRate * balance

	monthlyUnpaidBalance 	= balance - minMonthPayment

	updatedBalanceMonth 	= monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

	balance 				= updatedBalanceMonth
	counter -= 1
	print(round(balance, 2))



print('Remaining balance: ', round(updatedBalanceMonth, 2))