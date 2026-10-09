# Publish to GitHub

The repository is already complete and git-ready. If you have GitHub CLI locally:

```bash
git init
git add .
git commit -m "docs: publish Agent Harness Interview 100"
gh repo create agent-harness-interview-100 --public --source=. --remote=origin --push
```

Or create an empty GitHub repository in the UI and push this directory with normal `git remote add origin ...` / `git push` commands.

> The ChatGPT GitHub connector used to build this package can write files to existing repositories but does not expose a create-new-repository action, so this package intentionally does not alter any unrelated repository in the linked account.
