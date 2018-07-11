import string,os,sys

from random import *
os.system('clear')
def main ():

    char = string.ascii_letters + string.punctuation + string.digits + string.hexdigits

    passs = "".join(choice(char) for x in range(randint(8, 16)))
    print("\nEnter p to generate your password\n\nEnter e to exit\n")

    i = input("~> ")

    if i == "p" or i == "P":

            print("Your password is: \n")

            print(passs)

    s = input("\nPress enter")
    
    if s == "":
        
            os.system('clear')
        
    if i == "e":
        
        exit()
        
    main()
    
while True:

    main()

#t.me/KaMrAn_ZoNe

#t.me/DarkPy
