# teresayun.me

Teresa Wong's personal site: one page, a day side (engineer/researcher) and a night side (musician), switched with the toggle at the bottom.

## Layout

| Path | What it is |
| --- | --- |
| `prototype/index.html` | The source. Edit this file. It is also what gets published to the Claude artifact preview. |
| `prototype/fonts/`, `prototype/audio/` | Files the page loads by relative path (the Cookie Monster font, the two Danger in Pompeii tracks as AAC `.mp4`). The build copies them into `docs/`. |
| `tools/build_site.py` | Wraps the prototype in a full HTML document and writes the deployable site to `docs/`. |
| `docs/` | The built site that GitHub Pages serves: `index.html`, `404.html` (`loss = NaN`), `favicon.svg`, `CNAME`, `.nojekyll`. Don't edit by hand; rebuild instead. |

## Update the site

```bash
python3 tools/build_site.py
```

Then commit and push. GitHub Pages redeploys on its own.

## Going live (one-time setup)

1. Create a GitHub repository (for example `teresaecho22/teresayun.me`) and push this folder to it.
2. In the repository: **Settings → Pages → Build and deployment → Deploy from a branch**, branch `main`, folder `/docs`.
3. Verify the domain first: **GitHub Settings (your account) → Pages → Add a domain** → `teresayun.me`, then add the TXT record it shows at Namecheap.
4. At Namecheap, **Domain List → teresayun.me → Advanced DNS**, add:

   | Type | Host | Value |
   | --- | --- | --- |
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |
   | CNAME | `www` | `teresaecho22.github.io.` |

   Optional IPv6 (AAAA, host `@`): `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.
5. Back in **Settings → Pages**, the custom domain reads `teresayun.me` (from `docs/CNAME`). Once the DNS check passes, tick **Enforce HTTPS**.

DNS changes can take from a few minutes up to a day to spread.

## Still placeholders

- Project previews (rocket, VEX) are ASCII stand-ins until the videos are ready.
- Off-duty photos and the publication thumbnails are drawn placeholders.
- The リモコン easter egg (↑↑↓↓←→←→BABA) plays an original beat and links to the real song; embed the official video here once the site is on its own domain.
