
commision_amount=0.0
transaction_amount=float(input("Enter an amount of transaction : "))
if transaction_amount <2500:
    commision_amount=transaction_amount*1.7/100
    commision_rate=30+commision_amount
elif transaction_amount >=2500 and transaction_amount <6250:
    commision_amount=transaction_amount*0.66/100
    commision_rate=56+commision_amount
elif transaction_amount >=6250 and transaction_amount <20000:
    commision_amount=transaction_amount*0.34/100
    commision_rate=76+commision_amount
elif transaction_amount >=20000 and transaction_amount <50000:
    commision_amount=transaction_amount*0.22/100
    commision_rate=100+commision_amount
elif transaction_amount >=50000 and transaction_amount <500000:
    commision_amount=transaction_amount*0.11/100
    commision_rate=155+commision_amount
elif transaction_amount >=500000:
    commision_amount=transaction_amount*0.09/100
    commision_rate=225+commision_amount
print("The commision rate is : %.2f "%commision_rate)
