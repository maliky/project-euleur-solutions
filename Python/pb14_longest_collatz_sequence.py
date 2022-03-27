import time


def main(under=10 ** 6):
    """
    find the longuest collatz sequence

    pourrait être amélioré on garde en mémoire toutes les valeurs ils se sont
    rencontrés sur le chemin du pont et pas seulement celles inférieures.
     donc lorsque j'arrive à une séquence de marie-jo toute la longueur intermédiaires.
    """

    collatz_seq = dict()
    collatz_max = (0,)
    for start_value in range(1, int(under)):
        n = start_value
        collatz_seq[start_value] = 1
        seq = []
        # print(f"start_value={start_value} ({start_value/under:.0%}", end="\r")
        while n > 1:
            if n % 2:
                n = 3 * n + 1
            else:
                n /= 2
            if collatz_seq.get(n, False):
                collatz_seq[start_value] += collatz_seq[n]
                break
            collatz_seq[start_value] += 1
            seq.append((n, collatz_seq[start_value]))

        # adding what I talke about but does not do much in time.
        for intermediary_n, val in seq:
            collatz_seq[intermediary_n] = collatz_seq[start_value] - val + 1

        # collatz_seq[start_value] += 1
        if collatz_seq[start_value] > collatz_max[0]:
            collatz_max = (collatz_seq[start_value], start_value)
            # print(f"collatz_max={collatz_max}", end="\n")

    return collatz_max


if __name__ == "__main__":
    print("")
    start = time.time()
    res = main()
    stop = time.time()
    print(res, stop - start)
