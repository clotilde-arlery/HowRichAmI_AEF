def get_deductible_amount(donation, income):
    """Return the tax-deductible amount from a donation"""
    income_tax = get_income_tax(income)
    deductibility_cap = 0.20 * income
    deductibility_rate = 0.66
    
    if donation <= deductibility_cap and donation <= income_tax:
        eligible_amount = donation
    elif donation > deductibility_cap and donation <= income_tax:
        eligible_amount = deductibility_cap
    elif donation <= deductibility_cap and donation > income_tax:
        eligible_amount = income_tax
    elif donation > deductibility_cap and donation > income_tax:
        eligible_amount = min(income_tax, deductibility_cap)
    else:
        raise ValueError("Deductible amount could not be computed.")
        
    deductible_amount = eligible_amount * deductibility_rate
    return deductible_amount


# Test 
def get_income_tax(income):
    return 0.1 * income

get_deductible_amount(0, 100)
get_deductible_amount(5, 100)
get_deductible_amount(10, 100)
get_deductible_amount(11, 100)
get_deductible_amount(20, 100)
get_deductible_amount(21, 100)

def get_income_tax(income):
    return 0.3 * income

get_deductible_amount(0, 100)
get_deductible_amount(5, 100)
get_deductible_amount(10, 100)
get_deductible_amount(20, 100)
get_deductible_amount(21, 100)