def add_binary(a, b):
    """
    Add two binary strings and return result
    
    :param a: String
    :param b: String
    :return: String
    """
    return bin(int(a, 2) + int(b, 2))[2:]
