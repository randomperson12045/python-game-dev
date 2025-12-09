countryDb={}
while True:
    print("1.Insert")
    print("2.Display all countries")
    print("3.Display all capitals")
    print("4.Get capital")
    print("5.Delete")
    
    choice=int(input("Enter your choice.(1-5)"))
    if choice==1:
        country=input("Enter country: ").upper()
        capital=input("Enter capital: ").upper()
        countryDb[country]=capital
    elif choice==2:
        print(list(countryDb.keys()))
    elif choice==3:
        print(list(countryDb.values()))
    elif choice==4:
        country=input("enter country: ").upper()
        print(countryDb[country])
    elif choice==5:
        country=input("Which country would you like to delete?").upper()
        del countryDb[country]
    else:
        break
    