# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1833667/20200803         
  
# Date:  12.07.2021

Pass = int(input("Please enter your credits at Pass: "))    # prompt Pass credit from the user.
Defer = int(input("Please enter your credits at Defer: "))  # prompt Defer credit from the user.
Fail = int(input("Please enter your credits at Fail: "))    # prompt Fail credit from the user.

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
