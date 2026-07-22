import { Field, ZkProgram, Struct, Bool } from 'o1js';

// Struct representing a short-range block header hash transition
export class BlockState extends Struct({
  slotNumber: Field,
  stateHash: Field,
  parentHash: Field,
}) {}

// ZkProgram that verifies a valid non-divergent transition between two fork blocks
export const ForkAuditorCircuit = ZkProgram({
  name: 'fork-auditor-circuit',
  publicInput: BlockState,
  publicOutput: Bool,

  methods: {
    verifyStep: {
      privateInputs: [BlockState],

      async main(parentState: BlockState, currentState: BlockState) {
        // 1. Check parent link integrity
        currentState.parentHash.assertEquals(parentState.stateHash);

        // 2. Ensure slot progression is strictly increasing
        currentState.slotNumber.assertGreaterThan(parentState.slotNumber);

        return {
          publicOutput: Bool(true),
        };
      },
    },
  },
});
