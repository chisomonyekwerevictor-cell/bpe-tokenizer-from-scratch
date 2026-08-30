token_to_id = {
    ' ': 0,
    ' t': 1,
    ' the ': 2,
    '.': 3,
    'A': 4,
    'B': 5,
    'I': 6,
    'M': 7,
    'N': 8,
    'P': 9,
    'T': 10,
    'W': 11,
    'a': 12,
    'an': 13,
    'b': 14,
    'c': 15,
    'd': 16,
    'd ': 17,
    'e': 18,
    'e ': 19,
    'er': 20,
    'f': 21,
    'g': 22,
    'h': 23,
    'he ': 24,
    'i': 25,
    'k': 26,
    'l': 27,
    'le': 28,
    'm': 29,
    'n': 30,
    'o': 31,
    'p': 32,
    'q': 33,
    'r': 34,
    're': 35,
    's': 36,
    't': 37,
    't ': 38,
    'u': 39,
    'v': 40,
    'w': 41,
    'y': 42,
}


id_to_token = {}

for token, token_id in token_to_id.items():
    id_to_token[token_id] = token



def decode_ids(ids):

    tokens = []

    for token_id in ids:
        tokens.append(id_to_token[token_id])

    return "".join(tokens)


ids = [37, 34, 13, 36, 21, 20, 0, 32, 12, 42, 29, 18, 30, 37]

text = decode_ids(ids)

print("Decoded text:", text)