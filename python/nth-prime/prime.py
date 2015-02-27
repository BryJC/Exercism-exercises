def nth_prime(position):
    
    primes_list = [2, 3, 5, 7, 9]
    count = 10
    while len(primes_list) < position+1:
        for i in range(2,9):
            if count%i == 0:
                count += 1
                break
            else:
                primes_list.append(count)
    
