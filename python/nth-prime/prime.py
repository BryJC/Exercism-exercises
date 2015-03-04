def nth_prime(position):
    
    primes_list = [2, 3, 5, 7]
    count = 10
    while len(primes_list) <= position:
        if any(x == 0 for x in [count % i for i in range(2,9)]):
            count += 1
        elif all(x != 0 for x in [count % i for i in range(2,9)]):
            primes_list.append(count)
            count += 1
    return primes_list[position-1]
    
