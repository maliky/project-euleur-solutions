# -*- coding: utf-8 -*-
from pb3_prime_decomposition import get_primes_factor_decomposition


def compte_x_in_list(x, list_):
    """renvois le nombre d'occurence de x dans list_"""
    return len([True for e in list_ if x == e])


def compte_x_in_decompo(x, seq):
    return compte_x_in_list(x, seq)


def compte_max_prime_factor(primes_decompositions_):
    """Renvois un dictionnaire de primes avec leur effectif maximun dans la primes_decomposition: sequence"""
    _primes_factors = {p for _primes in primes_decompositions_ for p in _primes}

    def _compte_max_x_in_decompo(x, seq=primes_decompositions_):
        max_x = 0
        for s in seq:
            compte = compte_x_in_list(x, s)
            if max_x < compte:
                max_x = compte
        return max_x

    cp = zip(_primes_factors, map(_compte_max_x_in_decompo, _primes_factors))
    return dict(cp)


def primes_decompo_up_to(to_):
    """Return all prime decomposition  to_ elt, excluded"""
    sol = dict()
    for elt in range(2, to_ + 1):
        sol[elt] = get_primes_factor_decomposition(elt)
    return sol


def main():
    """"""
    prod = 1
    pd = primes_decompo_up_to(20)
    for f, p in compte_max_prime_factor(pd.values()).items():
        prod *= f ** p

    return prod


if __name__ == "__main__":
    print(main())
