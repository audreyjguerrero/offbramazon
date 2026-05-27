Local hosting instructions

Quick steps to serve this project locally for development and testing.

Python (recommended, no extras required):

```bash
# default port 8000
python server.py
# or specify a port
python server.py 3000

# alternatively (built-in):
python -m http.server 8000
```

Node (if you prefer):

```bash
# using npx (no install required)
npx http-server -p 8000
```

Windows PowerShell one-liner:

```powershell
python -m http.server 8000
```

Open in browser:

- The Python `server.py` attempts to open your default browser automatically. If it doesn't, visit `http://localhost:8000` (or the IP shown in the terminal).

Why this helps:

- Serving the files over HTTP resolves CORS and fetch issues that occur when opening `index.html` directly via `file://`.

Files in this repo:

- `index.html` — main page
- `products.json` — sample product data
- `images/` — image assets
- `server.py` — the small server script you can run

If you'd like, I can add a `start` script to `package.json` or a PowerShell/Batch helper next.