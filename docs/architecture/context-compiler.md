# Context Compiler

Context is intentionally assembled to reduce token waste.

Inputs:
- user request
- project instructions
- session/repo memory
- selected files
- prior summaries
- recent tool outputs

Budgeting uses an approximate token estimate (`len(text)//4`) in MVP.
