# list data structure
# a list enables you to chande data
myclassmates = ['Maggie', 'Eric', 'Joan', 'Daniel', 'Susan']
mynos = [4, 9, 20, 3, 1, 50, -9]
myclassmates[4] = 'Purity'
mynos.sort()
myclassmates.append('Christine')
myclassmates.insert(2, 'Michael')
myclassmates.pop(3)
print(myclassmates)
print(mynos)

for classmembers in myclassmates:
    print(classmembers)
# this is a tuple
countries = ('Kenya', 'Uganda', 'Tanzania', 'Burundi')
print(countries)
for x in countries:
    print(x)

# sets datastructures
cars = {'Toyota', 'Nissan', 'Mercedes', 'Subaru', 'Rangerover'}
print(cars)
for y in cars:
    print(y)

#dictionaries data structures

matunda={
    'price':50,
    'color':'Yellow',
    'Name':'Banana'
}
matunda.update({'shape':'curved'})
matunda.pop('color')
print(matunda)
bei=matunda['price']
print(bei)







