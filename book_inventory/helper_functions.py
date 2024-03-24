def get_non_empty_string(prompt: str, min_limit: int, max_limit: int) -> str:
    while True:
        output = input(prompt)
        if min_limit <= len(output) <= max_limit:
            return output
        elif max_limit < len(output):
            print("Maximum characters allowed is {0}".format(max_limit))
        elif min_limit > len(output):
            print("Input must be at least {0} characters long".format(min_limit))
        

def get_positive_number(prompt: str, min_limit: int, max_limit: int) -> int:
    while True:
        try:
            output = int(input(prompt))
            if min_limit <= output <= max_limit:
                break
            else:
                print("Please enter value between {0} and {1}!".format(min_limit, max_limit))
        except ValueError:
            print("Numeric value only!")
    return output


def read_file(filename, data_type="string") -> list:
    new_list = []
    with open(filename) as connection:
        for line in connection:
            if data_type == "string":
                new_list.append( line.rstrip() )
            if data_type == "int":
                new_list.append( int(line.rstrip()) )
            if data_type == "float":
                new_list.append( float(line.rstrip()) )
    return new_list


def write_file(filename, content):
    with open(filename, 'w') as f:
        for line in content:
            f.write(f"{line}\n")



