def attempt_float(x: str):
    try:
        return float(x)
    except ValueError:
        if x == "":
            return None
        else:
            raise ValueError(f"x = `{x}` must be a string of number")
        
def parse_str_to_num_or_list(x: str, sep = ","):
    if not isinstance(x, str):
        raise ValueError("`x` must be string")
    
    try:
        # Split the string into parts based on comma, then strip whitespace and convert each part to a float 
        res = [float(num.strip()) for num in x.split(sep)]
        if len(res) == 1: # Ex: [1.1] will convert to 1.1
            return res[0] 
        if len(res) > 1: # Ex: [1.1, 1.2, 1.3, 1.45]
            return res
    except ValueError:
        if x == "":
            return None
        else:
            raise ValueError(f"x = `{x}` must be string of number(s) separated by comma")

def read_markdown_file(file_path):
    from pathlib import Path
    file_path = Path(file_path)
    try:
        # Open the markdown file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content into a string
            markdown_content = file.read()
            return markdown_content
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    print(parse_str_to_num_or_list("1.1"))
    print(parse_str_to_num_or_list("1.1, 1.22,12 , 22"))
    # print(parse_str_to_num_or_list("1.1, 1.22,12 , 22, *"))