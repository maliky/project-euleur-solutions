# -*- coding: utf-8 -*-
from sys import exit
from primes import find_all_primes_under

# PRIMES = find_all_primes_under(int(2 ** 16))


def triangle_num(n, start=0):
    return int(n * (n + 1) / 2)


def main(lim_num_factors=500, T_index=1):
    # T:8756 480 comment attraper KeyboardInterrupt?+
    # PRIMES = find_all_primes_under(10000000)

    T_val = triangle_num(T_index)
    max_factors = (2,)
    primes_factors = dict()
    while max_factors[0] < lim_num_factors:
        print(f"T_index : {T_index}.   Max_factors {max_factors}", end="\r")
        T_index += 1
        T_val += T_index
        factor_lim = T_val
        primes_factors = dict()

        if T_val % 2 == 0:
            primes_factors[2] = 1
            factor_lim //= 2
            while factor_lim % 2 == 0:
                factor_lim //= 2
                primes_factors[2] += 1

        f_candidate = 3

        while factor_lim >= f_candidate:
            if factor_lim % f_candidate == 0:
                factor_lim //= f_candidate
                primes_factors[f_candidate] = 1
                while factor_lim % f_candidate == 0:
                    factor_lim //= f_candidate
                    primes_factors[f_candidate] += 1

            f_candidate += 2

        nb_factors = get_nb_factors_from_prime_decomposition(primes_factors)
        if nb_factors > max_factors[0]:
            max_factors = (
                nb_factors,
                f"T_index={T_index}",
                f"T_val={T_val}",
            )
    # print(f"max_factors {max_factors}", end="\r")
    return max_factors


def get_nb_factors_from_prime_decomposition(prime_decomposition: dict):
    """Return the number of factors for prime decomposition"""
    n = 1
    for exponent in prime_decomposition.values():
        n *= exponent + 1
    return n


if __name__ == "__main__":
    try:
        print(main())
    except KeyboardInterrupt as ke:
        print(ke)
        print("I should do something on keyboard interrupt ?")
    except Exception as e:
        print("stop")
        raise (e)

    exit()
