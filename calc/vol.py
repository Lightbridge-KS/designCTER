# Ellipsoid Volume
from typing import List

def prostate_vol(x: List[float]):
    """Calculate prostate volume (ml) and diagnosis"""
    v = ellipsoid_list(x)
    if v < 25:
        dx = "Normal"
    elif v == 25:
        dx = "Normal or Prominent"
    elif v < 40:
        dx = "Prominent"
    elif v == 40:
        dx = "Prominent or Enlarged"
    else:
        dx = "Enlarged"
        
    return f"Prostate vol: {round(v, 2)} ml ({dx})"



def ellipsoid(d1, d2, d3):
    """Calculate ellipsoid volume from 3 perpendicular **diameters**"""
    import math
    volume = (4/3) * math.pi * d1/2 * d2/2 * d3/2
    return volume

def ellipsoid_list(x: List[float]):
    """Calculate ellipsoid volume from 3 perpendicular **diameters** (List input)"""
    try: 
        return ellipsoid(*x)
    except TypeError:
        raise TypeError(f"{x} must be a list of three floats")