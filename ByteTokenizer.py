corpus_text = """
Please transfer the payment to my wallet balance today.
The customer requested a refund for the failed transaction.
Bank branch confirmed the deposit and updated the account balance.
Merchant sent an invoice and receipt after the settlement.
Withdraw funds from the account using the correct IBAN and routing number.
"""


with open("Data.text.py", "r", encoding="utf-8") as file:
    corpus_text = file.read()


# --------------------------------------------------
# 1. Convert each line into byte tokens
# --------------------------------------------------

byte_sequences = []

for line in corpus_text.splitlines():

    if not line.strip():
        continue

    byte_sequence = tuple(
        bytes([b]) for b in line.encode("utf-8")
    )

    byte_sequences.append(byte_sequence)


print("First byte sequence:")
print(byte_sequences[0])


# --------------------------------------------------
# 2. Build vocabulary
# --------------------------------------------------

vocab = {}

for tokens in byte_sequences:

    if tokens not in vocab:
        vocab[tokens] = 1
    else:
        vocab[tokens] += 1


# --------------------------------------------------
# 3. Count adjacent pairs
# --------------------------------------------------

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


pair_counts = get_pair_counts(vocab)




best_pair = max(pair_counts, key=pair_counts.get)

print("\nMost frequent byte pair:")
print(best_pair)

print("Frequency:")
print(pair_counts[best_pair])




def merge_pair(tokens, pair):

    merged_tokens = []

    i = 0

    while i < len(tokens):

        # Check if current token + next token
        # are the pair we want to merge
        if (
            i < len(tokens) - 1
            and tokens[i] == pair[0]
            and tokens[i + 1] == pair[1]
        ):

            # Combine the two byte tokens
            merged_token = tokens[i] + tokens[i + 1]

            # Add merged token
            merged_tokens.append(merged_token)

            # Skip both tokens
            i += 2

        else:

            
            merged_tokens.append(tokens[i])

            i += 1

    
    return tuple(merged_tokens)



merged = merge_pair(
    byte_sequences[0],
    best_pair
)


print("\nBefore merge:")
print(byte_sequences[0])


print("\nAfter merge:")
print(merged)


def learn_merges(vocab, num_merges):

    merges = []

    for step in range(num_merges):

        # Count all adjacent pairs
        pair_counts = get_pair_counts(vocab)

        # Stop if there are no pairs left
        if not pair_counts:
            break

        # Find the most frequent pair
        best_pair = max(pair_counts, key=pair_counts.get)

        # Save the merge rule
        merges.append(best_pair)

        print(
            f"Merge {step + 1}:",
            best_pair,
            "Frequency:",
            pair_counts[best_pair]
        )

        # Create a new vocabulary
        new_vocab = {}

        # Apply the merge to every sequence
        for tokens, frequency in vocab.items():

            merged_tokens = merge_pair(
                tokens,
                best_pair
            )

            new_vocab[merged_tokens] = frequency

        vocab = new_vocab

    return vocab, merges
vocab, merges = learn_merges(vocab, 10)


token_set = set()

for tokens in vocab:
    for token in tokens:

        token_set.add(token)
# possible base byte tokens

for byte_value in range(256):

    token_set.add(bytes([byte_value]))


sorted_tokens = sorted(
    token_set,
    key=lambda token: (len(token), token)
)


token_to_id = {}

for token_id, token in enumerate(sorted_tokens):

    token_to_id[token] = token_id

print("\nVocabulary size:")
print(len(token_to_id))

print("\nFirst 20 tokens:")

for token, token_id in list(token_to_id.items())[:20]:

    print(token, "→", token_id)