# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1833667/20200803         
  
# Date:  12.07.2021

Pass = -1
Defer = -1
Fail = -1
progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
i = 0
data_list = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

def read(b):                    # Read data from the data_list.
        """Read data from the list""" 
        return data_list[i][b]
def result(a,b):
        a+=1
        print(b)
        return a
def horizontal_histogram_line(a,b):                     # Making the horizontal histogram.
        """Prints one line in the horizontal histogram"""
        print(f"{b} {a} : {'*' * a}")
def horizontal_histogram():
        horizontal_histogram_line(progress,"\nProgress ")
        horizontal_histogram_line(module_trailer,"Trailer  ")
        horizontal_histogram_line(module_retriever,"Retriever")
        horizontal_histogram_line(exclude,"Excluded ")

#checking pass , defer and fail Credits then show the progression out come.

        
while i <= len(data_list)-1:
        Pass = read(0)
        Defer = read(1)
        Fail = read(2)
        i+=1
        if Pass == 120: 
                progress=result(progress,"Progress")
        elif Pass == 100:
                module_trailer=result(module_trailer,"Progress (module trailer)")
        elif Pass == 80:
                module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif Pass == 60:
                module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif Pass == 40:
                if Fail == 80:
                        exclude=result(exclude,"Exclude")
                else:
                        module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif Pass == 20:
                if Fail == 80 or Fail == 100:
                        exclude=result(exclude,"Exclude")
                else:
                        module_retriever=result(module_retriever,"Do not Progress - module retriever")
        elif Fail == 80 or Fail == 100 or Fail == 120:
                        exclude=result(exclude,"Exclude")
        
total = progress + module_trailer + module_retriever + exclude
horizontal_histogram()

print(f'\n{total} outcomes in total.')
