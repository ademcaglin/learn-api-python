def reverse_words(str):
    return ".".join(str.split(".")[::-1])

def pow_mod(a, n, m):
    return pow(a, n) % m 

def is_prime(n):
    return 2 in [n, 2**n % n]