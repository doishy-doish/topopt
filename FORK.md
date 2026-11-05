# FORK — doishy-doish/topopt

Upstream: https://github.com/zfergus/topopt (Zachary Ferguson, MIT License).

Policy (same as our rodin fork):
- Upstream files are NEVER modified. All additions live in new files only.
- LICENSE (MIT, (c) 2019 Zachary Ferguson) is preserved; this notice + the
  copyright line are reproduced in every substantial port we take elsewhere.
- Upgrade goal: make the higher-language reference directly comparable to our
  browser core, then port the portable algorithmic parts (no numpy/scipy/nlopt
  dependency can ship in the zero-dep WASM core — ideas cross, code is
  re-implemented in C++/JS from the documented method).

## What this fork adds
- `WASM-PORT.md` — feature map: upstream concept -> browser-core equivalent.
- `bench/reference.json` — 5 shared contracts (cantilever/bridge/mbb/lbracket/3d)
  mirrored from our topo-cpp bench so any port can be checked to tip 1% /
  trajectory 2%.
- `tools/compare_topo.py` — stdlib-only checker (same thresholds).
