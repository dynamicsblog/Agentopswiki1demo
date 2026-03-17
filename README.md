# Business Central Agent Playground Wiki

This repository contains a multi-page Markdown wiki for **GitHub Pages**.

## Project pages

- `index.md` - home page and global navigation
- `overview.md` - scope and purpose
- `toolkit-components.md` - architecture and building blocks
- `setup.md` - prerequisites and quickstart
- `playground-scenarios.md` - practical scenario ideas
- `references.md` - source links and maintenance notes

## GitHub Pages setup (one-time)

1. Create a GitHub repository.
2. Add the remote:
   ```bash
   git remote add origin https://github.com/<USER>/<REPO>.git
   ```
3. Push the branch:
   ```bash
   git push -u origin main
   ```
4. In GitHub: **Settings → Pages → Build and deployment → Source = GitHub Actions**.
5. The workflow `.github/workflows/deploy-pages.yml` will publish the site automatically.

## Local checks

Run a fast local link check before pushing:

```bash
python scripts/check_links.py
```

## Notes

- This repository is already prepared for Actions-based GitHub Pages deployment.
- Actual publication requires a configured GitHub remote and push permissions.
