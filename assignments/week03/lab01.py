# Complete this program to classify people by age

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter age: "))
if age > 0 and age <=12 :
    print(f"{age} years old is Child")
elif age > 12 and age <= 19 :
    print(f"{age} years old is Teenager")
elif age > 19 and age <= 59 :
    print(f"{age} years old is Adult") 
elif age > 59 and age < 200 :
    print(f"{age} years old is Senior")
else :
    print("Input Invalid")