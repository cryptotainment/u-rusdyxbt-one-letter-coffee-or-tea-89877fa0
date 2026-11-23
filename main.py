"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt: A for coffee, B for tea.
No words, no explanation, no punctuation — one byte, nothing else.

Choice: A (coffee). Coffee is the more vivid stance — the ritual, the
urgency, the "don't talk to me before my coffee" energy — where tea reads
calm and polite. On the judge's criteria, vividness first, the bolder,
more alive answer wins the pairwise comparison.
"""

import os

CHOICES = {"coffee": "A", "tea": "B"}
LETTER = CHOICES["coffee"]  # A = coffee

# Gate guard, mirroring the sealed scorer: exactly 1 char, not whitespace.
assert len(LETTER) == 1 and not LETTER.isspace(), "entry must be one letter"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LETTER)
