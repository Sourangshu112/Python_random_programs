name=str(input("Enter your name"))
#roll=int(input("Enter your roll no."))
#sec=str(input("Enter your section"))
marks1=float(input("Enter marks of first subject"))
marks2=float(input("Enter marks of second subject"))
marks3=float(input("Enter marks of third subject"))
marks4=float(input("Enter marks of fourth subject"))
marks5=float(input("Enter marks of fifth subject"))
total = marks1+marks2+marks3+marks4+marks5
avg=total/5
print("name - ",name)
#print("roll no - ",roll , "section - ",sec)
print("subject 1 marks = ",marks1 ,"subject 2 marks = ",marks2 ,"subject 3 marks = ",marks3 ,"subject 4 marks = ",marks4 ,"subject 5 marks = ",marks5)
print("Total marks = ",total)
print("average marks = ",avg)
percent = (total/500) * 100
if percent >= 70:
   print(percent ," Grade A")
elif percent >= 50 and percent <70:
   print(percent ," Grade B")
else:
    print(percent ," Fail")
