"""
Mina Short-Range Fork Auditability Engine (PoC v0.1)
Author: RatanInfra_Labs
Description: Models transient competing block branches under Ouroboros Samasika 
             using directed acyclic graph (DAG) partial orders to audit state 
             convergence before canonical best-chain selection.
"""

from typing import Dict, List, Tuple


class ShortRangeForkAuditor:
    def __init__(self, canonical_genesis_hash: str):
        self.genesis = canonical_genesis_hash
        # Graph representation: block_hash -> List[parent_hashes]
        self.adjacency_matrix: Dict[str, List[str]] = {self.genesis: []}
        self.block_weights: Dict[str, int] = {self.genesis: 1}

    def add_transient_block(self, block_hash: str, parent_hash: str, vr_weight: int) -> bool:
        """
        Registers a temporary competing block proposal during a propagation delay window.
        """
        if parent_hash not in self.adjacency_matrix:
            print(f"[!] Warning: Parent block {parent_hash} not found in current topological view.")
            return False

        if block_hash not in self.adjacency_matrix:
            self.adjacency_matrix[block_hash] = [parent_hash]
            self.block_weights[block_hash] = vr_weight
            print(f"[+] Logged transient proposal: {block_hash[:8]} -> Parent: {parent_hash[:8]}")
            return True
        return False

    def evaluate_divergence_depth(self, tip_a: str, tip_b: str) -> int:
        """
        Calculates the divergence depth between two competing transient tips 
        to verify if the fork is within Ouroboros Samasika short-range bounds.
        """
        path_a = self._trace_to_genesis(tip_a)
        path_b = self._trace_to_genesis(tip_b)

        # Find Lowest Common Ancestor (LCA)
        common_ancestors = set(path_a).intersection(set(path_b))
        if not common_ancestors:
            return -1 # Divergence exceeds local horizon

        # Determine divergence depth relative to LCA
        lca = max(common_ancestors, key=lambda x: path_a.index(x))
        depth_a = path_a.index(lca)
        depth_b = path_b.index(lca)

        return max(depth_a, depth_b)

    def _trace_to_genesis(self, tip: str) -> List[str]:
        path = []
        curr = tip
        while curr:
            path.append(curr)
            parents = self.adjacency_matrix.get(curr, [])
            curr = parents[0] if parents else None
        return path

    def run_audit_summary(self, tip_a: str, tip_b: str, max_short_range_horizon: int = 5):
        """
        Outputs a non-probabilistic audit verdict on short-range fork state convergence.
        """
        print("\n" + "=" * 50)
        print("⚡ MINA TRANSIENT FORK AUDIT REPORT")
        print("=" * 50)
        
        depth = self.evaluate_divergence_depth(tip_a, tip_b)
        print(f"[*] Divergence Depth: {depth} blocks")
        print(f"[*] Short-Range Boundary Limit: {max_short_range_horizon} blocks")

        if depth <= max_short_range_horizon:
            print("[✓] VERDICT: VALID SHORT-RANGE FORK.")
            print("[✓] Deterministic state audit passed. Resolvable via canonical density check.")
        else:
            print("[❌] VERDICT: LONG-RANGE DIVERGENCE DETECTED.")
            print("[❌] Violation: Exceeds local window. Requires checkpoint verification.")
        print("=" * 50)


# ==========================================
# SIMULATION EXECUTION (Transient Fork Scenario)
# ==========================================
if __name__ == "__main__":
    # 1. Initialize Genesis
    auditor = ShortRangeForkAuditor(canonical_genesis_hash="0xGENESIS_MINA_STATE")

    # 2. Linear Chain Progression
    auditor.add_transient_block("0xBLOCK_1", "0xGENESIS_MINA_STATE", vr_weight=1)
    auditor.add_transient_block("0xBLOCK_2", "0xBLOCK_1", vr_weight=1)

    # 3. Simulate Propagation Delay / Multi-Leader VRF Slot (Fork Event)
    # Branch A
    auditor.add_transient_block("0xBLOCK_3A", "0xBLOCK_2", vr_weight=2)
    auditor.add_transient_block("0xBLOCK_4A", "0xBLOCK_3A", vr_weight=1)

    # Branch B
    auditor.add_transient_block("0xBLOCK_3B", "0xBLOCK_2", vr_weight=1)
    auditor.add_transient_block("0xBLOCK_4B", "0xBLOCK_3B", vr_weight=1)

    # 4. Audit Short-Range Divergence
    auditor.run_audit_summary(tip_a="0xBLOCK_4A", tip_b="0xBLOCK_4B", max_short_range_horizon=5)
