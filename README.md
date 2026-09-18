# Nemotron kernel gate

Accept a kernel draft from an NVIDIA Nemotron model served on Nebius Token Factory only when discrete outputs match exactly. Continuous kernels still use a relative tolerance.

## Setup

```bash
export NEBIUS_API_KEY=...
export NEBIUS_BASE_URL=https://api.tokenfactory.nebius.com/v1
python -m nemotron_kernel.gate
```
