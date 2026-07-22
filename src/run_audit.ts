import { Field, Bool } from 'o1js';
import { ForkAuditorCircuit, BlockState } from './ForkAuditorCircuit.js';

async function main() {
  console.log('=== Mina Transient Fork Auditability Engine ===');
  console.log('Compiling o1js ForkAuditorCircuit...');
  
  const { verificationKey } = await ForkAuditorCircuit.compile();
  console.log('Verification Key Hash generated successfully!');

  // Define two synthetic blocks in a short-range fork window
  const blockA = new BlockState({
    slotNumber: Field(100),
    stateHash: Field(123456789),
    parentHash: Field(0),
  });

  const blockB = new BlockState({
    slotNumber: Field(101),
    stateHash: Field(987654321),
    parentHash: Field(123456789), // Valid parent link
  });

  console.log('Verifying state transition integrity...');
  const proof = await ForkAuditorCircuit.verifyStep(blockA, blockB);
  
  console.log('Proof Verification Result:', proof.publicOutput.toBoolean() ? 'SUCCESS (State Valid)' : 'FAILED');
}

main().catch((err) => {
  console.error('Audit Engine Execution Error:', err);
});
