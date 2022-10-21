def search4vowels(phrase:str):
    vowels = set("aeiıöoüu")
    found = vowels.intersection(set(phrase))
    return found
    # for vowel in found:
    #     print(vowel)

def search4letters(phrase:str, letters:str) -> set:
    """Return a set of the letters found in phrase."""
    return set(letters).intersection(set(phrase))


# inp = input("Provide a phrase to search for vowels:")
# rt = search4vowels(inp)

# for i in rt:
#     print(i)

# liste = ["elma", "armut", "çilek", "portakal"]

# for i in liste:
#     print(i)
#     r = search4vowels(i)
#     for j in r:
#         print(j)
#     print("--")


rt = search4letters("bir sürahi","klhmn")
for i in rt:
    print(i)
