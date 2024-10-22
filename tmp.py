import gmpy2

def extended_gcd(a, b):
    """ Zwraca NWD a i b oraz współczynniki x i y takie, że ax + by = gcd(a, b) """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(b, n):
    """ Zwraca odwrotność b w grupie Φ(n) """
    gcd, x, _ = extended_gcd(b, n)
    
    if gcd != 1:
        raise ValueError(f"Odwrotność nie istnieje, ponieważ gcd({b}, {n}) = {gcd} != 1")
    
    # Upewnij się, że x jest dodatni
    return x % n

# Przykładowe użycie
n = 14  # Przykładowa wartość n
b = 5   # Przykładowa liczba b, która jest względnie pierwsza z n

try:
    inverse = modular_inverse(b, n)
    print(f"Odwrotność liczby {b} w grupie Φ({n}) to {inverse}")
except ValueError as e:
    print(e)