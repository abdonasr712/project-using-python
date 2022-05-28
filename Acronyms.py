user_input = str(input("Enter a Phrase: "))
text = user_input.split()
x = " "
for i in text:
    x = x + str(i[0]).upper()
print("Acronym is : "+x)