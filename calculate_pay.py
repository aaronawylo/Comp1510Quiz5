def calculate_pay(hours, wage):
    if hours <= 0 or wage <= 0:
        return 0
    if hours > 40:
        base_wages = hours * wage
        overtime = (hours - 40) * (2 * wage)
        wages = base_wages + overtime
    else:
        wages = hours * wage
    return wages
