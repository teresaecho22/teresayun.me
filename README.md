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

The domain is registered at Cloudflare, so its DNS lives there too.

1. Create a public GitHub repository `teresaecho22/teresayun.me` and push this folder to it. (Free GitHub Pages needs a public repo.) Commits use the GitHub noreply address `241268677+teresaecho22@users.noreply.github.com` (set in this repo's git config), so the Gmail address stays private.
2. In the repository: **Settings → Pages → Build and deployment → Deploy from a branch**, branch `main`, folder `/docs`.
3. Verify the domain: **GitHub Settings (your account) → Pages → Add a domain** → `teresayun.me`, then add the TXT record it shows in Cloudflare (step 4). This stops anyone else's repo from claiming the domain.
4. In Cloudflare, **teresayun.me → DNS → Records → Add record**, set **Proxy status to "DNS only" (grey cloud)** on every record so GitHub can issue the HTTPS certificate:

   | Type | Name | Content |
   | --- | --- | --- |
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |
   | CNAME | `www` | `teresaecho22.github.io` |
   | TXT | the name GitHub shows in step 3 | the code GitHub shows in step 3 |

   Optional IPv6 (AAAA, name `@`): `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.
5. Back in **Settings → Pages**, the custom domain reads `teresayun.me` (from `docs/CNAME`). Once the DNS check passes, tick **Enforce HTTPS**.

DNS changes usually show up within minutes on Cloudflare; the HTTPS certificate can take up to an hour.

## Still placeholders

- Project previews (rocket, VEX) are ASCII stand-ins until the videos are ready.
- Off-duty photos and the publication thumbnails are drawn placeholders.
- The リモコン easter egg (↑↑↓↓←→←→BABA) plays an original beat and links to the real song; embed the official video here once the site is on its own domain.
