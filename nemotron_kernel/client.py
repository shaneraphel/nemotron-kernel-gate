"""Call a Nemotron model on Nebius Token Factory."""

from __future__ import annotations

import json
import os
import urllib.request


def complete(prompt: str) -> str:
    body = json.dumps(
        {
            "model": os.environ.get("NEMOTRON_MODEL", "nvidia/nemotron"),
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode()
    req = urllib.request.Request(
        os.environ["NEBIUS_BASE_URL"] + "/chat/completions",
        data=body,
        headers={
            "Authorization": "Bearer " + os.environ["NEBIUS_API_KEY"],
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        payload = json.loads(resp.read().decode())
    return payload["choices"][0]["message"]["content"]
