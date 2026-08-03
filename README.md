# Lumera Protocol documentation

Developer documentation for [Lumera Protocol](https://lumera.io), built with [Mintlify](https://mintlify.com). Lumera is a Cosmos SDK Layer 1 for permanent decentralized storage (Cascade) and AI powered content services (Sense).

## Structure

- `docs.json` holds the site config and navigation.
- Pages are MDX files. The folder layout mirrors the sidebar (cascade/, smart-contracts/, sdk/, validators-mainnet/, validators-testnet/, supernodes/, cross-chain/, upgrades/, protocol/, hub/, api/).
- `sources/` holds scraped research material. It is excluded from the build by `.mintignore`.
- `drafts/` holds content that is written but not yet published. Also excluded from the build.

## Local development

Install the Mintlify CLI and run the dev server from the repo root.

```bash
npm i -g mint
mint dev
```

The preview runs at `http://localhost:3000`. Run `mint broken-links` to check internal links before pushing.

## Style

Writing rules live in `AGENTS.md`. The short version. Simple sentences. Active voice. No em dashes. No semicolons in prose. Avoid colons in prose and titles. Verify every command, version, and endpoint against the official [LumeraProtocol](https://github.com/LumeraProtocol) repos before publishing.

## Publishing

Changes deploy automatically after a push to `main` through the Mintlify GitHub app.
