"""proxiech - free proxy hunter for SMM gateway orders.

Verifies free http/socks4/socks5 proxies against the exact gateway the
order placer uses and writes working exits to alive_proxies.txt.
"""

from .cli import main, probe, verdict, fetch_sources, normalize

__version__ = "1.0.0"
__all__ = ["main", "probe", "verdict", "fetch_sources", "normalize", "__version__"]
