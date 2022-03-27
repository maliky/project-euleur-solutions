# -*- coding: utf-8 -*-
from pathlib import Path
import pickle
import logging

logger = logging.getLogger(__name__)

FNAME = Path("Primes/2_to_1000003.prime")
FSOLNAME = Path("Primes/pb50_sol_dict.csv")


def load_pickle(data, fromf):
    """write a pickled version of data to file byte stream"""
    with open(fromf, "rb") as f:
        model = pickle.load(f)
    return model
    print(f"fromf={fromf} n'existe pas, donc pas chargé!")


def save_pickle(data, tof=""):
    """write a pickled version data to file byte stream"""
    if tof:
        logger.info(f"Saving a data en écrasant to {tof}")
        with open(tof, "wb") as f:
            pickle.dump(data, f)


def save_primes(data: list, fOut: Path = FNAME):
    """
    Save a list of elements to a file
    """
    with open(fOut, "w") as f:
        for datum in data:
            f.write(f"{datum}\n")


def load_primes(fIn: Path = FNAME) -> list:
    """
    Load in a List a file where each line
    becomes an int element of the list
    """
    primes = []
    with open(fIn, "r") as f:
        p = f.readline()
        while p:
            primes.append(int(p))
            p = f.readline()
    return primes
