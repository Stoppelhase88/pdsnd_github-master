# Aufgabe 1: Initiales Setup & erster Commit

**Ziel:** Lokales Repo initialisieren (oder Repo klonen), Python-Umgebung aufsetzen, erster Commit.

1. Repo vorbereiten:
   ```bash
   git init -b main
   git add .
   git commit -m "chore: initial project scaffold"
   ```
2. GitHub-Remote anlegen und pushen:
   ```bash
   gh repo create {project_name} --public --source=. --remote=origin --push
   # oder manuell im Browser anlegen und dann
   git remote add origin git@github.com:Stoppelhase88/pdsnd_github-master.git
   git push -u origin main
   ```
3. CI checken: In GitHub unter **Actions** prüfen, ob die Tests laufen.

