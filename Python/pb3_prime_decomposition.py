import logging

logger = logging.getLogger(__name__)


def get_primes_factor_decomposition(x):
    _primes = list()
    max_c = int(x ** (1 / 2))  # pourquoi la sqroot ?
    c = 2
    _prime = next_prime_gen([c])
    dividend = x
    while dividend > 1:
        if dividend % c == 0:
            # print(f"dividend={dividend} divisible par {c} donne {dividend/c}")
            _primes.append(c)
            dividend /= c
        else:
            c = next(_prime)
    return _primes


def fill_missing_prime(primes=[2, 7]):
    """Given a list of primes, find the missing ones"""
    small_prime = min(primes)
    max_prime = max(primes)
    assert is_prime(small_prime), f"Check that {small_prime} is a prime"
    assert is_prime(max_prime), f"Check that {max_prime} is a prime"

    primes_set = set(primes)
    prime_gen = next_prime_gen(primes=[small_prime])
    candidate = next(prime_gen)

    while candidate < max_prime:
        primes_set |= {candidate}
        candidate = next(prime_gen)

    return sorted(list(primes_set))




def is_missing_primes(primes=[2]):
    """Return True if no primes are missing in primes"""
    return len(missing_primes(primes))



def main():
    """Solve problem 3 of Euler"""
    n = 600851475143
    prime_decomposition = list(get_primes_factor_decomposition(n))
    sol = sorted(prime_decomposition)[-1]
    print("The largest prime factor of {n} is {sol}")


if __name__ == "__main__":
    main()
