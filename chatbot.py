a="That is really good!" 
b="I hope you get better"
c="oh, ok"
#these are variables that are hard coded and very depending on the input of the user 
name=input(("Hello there, what is your name?"))
feeling=input(("How are you?"))
website=input("Do you like my website?")
invest=input("Would you like to invest in it")
money=input("how much would you like to invest?")

print("Hello there, what is your name?")
print(name)

print("Hello there "+name+", how are you?")

print(feeling)

if(feeling=="happy" or feeling=="good"):
    print(a)
elif(feeling=="sad" or feeling=="bad"):
    print(b)
else:
    print(c)

print("Do you like my Website?")
#this print is the same as the variable, but it prints the question 
print(website)
if(website=="yes"):
    print("Thank you")
    
print("Would you like to invest in it?")  
if(invest=="yes"):
    print("yes, $"+str(money))
    print("thank you very much!")
elif(invest=="no"):
    print("No thank you")
    print("That is okay, have a nice day")
else:
    print("It is ok "+name+", email me when you have an answer")
