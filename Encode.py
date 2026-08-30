
#### learned merge
merges = [


('e', ' '), ('a', 'n'), (' ', 't'), ('h', 'e '), ('t', ' '), (' t', 'he '), ('e', 'r'), ('d', ' '), ('l', 'e'), ('r', 'e')]







def encode_word(word):

    tokens = list(word)


    for pair in merges:
        tokens = merge_tokens(tokens, pair)
        print("current rule:", pair)

    return tokens



def merge_tokens(tokens, pair_to_merge):

    new_tokens = []

    i = 0

    while i < len(tokens):

        if (
            i < len(tokens) - 1
            and (tokens[i], tokens[i + 1]) == pair_to_merge
        ):
            new_tokens.append(tokens[i] + tokens[i + 1])
            i += 2

        else:
            new_tokens.append(tokens[i])
            i += 1

    return new_tokens



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

def tokens_to_ids(tokens):

    ids = []

    for token in tokens:
        ids.append(token_to_id[token])

    return ids


new_word = "transfer payment"

tokens = encode_word(new_word)

ids = tokens_to_ids(tokens)

print("Tokens:", tokens)
print("IDs:", ids)


