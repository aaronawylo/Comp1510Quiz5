def calculate_pay(hours, wage):
    """
    Return the pay given the hours worked, factoring in overtime rates.

    :param hours: any number
    :param wage: any number
    :precondition hours: any valid number
    :precondtion wage: any valid number
    :postcondition: gives back properly calculated total wages
    :return: total wage amount for hours worked
    >>> calculate_pay(10, 10)
    100
    >>> calculate_pay(50, 10)
    600
    """

    if hours <= 0 or wage <= 0:
        return 0
    if hours > 40:
        base_wages = 40 * wage
        overtime = (hours - 40) * (2 * wage)
        total_wages = base_wages + overtime
    else:
        total_wages = hours * wage
    return total_wages


def main():

    if __name__ == "__main__":
        main()
