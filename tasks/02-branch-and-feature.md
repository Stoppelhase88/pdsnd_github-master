# Aufgabe 2: Feature-Branch & Implementierung

**Ziel:** Feature-Branch anlegen und kleine Änderung implementieren.

1. Branch erstellen:
   ```bash
   git checkout -b feature/avg-token-len
   ```
2. Erweiterung: Füge in `prompt_metrics.py` eine Kennzahl `chars_per_word` hinzu.
3. Tests ergänzen (`tests/`), lokal laufen lassen: `pytest -q`.
4. Commit & Push:
   ```bash
   git add -A
   git commit -m "feat(metrics): add chars_per_word metric"
   git push -u origin feature/avg-token-len
   ```
5. Erstelle auf GitHub einen Pull Request gegen `main`.
