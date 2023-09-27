def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = 0.25 * earnings
    else:
        tax_owed = 0.30 * earnings
    return tax_owed

def net_income(earnings):
    if earnings < 12000:
        take_home = earnings - (0.25 * earnings)
    else:
        take_home = earnings - (0.30 * earnings)
    return take_home


ana_take_home = net_income(9000)
bob_take_home = net_income(15000)

print(ana_take_home)
print(bob_take_home)

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)