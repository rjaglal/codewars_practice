def calculate_years(principal, interest, tax, desired, count=0):

    if principal >= desired:
        return count

    interest_earned = principal * interest

    print(interest_earned)

    tax_to_pay = interest_earned * tax

    print(tax_to_pay)

    principal_new = principal + (interest_earned - tax_to_pay)

    print(principal_new)

    if principal_new >= desired:
        return count + 1
    else:
        return calculate_years(principal_new, interest, tax, desired, count + 1)


if __name__ == '__main__':
    principal_in = 1000
    interest_in = 0.01625
    tax_in = 0.18
    desired_in = 1000
    print(calculate_years(principal_in, interest_in, tax_in, desired_in))
