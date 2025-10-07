"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    """
    temp_list = []
    for i in range(7):
        temp = float(input(f"Enter temperature for day {i+1}: "))
        temp_list.append(temp)
    """
    temp_list = [20, 21, 22, 23.5, 24.5, 26, 27]
    return temp_list


def analyze_temps(temp_list):
    average_temp = sum(temp_list) / len(temp_list)
    highest_temp = max(temp_list)
    lowest_temp = min(temp_list)
    return average_temp, highest_temp, lowest_temp


def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print(f"Average: {avg:.1f} C")
    print(f"Highest: {high} C")
    print(f"Lowest: {low} C")


def main():
    temps = get_temperatures()
    avg, high, low = analyze_temps(temps)
    display_analysis(avg, high, low)


main()
