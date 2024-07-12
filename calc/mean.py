from typing import List

def calc_mean(x: List | float):
    try: 
        if x == None:
            return ""
        if isinstance(x, float):
            return x
        if isinstance(x, list):
            return sum(x) / len(x)
    except ValueError:
        raise ValueError(f"x = `{x}` list of numbers or float")