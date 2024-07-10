import statistics
from typing import List, Union
    
def spine_ht_loss(normal_cm: float | List[Union[float, int]], bad_cm: float | List[Union[float, int]]) -> str:
    
    # Show Input
    normal_disp = show_nums_and_mean(normal_cm)
    bad_disp = show_nums_and_mean(bad_cm)
    # Calculate mean if input as list
    if isinstance(normal_cm, List):
        normal_cm = statistics.mean(normal_cm)
    if isinstance(bad_cm, List):
        bad_cm = statistics.mean(bad_cm)

    loss_pc = ( (normal_cm - bad_cm) / normal_cm) * 100
    dx = _spine_ht_loss_dx(loss_pc)

    out = f"""Height loss: {round(loss_pc, 1)} % ({dx})"""
    return out
        
    
        
def _spine_ht_loss_dx(loss_pc: float | int):
    # Negative case
    if loss_pc < 0:
        raise ValueError("`bad_cm` must less than `normal_cm`")
    
    if loss_pc < 20:
        dx = "less than mild"
    elif loss_pc < 25:
        dx = "mild"
    elif loss_pc == 25:
        dx = "mild to moderate"
    elif loss_pc < 40:
        dx = "moderate"
    elif loss_pc == 40:
        dx = "moderate to severe"
    elif loss_pc > 40:
        dx = "severe"

    return dx


def show_nums_and_mean(x: float | List[Union[float, int]]):
    
    if isinstance(x, List):
        # List
        x_bar = statistics.mean(x)
        vals = ", ".join(str(v) for v in x)
        out = f"{vals} (mean = {round(x_bar, 2)})"
    elif isinstance(x, (float, int)):
        # Int or Float
        out = x
    else:
        raise ValueError
    return out
        
if __name__ == "__main__":
      print(spine_ht_loss(2, 1))
      print(spine_ht_loss([2, 2.5], 1))
    # print(show_nums_and_mean(1))
    # print(show_nums_and_mean([1, 2]))
