# Documentation project instructions

## About this project

- This is the developer documentation for Lumera Protocol, built on [Mintlify](https://mintlify.com).
- Pages are MDX files with YAML frontmatter. Configuration lives in `docs.json`.
- This site is the first place developers meet Lumera. Keep it accurate and easy to read.

## Terminology

- "Lumera Protocol" on first mention of a page, then "Lumera".
- "Cascade" is the permanent storage service. "Sense" is the content authentication service.
- "SuperNode" in prose (capital S and N). The binary is `supernode` in code formatting.
- Token symbol is LUME. Base denom is `ulume` (1 LUME = 1,000,000 ulume). EVM denom is `alume` (18 decimals).
- Chain IDs in code formatting. `lumera-mainnet-1` and `lumera-testnet-2`.
- "Lumera Portal" is the explorer at portal.lumera.io. "Lumera Hub" is the app at hub.lumera.io.
- "LumeScope" is a read-only REST API aggregator. Never call it an explorer.
- `lumerad` is the node binary, always in code formatting.

## Style preferences

- Simple sentences. One idea per sentence. Aim for under 20 words.
- Use active voice and second person ("you").
- Never use em dashes or en dashes in prose. Rewrite the sentence instead.
- Never use semicolons in prose. Split into two sentences.
- Avoid colons in prose, page titles, headings, and descriptions. Rephrase instead. Colons are fine in YAML syntax, URLs, code, and table cells.
- Use sentence case for headings.
- Code formatting for file names, commands, paths, denoms, and code references.
- Every page needs frontmatter with title (3 to 7 words, no colon), sidebarTitle (1 to 3 words), and description (one sentence, no colon).
- Prefer Steps for procedures, Tabs for mainnet and testnet variants, CodeGroup for multi language snippets. At most two callouts per page.
- End developer pages with a "Next steps" CardGroup.

## Content boundaries

- Every command, version, endpoint, and number must be verified against the official LumeraProtocol GitHub repos or live endpoints. Never invent values.
- The JS SDK is `@lumera-protocol/sdk-js` on npm. Never reference `@0xkaleab/sdk-js`. The Go SDK is `github.com/LumeraProtocol/sdk-go` and the Rust SDK is `github.com/LumeraProtocol/sdk-rs`.
- Modules are documented on the single `protocol/modules` page, not as per module x/ reference pages.
- Individual LEPs are not documented. The `protocol/governance` page covers governance and links to the LEP files on GitHub.
- The Smart contracts section covers the EVM (overview, MetaMask, Remix, OpenRPC, precompiles). The EVM is live on testnet only. Mainnet runs v1.12.0 until its upgrade. Never claim the EVM is live on mainnet.
- Do not document the Pastel claims or legacy migration flow. The team ruled it out for now. Related drafts live in `drafts/`.
- Network upgrade migration details belong in the Network upgrades section, not in the validator or SuperNode sections.
- When quoting fee numbers or parameters, note that governance can change them.
