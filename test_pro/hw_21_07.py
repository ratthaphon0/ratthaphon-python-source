def even_odd(number):
    if number%2 == 0:
        output = "Even number"
    else : 
        output = "Odd number"
    return output


if __name__ == "__main__":
    print("Program to check even or odd number")
    number = int(input("Enter a number :")) 

    output = even_odd(number)
    print(number,"is",output)                      