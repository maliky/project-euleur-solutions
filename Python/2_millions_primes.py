# -*- coding: utf-8 -*-
"""
Génère des nombre premiers
"""
from pb3_prime_decomposition import get_primes_up_to


def main():
    """"""
    args = parse_args()
    fout=Path(args.folder),
    n_primes=args.action,
    
    primes = get_primes_up_to(max_=n_primes, log=True)

    with open(fout, "w") as f:
        f.write(primes)
    print('Done')


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--fout",
        "-f",
        type=str,
        default="Primes/new.primes",
    )

    parser.add_argument("n_primes", "n", type=int, default=100)

    return parser.parse_args()


if __name__ == "__main__":
    main()
