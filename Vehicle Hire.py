print("Welcome to CAB service")
#each list contains vehicles with their vehicle types
accar=["MT4556 toyota","CAB4567 nissan","VN0876 motorolla"]
hireacc=[] #hired ac car will add here
nonaccar=["62-6789 toyota","CY4567 fiet","65-7890 toyota"]
hirenacc=[]

acvan=["CAC7658 nissan","KL4567 toyoya","WB6547 mazda"]
hireacv=[]
nonacvan=["56-9876 toyota","VV8764 mitsubishi","67-0987 toyota"]
hirenacv=[]

tw=["AAB5678 bajaj","QU7423 bajaj","AAC4569 tvs"]
hiretw=[]

truck7=["NB4321 suzuki","NA8976 toyota","NG4321 tata"]
hiret7=[]
truck12=["NT6890 volvo","MY9874 daf","NN0345 scania"]
hiret12=[]

lorry25=["NH5678 suzuki","NY9875 mrf","MM5098 toyota"]
hirel25=[]
lorry35=["MY9876 tata","HH7536 layland","KL5632 tata"]
hirel35=[]
#start of defined functions
#vehicle list function will show vehicles in system
def vehiclelist():
    print("1.car")
    print("2.van")
    print("3.threewheeler")
    print("4.truck")
    print("5.lorry")
#each vehicle has different types,types are in below functions
def cartype():
    print("1.AC Car")
    print("2.Non-AC Car")

def vantype():
    print("1.AC Van")
    print("2.Non-AC Van")

def trucktype():
    print("1.7ft truck")
    print("2.12ft truck")

def lorrytype():
    print("1.2500kg lorry")
    print("2.3500kg lorry")
#loop starts here and end of defined functions
while True:
    print("1.Add vehicle")
    print("2.Remove vehicle ")
    print("3.Show vehicles ")
    print("4.Hire ")
    print("5.Re-list ")
    print("6.Hired list ")
    print("7.quit")
    choice=int(input("Enter service you need from list "))
#take inputs and see for valid condition
    if choice==1: #vehicle adding condition
        vehiclelist() #function call for vehicles list
        vinput=int(input("Enter vehicle number from list "))
        if vinput==1:
            cartype() #vehicle type function call

            typeinput=int(input("Enter car type number from list"))
            if typeinput==1:
                element=input("Enter car number and model with spaces(ex-CAR0001 model) ")
                accar.append(element) #by using append item will add to end of represented list
                print(element,"is added")
            if typeinput==2:
                element=input("Enter car number and model with spaces(ex-CAR0001 model) ")
                nonaccar.append(element)
                print(element,"is added")

        if vinput==2:
            vantype()

            typeinput=int(input("Enter van type number from list"))
            if typeinput==1:
                element=input("Enter van number and model with spaces(ex-CAR0001 model) ")
                acvan.append(element)
                print(element,"is added")
            if typeinput==2:
                element=input("Enter van number and model with spaces(ex-CAR0001 model) ")
                nonacvan.append(element)
                print(element,"is added")

        if vinput==3:
            element=input("Enter threewheeler number and model with spaces(ex-CAR0001 model) ")
            tw.append(element)
            print(element,"is added")

        if vinput==4:
            trucktype()

            typeinput=int(input("Enter truck type number from list"))
            if typeinput==1:
                element=input("Enter truck number and model with spaces(ex-CAR0001 model) ")
                truck7.append(element)
                print(element,"is added")
            if typeinput==2:
                element=input("Enter truck number and model with spaces(ex-CAR0001 model) ")
                truck12.append(element)
                print(element,"is added")

        if vinput==5:
            lorrytype()

            typeinput=int(input("Enter lorry type number from list"))
            if typeinput==1:
                element=input("Enter lorry number and model with spaces(ex-CAR0001 model) ")
                lorry25.append(element)
                print(element,"is added")
            if typeinput==2:
                element=input("Enter lorry number and model with spaces(ex-CAR0001 model) ")
                lorry35.append(element)
                print(element,"is added")
#adding vehicle will end here
    elif choice==2: #remove vehicle condition
        vehiclelist()
        vinput=int(input("Enter vehicle number from list "))

        if vinput==1:
            cartype()

            typeinput=int(input("Enter car type number from list"))
            if typeinput==1:
                e=accar.pop(0) #by using pop method item that added last or item at the end of list will remove
                print("removed ",e)
            if typeinput==2:
                e=nonaccar.pop(0)
                print("removed ",e)

        if vinput==2:
            vantype()

            typeinput=int(input("Enter van type number from list"))
            if typeinput==1:
                e=acvan.pop(0)
                print("removed ",e)
            if typeinput==2:
                e=nonacvan.pop(0)
                print("removed ",e)

        if vinput==3:
            e=tw.pop(0)
            print("removed ",e)


        if vinput==4:
            trucktype()

            typeinput=int(input("Enter truck type number from list"))
            if typeinput==1:
                e=truck7.pop(0)
                print("removed ",e)
            if typeinput==2:
                e=truck12.pop(0)
                print("removed ",e)

        if vinput==5:
            lorrytype()

            typeinput=int(input("Enter lorry type number from list"))
            if typeinput==1:
                e=lorry25.pop(0)
                print("removed ",e)
            if typeinput==2:
                e=lorry35.pop(0)
                print("removed ",e)
#remove vehicles end here
    elif choice==3: #display vehicles condition
        vehiclelist()
        vinput=int(input("Enter vehicle number from list "))

        if vinput==1:
            cartype()

            typeinput=int(input("Enter car type number from list"))
            if typeinput==1:
                print(*accar,sep='\n') #print each list as user call line by line
            if typeinput==2:
                print(*nonaccar,sep='\n')

        if vinput==2:
            vantype()

            typeinput=int(input("Enter van type number from list"))
            if typeinput==1:
                print(*acvan,sep='\n')
            if typeinput==2:
                print(*nonacvan,sep='\n')

        if vinput==3:
            print(*tw,sep='\n')

        if vinput==4:
            trucktype()

            typeinput=int(input("Enter truck type number from list"))
            if typeinput==1:
                print(*truck7,sep='\n')
            if typeinput==2:
                print(*truck12,sep='\n')

        if vinput==5:
            lorrytype()

            typeinput=int(input("Enter lorry type number from list"))
            if typeinput==1:
                print(*lorry25,sep='\n')
            if typeinput==2:
                print(*lorry35,sep='\n')
#display vehicles end here
    elif choice==4:#hire vehicles condition
        vehiclelist()
        vinput=int(input("Enter vehicle number from list "))
        if vinput==1:
            cartype()
            typeinput=int(input("Enter car type number from list"))
            if typeinput==1:
                a=hireacc.append(accar.pop(0))#in here vehicle need to hire will add to each vehicle hiring list
                print("Hired")
            if typeinput==2:
                a=hirenacc.append(nonaccar.pop(0))
                print("Hired")

        if vinput==2:
            vantype()

            typeinput=int(input("Enter van type number from list"))
            if typeinput==1:
                a=hirenacv.append(acvan.pop(0))
                print("Hired")
            if typeinput==2:
                a=hirenacv.append(nonacvan.pop(0))
                print("Hired")

        if vinput==3:
            a=hiretw.append(tw.pop(0))
            print("Hired")

        if vinput==4:
            trucktype()

            typeinput=int(input("Enter truck type number from list"))
            if typeinput==1:
                a=hiret7.append(truck7.pop(0))
                print("Hired")
            if typeinput==2:
                a=hiret12.append(truck12.pop(0))
                print("Hired")

        if vinput==5:
            lorrytype()

            typeinput=int(input("Enter lorry type number from list"))
            if typeinput==1:
                a=hirel25.append(lorry25.pop(0))
                print("Hired")
            if typeinput==2:
                a=hirel35.append(lorry35.pop(0))
                print("Hired")
#hiring vehicles end here
    elif choice==5:#re-list condition
        vehiclelist()
        vinput=int(input("Enter vehicle number from list "))

        if vinput==1:
            cartype()

            typeinput=int(input("Enter car type number from list"))
            if typeinput==1:
                a=accar.append(hireacc.pop(0))#vehicle user need to add back to vehicle list
                print("Re-listed")
            if typeinput==2:
                a=nonaccar.append(hirenacc.pop(0))#take from hired list add to each vehicles list
                print("Re-listed")

        if vinput==2:
            vantype()

            typeinput=int(input("Enter van type number from list"))
            if typeinput==1:
                a=acvan.append(hirenacv.pop(0))
                print("Re-listed")
            if typeinput==2:
                a=nonacvan.append(hirenacv.pop(0))
                print("Re-listed")

        if vinput==3:
            a=tw.append(hiretw.pop(0))
            print("Re-listed")

        if vinput==4:
            trucktype()

            typeinput=int(input("Enter truck type number from list"))
            if typeinput==1:
                a=truck7.append(hiret7.pop(0))
                print("Re-listed")
            if typeinput==2:
                a=truck12.append(hiret12.pop(0))
                print("Re-listed")

        if vinput==5:
            lorrytype()

            typeinput=int(input("Enter lorry type number from list"))
            if typeinput==1:
                a=lorry25.append(hirel25.pop(0))
                print("Re-listed")
            if typeinput==2:
                a=lorry35.append(hirel35.pop(0))
                print("Re-listed")
#re-list end
    elif choice==6: #print hired vehicles
        vehiclelist()
        vinput=int(input("Enter vehicle number from list "))

        if vinput==1:
            cartype()

            typeinput=int(input("Enter car type number from list"))
            if typeinput==1:
                print(*hireacc,sep='\n')#print represented list
            if typeinput==2:
                print(*hirenacc,sep='\n')

        if vinput==2:
            vantype()

            typeinput=int(input("Enter van type number from list"))
            if typeinput==1:
                print(*hireacv,sep='\n')
            if typeinput==2:
                print(*hirenacv,sep='\n')

        if vinput==3:
            print(*hiretw,sep='\n')

        if vinput==4:
            trucktype()

            typeinput=int(input("Enter truck type number from list"))
            if typeinput==1:
                print(*hiret7,sep='\n')
            if typeinput==2:
                print(*hiret12,sep='\n')

        if vinput==5:
            lorrytype()

            typeinput=int(input("Enter lorry type number from list"))
            if typeinput==1:
                print(*hirel25,sep='\n')
            if typeinput==2:
                print(*hirel35,sep='\n')
#end of show hired vehicles
    elif choice==7: #when want to exit this will execute
        print("Good Bye")
        break#program will stop from here
    else:
        print("Try again with valid number")#if number is not in vehicle list this will comeup
#end of the program
