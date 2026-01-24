import re
import sys

def main():
    html = input()
    print(parse(html))

def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"'
    match = re.search(pattern, s)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None

if __name__ == "__main__":
    main()
