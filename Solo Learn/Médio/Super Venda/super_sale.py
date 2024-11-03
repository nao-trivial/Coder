def calculate_savings(prices_str):
    # Parse the input string into a list of floats
    prices = list(map(float, prices_str.split(',')))
    
    # Indentifique os itens mais caros
    max_price = max(prices)
    
    # Calculate the total savings for the discounted items
    savings = sum(price * 0.30 for price in prices if price != max_price)
    
    # Apply sales tax to the savings
    savings_with_tax = savings * 1.07
    
    # Convert the savings to an integer
    savings_int = int(savings_with_tax)
    
    # Calculate the tip (the fractional part of the savings_with_tax)
    tip = savings_with_tax - savings_int
    
    # Leave anything below a dollar as a tip
    if 0 < tip < 1:
        return savings_int
    else:
        return savings_int

# Example usage
prices_str = input()
print(calculate_savings(prices_str))  # Output: 38
