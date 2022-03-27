# -*- coding: utf-8 -*-
from sys import exit

# from primes import find_all_primes_under


def triangle_num(n, start=0):
    return int(n * (n + 1) / 2)


def main(lim_num_factors=100, T_index=1):
    # T:8756 480 comment attraper KeyboardInterrupt?+
    # PRIMES = find_all_primes_under(10000000)
    T_val = triangle_num(T_index)
    max_factors = (2,)
    while max_factors[0] < lim_num_factors:
        print(f"T_index : {T_index}.   Max_factors {max_factors}", end="\r")
        T_index += 1
        T_val += T_index
        factor_lim = T_val
        factors_cpt = 2
        f_candidate = 2
        while factor_lim >= f_candidate:
            if T_val % f_candidate == 0:
                factor_lim //= f_candidate
                factors_cpt += 2
                while factor_lim % f_candidate == 0:
                    factor_lim //= f_candidate
                    factors_cpt += 2

            f_candidate += 2

        if factors_cpt > max_factors[0]:
            max_factors = (
                factors_cpt,
                f"T_index={T_index}",
                f"T_val={T_val}",
            )
    # print(f"max_factors {max_factors}", end="\r")
    return max_factors


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
