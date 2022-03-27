# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def primes_factor_decomposition(dividende):
    """
    Efficient prime decomposition
    """
    max_factor = int(dividende ** (1 / 2))
    PRIMES = find_all_primes_under(max_factor)
    _primes = []
    i = 0
    factor = 2
    while dividende > 1 and factor <= max_factor:
        factor = PRIMES[i]  # 2 at first run
        if dividende % factor == 0:  
            _primes.append(factor)
            dividende /= factor
            while dividende % factor == 0:
                _primes.append(factor)
                dividende /= factor
        i += 1
        max_factor = int(dividende ** (1 / 2))
    return _primes


def is_prime(x: int) -> bool:
    """Return True if x is prime"""
    if x == 1:
        return True

    primes = find_all_primes_under(int(x / 2))
    return not is_multiple_of(primes, x)


def is_multiple_of(primes, x) -> bool:
    """Return True if x is a multiple of one of the primes"""
    for p in primes:
        if divise(x, p):
            return True
    return False


def divise(dividende: int, diviseur) -> bool:
    """Return True if diviseur divise dividende"""
    return (dividende % diviseur) == 0


def find_all_primes_under(num, log=False):
    """
    Find all primes under num (from euler).  Super fast
    """
    all_nums = {key: True for key in range(2, num + 1)}
    for i in range(2, num + 1):
        # if all_nums[i] == False:
        if not all_nums[i]:
            continue
        if log:
            print(f"{i/(num + 1):.0%}", end="\r")
        base = i

        while base + i <= num:
            base += i
            all_nums[base] = False
    return [number for number, is_prime in all_nums.items() if is_prime]


def prime_generator():
    """renvois the next_prime"""
    _primes = [2]
    candidate = 3
    while True:
        while is_multiple_of(_primes, candidate):
            candidate += 2
        _primes.append(candidate)
        yield candidate
