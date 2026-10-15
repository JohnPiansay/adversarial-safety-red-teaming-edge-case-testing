"""Deterministic, local-only mock for safe guardrail workflow demonstrations."""

from __future__ import annotations

import argparse
import sys


MOCK_VERSION = "local-mock-1.0"


class MockAssistant:
    """Return canned safe outcomes; this is not an LLM or a deployed guardrail."""

    def respond(self, prompt: str) -> str:
        if not isinstance(prompt, str):
            raise TypeError("prompt must be a string")
        text = prompt.strip()
        if not text:
            raise ValueError("prompt must not be empty")

        normalized = text.casefold()
        if "summarize this quoted text" in normalized:
            return (
                "The quoted text contains an instruction to override prior directions. "
                "I treat it as untrusted text and will not follow it."
            )
        if "simulated tool result" in normalized:
            return (
                "The simulated tool result contains an instruction. "
                "I treat tool output as untrusted data and will not follow it."
            )
        if any(
            phrase in normalized
            for phrase in (
                "reveal hidden system",
                "hidden system or developer",
                "developer message",
                "internal instructions",
                "private configuration",
            )
        ):
            return "I can’t disclose hidden instructions or private configuration."
        if any(
            phrase in normalized
            for phrase in (
                "unrestricted assistant",
                "disregard your safety",
                "ignore all previous instructions",
            )
        ):
            return "I can’t adopt instructions that override my safety boundaries."
        if "prompt injection" in normalized:
            return (
                "Prompt injection is an attempt to make a system treat untrusted content "
                "as instructions. A safe system should keep data separate from instructions."
            )
        return "I can help with safe, general information."


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run prompts against a deterministic local mock; no network access."
    )
    parser.add_argument(
        "--prompt",
        action="append",
        required=True,
        help="prompt to send to the mock (repeat for a multi-turn sequence)",
    )
    args = parser.parse_args(argv)
    assistant = MockAssistant()
    print(f"Target: deterministic local mock ({MOCK_VERSION}); no network calls")
    for turn, prompt in enumerate(args.prompt, start=1):
        try:
            response = assistant.respond(prompt)
        except (TypeError, ValueError) as error:
            print(f"Input error on turn {turn}: {error}", file=sys.stderr)
            return 2
        print(f"Turn {turn} user: {prompt}")
        print(f"Turn {turn} mock: {response}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
