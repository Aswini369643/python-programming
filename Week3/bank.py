def credit(Bal,value):
    Bal+=value
    return Bal
def debit(Bal,value):
    Bal_=value
    return Bal
def checkbalance(Bal):
    print("check Balance:"Bal)
Bal=0
Bal=credit(Bal,10000)
print("Amount credited:"Bal)
Bal=debit(Bal,200)
print("Amont debited:"Bal)
checkbalance(Bal)
