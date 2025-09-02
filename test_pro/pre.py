'''
No.1

age = int(input("How old are you?: "))
if age >= 18 :
    print("You are Adult")
else :
    print("You still children")
'''

'''
No.2

number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
print(f"{number1} * {number2} = {number1 * number2}")
print(f"{number1} / {number2} = {number1 / number2}")
'''
'''
No.3

for i in range(1,21):
    if i % 2 == 0 :
        print(f"{i} is even number")
    else :
        continue
'''
name = ['ashif','ben','ming','baimon']
'''
No.4

while True :  
    user_name = input("Enter a name : ")
    if user_name in name:
        print(f"{user_name} is in a list")
        break
    else :
        print("None")
        
'''
'''
fruit = ('apple','banana','orange')
country = {"Thailand":"Chonburi","Japan":"Tokyo"}
countrys = dict(Thailand="Chonburi",Japan="Tokyo")
number = {1,2,3,4,5}
lissst = [2,3,4,"apple"]

print(fruit)
print(country)
print(countrys)
print(number)
print(lissst)
'''
'''
sum = 0
number = int(input("Enter a number: "))
for i in range(1,number):
    if i % 2 == 1 :
        sum += i
        print(i,end=" + ")
    else :
        continue
print(sum)

'''
'''

score  = []
sum = 0
for i in range (0,5):
    user = int(input(f"Enter a score {i+1}: "))
    score.append(user)
print(score)
for i in range(0,5):
    sum += score[i]
average = sum / len(score)    
print(f"{sum} / {len(score)} = {average}")
print("Max score is : ",max(score))
print("Min score is : ",min(score))
'''

'''
months = ("January","Febuary","March","April","May")
pick = int(input("Enter month in number : "))
answer = input("Enter month in that number : ")
if answer == months[pick-1]:
    print("Correct")
else :
    print("None")
'''
student = {6730202734:"Ashif", 6730202733:"Ben", 6730202732:"Ming"}
choose = int(input("Enter student number "))
print(f"Student {choose} is {student.get(choose,'Not found')}")