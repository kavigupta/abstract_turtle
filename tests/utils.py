
import unittest
import json

def json_proc(value):
    return json.loads(json.dumps(value))

class FuzzyFloat(float):
    def __new__(self, value, places=7):
        del places
        return float.__new__(self, value)

    def __init__(self, value, places=7):
        float.__init__(value)
        self.__places = places
    def __eq__(self, other):
        if isinstance(other, float):
            return 2 * abs(self - other) <= 10 ** (-self.__places)
        else:
            return super().__eq__(self, other)
    def __repr__(self):
        return repr(round(self, self.__places + 2))

def fuzzify(obj, places):
    if isinstance(obj, str):
        return obj
    if isinstance(obj, list):
        return [fuzzify(x, places) for x in obj]
    if isinstance(obj, dict):
        return {a : fuzzify(b, places) for a, b in obj.items()}
    if isinstance(obj, (float, int)):
        return FuzzyFloat(obj)
    raise RuntimeError("Invalid object type for fuzzification: {}".format(type(obj)))

class TestCase2(unittest.TestCase):
    def assertContainersAlmostEqual(self, first, second, places=7, canonicalizer=json_proc, **kwargs):
        """
        Checks if two container items are almost equal. Numbers are compared via `self.assertAlmostEqual`.

        Arguments:
            first, second: things to check
            canonicalizer: thing that converts the containers to only json-compatible types
        """
        first = fuzzify(canonicalizer(first), places)
        second = fuzzify(canonicalizer(second), places)
        self.assertEqual(first, second, **kwargs)
