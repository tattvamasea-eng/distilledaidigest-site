# Agent 101 — Concepts Already Used (do not repeat)

Checked against the full run in the repo (#14 onward; #1–13 are Beehiiv-only and not in the repo — only #13 is known: "The Agent Harness"; #20, #30, #40 are Deca editions with no Agent 101). Update this after every new issue.

#13 — The Agent Harness (Beehiiv-only; per project instructions)
#14 — The Evaluation Gate
#15 — The Handoff Protocol
#16 — Persistent State (why always-on agents are architecturally different)
#17 — The Orchestration Layer
#18 — The Context Window as Working Memory
#19 — Model Routing and Fallback
#21 — Human-in-the-Loop Checkpoints
#22 — Agent Observability and Logging
#23 — Agent Permissions and Scoping
#24 — AI Identity and Access Management (AI IAM)
#25 — The Reverse Information Paradox
#26 — Trajectory Monitoring
#27 — Agent Sprawl
#28 — What "Agentic" Actually Means
#29 — Non-Human Identity
#31 — Prompt Injection (why an agent can't fully trust what it reads)
#32 — The Tool Interface Contract (tool/function-calling mechanics)
#33 — The Folder Is the Agent (the project folder as the durable agent boundary)
#34 — The Sandbox (the bounded execution environment; deny-by-default containment vs. trusting refusals)
#35 — The Token Bill (what one agent run costs; tokens re-billed every loop step; caching, context trimming, step budgets, model tiering)
#36 — Planning and Task Decomposition (goal -> ordered subtasks, re-planning, stopping condition; the plan is where purpose becomes conduct)
#37 — Determinism vs. Sampling (why the same agent can act differently on the same task; temperature; assurance is a pass rate over repeated runs; deterministic code around high-stakes steps)
#38 — Agent Memory vs. Retrieval (retrieval = looking up from a source at the moment of need, RAG; memory = records the agent writes and carries across sessions; govern retrieval through the source, treat memory as new records needing an owner, retention and correction)
#39 — Evals vs. Guardrails (evals = offline tests before release scored as a pass rate; guardrails = run-time checks that block or escalate inputs, outputs and actions; you need both and must measure both, including the guardrail's catch rate; adjacent to #14 The Evaluation Gate and #26 Trajectory Monitoring)

Whole areas now saturated — steer clear: identity / credentials / IAM (#24 + #29); observability/monitoring (#22 + #26); trust-boundary/injection (#31); containment/environment (#34 + #23 permissions — adjacent); tool/function-calling mechanics (#32); cost/token economics (#35); planning & task decomposition (#36); determinism/sampling & run-to-run variance (#37); memory vs. retrieval (#38; adjacent to #16 persistent state and #18 context window); evals & guardrails (#14 + #39).

Candidate fresh directions not yet used: long-horizon coherence & why agents drift, multi-agent coordination protocols, agent-to-agent auth (A2A), MCP as an interface standard.

Note on #1–12: these ran on Beehiiv only (pre-repo) and their Agent 101 concepts are not captured here. If full historical de-duplication is needed, reconstruct them from the Beehiiv archive.
