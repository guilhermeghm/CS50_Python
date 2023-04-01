import re

def main():
    print(parse(input("HTML: ")))

def parse(html):
    src_url_match = re.search(r'src=[\'"]([^\'"]+)', html)
    if src_url_match:
        src_url = src_url_match.group(1)
        if re.search(r'(youtube)', src_url):
            video_id = re.sub(r"^(https?://)?(www\.)?youtube\.com/([a-z0-9_]+)", "", src_url)
            return f"https://youtu.be{video_id}"
    return None


if __name__ == "__main__":
    main()
