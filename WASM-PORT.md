# WASM-PORT — zfergus/topopt -> doishy-doish/topo-cpp + topo-toy

Upstream: Python + numpy/scipy/cvxopt/nlopt (MMA via NLopt LD_MMA, OC variant,
inner-loop OC in problems.py, density filter H-matrix in filters.py,
von Mises stress in von_mises_stress.py, BCs in boundary_conditions.py).

## Feature map (idea crosses, code is re-implemented)
| upstream concept | browser-core equivalent | status |
|---|---|---|
| SIMP penal p=3, OC update (problems.py) | legacy path, default | shipped |
| Sensitivity filter rmin (filters.py) | legacy path, default | shipped |
| Density filter H-matrix variant | opt-in mode | shipped (PRO-WASM) |
| Heaviside projection + continuation | opt-in mode | shipped (PRO-WASM) |
| Penal continuation (p 1->3->5 schedule) | opt-in mode | shipped |
| Per-element von Mises stress field | results overlay + export | shipped |
| NLopt MMA (solvers.py TopOptSolver) | NOT ported: nlopt cannot ship in zero-dep SINGLE_FILE wasm; documented rejection | evaluated |
| Multi-load weighted compliance (examples/) | NOT ported: changes load plumbing; parked | parked |
| Mechanism synthesis (mechanisms/) | NOT ported: different objective; parked | parked |

## Contracts
bench/reference.json mirrors topo-cpp bench v1/v2/corpus-v3 (same numbers).
A port passes when tip is within 1% and the sampled trajectory within 2%.
