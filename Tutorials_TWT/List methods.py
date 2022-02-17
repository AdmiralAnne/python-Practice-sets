color=(255,255,255)
print(type(color)) #prints class

# lets make a list

fruits=['apples','banana','pears','strawberry']

for fruit in fruits: #for every fruit in Fruits list, one by one.. print them~
    print(fruit)

for x in range(0,len(fruits)):
    print(fruits[x])

#  some methods
text = input("enter anything: ")
print(text.strip()) #removes all the whitespaces 

print(len(text)) #number of characters and spaces

print(text.lower())

#split mehtod~ 
#creates a list out of the list you've Given~

text=input('enter some words: ')
print(text.split('.')) #anything separated by period goes into new list as new element
#It prints it in the form of a  list ~ which is kinda cool and useful
print(text.split()) # run this and see the ,magic