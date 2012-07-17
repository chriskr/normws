import os
import argparse

def main():
    desc = "Script to normalize line breaks and remove trailing whitespace"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("target", help="the target directory")
    args = parser.parse_args()
    for root, dirs, files in os.walk(args.target):
        for name in files:
            if name.endswith(".js"):
                lines = None
                path = os.path.join(root, name)
                with open(path, "rb") as f:
                    lines = f.readlines()
                if lines:
                    c = "\n".join(map(lambda s: s.rstrip(), lines)) + "\n"
                    if not c == "".join(lines):
                        with open(path, "wb") as f:
                            f.write(c)
                            print "fixed", path

if __name__ == "__main__":
    main()
