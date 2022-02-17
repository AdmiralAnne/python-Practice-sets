# conditional statements 

age = input("Enter your age: ")
if int(age)==12:
    print("you are 12 years old")
else:
    print("not what i was looking for")

#for loops and while loops

for i in range(1,10,2): # start, stop, step
    print(i)

while int(age)==12:
    name=input("whts your name ?: ")
    if name==("stop"):
        age=1
        # break
        
# above loops stops only when name== stop ie age != 12

# working with lists~ 

fruits=['apple','banana','strawberry']
print(fruits)

fruits.append('Pineapple')
print(fruits)

fruits.append('pear')
print(fruits)

fruits[1]="blueberry"
print(fruits)