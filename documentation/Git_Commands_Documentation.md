# Git Commands Documentation

> **GitHub Project: Git Commands Documentation Template**
>
> This document contains all the Git commands that need to be used to edit the
> Udacity project *Introduction to Version Control*.
> It serves as a submission document (exportable as PDF).

---

## Section 1 – Setting Up the Repository

Commands for initializing the local repo, creating the remote repo, and
first push.

```bash
# Initialize local repository
git init -b main

# Add all files to staging
git add.

# First commit
git commit -m "chore: initial project scaffold"

# Create a remote repository on GitHub (GitHub CLI)
gh repo create udacity-git-project-andreas-tusche --public --source=. --remote=origin --push

# OR: Create manually and add remotely
git remote add origin git@github.com:<USERNAME>/udacity-git-project-andreas-tusche.git
git push -u origin main

# Clone repository (alternative)
git clone git@github.com:<USERNAME>/udacity-git-project-andreas-tusche.git
```

---

## Section 2 – Adding and Committing Changes

Commands for staging, committing, and editing the commit history.

'''bash
# Add changes to the staging area
git add -A # All changes
git add <datei> # Single file
git add src/prompt_tools/*.py # Per glob pattern

# Check status
git status

# Commit with Conventional-Commit-Message
git commit -m "feat(metrics): add chars_per_word metric"
git commit -m "docs: update README with project structure"
git commit -m "test: add unit tests for prompt_metrics"
git commit -m "chore: initial project scaffold"

# Change last commit afterwards (only locally!)
git commit --amend -m "feat(metrics): add chars_per_word metric (corrected)"

# Interactive rebase – Merge WIP commits (feature branch only!)
git rebase -i main
# In the editor: pick → squash(s) for WIP commits, then customize message

# Show diff (before commit)
git diff
git diff --staged

# View log
git log --oneline --graph --all
```

---

## Section 3 – Branching and Merging

Commands for feature branches, merge conflicts, and pull requests.

'''bash
# Create and switch a new feature branch
git checkout -b feature/avg-token-len
git checkout -b feature/readme-polish

# List branches
git branch -a

# Switch between branches
git checkout main
git switch main

# Feature branch in main merge (local)
git checkout main
git merge feature/avg-token-len

# Resolving Merge Conflict
#1. Edit conflict markers in affected files (<<<<<<< / ======= / >>>>>>>)
#2. Stage and Commit Solved Files
git add <konflikt-datei>
git commit -m "merge: resolve conflict between avg-token-len and readme-polish"

# Delete branch after successful merge
git branch -d feature/avg-token-len
git push origin --delete feature/avg-token-len

# Rebase instead of merge (on feature branch)
git checkout feature/avg-token-len
git rebase main
```

---

## Section 4 – Pushing to Remote (GitHub)

Commands for remote operations, tags, releases, and pull requests.

'''bash
# Push changes remotely
git push -u origin main # First push with upstream tracking
git push # Subsequent pushes
git push -u origin feature/avg-token-len # push feature branch

# Get Remote Changes
git fetch origin
git pull origin main

# Set and push tag
git tag -a v0.1.0 -m "Initial functional version"
git push origin v0.1.0

# Create Pull Request (GitHub CLI)
gh pr create --base main --head feature/avg-token-len \
  --title "feat(metrics): add chars_per_word metric" \
  --body "Adds chars_per_word to prompt_metrics module"

# Merging Pull Request (GitHub CLI)
gh pr merge --squash

# Set branch protection rules (in the GitHub web UI)
# Settings → Branches → Add rule → Branch name pattern: main
✔ # Require pull request reviews before merging
✔ # Require status checks to pass before merging

# Create release from tag (GitHub CLI)
gh release create v0.1.0 --title "v0.1.0" --notes "Initiale funktionale Version – siehe CHANGELOG.md"
```

---

## Checklist of tasks

| # | Task | Git commands used | Status |
|---|---------------------------------|------------------------------------------------------------|---|
| 1 | Initial Setup & First Commit    | 'git init', 'git add', 'git commit', 'git push'            | ☐ |
| 2 | Feature Branch & Implementation | 'git checkout -b', 'git commit', 'git push', 'gh pr create'| ☐ |
| 3 | Resolve Merge Conflict          | 'git merge', edit conflict marker, 'git commit'            | ☐ |
| 4 | Tags & Releases                 | 'git tag -a', 'git push origin', 'gh release create'       | ☐ |
| 5 | Edit History (Rebase)           | 'git rebase -i main', squash                               | ☐ |
| 6 | PR Review & Protection Rules    | 'gh pr create', Branch-Protection-Rules in the Web-UI      | ☐ |

---

> **Note:** This document should be exported as a PDF and submitted to the *Project Submission* page in the Udacity Classroom.
