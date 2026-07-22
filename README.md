# mina-transient-fork-audit
Non-probabilistic topological verification &amp; o1js state audit framework for short-range forks under Ouroboros Samasika.
# Mina Transient Fork Auditability Framework

## Abstract
In succinct blockchains operating under Ouroboros Samasika (such as Mina Protocol), state updates rely on recursive zero-knowledge proofs without full historical chain state storage. During short-range fork windows—arising from network latency, propagation jitter, or multi-leader VRF slot assignments—competing block proposals temporarily create divergent state transitions before canonical resolution.

This research presents a non-probabilistic structural verification framework that models transient fork topologies using partial-order graph structures. By evaluating sequence integrity and state transitions during asynchronous execution windows, the framework generates cryptographic proofs of structural convergence. Designed for execution via o1js, this layer allows off-chain provers, L2 rollups (e.g., Zeko), and archive nodes to audit pre-settlement sequence integrity without altering Mina’s underlying 22KB core consensus model.

---

## 🎯 Architecture Overview & Key Focus Areas

### 1. Transient Fork Topology Mapping
* Graph-theory representation of temporary block forks under Ouroboros Samasika rules.
* Audits sequence divergences during localized asynchronous network windows.

### 2. Deterministic Sequence Auditing
* Non-probabilistic verification of account state updates prior to canonical consensus lock-in.
* Isolates sequence irregularities during best-chain selection evaluation.

### 3. o1js Circuit Integration Model
* Off-chain zero-knowledge proof generation for sequence divergence tracking.
* Verifies external DAG/partial-order state data prior to settlement on Mina.

---

## 🔬 Target Applications
* **L2 Rollups & Sequencers (e.g., Zeko):** Verifying pre-settlement batch ordering.
* **Archive & Proof Nodes:** Auditing transient sequence health under variable propagation delays.
* **Consensus Boundary Research:** Quantitative modeling of short-range fork dynamics.

---

## 🚀 Quick Start & Proof Execution

### Prerequisites
* Node.js v18+
* npm / yarn

### Run the o1js Proof Engine

```bash
# Clone the repository
git clone [https://github.com/rataninfralabs/mina-transient-fork-audit.git](https://github.com/rataninfralabs/mina-transient-fork-audit.git)
cd mina-transient-fork-audit

# Install dependencies (o1js framework)
npm install

# Run Python mathematical model
python audit_fork_topology.py

# Run o1js ZK proof verification runner
npm start

*Maintained by RatanInfra_Labs — Independent Infrastructure & Mathematical Modeling Research.*
