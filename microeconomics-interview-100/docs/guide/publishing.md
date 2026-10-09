# 发布到 GitHub

本目录已经按独立仓库结构组织。为避免误写入已有仓库，发布时请新建一个空 GitHub repository，然后在本地执行：

```bash
git init -b main
git add .
git commit -m "feat: initial microeconomics interview playbook"
git remote add origin git@github.com:<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git
git push -u origin main
```

若使用 HTTPS，把 `origin` 改成对应 HTTPS clone URL。

## 推荐仓库名

- `microeconomics-interview-100`
- `microeconomics-interview-playbook`

## 发布前检查

```bash
python scripts/verify_repo.py
```

公开发布前还应由维护者自行选择许可证；当前仓库只放置 `NOTICE.md`，没有替维护者做许可证决定。
