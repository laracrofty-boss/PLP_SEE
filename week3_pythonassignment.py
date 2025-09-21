# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
    This function takes in the original price and the discount percentage.
    If the discount is 20% or higher, it applies the discount.
    Otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(original_price, discount)

# Print the result
if discount >= 20:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")
