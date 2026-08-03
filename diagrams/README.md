# Diagram sources

Hand drawn style diagrams for the docs, ported from lumera.help. The build
renders every definition to a light and a dark SVG in `images/diagrams/` with
the Shantell Sans font subset embedded, so the images work in any `<img>` tag.

- `diagrams.json` holds the definitions ported from lumera.help (`lib/diagrams.ts`).
- `diagrams-extra.json` holds definitions authored for this site.
- `fonts/` holds the Shantell Sans latin woff2 sources (Google Fonts, OFL license).

Definitions are boxes, arrows, and text with x, y coordinates. See the
existing entries for the schema.

## Rebuild

```bash
pip install fonttools brotli
python3 diagrams/build.py
```

Pages embed the output as a light and dark image pair.

```mdx
<img className="block dark:hidden mx-auto" src="/images/diagrams/name-light.svg" alt="..." />
<img className="hidden dark:block mx-auto" src="/images/diagrams/name-dark.svg" alt="..." />
```
