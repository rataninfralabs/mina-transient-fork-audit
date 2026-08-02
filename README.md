# Mina Transient Fork Audit Framework
**RCR Labs (Ratan Core Research Labs)** | *Lead Architect: Amardeep Singh | Sentinel: Aarya*

---

## 1. Executive Summary & Problem Statement
During periods of localized network latency, Mina Protocol nodes experience temporary sequence divergences before block resolution via Ouroboros Samasika into the canonical chain. Standard probabilistic models often fail to capture structural integrity during asynchronous latency windows. 

This repository introduces a non-probabilistic, graph-theory audit framework using `o1js` zero-knowledge circuits to evaluate competing block structures and verify state divergences prior to canonical settlement.

---

## 2. Architecture & Mathematical Framework
* **Topological Mapping:** Representing transient fork trees as directed acyclic sub-graphs ($G = (V, E)$) to trace transaction sequencing across competing block proposals.
* **Non-Probabilistic Verification:** Auditing sequence integrity and state transitions without relying on heuristic gas/weight assumptions.
* **Circuit Integration (`o1js`):** Modular zk-proof verification validating block header assertions within asynchronous execution windows.

---

## 3. Directory Structure & File Map
```text
/mina-transient-fork-audit
├── /circuits
│   └── ForkAuditCircuit.ts      <-- o1js assertion logic for block header validation
├── /models
│   └── topological_graph.py     <-- Graph-theory sequence divergence mapping
├── /docs
│   └── ARCHITECTURE.md          <-- Mathematical spec & Samasika alignment paper
├── README.md                    <-- Framework documentation
└── LICENSE                      <-- MIT License
