import time

def is_prime(num, prime_num):
    for x in prime_num:
        remainder =num%x
        if remainder == 0:
            return False
        #else:
        #    continue
    return True

def generate_primes(maxnum):
    start = time.time()
    prime_nums=[]
    #maxnum=1000
    for num in range(2,maxnum+1):
        if is_prime(num, prime_nums):
            prime_nums.append(num)
    end = time.time()
    print("Generate primes under %d, use time: %f" %(maxnum, end - start))
    return prime_nums

if __name__ == "__main__":
    prime_nums = generate_primes(10000)
    print(prime_nums)
    print(len(prime_nums))