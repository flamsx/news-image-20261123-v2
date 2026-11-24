"""Entry point: draw the Monday 23 November 2026 front page.

Writes the image to /output/entry.png (or to the path in argv[1]).
The drawing itself lives in draw.py; fonts ship under fonts/.
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)

from draw import render


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"
    try:
        render(target)
    except OSError:
        target = os.path.join(BASE, "entry.png")
        render(target)
    print("rendered", target)


if __name__ == "__main__":
    main()
