#!/usr/bin/env python3
import argparse
import random
import shutil
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
BUILD = ROOT / "build"
VENV = ROOT / ".venv"
OUT = DIST / "duck.txt"

DUCKS = [
    r"""
        __
      <(o )___
       ( ._> /
        `---'
""",
    r"""
       __
     /({o}>\______
     \__/        \
        \________/
""",
    r"""
        __
      <(o )___
       ( ._> /
     ___.---.___
    (___________)
     \_________/
""",
    r"""
         .-.
        /   \
       | o o |
       |  ^  |
        \___/
      __/   \__
    _/         \_
   (_____________)
""",
]


def random_duck() -> str:
    return random.choice(DUCKS)


def run(_: argparse.Namespace) -> None:
    print(random_duck())


def setup(_: argparse.Namespace) -> None:
    if VENV.exists():
        print(f"virtualenv already exists: {VENV}")
        return
    venv.create(VENV, with_pip=True)
    print(f"created virtualenv: {VENV}")


def build(_: argparse.Namespace) -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    OUT.write_text(random_duck().strip("\n") + "\n", encoding="utf-8")
    print(f"built: {OUT}")


def clean(_: argparse.Namespace) -> None:
    for path in (DIST, BUILD, ROOT / "__pycache__"):
        if path.exists():
            shutil.rmtree(path)
            print(f"removed: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Random duck ASCII art")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("run", help="print a random duck")
    sub.add_parser("setup", help="create a virtualenv")
    sub.add_parser("build", help="write a duck to dist/")
    sub.add_parser("clean", help="remove build artifacts")

    args = parser.parse_args()
    command = args.command or "run"
    globals()[command](args)


if __name__ == "__main__":
    main()
