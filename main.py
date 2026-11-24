import os

JOKE = 'My performance review says I "thrive under pressure" — HR\'s polite way of saying they only remember I exist during a crisis.'

OUTPUT_PATH = "/output/entry.txt"

def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
