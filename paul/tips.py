########################################
# no if else 
#########################################
condition = False
x = 1 if condition else 0
print (x)

########################################
# work with large number
#########################################
x = 10_000_000_000
y = 100_000_000_000
f = x + y
print ( f'{f:,}' )
###############################################
# use context manager with ( automatic close)
##############################################
f = open ( 'tips.py' , 'r')
content = f.read()
f.close()

with open ( 'tips.py' , 'r') as f: # context manager for resources
    content = f.read()
#############################################  
# enum
###############################################
names = [ 'Paul', 'Arno', 'Hans']
ages = [ '59' , '55' , '64' ]
eyes = [ 'brown', 'brown' , 'grey']
index = 0
for name in names:
    print ( index, name )
    index += 1

# beter practice    
for index, name in enumerate(names):
    a = ages[index]
    print ( index, name, a )

# loop over more list
for name, age , eye in zip( names, ages, eyes ):
    print ( f'naam:{name} age:{age} eye:{eye}')

################################################
# Unpacking var
################################################
a, b, *c ,d= ( 1,2,3,4,5,7,8)
print(a)
print(b)
print(c)
print(d)
# ignore c
a, b, *_ ,d= ( 1,2,3,4,5,7,8)
print(a)
print(b)
print(c)
print(d)

#####################################################
# variable attr on a class
####################################################

class person():
    pass

age = 'leeftijd'
value = '40'

setattr(person, age, value)

v = getattr( person, age )

print ( v )

######################################################
# set dict to class
######################################################
person = person()

personInfo = { 'name': 'paul', 'age': '59'} # dict key/value
for key, value in personInfo.items():
    setattr(person, key , value)

for key in personInfo.keys():
    print (getattr(person, key))
