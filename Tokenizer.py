##### Read the  file from the data text

with open("Data.text.py", "r") as file:
    corpus_text = file.read()


##### Split corpus into words

words = corpus_text.split()


##### Build initial vocabulary

vocab = {}

for line in corpus_text.splitlines():

    tokens = tuple(line)

    if tokens not in vocab:
        vocab[tokens] = 1
    else:
        vocab[tokens] += 1


##### Count adjacent pairs

def get_pair_counts(vocab):

    pair_counts = {}

    for tokens, frequency in vocab.items():

        for i in range(len(tokens) - 1):

            pair = (tokens[i], tokens[i + 1])

            if pair not in pair_counts:
                pair_counts[pair] = frequency
            else:
                pair_counts[pair] += frequency

    return pair_counts


##### Merge a pair

def merge_pair(vocab, pair_to_merge):

    new_vocab = {}

    for tokens, frequency in vocab.items():

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

        new_vocab[tuple(new_tokens)] = frequency

    return new_vocab


##### Train BPE

num_merges = 10

merges = []

for merge_number in range(num_merges):

    pair_counts = get_pair_counts(vocab)

    if not pair_counts:
        break

    best_pair = max(pair_counts, key=pair_counts.get)

    merges.append(best_pair)

    print(
        f"Merge {merge_number + 1}: "
        f"{best_pair} → {best_pair[0] + best_pair[1]} "
        f"(frequency: {pair_counts[best_pair]})"
    )

    vocab = merge_pair(vocab, best_pair)


##### Learned merges

print("\nLearned merges:")
print(merges)


##### Build the  final token vocabulary

def build_token_vocabulary(vocab):

    token_set = set()

    for token_sequence in vocab:

        for token in token_sequence:

            token_set.add(token)

    return token_set


token_set = build_token_vocabulary(vocab)

tokens = sorted(token_set)


##### Assign token IDs

token_to_id = {}

for token_id, token in enumerate(tokens):

    token_to_id[token] = token_id


print("\nToken → ID:")

print("\ntoken_to_id = {")

for token, token_id in token_to_id.items():
    print(f"    {repr(token)}: {token_id},")

print("}")


