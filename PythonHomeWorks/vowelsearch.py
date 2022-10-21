def search4letters(phrase:str, letters:str='aeiouöüı') -> set:
    return set(letters).intersection(set(phrase))
