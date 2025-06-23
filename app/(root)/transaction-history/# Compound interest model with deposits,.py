# Initial values
initial_monthly_expense_per_6_phones = 34
cost_per_phone = 32
monthly_income_increase_per_phone = 5.67
additional_income_after_3_months = 162
initial_phones_owned = 6
total_phones = initial_phones_owned
months = 0
savings = 0
capital_added = 0
monthly_income = 0

# Calculate initial monthly expenses based on the initial number of phones
monthly_expenses = (initial_phones_owned / 6) * initial_monthly_expense_per_6_phones
capital_added += monthly_expenses  # Initial capital to cover the first month's expense

# Track values to calculate phones owned and savings after 9 months
phones_after_9_months = total_phones
savings_after_9_months = 0
profitability_reached = False

# Simulation loop until monthly income >= monthly expenses
while True:
    months += 1

    # Add extra monthly income after the 3rd month
    if months > 3:
        monthly_income += additional_income_after_3_months

    # Calculate monthly savings and adjust savings balance
    monthly_savings = monthly_income - monthly_expenses
    savings += monthly_savings

    # Check if enough savings to buy a new phone
    while savings >= cost_per_phone:
        savings -= cost_per_phone
        total_phones += 1
        monthly_income += monthly_income_increase_per_phone

        # Increase expenses for every 6 additional phones bought
        if total_phones % 6 == 0:
            monthly_expenses += initial_monthly_expense_per_6_phones

    # Track savings and phones owned after 9 months
    if months == 9:
        phones_after_9_months = total_phones
        savings_after_9_months = savings

    # Add capital if monthly income still doesn't cover expenses
    if monthly_income < monthly_expenses:
        capital_added += (monthly_expenses - monthly_income)

    # Check if profitability has been reached
    if monthly_income >= monthly_expenses and not profitability_reached:
        profitability_reached = True
        break_even_month = months

    # Exit loop if 9 months have passed to analyze profit after 9 months
    if months == 9:
        break

# Calculate monthly phone growth after profitability
months_since_profitability = max(0, months - break_even_month)
average_phone_increase_per_month = (
    (phones_after_9_months - initial_phones_owned) / months_since_profitability
    if months_since_profitability > 0
    else 0
)

# Final results
print("Months until profitability:", break_even_month)
print("Total phones owned at the end:", total_phones)
print("Total capital added:", capital_added)
print("Breakeven after 3 months:", break_even_month <= 3)
print("Profit after 9 months:", savings_after_9_months)
print("Estimated phones after 9 months:", phones_after_9_months)
print("Average increase in phones per month:", average_phone_increase_per_month)
