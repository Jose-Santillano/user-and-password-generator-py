import random
import os

#This function creates a random user.
def randomUser():
    user=''
    for i in range(10): user+=random.choice('abcdefghijklmnñopqrstuvwxyz')
    for i in range(3): user+=random.choice('1234567890')
    user+="@gmail.com"
    return user

#This function creates a random password.
def randomPassword():
    password=''
    for i in range(10): password+=random.choice('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890')
    return password

#This function manage the multiples options for the menu.
def manager(option, qty):
    print("\n")
    #Option 1, just users.
    if(int(option)==1):
        i = 0
        while (i < int(qty)):
            print(randomUser())
            i += 1
    else:
        if(int(option)==2):
            i = 0
            while (i < int(qty)):
                print(randomPassword())
                i += 1
        else:
            if (int(option) == 3):
                i = 0
                while (i < int(qty)):
                    print(randomUser() + " " + randomPassword())
                    i += 1

def menu():
    option=1
    while(int(option)!=4):
        os.system("cls")
        print(" _/[  U S E R  F A S T v.1.0  ]\\_ \n\n"
              ">> Welcome to UserFast | Created by: José Santillano << \n"
              "This program will help you for create a random users \n\n"
              "Menu \n\n"
              "( 1 ) Create user\n( 2 ) Create password\n( 3 ) Create user and password\n( 4 ) Leave \n")
        option = input("Please choose the option: ")
        if int(option) == 1:
            optionCreateUser=1
            while(int(optionCreateUser)!=0):
                os.system('cls')
                print("^ CREATE AN USER ^ \n")
                qtyUsers = input("How many users do you need?: ")
                manager(1, qtyUsers)
                optionCreateUser=input("\nChoose an option ( 1 ) Continue | ( 0 ) Back : ")
        else:
            if int(option) == 2:
                optionCreatePassword = 1
                while (int(optionCreatePassword) != 0):
                    os.system('cls')
                    print("^ CREATE A PASSWORD ^ \n")
                    qtyPassword = input("How many passwords do you need?: ")
                    manager(2, qtyPassword)
                    optionCreatePassword = input("\nChoose an option ( 1 ) Continue | ( 0 ) Back : ")
            else:
                if int(option) == 3:
                    optionCreateUserPassword = 1
                    while (int(optionCreateUserPassword) != 0):
                        os.system('cls')
                        print("^ CREATE AN USER AND PASSWORD ^ \n")
                        qtyUserPassword = input("How many passwords do you need?: ")
                        manager(3, qtyUserPassword)
                        optionCreateUserPassword = input("\nChoose an option ( 1 ) Continue | ( 0 ) Back : ")
                else:
                    if int(option) == 4:
                        print("See you later, thanks for your time little boy :)")
                        os.system("cls")
                    else:
                        print("\nPlease respect the options range >:/ \n")
                        input("Press ENTER ")
                        os.system("cls")
                        
#We call the main function to execute the program :)
menu()