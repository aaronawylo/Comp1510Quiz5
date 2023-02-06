def calculate_pay(hours, wage):
    if hours <= 0 or wage <= 0:
        return 0
    if hours > 40:
        base_wages = 40 * wage
        overtime = (hours - 40) * (2 * wage)
        total_wages = base_wages + overtime
    else:
        total_wages = hours * wage
    return total_wages
