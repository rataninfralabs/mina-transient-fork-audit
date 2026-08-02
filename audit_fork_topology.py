"""
RCR LABS — MINA TRANSIENT FORK TOPOLOGY AUDITOR
Author: Amardeep Singh (Architect) + Aarya (Sentinel)
Description: Graph-theory verification model for auditing transient sequence
divergences in asynchronous network latency windows prior to Ouroboros Samasika settlement.
"""

import networkx as nx

class ForkTopologyAuditor:
    def __init__(self, canonical_head: str):
        self.graph = nx.DiGraph()
        self.canonical_head = canonical_head
        self.graph.add_node(canonical_head, weight=1.0, canonical=True)

    def register_block(self, block_id: str, parent_id: str, latency_ms: float, weight: float):
        """Registers a proposed block into the transient fork tree."""
        if parent_id not in self.graph:
            raise ValueError(f"Parent block {parent_id} missing from topological graph.")
        
        is_canonical = (parent_id == self.canonical_head and latency_ms < 200)
        self.graph.add_node(block_id, weight=weight, latency=latency_ms, canonical=is_canonical)
        self.graph.add_edge(parent_id, block_id)

    def calculate_divergence_depth(self, tip_a: str, tip_b: str) -> int:
        """Calculates structural divergence depth between two competing block tips."""
        try:
            lca = nx.lowest_common_ancestor(self.graph, tip_a, tip_b)
            path_a = nx.shortest_path_length(self.graph, lca, tip_a)
            path_b = nx.shortest_path_length(self.graph, lca, tip_b)
            return max(path_a, path_b)
        except (nx.NetworkXError, nx.NodeNotFound):
            return -1

    def audit_summary(self):
        """Prints high-integrity audit report of active fork tree."""
        print("=== RCR LABS FORK TOPOLOGY AUDIT REPORT ===")
        print(f"Total Nodes Processed: {self.graph.number_of_nodes()}")
        print(f"Total Edges (Dependencies): {self.graph.number_of_edges()}")
        for node, data in self.graph.nodes(data=True):
            status = "CANONICAL" if data.get("canonical") else "TRANSIENT_FORK"
            print(f" -> Block: {node} | Status: {status} | Latency: {data.get('latency', 0)}ms")

if __name__ == "__main__":
    # Test Verification Simulation
    auditor = ForkTopologyAuditor(canonical_head="GENESIS_BLOCK_0")
    auditor.register_block("BLOCK_1A", "GENESIS_BLOCK_0", latency_ms=120, weight=10.5)
    auditor.register_block("BLOCK_1B_FORK", "GENESIS_BLOCK_0", latency_ms=450, weight=10.2)
    auditor.register_block("BLOCK_2A", "BLOCK_1A", latency_ms=95, weight=21.0)
    
    auditor.audit_summary()
    depth = auditor.calculate_divergence_depth("BLOCK_2A", "BLOCK_1B_FORK")
    print(f"Structural Divergence Depth: {depth} blocks.")
