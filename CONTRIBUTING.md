# Contributing

Thanks for improving the Lumera Protocol documentation.

## Before you open a pull request

- Read `AGENTS.md` for the writing rules. Simple sentences, active voice, no em dashes, no semicolons in prose.
- Verify every command, version, endpoint and number against the official LumeraProtocol repos or a live endpoint. Never invent values.
- Label anything that changes over time, such as versions, heights, parameters and fees, with the network it applies to.
- Run `mint validate` and `mint broken-links` from the repo root. Both must pass.

## Adding your public endpoints or snapshots

Infrastructure operators can add an entry to the Community providers section on `networks.mdx`.

Open your pull request with this URL so the provider form loads, replacing the branch name.

```
https://github.com/LumeraProtocol/mintlify-docs/compare/main...YOUR-BRANCH?template=provider-listing.md
```

If that does not load, copy `.github/PULL_REQUEST_TEMPLATE/provider-listing.md` into the description by hand.

We run every endpoint against the live chain before merging. Anything that does not answer, or reports a different chain ID, is removed from the pull request.

## Local development

```bash
npm i -g mint
mint dev
```

The preview runs at `http://localhost:3000`.
