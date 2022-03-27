"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""
from re import sub

def decompose_num(x):
    """Ecris le num comme une somme de puissance de 10"""
    u = x % 10
    d = (x // 10) % 10
    h = x // 100
    return h, d, u


def d_to_letters(d, u):
    if d >= 2:
        unit = N2L[(0, 0, u)] if u else ""
        return f"{N2L[(0,d,0)]} {unit}"
    if d or u:
        return N2L[(0, d, u)]
    return ""


def h_to_letters(h, d, u):
    suffix = " and" if d or u else ""
    if h == 10:
        return "one thousand"
    if h:
        return f"{N2L[(0,0,h)]} hundred{suffix}"
    else:
        return ""


def num_to_letter(h, d, u):
    """Transforme un triplet h, d, u  en lettres"""
    return f"{h_to_letters(h,d,u)} {d_to_letters(d,u)}"


def main(N=1001):
    """get the numbers in letter and sum the lenght of each"""
    num_in_letters = [
        sub(" ", "", num_to_letter(*decompose_num(n))) for n in range(1, N)
    ]
    return sum(map(len, num_in_letters))


def create_translation_dictionary():
    lnum = "one tow three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand".split(
        " "
    )
    num = list(range(1, 20)) + list(range(20, 100, 10)) + [100, 1000]
    return {decompose_num(k): v for (k, v) in zip(num, lnum)}


if __name__ == "__main__":
    global N2L
    N2L = create_translation_dictionary()
    print(main(1001))
