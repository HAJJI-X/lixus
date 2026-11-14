# lixus

My own language model — built from first principles, in public.

Not a wrapper. Not a fine-tune of someone else's stack as the end goal.
A model I understand end to end: tokens → architecture → training → inference.

## Status

**Now:** tokenization — turning raw text into the numbers a model can learn from.

**Next:** a small transformer trained from scratch on my own data.

**Later:** scale it, specialize it, ship it.

## Layout

```
lixus/
├── learn/           # core build steps (the model, piece by piece)
│   └── 01_tokens/   # vocabulary, encode / decode
└── README.md
```

## Run

```bash
python learn/01_tokens/tokenize.py
```

---

**HAJJI-X** · building in public
