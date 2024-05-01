import typing as typ
from fuzzywuzzy import fuzz

from .conf import settings


def distance(q1: str, q2: str, partial: bool = False) -> int:
    """
    Calculate the Levenshtein distance between two strings

    :param q1:
    :type q1: str
    :param q2:
    :type q2: str
    :param partial:
    :type partial: bool
    :return: Calculated Levenshtein distance
    :rtype: int
    """
    if partial:
        return fuzz.partial_ratio(q1.lower(), q2.lower())
    return fuzz.token_set_ratio(
        q1.lower(), q2.lower(),
        full_process=settings.TOKEN_FULL_PROCESS
    )


def match(q1: str, q2: str, th: int = settings.LEVENSHTEIN_MATCH_THRESHOLD,
          partial: bool = False) -> typ.Tuple[bool, int]:
    dist = distance(q1, q2, partial)
    return dist >= th, dist


class KMPSearch:
    """
        KMP (Knuth–Morris–Pratt) search algorithm
        Link: https://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
    """
    @classmethod
    def search(cls, text, pattern):
        """
        text - T
        pattern - P
        Return all the matching position of pattern string P in T
        """
        result = []
        partial = cls.partial_match(pattern)
        j = 0
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = partial[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                result.append(i - (j - 1))
                j = partial[j - 1]

        return result

    @staticmethod
    def partial_match(pattern):
        """
        Calculate partial match table (also known as "failure function")
        """
        result = [0]

        for i in range(1, len(pattern)):
            j = result[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = result[j - 1]
            result.append(j + 1 if pattern[j] == pattern[i] else j)
        return result

