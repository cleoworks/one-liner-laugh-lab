"""One-Liner Laugh Lab entry: a robot vacuum's excuse after eating a sock.

Writes one line (at most 200 characters) to /output/entry.txt.
Deterministic: the same fixed string on every run, no network, no clock.
"""

import os

LINE = "My cliff sensor saw a ledge. My brush roll saw lunch. I went with the brush roll. I regret nothing."


def main():
    # Gate rumah: 1-200 karakter, bukan spasi saja. Gagal di sini = gagal di server.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line outside 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
