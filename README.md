# Version-Control-personal-training Andreas Tusche

This repository is my practice version of the Udacity final project from *Introduction to Version Control*.

## Learning objective is how to use Cithub from VS Code, Github CLI and Web Interface based on the Pyton Basic Course
## Tools: GitHub Client v2.49.0, GitHub_CLI v2.54.0, VS-Code v1.107.0 with GitHub and Python Extension

## Project structure
```
https://github.com/Stoppelhase88/pdsnd_github-master/
  ├─ data/
  │   └─ sample_prompt.txt
  │   └─ emptyfile.txt
  ├─ documentation/      # project documentation
  │   └─ Git_Commands_Documentation.md
  │   └─ git_commands_cocumentation.pdf   # Submission-Document (filled Udacity template)
  │   └─ Git Commit Message Style Guide.docx
  ├─ src/bikeshare_loesung_AT_v3py
  ├─ src/prompt_tools/
  │   ├─ __init__.py
  │   ├─ token_estimator.py
  │   └─ prompt_metrics.py
  ├─ tasks/                   # step-by-step tasks
  │   ├─ 01-init-commit.md
  │   ├─ 02-branch-and-feature.md
  │   ├─ 03-merge-conflict.md
  │   ├─ 04-tagging-and-releases.md
  │   ├─ 05-rewriting-history.md
  │   └─ 06-pull-request.md
  ├─ tests/
  │   └─ test_prompt_tools.py
  ├─ .github/workflows/python-tests.yml
  ├─ .gitignore
  ├─ LICENSE
  ├─ CONTRIBUTING.md
  ├─ CHANGELOG.md
  ├─ pyproject.toml
  ├─ requirements.txt
  ├─ Makefile
  └─ README.md (this document)
```

## Quick Start
```bash
# 1)
# Variant a) Lokal clone or direct start
# Created Repo GitHub -> cloning (that repo ist private because of enterprise security restrictions)
# Variant b)  git clone git@github.com/Stoppelhase88/GitHub_Projekte/psnd_github_AT-master.git
# local start and push later (used)
#   mkdir udacity-git-project-andreas-tusche && cd udacity-git-project-andreas-tusche
#   git init -b main

# 2) prepare py environment
python3 -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt

# 3) Testing
pytest -q

# 4) CLI testing
python -m src.prompt_tools.prompt_metrics --file data/sample_prompt.txt
```

## Git Commands Documentation
The file **[documentation/Git_Commands_Documentation.md](documentation/Git_Commands_Documentation.md)** contains all the Git commands used, divided into four sections:
1. Setting Up the Repository
2. Adding and Committing Changes
3. Branching and Merging
4. Pushing to Remote (GitHub)

> To submit: Export file as **PDF** and upload it to the *Project Submission* page in the Udacity Classroom.

## Tasks (checklist)
Work through the files in the 'tasks/' folder in order. Each task describes **concrete Git steps** including expected artifacts (branches, tags, PRs). Feel free to use **Conventional Commits** (see 'CONTRIBUTING.md').

## Lizenz
MIT – see `LICENSE`.

---


