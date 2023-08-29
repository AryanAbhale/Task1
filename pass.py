import random
import string
print("welcome to pass generator")
def pa():
    length=int(input("enter the length of pass "))
    low=string.ascii_lowercase
    upper=string.ascii_uppercase
    dig=string.digits
    symb=string.punctuation
    combo=low+upper+dig+symb
    #print(combo)
    x=random.sample(combo,length)
    #print(x)     #it gives values in form of lists so we use join method to join it with empty string 
    pas="".join(x)
    print(pas)
 
pa()


