You can use the following python script to calculate the number of cases of hull cleaner sold:

```Python
import math

def calculate_cases_sold(bottles_sold: int) -> int:
    """
    Calculate the number of cases of hull cleaner sold.

    Args:
        bottles_sold (int): The number of bottles of hull cleaner sold.

    Returns:
        int: The number of cases sold.
    """
    bottles_per_case = 12
    cases_sold = math.ceil(bottles_sold / bottles_per_case)
    return cases_sold

def main():
    hull_cleaner_sold = int(input("Please enter the number of bottles of hull cleaner sold: "))
    cases = calculate_cases_sold(hull_cleaner_sold)
    print(f"The number of cases sold is: {cases}")

    # Calculate invoice amount for 10% rebate on each case sold
    price_per_case = 100  # You can update this with the actual price per case
    rebate_percentage = 0.1
    invoice_amount = cases * price_per_case * rebate_percentage
    print(f"Invoice amount to send to the manufacturer is: ${invoice_amount}")

if __name__ == "__main__":
    main()
```

This script contains a function `calculate_cases_sold()` that calculates the number of cases of hull cleaner sold, as specified in the User Story. The function takes an integer, `bottles_sold`, and divides it by 12. The result is then rounded up to the nearest whole case using `math.ceil()`.

The script also contains a `main()` function that prompts the user for the number of bottles of hull cleaner sold, calls the `calculate_cases_sold()` function with that input, and then calculates the invoice amount for the 10% rebate on each case sold. The invoice amount is then printed to the console.

To run the script, save it to a file (e.g. `hull_cleaner.py`) and run it using the python interpreter:

```
python hull_cleaner.py
```