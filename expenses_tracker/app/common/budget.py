def calculate_budget_left(expenses, profile):
    expenses_cost = sum(expense.price for expense in expenses)
    return profile.budget - expenses_cost
