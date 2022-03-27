# -*- coding: utf-8 -*-
import argparse
import logging
from pathlib import Path

"""
Génère des nombre premiers
"""
from pb3_prime_decomposition import get_primes_up_to

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    """"""
    args = parse_arguments()
    # primes = get_primes_up_to(max_=args.n_primes, log=True)
    print("Computing {args.n_primes} primes.")
    primes = compute_primes(n=args.n_primes)

    logger.info(f"Computing {len(primes)} primes.")

    fout = Path(args.fout)
    with open(fout, "w") as f:
        for p in primes:
            f.write(f"{p}\n")

    logger.info("Saved in {fout}")


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

    parser.add_argument("--n_primes", "-n", type=int, default=100)

    return parser.parse_args()


if __name__ == "__main__":
    main()
    
