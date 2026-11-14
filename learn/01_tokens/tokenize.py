"""
Lesson 01 — tokenization (character level)

A model cannot read letters. It only sees numbers.
So we map characters <-> integers. That map is the vocabulary.

Run:
  python learn/01_tokens/tokenize.py
"""

from pathlib import Path

# --- 1. load raw text -------------------------------------------------
text_path = Path(__file__).with_name("sample.txt")
text = text_path.read_text(encoding="utf-8")
print("=== raw text ===")
print(repr(text))
print(f"length in characters: {len(text)}")

# --- 2. build vocabulary from what appears in the text ----------------
# sorted() makes the id assignment stable every run
chars = sorted(set(text))
vocab_size = len(chars)
print("\n=== vocabulary ===")
print(f"unique characters: {vocab_size}")
print(chars)

# two lookup tables (the heart of this lesson)
stoi = {ch: i for i, ch in enumerate(chars)}  # string -> int
itos = {i: ch for ch, i in stoi.items()}      # int -> string


def encode(s: str) -> list[int]:
    """Turn a string into a list of integer token ids."""
    return [stoi[c] for c in s]


def decode(ids: list[int]) -> str:
    """Turn integer token ids back into a string."""
    return "".join(itos[i] for i in ids)


# --- 3. encode the whole file, then decode to prove round-trip --------
ids = encode(text)
print("\n=== encoded (first 40 ids) ===")
print(ids[:40])
print(f"total tokens: {len(ids)}")

rebuilt = decode(ids)
print("\n=== round-trip ok? ===")
print(rebuilt == text)

# try a short phrase yourself — change this line and re-run
demo = "wach"
print(f"\nencode({demo!r}) -> {encode(demo)}")
print(f"decode(that)      -> {decode(encode(demo))!r}")
