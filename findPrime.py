import math

#Erasthenos sieve: calculate prime numbers up to some number n.

n = 1000
n_root = math.sqrt(n)

n_list = []
for i in range(2, n+1):
    n_list.append(i)

i = 2
while i <= n_root: #only needs to check list until square root of n
    for k in n_list:
        if k != i and k % i == 0:
            n_list.remove(k) #remove non-prime numbers
    i += 1

print(n_list)
