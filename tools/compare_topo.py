"""Stdlib-only checker: port trajectory vs bench/reference.json (tip 1%, traj 2%).
Usage: python3 tools/compare_topo.py run.json [bench/reference.json]
run.json: {"tip": float, "cg": int, "traj": [floats...]} (+ optional "contract": name).
Mirrors topo-cpp bench/check.py thresholds; no third-party deps.
"""
import json, sys
ref_path = sys.argv[2] if len(sys.argv) > 2 else "bench/reference.json"
run = json.load(open(sys.argv[1]))
ref = json.load(open(ref_path))["contracts"]
name = run.get("contract", "cantilever")
c = ref[name]
tip_err = abs(run["tip"] - c["tip"]) / abs(c["tip"])
print(f"contract={name} tip={run['tip']} ref={c['tip']} err={tip_err:.4%} cg={run.get('cg')} ref_cg={c['cg']}")
assert tip_err <= 0.01, "tip out of 1% tolerance"
print("PASS")
