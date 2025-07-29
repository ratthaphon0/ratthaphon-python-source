"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        pass
        num = int(input(f"Enter number [{i+1}]: "))
        numbers.append(num)
        
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = []
    odd_numbers = []
    
    # Calculate average
    average = sum(numbers) / len(numbers)
    
    # Numbers greater than average
    above_average = []
    
    for i in range(10):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else :
            odd_numbers.append(numbers[i])
        if numbers[i] > average :
            above_average.append(numbers[i])

    #Display result
    print("Even Numbers : ",even_numbers)
    print("Odd Numbers : ",odd_numbers)
    print("Above average : ",above_average)
    print("Sum : ",sum(numbers))
    print("Average : ",average)
    print("Min : ",min(numbers))
    print("Max : ",max(numbers))
    
    
if __name__ == "__main__":
    number_operations()