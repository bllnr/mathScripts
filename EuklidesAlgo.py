#Euklides Algorithm
#Find the greatest common divisor of two numbers

input_a = input("Input first number:\n")
input_b = input("Input second number:\n")

#input_a=876
#input_b=204

try:
    a = int(input_a)
    b = int(input_b)
except ValueError:
    print("Input must be number!")
    exit()

if input_a == 0 or input_b == 0:
    print("Number can't be zero. Exiting.")
    exit()

a, b = max(a,b), min(a,b)

def find_q(a,b):
    q = a//b
    return q

def find_r(a,b,q):
    r = a-(b*q)
    return r

gcd = 1
r = 1
results = []
#find the greatest common divisor recursively
while r > 0:
    r = find_r(a,b,find_q(a,b))
    j = [a,b,find_q(a,b),r]
    results.append(j)
    a = b
    b = r
    if r != 0:
        gcd = r
    else:
        break

print(f"Greatest common divisor of {input_a} and {input_b} is {gcd}.")

if gcd == 1:
    print("Mutually prime!")    