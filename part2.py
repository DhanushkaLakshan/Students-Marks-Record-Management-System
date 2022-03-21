# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1833667/20200803         
  
# Date:  12.07.2021

total = 0
Pass = -1
Defer = -1
Fail = -1
def within_range(x,y):
    """"Getting user input and validating range"""
    while x  not in range(0,121,20):
            x = int(input(f"Please enter your credits at {y}:"))  # prompt input credits from the user. #checking the input is integer.
            if x not in range(0,121,20):
                print("Out of range")   #if the input data is not in range then print "Out of range" while the input data is in range.
    return x
while total != 120:
    try:
        Pass = within_range(Pass,"Pass")
        Defer = within_range(Defer,"Defer")
        Fail = within_range(Fail,"Fail")
        total = Pass +  Defer + Fail
        if total != 120:
            print("Total incorrect")
            Pass = -1
            Defer = -1
            Fail = -1
    except ValueError:                  #handling the ValueError untill the input dta is valid integer.
        print("Integer required")

#checking the input data is in Credit Ranges.

if Pass == 120: 
        print("Progress")
elif Pass == 100:
        print("Progress (module trailer)")
elif Pass == 80:
        print("Do not Progress - module retriever")
elif Pass == 60:
        print("Do not Progress - module retriever")
elif Pass == 40:
        if Fail == 80:
                print("Exclude")
        else:
                print("Do not Progress - module retriever")
elif Pass == 20:
        if Fail == 80 or Fail == 100:
                print("Exclude")
        else:
                print("Do not Progress - module retriever")
elif Fail == 80 or Fail == 100 or Fail == 120:
                print("Exclude")
       
