stuDetails=("Tyler",12)
print(stuDetails)

#packing
Address="26","Princess Of Wales Rd","Singapore","Singapore","266978"
for i in Address:
    print(i,end=' ')

#unpacking
HouseNumber,AreaName,City,State,pin=Address
print()
print('Hnumber',HouseNumber)
print('Area',AreaName)

#Nested tuple
Elliot=("There are two people with this name in my class",[0,10,100,1000],[0,20,200,2000])
print(Elliot[1][3])