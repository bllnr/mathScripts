#Euklides Algorithm
#Find the greatest common divisor of two numbers

input_a = input("input first number:\n")
input_b = input("input second number:\n")

#input_a=3042
#input_b=4485

a = int(input_a)
b = int(input_b)
a, b = max(a,b), min(a,b)

def find_q(a,b):
    q = a//b
    return q

def find_r(a,b,q):
    r = a-(b*q)
    return r

gcd = 1
r = 1
#find the greatest common divisor recursively
while r > 0:
    r = find_r(a,b,find_q(a,b))
    a = b
    b = r
    if r != 0:
        gcd = r
    else:
        break

print(f"Greatest common divisor of {input_a} and {input_b} is {gcd}.")

if gcd == 1:
    print("Mutually prime!")


