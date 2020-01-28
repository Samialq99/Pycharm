print("Hello Python")


def printb(a):
    print(a)


text1 = "Functional printing"

printb(text1)
print(id(text1))  # this will print the memory address of the variable using fn id()


product = {
    "productID": 0,
    "description": "",
    "categoryID": 0,
    "price": 0.00,

}

# use len to get length of array or any container

print(len(product))
print(text1[0])
print(text1[-1])  # will print very last character
print(text1[-2])
print(text1[0:5])  # range 0-5

text2 = 'Python "Programming"'
print(text2)

text3 = 'Pyt\"hon \n "Pr\\ogramming"'
print(text3)

text4 = f"{text1} {text2}"
print(text4)
# to get list of functions on a string use the variable.

print(text2.strip())
print(text2.upper())

print("programming" in text2)  # use in boolean to see if matches
print("Programming" in text2)

txt = 'one one was a race horse, two two was one too.'
x = txt.replace('one', 'three', 2)
print(x)
