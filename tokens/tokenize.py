"""
character level tokenizer for lixus

models take integers not characters
this builds a vocab from the corpus and maps both ways

  python tokens/tokenize.py
"""

from pathlib import Path

text_path = Path(__file__).with_name("sample.txt")
text = text_path.read_text(encoding="utf-8")

print("raw text")
print(repr(text))
print(f"chars: {len(text)}")

# stable ids: sort unique characters once
chars = sorted(set(text))
vocab_size = len(chars)

print("\nvocab")
print(f"size: {vocab_size}")
print(chars)

stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}


def encode(s: str) -> list[int]:
    return [stoi[c] for c in s]


def decode(ids: list[int]) -> str:
    return "".join(itos[i] for i in ids)


ids = encode(text)
print("\nencoded (first 40)")
print(ids[:40])
print(f"tokens: {len(ids)}")

print("\nround trip")
print(decode(ids) == text)

demo = "wach"
print(f"\nencode({demo!r}) -> {encode(demo)}")
print(f"decode -> {decode(encode(demo))!r}")
