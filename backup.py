def enqueueCarAc():
    element=input("Enter car number and model with spaces(ex-CAR0001 model) ")
    accar.append(element)
    print(element,"is added")

def enqueueCarNAc():
    element=input("Enter car number and model with spaces(ex-CAR0001 model) ")
    nonaccar.append(element)
    print(element,"is added")

def enqueueVanAc():
    element=input("Enter van number and model with spaces(ex-CAR0001 model) ")
    acvan.append(element)
    print(element,"is added")

def enqueueVanNAc():
    element=input("Enter van number and model with spaces(ex-CAR0001 model) ")
    nonacvan.append(element)
    print(element,"is added")

def enqueueTw():
    element=input("Enter threewheeler number and model with spaces(ex-CAR0001 model) ")
    tw.append(element)
    print(element,"is added")

def enqueueTruck7():
    element=input("Enter truck number and model with spaces(ex-CAR0001 model) ")
    truck7.append(element)
    print(element,"is added")

def enqueueTruck12():
    element=input("Enter truck number and model with spaces(ex-CAR0001 model) ")
    truck12.append(element)
    print(element,"is added")

def enqueueLorry25():
    element=input("Enter lorry number and model with spaces(ex-CAR0001 model) ")
    lorry25.append(element)
    print(element,"is added")

def enqueueLorry35():
    element=input("Enter lorry number and model with spaces(ex-CAR0001 model) ")
    lorry35.append(element)
    print(element,"is added")

def dequeueCarAc():
    e=accar.pop(0)
    print("removed ",e)

def dequeueCarNAc():
    e=nonaccar.pop(0)
    print("removed ",e)

def dequeueVanAc():
    e=acvan.pop(0)
    print("removed ",e)

def dequeueVanNAc():
    e=nonacvan.pop(0)
    print("removed ",e)

def dequeueTw():
    e=tw.pop(0)
    print("removed ",e)

def dequeueTruck7():
    e=truck7.pop(0)
    print("removed ",e)

def dequeueTruck12():
    e=truck12.pop(0)
    print("removed ",e)

def dequeueLorry25():
    e=lorry25.pop(0)
    print("removed ",e)

def dequeueLorry35():
    e=lorry35.pop(0)
    print("removed ",e)
