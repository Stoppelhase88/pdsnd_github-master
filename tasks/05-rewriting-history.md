# Aufgabe 5: History bearbeiten (vorsichtig!)

**Ziel:** Commit-Historie lokal aufräumen (Squash/Rebase) – nur auf Feature-Branches.

1. Interaktives Rebase auf Feature-Branch:
   ```bash
   git rebase -i main
   ```
2. Squashe WIP‑Commits, schreibe präzise Nachrichten. **Nie** öffentliche History auf `main` umschreiben.
