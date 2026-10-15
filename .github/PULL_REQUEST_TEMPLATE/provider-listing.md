## Provider

**Name:**
**Website:**
**Contact for outages:**

## Endpoints

Fill in only what you actually operate. Leave a cell empty rather than guessing, and list each network separately — most providers serve mainnet only.

| Service | Mainnet (`lumera-mainnet-1`) | Testnet (`lumera-testnet-2`) |
| --- | --- | --- |
| RPC | | |
| LCD (REST) | | |
| gRPC (`host:port`) | | |

**Rate limits:**
**Archive or pruned:**

## Snapshot (optional)

| | Mainnet | Testnet |
| --- | --- | --- |
| URL | | |
| Approximate size | | |
| Refresh cadence | | |

## Prove it answers

Run these against the endpoints you listed and paste the output. Both must print the chain ID of the network you are claiming.

```bash
# RPC
curl -s https://<your-rpc>/status | jq -r '.result.node_info.network'

# LCD
curl -s https://<your-lcd>/cosmos/base/tendermint/v1beta1/node_info \
  | jq -r '.default_node_info.network'
```

<!-- paste output here -->

## Checklist

- [ ] Each endpoint above printed the correct chain ID when I ran the commands
- [ ] I listed a network only if I actually serve it
- [ ] Snapshot links resolve and the size and cadence are current
- [ ] One provider per pull request
- [ ] I did not change `docs.json` navigation or any unrelated page
- [ ] `mint validate` and `mint broken-links` both pass

## How we review

We re-run every command above against your endpoints before merging. Anything that does not answer, or reports a different chain ID, gets dropped from the PR rather than published. Listings that go dark are removed when we next audit them.

Public endpoints are documented as community infrastructure that may be rate-limited and is not guaranteed production infrastructure. Listing does not imply endorsement or an SLA.
