# input: rhdt:246 , ghftd:1246
# explanation: here every string is associated with the number separated by:
# -->if sum of squares of digits is even then rotate the string by 1
# -->if sum of squarea of digits is odd then rotate the string left by 2 position
# 2*2=4*4+6*6=56 whcih is even so rotate rhdt=trhd
#--------------------------------------------------
# given a number n, write a program to find the sum of the largest prime factors of each of nine consecutive
# starting from n.
# g(n)= f(n)+f(n+1)+f(n+2)+
def largest_prime_factor(n: int) -> int:
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

n = 10 
count = 9 

sum_of_largest_prime_factors = 0
for i in range(n, n+count):
    lpf = largest_prime_factor(i)
    sum_of_largest_prime_factors += lpf

print(sum_of_largest_prime_factors)