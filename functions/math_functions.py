import math


# Euclidean Algorithm to find GCD
def gcd(a, b):
    """
    Euclidean Algorithm
    gcd(a, b)
    print("gcd =", GCD(a, b))
    """
    while b:
        a, b = b, a % b
    return abs(a)


# Extended Euclidean Algorithm (Bezout Identity)
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("---------------------------------------------------------")
a = 113
b = 143
gcd, alpha, beta = gcdExtended(a, b)
print("Extended Euclidean Algorithm (Bezout Identity)")
print("a =", a)
print("b =", b)
print("gcd =", gcd)
print()
print("alpha =", alpha)
print("beta =", beta)
print("---------------------------------------------------------")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Set of all Units Modulo n (U_n)
def Find_Units_n(n):
    print("---------------------------------------------------------")
    print("Units N")
    print("n =", n)
    Units_n = []
    for i in range(n):
        if gcd(i, n) == 1:
            Units_n.append(i)
    print(Units_n)
    print("---------------------------------------------------------")
    return Units_n


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = 24
Find_Units_n(n)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Find the Multiplicative Inverse of a modulo n
def modInverse(a, n):
    print("---------------------------------------------------------")
    print("Multiplicative Inverse")
    print(str(a) + " modulo " + str(n))
    for x in range(1, n):
        if ((a % n) * (x % n)) % n == 1:
            print()
            print(x)
            print("---------------------------------------------------------")
            return x
    print("Not Found")
    print("---------------------------------------------------------")
    return -1


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
a = 5
n = 72
modInverse(a, n)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Find the Prime Power Factorization
def Prime_Power_Factorization(n):
    print("---------------------------------------------------------")
    print("Prime Power Factorization")
    print("n =", n)
    PPF = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        PPF.append(2)
        n = n / 2
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i and divide n
        while n % i == 0:
            PPF.append(i)
            n = n / i
    # Condition if n is a prime number greater than 2
    if n > 2:
        PPF.append(n)
    exponents = []
    i = 0
    while 1:
        if i not in range(len(exponents)):
            exponents.append(1)
        if i + 1 == len(PPF):
            break
        if PPF[i] == PPF[i + 1]:
            PPF.pop(i + 1)
            exponents[i] += 1
        if i + 1 == len(PPF):
            break
        if PPF[i] != PPF[i + 1]:
            i += 1
    i = 0
    while i < len(PPF):
        print(str(int(PPF[i])) + "^" + str(exponents[i]), end="")
        if i != len(PPF) - 1:
            print(end=" * ")
        i += 1
    print("\n---------------------------------------------------------")
    return PPF, exponents


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = 341
Prime_Power_Factorization(n)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Euler's Function
def Eulers_Totient(n):
    print("---------------------------------------------------------")
    print("Euler's Totient")
    print("n =", n)
    PPF, exponents = Prime_Power_Factorization(n)
    i = 0
    phi = 1
    while i < len(PPF):
        phi *= pow(PPF[i], exponents[i]) - pow(PPF[i], exponents[i] - 1)
        i += 1
    print("phi(" + str(n) + ") =", phi)
    print("---------------------------------------------------------")
    return phi


n = 360
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
Eulers_Totient(n)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

"""
# k is size of num[] and rem[]. 
# Returns the smallest number x 
# such that:
# x % num[0] = rem[0], 
# x % num[1] = rem[1], 
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[] 
# are pairwise coprime (gcd for
# every pair is 1)
"""


# Find's Min X using Chinese Remainder Theorem
def Chinese_Remainder_Theorem(num, rem, k):
    print("---------------------------------------------------------")
    print("Chinese Remainder Theorem")
    print("Modulos N =", num)
    print("Remainders R =", rem)
    print("k =", k)

    x = 1
    # Initialize result
    # As per the Chinese remainder
    # theorem, this loop will
    # always break.
    while True:
        # Check if remainder of
        # x % num[j] is rem[j]
        # or not (for all j from
        # 0 to k-1)
        j = 0
        while j < k:
            if x % num[j] != rem[j]:
                break
            j += 1
        # If all remainders
        # matched, we found x
        if j == k:
            i, product = 0, 1
            while i < k:
                product *= num[i]
                i += 1
            print()
            print(str(x) + " mod " + str(product))
            print("---------------------------------------------------------")
            return x
        # Else try next number
        x += 1


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
modulus = [6, 7, 11]
remainder = [2, 2, 9]
k = 3
Chinese_Remainder_Theorem(modulus, remainder, k)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# RSA Encryption given n, e, m
def RSA_Encryption(n, e, m):
    print("---------------------------------------------------------")
    print(
        "RSA Encryption of n = " + str(n) + "; e = " + str(e) + "; m = " + str(m) + " :"
    )
    c = pow(m, e, n)  # m^e % n
    print("c =", c)
    print("---------------------------------------------------------")
    return c  # encrypted message


def RSA_Decryption(n, e, c):
    print("---------------------------------------------------------")
    print(
        "RSA Decryption of n = " + str(n) + "; e = " + str(e) + "; c = " + str(c) + " :"
    )
    phi_n = int(Eulers_Totient(n))
    d = modInverse(e, phi_n)
    m = pow(c, d, n)  # c^d % n
    print("m =", m)
    print("---------------------------------------------------------")
    return m  # decrypted message


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = 91
e = 5
m = 9
RSA_Encryption(n, e, m)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = 77
e = 7
c = 3
RSA_Decryption(n, e, c)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# utility function to find pow(x, y) under
# given modulo mod
# same as pow(x, y, mod)
def power(x, y, mod):
    if y == 0:
        return 1
    temp = power(x, y // 2, mod) % mod
    temp = (temp * temp) % mod
    if y % 2 == 1:
        temp = (temp * x) % mod
    return temp


# This function receives an integer n and
# finds if it's a Carmichael number
def isCarmichaelNumber(n):
    print("---------------------------------------------------------")
    print("Is " + str(n) + " a Carmichael Number?")
    a = 2
    while a < n:
        # If "b" is relatively prime to n
        if gcd(a, n) == 1:
            # And pow(b, n-1)% n is not 1,
            # return false.
            if power(a, n - 1, n) != 1:
                print("No")
                print("---------------------------------------------------------")
                return False  # 0
        a += 1
    print("Yes")
    print("---------------------------------------------------------")
    return True  # 1


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = 1729
isCarmichaelNumber(n)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


def MillerRabinTest(n, a):
    print("---------------------------------------------------------")
    print("Miller Rabin Test")
    print("n =", n)
    print("a =", a)
    # n - 1 = (2^k)(q)
    q = 1
    k = 2  # start at 2 because 2^1 will always give result cuz even
    # Find q
    while True:
        q = (n - 1) / pow(2, k)
        if q.is_integer():
            q = int(q)
            break
        k += 1
    # Miller Rabin Test
    list = []
    for i in range(10):
        list.append(pow(a, pow(2, i) * q, n))
    print()
    print(list)
    print("---------------------------------------------------------")
    return list


# If -1 is NOT an element, a witnesses compositeness of n
# If -1 is an element, a fails to recognize the compositeness of n
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = 341
a = 2
MillerRabinTest(n, a)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Pollard's P - 1 Algorithm
# Non-Trivial Factor is any number other than 1
def Pollards_P_1_Algorithm(n, a):
    print("---------------------------------------------------------")
    print("Pollard's P - 1 Algorithm")
    print("n =", n)
    print("a =", a)
    L = a
    """ Visualization lists
    #lst_L = []
    #factors = []
    #lst_k = []
    """
    # Just a long range, could still be possible after 50 but ehhh
    for k in range(1, 50):
        # a^k! = (a^(k-1))^k
        # L = (a^(k!)) mod n
        L = pow(L, k, n)
        factor = gcd(L - 1, n)
        """ Visualization
        #lst_L.append(L)
        #factors.append(factor)
        #lst_k.append(k)
        """
        if factor != 1:
            """Visualization
            #print(lst_L)
            #print(factors)
            #print(lst_k)
            """
            print()
            print("Non-Trivial Factor = " + str(factor))
            print("Found with k! = " + str(k) + "!")
            print("---------------------------------------------------------")
            return factor, k
    print("Non-Trivial Factor Not Found")
    print("---------------------------------------------------------")
    return -1, -1


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
n = 7373
a = 2
Pollards_P_1_Algorithm(n, a)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# LeftHandSide = [x1, x2, ..., xn] without squaring
# Only works if RHS can be sqrt evenly
def Quadratic_Sieve_Algorithm(LeftHandSide, N):
    print("---------------------------------------------------------")
    print("Quadratic Sieve Algorithm (Factor via Difference of Squares)")
    print("a^2 ≡ b^2 mod N")
    a, b = 1, 1
    for x in LeftHandSide:
        a *= x
        RHS_Ints, RHS_Exponents = Prime_Power_Factorization(pow(x, 2, N))
        i = 0
        while i < len(RHS_Ints):
            b *= pow(RHS_Ints[i], RHS_Exponents[i])
            i += 1
    a = a % N
    b = int(math.sqrt(b) % N)
    print("a =", a)
    print("b =", b)
    print("N =", N)
    Factor_One = gcd(a - b, N)
    Factor_Two = gcd(a + b, N)
    print()
    print("gcd(a-b, N) =", Factor_One)
    print("gcd(a+b, N) =", Factor_Two)
    print("---------------------------------------------------------")
    return Factor_One, Factor_Two


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
LHS = [620, 621, 645, 655]
N = 377753
Quadratic_Sieve_Algorithm(LHS, N)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Define function inside
def Pollards_Rho_Algorithm(x1, N):
    print("---------------------------------------------------------")
    print("Pollard's Rho Algorithm")
    print("x1 =", x1)
    print("N =", N)

    def f(x):
        return (pow(x, 2) + 1) % N

    x2 = f(x1)
    gcd = gcd(x2 - x1, N)
    x_lst = [x1, x2]
    i = 1
    # print("GCD(" + str(x_lst[i]) + "-" + str(x_lst[i//2]) + ", " + str(N) + ") = " + str(gcd))
    while gcd == 1:
        x_lst.append(f(x_lst[i]))
        i += 1
        x_lst.append(f(x_lst[i]))
        i += 1
        gcd = gcd(x_lst[i] - x_lst[i // 2], N)
        # print("GCD(" + str(x_lst[i]) + "-" + str(x_lst[i//2]) + ", " + str(N) + ") = " + str(gcd))
    """ Visualization
    print("X List = " + str(x_lst))
    print("x" + str(i+1) + " = " + str(x_lst[i]))
    print("x" + str((i+1)//2) + " = " + str(x_lst[i//2]))
    print()
    print("GCD(" + str(x_lst[i]) + "-" + str(x_lst[i//2]) + ", " + str(N) + ") = " + str(gcd))
    """
    print()
    print("Non-Trivial Factor =", gcd)
    print("---------------------------------------------------------")
    return gcd


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
x1 = 3
N = 4891
Pollards_Rho_Algorithm(x1, N)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Finding the Possible Order Elements
n = 71
# Order of a
a = 2
# Check for distinct a^m % n for everything up to n-1
lst = [0] * (n)
for i in range(1, n):
    lst[pow(a, i, n)] = lst[pow(a, i, n)] + 1
    if lst[pow(a, i, n)] > 1:
        print(str(i) + ": " + str(pow(a, i, n)))
        break
print(lst)
print()

# Discrete Log list
g = 2
x = 0
n = 29
while x < n:
    h = pow(g, x, n)
    print(str(g) + "^" + str(x) + " = " + str(h) + " mod " + str(n))
    x += 1
print()

# Computational Diffie-Hellman Problem (CDH)
A = 18
B = 14
a = 11
b = 13
print("A^b % n:", pow(A, b, n))
print("B^n % n:", pow(B, a, n))
print("g^(ab) % n:", pow(g, a * b, n))
print()

# El Gamal
c1 = 6
c2 = 10
a = 21
n = 29
x = pow(c1, n - 1 - a, n)
print(x)
m = (c2 * x) % n
print(m)
x = pow(c1, a, n)
m = (c2 * pow(x, n - 2)) % n
print(m)
print()

# Baby Step Giant Step
g = 2
n = 53
h = 31
I = 1 + math.floor(math.sqrt((Eulers_Totient(n))))
bs = []
for i in range(I + 1):
    bs.append(pow(g, i, n))

g_inverse = modInverse(pow(g, I), n)
gs = []
for i in range(I + 1):
    gs.append((h * pow(g_inverse, i, n)) % n)
print(bs)
print(gs)
print()
print(pow(2, 33, 53))
print()

# Pohlig-Hellman
g = 2
n = 53
h = 21

p1 = pow(2, 2)
n1 = int((n - 1) / p1)
g1 = pow(g, n1, n)
h1 = pow(h, n1, n)
print("p1 = " + str(p1))
print("n1 = " + str(n1))
print("g1 = " + str(g1))
print("h1 = " + str(h1))
p2 = 13
n2 = int((n - 1) / p2)
g2 = pow(g, n2, n)
h2 = pow(h, n2, n)
print("p2 = " + str(p2))
print("n2 = " + str(n2))
print("g2 = " + str(g2))
print("h2 = " + str(h2))
print()
x1, x2 = 0, 0
i = 0
while x1 != h1:
    i += 1
    x1 = pow(g1, i, n)
print(str(g1) + "^" + str(i) + " = " + str(h1) + " mod " + str(n))
x1 = i
i = 0
while x2 != h2:
    i += 1
    x2 = pow(g2, i, n)
print(str(g2) + "^" + str(i) + " = " + str(h2) + " mod " + str(n))
x2 = i
modulos = [int(n / n1), int(n / n2)]
remainders = [x1, x2]
print()
x = Chinese_Remainder_Theorem(modulos, remainders, 2)
print("x:", pow(g, x, n))  # Should be equal to h
print("Should be equal to h:", h)
print()

# Discrete Log!
# log_g(h) = x
# g^x = h mod n
print(pow(5, 37, 43))

Eulers_Totient(35)


Chinese_Remainder_Theorem([47, 79], [18, 44], 2)
x = 0
d = 79
n = 47
i = 0
while x != 1:
    i += 1
    x = (d * i) % n
print(x)
print(i)
print(pow(123, 2))

modInverse(7, 11)
