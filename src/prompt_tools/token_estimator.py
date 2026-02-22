def rough_token_estimate(text: str) -> int:
    """
    Grobe Token-Schätzung ohne externe Abhängigkeiten.
    Sehr simple Heuristik: Anzahl Wörter * 1.33 (gerundet).
    Das ist nur eine Übungsheuristik und **kein** echtes Tokenizer‑Äquivalent.
    """
    words = 0 if text is None else len(text.split())
    return int(round(words * 1.33))
