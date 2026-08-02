# Mina Transient Fork Audit Framework
**RCR Labs (Ratan Core Research Labs)** | *Lead Architect: Amardeep Singh | Sentinel: Aarya*

---

## 1. Executive Summary & Problem Statement
During periods of localized network latency, Mina Protocol nodes experience temporary sequence divergences before block resolution via Ouroboros Samasika into the canonical chain. Standard probabilistic models often fail to capture structural integrity during asynchronous latency windows.

This repository introduces a non-probabilistic audit framework using graph-theory topology models combined with `o1js` zero-knowledge assertion circuits to evaluate competing block structures and verify state divergences prior to canonical settlement.

---

## 2. Architecture & Technical Components
* **Topological Mapping (`audit_fork_topology.py`):** Directed Acyclic Subgraph ($G = (V, E)$) representation modeling latency-driven block split variations.
* **Zero-Knowledge Assertions (`circuits/ForkAuditCircuit.ts`):** `o1js` modular circuits verifying block transition rules within bounded $\le 500\text{ms}$ latency windows.

---

## 3. Directory Structure
```text
mina-transient-fork-audit/
├── audit_fork_topology.py     <-- Graph-theory sequence divergence script
├── circuits/
│   └── ForkAuditCircuit.ts    <-- o1js block header assertion circuit
├── package.json               <-- Node.js dependencies & o1js runtime specs
└── README.md                  <-- Technical documentation
