# BPE Tokenizer From Scratch

A Byte Pair Encoding (BPE) tokenizer implemented from scratch in Python to understand how modern subword tokenizers work internally.

This project started with a character-level BPE implementation and was later extended to byte-level BPE using UTF-8 encoding.

The goal was not simply to use an existing tokenizer library, but to understand the mechanics behind tokenization by implementing the core algorithm myself.

---

## What is BPE?

Byte Pair Encoding (BPE) is a tokenization algorithm commonly used in modern NLP systems.

Instead of treating an entire word as one token, BPE starts with small units and repeatedly merges the most frequent neighboring pair.

For example:

```text
a n d
↓
an d
↓
and

The tokenizer learns these merge rules from a training corpus.

Project Progression
1. Character-Level BPE

The first implementation represented text as individual characters.

For example:

"transfer"
↓
t r a n s f e r

The tokenizer then

Counted adjacent character pairs.
Found the most frequent pair.
Merged the pair.
Repeated the process.
Built a vocabulary.
Assigned token IDs.
Encoded and decoded text.

This implementation helped me understand the core mechanics of BPE.

2. Byte-Level BPE

The second implementation moved from characters to bytes.

Text is first encoded using UTF-8:

"transfer"
↓
UTF-8
↓
bytes

For example:

"transfer".encode("utf-8")

produces the byte representation of the text.

The bytes are then treated as the initial tokens.

For learning purposes, the implementation represents each base byte as a one-byte bytes object:

b't'
b'r'
b'a'
b'n'
...

BPE can then merge these byte tokens:

b'a' + b'n'
↓
b'an'

and later:

b't' + b'h'
↓
b'th'
Byte-Level BPE Training Pipeline

The current implementation follows this process:

Raw Text
   ↓
UTF-8 Encoding
   ↓
Byte Tokens
   ↓
Build Vocabulary
   ↓
Count Adjacent Pairs
   ↓
Find Most Frequent Pair
   ↓
Merge Pair
   ↓
Repeat
   ↓
Learned Merge Rules
   ↓
Final Vocabulary
   ↓
Token IDs
Example Learned Merges

Using the training corpus, the tokenizer learned rules such as:

(b'e', b' ') → b'e '
(b'a', b'n') → b'an'
(b' ', b't') → b' t'
(b'h', b'e ') → b'he '
(b't', b' ') → b't '

The important observation is that the tokenizer does not receive linguistic rules such as "an is a common suffix."

It discovers frequent patterns statistically from the training data.

Encoding

Once the merge rules have been learned, new text can be encoded by:

New Text
   ↓
UTF-8 Bytes
   ↓
Initial Byte Tokens
   ↓
Apply Learned Merge Rules
   ↓
BPE Tokens
   ↓
Token IDs

For example:

"transfer"

may begin as:

b't' b'r' b'a' b'n' b's' b'f' b'e' b'r'

and after applying learned merges may contain larger tokens such as:

b'an'
b'er'

depending on the learned vocabulary.

Decoding

Decoding reverses the process:

Token IDs
   ↓
BPE Tokens
   ↓
Bytes
   ↓
UTF-8 Decoding
   ↓
Original Text
Why Byte-Level BPE?

Character-level tokenization has a limitation: it depends on the characters available to the tokenizer.

Byte-level tokenization provides a fixed base vocabulary of 256 possible byte values.

This means text can ultimately be represented using bytes, including text containing characters that were not explicitly present in the training corpus.

For example:

English
é
你好
Arabic
Emojis

can all be represented through UTF-8 bytes.


What I Learned

Building this tokenizer from scratch helped me understand:

How BPE learns merge rules.
How adjacent pair frequencies are calculated.
How repeated merging creates larger reusable tokens.
The difference between characters, bytes, and token IDs.
How UTF-8 represents text as bytes.
Why byte-level tokenization can represent arbitrary text.
How a tokenizer builds and uses a vocabulary.
How encoding and decoding work.
Why token IDs are simply indices into a learned vocabulary.
Next Steps

The next stage of the project is to complete the byte-level encoder and decoder and then compare the implementation with production tokenizer designs.

The long-term goal is to understand tokenization deeply enough to move from tokenizers into the internals of Transformer models.