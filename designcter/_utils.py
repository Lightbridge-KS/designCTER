def bool_yesno(x: bool) -> str:
    return "Yes" if x else "No"

def dash_if_blank(x: str) -> str:
    return "-" if x == "" else x