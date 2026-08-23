# ==========================================
# WEEK 1: CAPM CALCULATION PRACTICE
# ==========================================

# 1. Define your inputs
ticker = 'BHP.AX'                     # String (text)
beta = 1.25                           # Float (decimal representation of volatility)
risk_free_rate = 0.041                 # Float (representing a 4.1% Australian Government Bond yield)
market_return = 0.085                  # Float (representing an 8.5% expected ASX index return)

# 2. Calculate the Expected Return using the CAPM formula
# Expected Return = Rf + Beta * (Rm - Rf)
expected_return = risk_free_rate + beta * (market_return - risk_free_rate)

# 3. Print the raw output
print("--- Raw Calculation Output ---")
print(expected_return)

# 4. BONUS: Format the output to a beautiful percentage
# We multiply by 100 and round to 2 decimal places, adding a '%' sign
formatted_return = f"{round(expected_return * 100, 2)}%"
print("\n--- Professional Output ---")
print(f"The Expected Return for {ticker} under CAPM is: {formatted_return}")