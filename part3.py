# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1833667/20200803         
  
# Date:  12.07.2021

print("Staff Version with Histogram")       #Print "Staff Version with Histogram".
print('')                                   #Print a Blank Line.
total = 0
PASS = -1
DEFER = -1
FAIL = -1
choice = True
progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
def within_range(x,y):
    """"Getting user input and validating range""" 
    while x  not in range(0,121,20):
            x = int(input(f"Enter your total {y} credits:")) # prompt input credits from the user. #checking the input is integer.
            if x not in range(0,121,20):
                print("Out of range")                       #if the input data is not in range then print "Out of range" while the input data is in range.
    return x
def result(a,y):
        a+=1
        print(y)
        return a
def horizontal_histogram_line(a,y):                             #Making horizontal histogram.
        """Prints one line in the horizontal histogram"""
        print(f"{y} {a} : {'*' * a}")
def horizontal_histogram():
        horizontal_histogram_line(progress,"\nProgress ")
        horizontal_histogram_line(module_trailer,"Trailer  ")
        horizontal_histogram_line(module_retriever,"Retriever")
        horizontal_histogram_line(exclude,"Excluded ")

#checking the input data is in range.

while choice == True:
        while total != 120:
            try:
                PASS = within_range(PASS,"PASS")
                DEFER = within_range(DEFER,"DEFER")
                FAIL = within_range(FAIL,"FAIL")
                total = PASS +  DEFER + FAIL
                if total != 120:
                    print("Total incorrect")
                    PASS = -1
                    DEFER = -1
                    FAIL = -1
            except ValueError:
                print("Integer required")               #handling the ValueError untill the input dta is valid integer.



#checking the input data is in Credit Ranges


        if PASS == 120: 
                progress=result(progress,"Progress")
        elif PASS == 100:
                module_trailer=result(module_trailer,"Progress (module trailer)")
        elif PASS == 80:
                module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif PASS == 60:
                module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif PASS == 40:
                if FAIL == 80:
                        exclude=result(exclude,"Exclude")
                else:
                        module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif PASS == 20:
                if FAIL == 80 or FAIL == 100:
                        exclude=result(exclude,"Exclude")
                else:
                        module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif FAIL == 80 or FAIL == 100 or FAIL == 120:
                        exclude=result(exclude,"Exclude")
                        
        choice = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        choice = choice.lower()
        
        if choice == "y" or choice == "yes":
            choice = True
            PASS = -1
            DEFER = -1
            FAIL = -1
            total = 0
        elif choice == "q" or choice == "quit":
            choice == False
        else:
            i= True
            while i == True:
                    print("Entered value is not recognized! Please try agian!")
                    choice = str(input("Enter 'y' for yes or 'q' to quit and view results: ")) # asking for continue or quit from the user ,if user enters "y" then go to starting point and again asking inputs.  
                    choice = choice.lower()                                                    # if user enters "q" then printing the horizontal histogram,printing total outputs and end the program.
                    if choice == 'y' or choice == 'yes':
                            i = False
                            choice = True
                            PASS = -1
                            DEFER = -1
                            FAIL = -1
                            total = 0
                    elif choice == 'q' or choice == 'quit':
                            i = False
                            choice == False
                            
total = progress + module_trailer + module_retriever + exclude
horizontal_histogram()

print(f'\n{total} outcomes in total.')










