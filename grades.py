
name= input("name:")
block = input("class:")
stream=input("stream:")
kisw=int(input("kisw:"))
Geo=int(input("Geo:"))
math=int(input("Math:"))
Eng=int(input("Eng:"))
Bio=int(input("Bio:"))
Chem=int(input("Chem:"))
Phy=int(input("Phy:"))
Agri=int(input("Agri:"))
#grade the marks
def get_grade(input):
    if input>=85:
     print("A")
    elif input>=80:
        print("A-")
    elif input>=75:
     print("B+")
    elif input>=70:
        print("B")
    else: 
       print("C")
get_grade(kisw)
get_grade(Geo)
get_grade(math)
get_grade(Eng)
get_grade(Bio)
get_grade(Chem)
get_grade(Phy)
get_grade(Agri)
#sum the total subjects 

marks=(int(kisw)+int(Geo)+int(math)+int(Eng)+int(Bio)+int(Chem)+int(Phy)+int(Agri))
#display the total marks
print(f"marks:{marks}")
subjects=input("subjects:")
mean=int(marks) // int(subjects)
print(f"mean:{mean}")
print("your mean grade is " ,mean,)
breakpoint
grade=mean
#award the  grade according to the mean gotten
if grade>=75:
    print("Excellent!!!!you have a potential to do better")
    print("teacher's comment:keep it up")
elif grade>=70:
    print("Good work!!!but work harder")
    print("teacher's comment:you did well but you have a better potential")
elif grade>=65:
    print("Good.aim higher")
    print("teacher's comment:good work but work better")
else:
    print("you tried but work better.The world is not for the lazy boy")
    print("teacher's comment:work hard")

#print a receipt of the marks
print("\n====END OF OF YEAR EXAMINATION====" "2025 OCTOBER 23rd")
print("\n=====Result slip====")
print(f"name:{name}")
print(f"block:{block}")
print(f"stream:{stream}")
print("-------------------")

print("\n====marks per subject===")
print(f"kisw:{kisw}")
print(f"Geo:{Geo}")
print(f"math:{math}")
print(f"Eng:{Eng}")
print(f"Bio:{Bio}")
print(f"Chem:{Chem}")
print(f"Phy:{Phy}")
print(f"Agri:{Agri}")

print("---------------------")

print("\n===Total marks===")
print(f"marks:{marks}")

print("\n===Mean grade====")
print(f"mean:{mean}")

   




    
    

          


    
