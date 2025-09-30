"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        user_input= float(input("insert a number, when you finish type done")).strip().lower()  # Get input from user
        if user_input=="done": # Check if user typed 'done'
            break
        try:
            numbers=float(user-input) # Try to convert to float and add to list
            numbers.append(numbers)
        except Value error:
            print("Insert either a number or done")# Handle invalid input gracefully

        pass

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

   analysis["count"]=len(numbers) # Calculate count
   analysis["sum"]=sum(numbers) # Calculate sum
   analysis["average"]=sum(numbers)/len(numbers) # Calculate average
   analysis["minimum"]=min(numbers)# Find minimum
   analysis["maximum"]=max(numbers) # Find maximum
   even_count=len([n for n in numbers if n % 2 == 0]) # Count even numbers (hint: use modulo operator)
   odd_count=len([n for n in numbers if n % 2 =! 0])# Count odd numbers
   analysis["even_count"] = even_count
   analysis["odd_count"] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    if isinstance(value, float):
      print(f"{key} : {value:.2f}")
    else:
      print(f"{key} : {value}")


    pass


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()