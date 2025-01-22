g=int(input('enter the principal amount '))
t=int(input('enter the time in years '))
r=int(input('enter the rate '))
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

print(f"Compound Interest (P={g}, R={r}%, T={t} years):", compound_interest(g,r,t))