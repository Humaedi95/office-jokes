import os

JOKE = 'My performance review says I "thrive under pressure" — HR\'s polite way of saying they only remember I exist during a crisis.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
