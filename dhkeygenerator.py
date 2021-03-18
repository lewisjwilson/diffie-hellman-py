"""
Diffie Hellman Algorithm

Step1:  Assume prime q, select alpha where alpha is a primitive root of q (alpha<q)
        *alpha is a primitive root of q if the following series is followed:
        alpha mod(q), alpha^2 mod(q), ... , alpha^(q-1) mod(q)
        = 1, 2, 3, ..., q-1

Step2:  Assume x_a (private key of user a) where x_a<q.
        Calculate public key y_a = alpha^(x_a) mod(q)

        Assume x_b (private key of user b) where x_b<q.
        Calculate public key y_b = alpha^(x_b) mod(q)

Step3:  Generate secret keys.
        User a has {x_a, y_b, q}
        User b has {x_b, y_a, q}

        User a: key k = (y_b)^(x_a) mod(q)
        User b: key k = (y_a)^(x_b) mod(q)

"""
import random
from Crypto.Util import number

def choose_alpha():
    chosen_alpha = random.randint(2, q - 1)
    # print("Choose alpha = " + str(chosen_alpha))
    # array of values to hold (alpha ** i) % q
    array = []
    for i in range(1, q):
        roottest = (chosen_alpha ** i) % q
        if roottest in array:
            # print(str(chosen_alpha) + " is not a primitive root of " + str(q))
            return -1
        array.append(roottest)

    # if loop is not broken, choose alpha
    return chosen_alpha


q = number.getPrime(13)
print("Prime q = " + str(q))

# finding alpha with alpha^(i) mod(11).
# all alpha^(i) mod(11) in the set from i=1...q-1 must be less than 11
# e.g. 2 satisfies the condition because:
# if alpha = 2; alpha^(i) mod(11) for 0 < i < 11 =
# 2, 4, 8, 5, 10, 9, 7, 3, 6, 1 (all values from 1...q-1 appear)

# primitive root (currently works in reasonable time for q of 4 digits or less
alpha = choose_alpha()
while alpha == -1:
    alpha = choose_alpha()
print("Primitive root alpha = " + str(alpha))

# assume secret key of user a
x_a = random.randint(1, q - 1)
print("Secret key of User a, x_a = " + str(x_a))

# then public key of user a :
y_a = (alpha ** x_a) % q
print("Public key of User a, y_a = " + str(y_a))

# assume secret key of user b
x_b = random.randint(1, q - 1)
print("Secret key of User b, x_b = " + str(x_b))

# then public key of user a :
y_b = (alpha ** x_b) % q
print("Public key of User b, y_b = " + str(y_b))

# User a key:
k_a = (y_b ** x_a) % q
print("User a generated key, k_a = " + str(k_a))

# User b key:
k_b = (y_a ** x_b) % q
print("User b generated key, k_b = " + str(k_b))

if (k_a == k_b):
    print("Matching keys, Success!")
else:
    print("Error: Keys do not match!")
