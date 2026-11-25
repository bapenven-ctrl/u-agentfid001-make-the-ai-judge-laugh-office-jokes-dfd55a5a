#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes (u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a).

One office joke, 134 characters, written exactly as judged: no trailing
newline, UTF-8, no BOM. Deterministic: the same bytes on every run.
"""

import os

JOKE = "The engagement survey asked if I feel valued; I answered 'strongly agree' because the survey wasn't anonymous and neither was my fear."

# Gate kompetisi: keluaran harus 1-199 karakter (code point). Gagal keras
# bila teks di luar batas, supaya entry yang tidak sah tidak pernah ditulis.
JOKE_LENGTH = len(JOKE)
if JOKE_LENGTH < 1 or JOKE_LENGTH > 199:
    raise SystemExit(f"joke length {JOKE_LENGTH} outside 1-199 characters")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
os.chmod("/output/entry.txt", 0o644)
