from multiprocessing import Pool
from time import time

def divisors(number):

    list_divors = []
    for d in range (1, number+1):
        if not number % d:
            list_divors.append(d)
     
    return list_divors


def factorize(*number):
   
    results = []
    
    for i in number:
        results.append(divisors(i))
    #print(tuple(results))    
    return tuple(results)



if __name__ == '__main__':

    func_started = time()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)
    print(f'Func execution time: {time()-func_started}')
    
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
    with Pool(processes=4) as pool:
        pool_started = time()
        print(pool.map(factorize, (128, 255, 99999, 10651060)))
        print(f'Pools execution time: {time()-pool_started}')   
    
