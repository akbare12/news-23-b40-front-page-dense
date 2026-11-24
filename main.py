"""news-23 b40 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1024 * 1024


def fail(msg):
    print("error: " + msg, file=sys.stderr)
    sys.exit(1)


def check_png(data, label):
    if len(data) < 8 or data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(label + ": bad PNG signature")
    if len(data) < 33:
        fail(label + ": truncated PNG")
    length, ctype = struct.unpack(">I4s", data[8:16])
    if ctype != b"IHDR" or length != 13:
        fail(label + ": bad IHDR chunk")
    width, height, depth, colour = struct.unpack(">IIBB", data[16:26])
    if (width, height) != (1024, 1024):
        fail(label + ": expected 1024x1024, got %dx%d" % (width, height))
    if depth != 8 or colour not in (2, 6):
        fail(label + ": expected 8-bit RGB/RGBA, got depth %d colour %d" % (depth, colour))
    if len(data) < 12 or struct.unpack(">I", data[-12:-8])[0] != 0 or data[-8:-4] != b"IEND":
        fail(label + ": malformed IEND trailer")
    if len(data) > MAX_BYTES:
        fail(label + ": %d bytes exceeds 1 MiB" % len(data))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        fail("MAKEFUN_OUTPUT_DIR is empty")
    out_dir_abs = os.path.abspath(out_dir)
    if out_dir_abs == HERE or out_dir_abs.startswith(HERE + os.sep):
        fail("MAKEFUN_OUTPUT_DIR must not be inside the repo")
    if not os.path.isfile(SRC):
        fail("entry.png not found next to main.py")
    with open(SRC, "rb") as f:
        data = f.read()
    check_png(data, "source entry.png")
    print("source entry.png: %d bytes" % len(data))
    os.makedirs(out_dir_abs, exist_ok=True)
    dst = os.path.join(out_dir_abs, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        out = f.read()
    if out != data:
        fail("output differs from source")
    check_png(out, "output entry.png")
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
