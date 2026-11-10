# anuj-proxy-hunter

**Free proxy hunter for SMM gateway orders** — verifies http / socks4 / socks5
exits against the exact API gateway used by Telegram-reaction and
Instagram-likes order placers, then saves the working ones.

```
pip install anuj-proxy-hunter
anuj-proxy-hunter
```

Author: **anuj**

## Why

Free proxy lists are full of dead ports, Cloudflare-banned datacenter IPs and
exits the panel refuses (`VPN / Proxy usage detected`). **proxiech** probes
every candidate with the *same request production sends* (same endpoint,
same headers), so only proxies that can really carry an order get saved.

## Usage

| Command | What it does |
|---|---|
| `anuj-proxy-hunter` | full run — all 28 sources (~87k candidates) |
| `anuj-proxy-hunter --workers 120` | more parallel probes |
| `anuj-proxy-hunter --limit 500` | quick test on the first 500 candidates |
| `anuj-proxy-hunter --deadline 1800` | stop after 30 min and save what we have |
| `python -m proxiech` | same thing via module (short alias: `proxiech`) |

Flow: intro banner + list fetching (~1 min) → screen clears → **live colored
dashboard** → `Ctrl+C` stops early and **still saves** results.

## Output files (written to the current folder)

* `alive_proxies.txt` — verified working exits; previous finds are
  **re-validated first** on every re-run
* `dead_proxies.txt` — everything that failed (reference)

## What counts as "alive"

A proxy is kept only if the gateway answers with a **real API response**
(the probe sends an empty link so a validation error comes back — **no order
is ever placed**). Everything else is rejected:

* connection errors / timeouts
* HTTP 403 / 407 (banned / auth required)
* HTML block pages (Cloudflare / WAF)
* `VPN / Proxy usage detected` answers (panel refuses the exit)

## Library use

```python
from proxiech import probe, fetch_sources

candidates, ok, failed = fetch_sources()
verdict = probe("http://1.2.3.4:8080")   # 'alive' | 'throttle' | 'dead'
```

## Requirements

Python 3.8+ with `requests` and `PySocks` (installed automatically).

## License

MIT
