def calculate_discount(price, discount_percent):
    """
    Calculates the final price after discount.
    Applies discount only if 20% or higher.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input
try:
    original_price = float(input("Enter the original price: $"))
    discount_pct = float(input("Enter discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_pct)
    
    # Display result
    if discount_pct >= 20:
        print(f"Discounted price: ${final_price:.2f} (You saved ${original_price - final_price:.2f})")
    else:
        print(f"No discount applied. Price remains: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers!")