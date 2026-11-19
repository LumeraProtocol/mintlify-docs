"""Local documentation contracts. No live network requests are made.

Run with python3 tests/test_network_help.py from any working directory.
"""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def page(path):
    return (ROOT / path).read_text(encoding="utf-8")


def section(text, heading):
    return text.split(heading + "\n", 1)[1].split("\n##", 1)[0]


class NetworkHelpTests(unittest.TestCase):
    def test_api_examples_use_the_target_network(self):
        text = section(page("api/overview.mdx"), "## Base URLs")
        self.assertIn("Examples use different networks.", text)
        self.assertIn("Choose the base URL for your target network", text)
        self.assertNotIn("All examples in this documentation target mainnet", text)
        self.assertIn("| Mainnet |", text)
        self.assertIn("| Testnet |", text)

    def test_cascade_faucet_is_testnet_only(self):
        text = section(page("cascade/error-handling.mdx"), "### Insufficient funds")
        self.assertIn("Fund your wallet on the network you are using.", text)
        self.assertIn("On testnet, you can request tokens from the [faucet](/faucet).", text)
        self.assertNotIn("Fund your wallet with testnet tokens", text)

    def test_cascade_supernodes_use_the_selected_network(self):
        text = section(page("cascade/error-handling.mdx"), "### SuperNodes unavailable")
        self.assertIn("SuperNodes on your selected network", text)
        self.assertNotIn("the testnet SuperNodes", text)

    def test_cascade_explorers_use_the_target_network(self):
        text = page("cascade/error-handling.mdx")
        for heading, action in (
            ("### Action not registered", "Confirm the transaction succeeded"),
            ("### Action not found", "Verify the action exists"),
        ):
            with self.subTest(heading=heading):
                advice = section(text, heading)
                self.assertIn(action, advice)
                self.assertIn("[Lumera Portal for your target network](/networks)", advice)
        self.assertIn("[Network explorers](/networks)", section(text, "## Getting help"))
        self.assertNotIn("https://portal.testnet.lumera.io", text)

    def test_supernode_funding_uses_the_target_network(self):
        text = section(page("supernodes/overview.mdx"), "## Prerequisites")
        self.assertIn("LUME on your target network for staking and transaction fees.", text)
        self.assertIn("On testnet, request tokens from the [testnet faucet](/faucet)", text)
        self.assertNotIn("- Testnet LUME tokens", text)

    def test_setup_grpc_matches_the_chain_id(self):
        text = page("supernodes/node-setup.mdx")
        self.assertIn("`--lumera-grpc` must point to the same network as `--chain-id` (testnet in this walkthrough).", text)
        self.assertNotIn("must point to a **testnet** gRPC endpoint", text)

    def test_supernode_references_scope_their_examples(self):
        for path in ("supernodes/register.mdx", "supernodes/operations.mdx"):
            with self.subTest(path=path):
                intro = page(path).split("\n##", 1)[0]
                self.assertIn("Examples use testnet.", intro)
                self.assertIn("Use the chain ID and endpoints for your target network", intro)
                self.assertIn("check its current parameters.", intro)

    def test_shared_help_links_resolve_locally(self):
        # Only the network-selection and faucet routes used by this contract.
        for route in ("networks", "faucet"):
            with self.subTest(route=route):
                self.assertTrue((ROOT / f"{route}.mdx").is_file())
        networks = page("networks.mdx")
        for network, url in (
            ("Mainnet", "https://portal.lumera.io/lumera-mainnet-1"),
            ("Testnet", "https://portal.testnet.lumera.io/lumera-testnet-2"),
        ):
            with self.subTest(network=network):
                tabs = re.findall(rf'<Tab title="{network}">(.*?)</Tab>', networks, re.S)
                self.assertTrue(any(f"]({url})" in tab for tab in tabs))


if __name__ == "__main__":
    unittest.main(verbosity=2)
