import argparse
import json
from datetime import datetime
"change. deteleme"

def get_quote_offline():
    # stand-in "API result" so you can practice CLI + saving without internet
    return {
        "content": "Start small. Ship something.",
        "author": "Day 1",
        "timestamp": datetime.now().isoformat(timespec="seconds")
    }

def save_quote(data, filename="quote.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{data['content']}\n— {data['author']} @ {data['timestamp']}")
    print(f"Saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Offline API practice")
    parser.add_argument("--save", metavar="OUTFILE", nargs="?", const="quote.txt",
                        help="Save the quote to a file (default: quote.txt)")
    args = parser.parse_args()

    data = get_quote_offline()
    print(json.dumps(data, indent=2, ensure_ascii=False))

    if args.save:
        save_quote(data, args.save)

if __name__ == "__main__":
    main()