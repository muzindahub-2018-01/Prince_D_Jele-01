"""
Author          : P D Jele  (@Umlamulankunzi)

Project title   : Math Challenge

Project Summary : -The program asks user to choose type of challenge i.e from
                  subtraction, multiplication, addition or division
                  -Program then asks the user 5 questions from the selected
                  challenge, awarding a point for each correct answer,
                  -Program returns total number of points earned by user after
                  challenge is over

Targeted Audience: The program targets grade 2s, and 3s, a fun way to master the
                   basics of math
"""

import random
import os
from time import sleep

def user_info():
    name = input("""
###############################################
#                                             #
#    WELCOME TO THE MATH CHALLENGE APP        #
#                                             #
#                "MCA"                        #
#                                             #
###############################################

Enter your name to continue\n:""").capitalize()
    return name

def clear_screen():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')
                  
def add():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    func_result = num1 + num2
    return num1, num2, func_result

def subtract():
    while True:
        try:
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
            if num1 - num2 < 0:
                raise ZeroDivisionError
            break
        except ZeroDivisionError:
            pass

    func_result = num1 - num2
    return num1, num2, func_result

def multiply():
    num1 = random.randint(2, 10)
    num2 = random.randint(2, 5)
    func_result = num1 * num2
    return num1, num2, func_result

def divide():
    while True:
        try:
            num1 = random.randint(2, 20)
            num2 = random.randint(2, 20)

            if num1 % num2 != 0:
                raise ValueError
            elif num1 == num2:
                raise ValueError
            break

        except ValueError:
            pass

    func_result = num1 / num2
    return num1, num2, int(func_result)

def choice():
    while True:
        try:
            choice_of_operation = input("""Choose your MATHS Challenge from below:

enter   "A"   - For addition
enter   "S"   - For subtraction
enter   "M"   - For Multiplication
enter   "D"   - For Division

Enter your selection here
: """).lower()
            
            if choice_of_operation not in ['a', 's', 'm', 'd']:
                raise NameError
            break
        
        except NameError:
            clear_screen()
            print ('Please enter correct option')
    return choice_of_operation

def main():
    mark = 0
    counter = 0
    name = user_info()
    user_choice = choice()
    results_list =[] #list of tuples containing results for each question
    clear_screen()

    print("""
+++++++++++++++++++++++++++++++++++
+                                 
+       WELCOME {}                
+                                 
+   Let The Challenge Begin       
+                                 
+++++++++++++++++++++++++++++++++++
""".format(name))
    print('\n' +('=' * 35))

    while counter < 5:
        if user_choice == 'a':
            num1, num2, result = add()
            sign = '+'
        elif user_choice == 's':
            num1, num2, result = subtract()
            sign ='-'
        elif user_choice == 'm':
            num1, num2, result = multiply()
            sign = 'x'
        else:
            num1, num2, result =divide()
            sign = '/'

        while True:
            try:
                user = int(input("{0} {1} {2} = ".format(num1, sign, num2)))
                break
            except ValueError:
                print("Enter a number please")

        counter += 1

        if user == result:
            print ('Well done Thats correct')
            mark = mark + 1
        else:
            print("Wrong! \n{0} {1} {2} = {3}".format(num1, sign, num2, result))
            
        results_list.append((num1, num2, result, user))

        if counter != 5:
            print('\nNext Question\n')

        if counter == 5:

            def show_results():
                clear_screen()
                index = 1
                print('==='*15)

                for item in results_list:
                    num_1, num_2, result_1, user_1 = item

                    if result_1 == user_1:
                        print('No.{0}: {1} {2} {3} = {4}'.format(index, num_1, sign, num_2, result_1),
                              '\tCorrect Answer ******\n')
                    else:
                        print('No.{0}: {1} {2} {3} = {4}'.format(index, num_1, sign, num_2, user_1),
                              '\tcorrection ----> {} {} {} = {}\n'.format(num_1, sign, num_2, result_1))
                    index += 1
                print('==='*15)
                
            if mark > 3:
                show_results()
                print("\n*** Very Good {}***".format(name))
                sleep(1)
            elif mark == 3:
                show_results()
                print('\n** Good {}**'.format(name))
                sleep(1)
            else:
                show_results()
                print('\n* Better Luck Next time {} *'.format(name))
                sleep(1)
                
            print('\nYou scored {} out of 5 marks. \nThe Math challenge is over.'.format(mark))
            input('\n\nPRESS ENTER TO CONTINUE')

            while True:
                try:
                    prompt = input("\n\nDo you want to try the"
                                   " \nMath Challenge again?"
                                   " \ny - To Play Again \nn - To quit\n").lower()
                    if prompt not in ['y','n']:
                        raise ValueError
                    break
                except ValueError:
                    print('Try again\n')

            if prompt == 'y':
                clear_screen()
                main()

            else:
                pass

if __name__=='__main__':
    main()
