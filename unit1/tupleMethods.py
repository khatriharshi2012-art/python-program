#Create a tuple

languages = ("C++" , "Java" , "PHP")

#Add item in tuple

languages = ("React",) + languages + ("Java",)
print("After adding elements to tuple :",languages)

#Check the item is available in tuple
if "python" in languages:
    print("React is in the tuple")
else:
    print("React is not in the language tuple")

#Check the length of the tuple

print("length of the tuple:",len(languages))

#Access the element of the tuple
print("First item of the tuple:",languages[0])
print("First item of the tuple:",languages[1])
print("Last item of the tuple:",languages[-1])