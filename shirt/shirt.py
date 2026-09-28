import sys
from PIL import Image, ImageOps

def main():
    in_put, out_put = verify()
    open(in_put, out_put)

def verify():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif sys.argv[1].endswith((".jpg", ".jpeg", ".png")) and sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
        if sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
            return sys.argv[1], sys.argv[2]
        else:
            sys.exit("Input and Output have different extensions")
    else:
        sys.exit("Invalid Input")

def open(inp, out):
    with Image.open(f"{inp}") as im, Image.open("shirt.png") as sh:
        cropped = ImageOps.fit(im, sh.size)
        cropped.paste(sh, (0, 0), sh)
        cropped.save(f"{out}")
main()
