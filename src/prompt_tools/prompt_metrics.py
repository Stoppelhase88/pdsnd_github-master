import argparse
from .token_estimator import rough_token_estimate


def stats(text: str) -> dict:
    if text is None:
        text = ""
    chars = len(text)
    words = len(text.split()) if text else 0
    tokens = rough_token_estimate(text)
    avg_word_len = (sum(len(w) for w in text.split()) / words) if words else 0.0
    return {
        "chars": chars,
        "words": words,
        "avg_word_len": round(avg_word_len, 3),
        "rough_tokens": tokens,
    }


def main():
    parser = argparse.ArgumentParser(description="Einfache Prompt-Metriken")
    parser.add_argument("--file", required=True, help="Pfad zu einer Textdatei")
    args = parser.parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Datei nicht gefunden: {args.file}")
        return 2
    s = stats(content)
    print(json_dump(s))
    return 0


def json_dump(d: dict) -> str:
    import json
    return json.dumps(d, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    raise SystemExit(main())
