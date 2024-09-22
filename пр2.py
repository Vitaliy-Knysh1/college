first_name = ("Віталій")
last_name = ("Книш")

age = (16)

#типи

if type(first_name) == type(last_name) and first_name != last_name:
    print ("Тип данних імені: ", type(first_name))
elif type(first_name) != type(last_name):
    print ("Типи данних не співпадають")
elif first_name == last_name:
    print (first_name, last_name)
         
if type(age) == int:
    print ("Тип данних віку - int")
elif type(age) != int:
    print ("Тип данних віку не int")
    
#list
list =[first_name, last_name]
print (list)
