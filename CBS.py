def CBS(sequence: str) -> bool:
    while '()' in sequence or '[]' in sequence:
        sequence.replace('()', '')
        sequence.replace('[]', '')
    return len(sequence) == 0


if __name__ == '__main__':
    print('function return True if bracket sequence is correct and False if incorrect. Example for CBS "[((())()(())]]"')
    CBS('[((())()(())]]')