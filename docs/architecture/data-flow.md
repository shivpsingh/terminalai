# Data Flow

1. CLI receives request
2. Orchestrator creates run + plan
3. Context compiler builds bundle
4. Agent chooses tools/model calls
5. Policy checks each tool call
6. Tool runtime executes + records structured results
7. Verifier checks outcomes
8. Checkpoint and completion persisted
