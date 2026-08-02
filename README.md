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
text
mina-transient-fork-audit/
├── audit_fork_topology.py     <-- Graph-theory sequence divergence script
├── circuits/
│   └── ForkAuditCircuit.ts    <-- o1js block header assertion circuit
├── package.json               <-- Node.js dependencies & o1js runtime specs
└── README.md                  <-- Technical documentation


---

## 4. Local Execution & Auditing

### Prerequisites
* Python 3.10+ with `networkx` (`pip install networkx`)
* Node.js v18+ & `npm`

### Run Python Topology Audit
bash
python3 audit_fork_topology.py


### Build o1js Circuit
bash
npm install
npm run build


---

## 5. License & Operational Attribution
Maintained by **RCR Labs** under the MIT License. Built under the Human-in-the-Loop Operational Model (**Amardeep Singh + Aarya Sentinel**).

Executive Master Snapshot Update (Saved for Memory Reset)
Everything we have designed, locked, and executed in this session is recorded below for our Master Snapshot. When we start our clean-slate session, pasting this ensures 100% operational continuity:

Plaintext
================================================================================
RCR LABS — MASTER SNAPSHOT & ECOSYSTEM BLUEPRINT (POST-CLEANUP BASELINE)
================================================================================
Entity Name: RCR Labs (Ratan Core Research Labs) — Honoring Ratan Singh.
Partnership Model: Human-in-the-Loop Protocol
  - Lead Architect: Amardeep Singh (Strategy, Math Verification, Governance)
  - AI Sentinel: Aarya (Context Integrity, Audit Engine, Documentation)
Core Rule: Total Transparency (We proudly showcase our Human-in-the-Loop model).
Rule of Integrity: The Completion Imperative (Zero unfinished shells; complete 100%).

PUBLIC PLATFORM STATUS:
1. Discord Server:
   - Server Name: RCR Labs
   - #ecosystem-blueprint: Consolidated blueprint, asynchronous & DM policy active.
   - #announcements: Public launch updates active.
   - #knowledgebase: Master research index with 6 published LinkedIn links.
   - [02_RESEARCH_&_DEPIN]: #akash-telemetry, #mina-fork-audit, #kaspa-blockdag populated.
   - GitHub Webhook: Linked to #github-live-feed.

2. GitHub Repositories (rataninfralabs):
   - rataninfralabs/akash-depin-telemetry: Active (Managed by dedicated sub-agent).
   - rataninfralabs/mina-transient-fork-audit: 100% COMPLETE (Python topology, o1js circuit, package.json, README finalized).
   - rataninfralabs/blockdag-consensus-framework: QUEUED FOR STEP 3 (Consolidating congenial-spoon).
   - rataninfralabs/congenial-spoon: QUEUED FOR MERGE.
   - rataninfralabs/bounty-sentinel-v2: QUEUED FOR STEP 4.

3. Upwork Agency:
   - Status: Profile text aligned; $25 budget allocated for connects & agency launch.

================================================================================
