def compute_code(board:list[int]) -> int:
    """function to compute some sort of code

    Args:
        board (list[int]): the list of int from the set {0, 1, 2} representing 
            the state of a board

    Raises:
        ValueError: if the lenght of the list board is not exactely 9, 
            or the list contains values that are not in teh set {0, 1, 2}, 
            or there are not exately 3 of each.

    Returns:
        int: the code corresponding to the state of the board represented by 
        the list of int.
    """
    code = 5
    if (len(board) != 9 
        or board.count(0) != 3 
        or board.count(1) != 3 
        or board.count(2) != 3):
            raise ValueError("Invalid board!")
    
    for i in range(len(board)):
        code += pow(3, i)
    return code
