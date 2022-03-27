from pb3_prime_decomposition import get_primes_up_to

import pandas as pd





def sum_seq(start, raison, taille):
    _sum = taille * (start + (taille - 1) / 2 * raison)
    return int(_sum)


def search_prime_sum(primes: list):
    sol = dict()
    N = len(primes)
    max_p = max(primes)
    min_known_len = 20
    taille_max = N - min_known_len

    for taille in range(min_known_len, taille_max):
        min_sum_seq = sum_seq(2, 2, taille)

        if min_sum_seq > max_p:
            break

        print(
            f"Taille : {taille} -- min_sum_seq {min_sum_seq} ({min_sum_seq/max_p:.0%}) "
        )

        i = 0
        _break_while = False

        while i < (N - taille - 1) and not _break_while:

            seq_primes = primes[i : i + taille]
            _sum_seq = sum(seq_primes)
            print(
                f"sum_search={_sum_seq/max_p:.0%}",
                end="\r",
            )

            if _sum_seq > max_p:
                _break_while = True
            elif _sum_seq in primes[i + taille :]:
                _break_while = True
                print(f">> Sol : len(seq)={taille}, sum_seq={_sum_seq} <<")
                sol[_sum_seq] = seq_primes
            else:
                i += 1

    return sol


def main(load_sol=True):
    """
    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?
    """
    if not load_sol:
        primes = load_primes()
        sol = search_prime_sum(primes)
        pd.Series(sol).to_csv(FSOLNAME)

    return load_solution()


def load_solution(fname=FSOLNAME):

    load = pd.read_csv(fname)
    load.columns = ["sum_p", "seq_p"]
    load = load.set_index("sum_p")

    def _str_list_to_list(str_list):
        return [int(x) for x in str_list.lstrip("[").rstrip("]").split(", ")]

    sol = pd.DataFrame(load.seq_p.apply(_str_list_to_list))

    sol.loc[:, "len_p"] = sol.seq_p.apply(len)
    return sol.iloc[-1]


if __name__ == "__main__":
    main()
