---
name: transfer-context
description: Transfer context by packaging all key information to seamlessly seed a new thread.
disable-model-invocation: true
version: 1.0.0
---

Package all key information from this conversation into a single, comprehensive text block that I can copy and paste to seamlessly continue work in a new thread. The new chat will rely entirely on this block to resume execution.

## Steps
1. Scan the full conversation history, not just the last few turns.
2. Draft the text block with exactly these 5 sections, in order:
   1. **Goals and Decisions:** current objectives, tasks, and the reasoning behind key decisions made.
   2. **State of Work:** exact progress update on what is finished, in-progress, and not-started.
   3. **Inventory:** every relevant file path, link, entity name, figure, or critical detail.
   4. **Next Steps:** exactly where we left off and the immediate next actions.
   5. **Unwritten Context:** discovered gotchas, environment quirks, or exhaustive granular details required to execute the next steps.
3. Present the block in a single fenced code block so it is one clean copy-paste unit.

## Completion criterion
Someone with zero memory of this conversation could paste the block into a new thread and immediately continue the next step without asking a clarifying question. If any section would leave them guessing, go back and add the missing detail before presenting the block.
