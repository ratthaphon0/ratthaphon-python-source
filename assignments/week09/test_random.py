import random

def test_random():
    # สร้างตัวแปร random_number ตัวแปรนี้คือการสุ่มเลขระหว่าง 1 - 10 
    random_number = random.randint(1, 10)
    guess_number = int(input("Guess the number between (1-10) : "))
    if guess_number == random_number :
        print("Congratulation")
    elif guess_number > random_number:
        print("Too high")
    else guess_number < random_number:
        print("Too low")


    
test_random()