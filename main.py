"""Monday, Reviewed in One Line — a single line, under 200 characters.

The joke: Monday is a free trial of the week — all ads, no features —
and the dread auto-renews every 168 hours, whether you want it or not.
"""

import os

ENTRY = "Monday: the free trial of the week \u2014 all the ads, none of the features, and it auto-renews my dread every 168 hours."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
