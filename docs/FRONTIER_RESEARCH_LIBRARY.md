# GlacierEQ Agentic PhD — Frontier Research and Technique Library

Updated: 2026-11-13 UTC. New source-check status labels carry the 2026-11-12 Honolulu local review date (2026-11-13 UTC). Source of truth: [machine-readable research index](../resources/research/frontier_sources.json). **52 curated links across 8 domains**; verified reading of the source is not equivalent to experimentally mastering or deploying its techniques.

## Research method and evidence hierarchy

1. Read the primary paper, official course, protocol or owning developer documentation; record date and exact artifact.
2. Write the mathematical or design hypothesis, failure mode, data provenance, competing baseline and falsifiable success criterion.
3. Reproduce a minimal result using public code/datasets where available; record environment, parameters, seed, trace and cost.
4. Perform adversarial and out-of-distribution tests; measure source-grounded correctness, tool reliability, context application, privacy and native provider effects.
5. Route verified gains through the **existing** `GlacierEQ/spiral-engine` (`SpiralEngine.run_mission` plus its controller and journal); keep an immutable receipt chain. Quality score never substitutes for real terminal outcomes.
6. Retain prior verified capabilities/facts and compare the full mission's intent; repair local regressions without erasing history. Proposed labs are **not completed experiments**.

## Doctoral-domain library

### Foundations

- **[F01] [Attention Is All You Need](https://arxiv.org/abs/1706.03762)** (paper; canonical url requires live recheck).
  - **Technique:** Transformer attention and representation geometry.
  - **Experiment:** Derive scaled dot-product attention and test token-position invariance.
- **[F02] [Stanford CS229: Machine Learning](https://cs229.stanford.edu/)** (course; canonical url requires live recheck).
  - **Technique:** Probability, generalization, optimization.
  - **Experiment:** Implement a calibration baseline and out-of-distribution split.
- **[F03] [Berkeley CS285: Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/)** (course; canonical url requires live recheck).
  - **Technique:** MDPs, policy optimization, offline evaluation.
  - **Experiment:** Model the Spiral decision loop as a constrained policy.
- **[F04] [Sutton and Barto: Reinforcement Learning](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)** (textbook; canonical url requires live recheck).
  - **Technique:** Bellman equations, control, credit assignment.
  - **Experiment:** Derive value functions for near/mid/far-horizon impacts.
- **[F05] [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)** (paper; canonical url requires live recheck).
  - **Technique:** Preference optimization against reference policies.
  - **Experiment:** Compare pairwise route preferences without conflating reward and outcomes.

### Agent architectures

- **[A01] [ReAct](https://arxiv.org/abs/2210.03629)** (paper; public source checked 2026-11-05).
  - **Technique:** Interleave reasoning, tool action and observations.
  - **Experiment:** Implement an act-observe-recover tool loop with failure injection.
- **[A02] [Reflexion](https://arxiv.org/abs/2303.11366)** (paper; public source checked 2026-11-05).
  - **Technique:** Feedback-driven episodic self-correction.
  - **Experiment:** Record one verified failure and test whether the next run avoids it.
- **[A03] [Tree of Thoughts](https://arxiv.org/abs/2305.10601)** (paper; public source checked 2026-11-05).
  - **Technique:** Search and evaluate alternative plans.
  - **Experiment:** Compare best-first, beam search and bounded backtracking.
- **[A04] [Self-Refine](https://arxiv.org/abs/2303.17651)** (paper; public source checked 2026-11-05).
  - **Technique:** Iterative criticism and revision.
  - **Experiment:** Run generator-critic-reviser ablation with external grading.
- **[A05] [Toolformer](https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/)** (research; public source checked 2026-11-05).
  - **Technique:** When to select external tools and use results.
  - **Experiment:** Create missing-tool and noisy-tool selection tests.
- **[A06] [Building effective agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents)** (engineering; public source checked 2026-11-05).
  - **Technique:** Compositional workflow versus autonomous agent decisions.
  - **Experiment:** Implement simplest successful baseline before orchestration.
- **[A07] [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)** (course; public source checked 2026-11-05).
  - **Technique:** Practical tool-using agents and benchmarks.
  - **Experiment:** Complete a tested ReAct-style project with explicit evaluation.
- **[A08] [OpenAI Agents SDK and sandboxed harness](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)** (engineering; public source checked 2026-11-05).
  - **Technique:** Sandboxed execution, tools, file and terminal interaction.
  - **Experiment:** Prove task outcome using workspace and environment readback.
- **[A09] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)** (paper; Nature 2025, revised 2026-01-04; public source checked 2026-11-05).
  - **Technique:** Reinforcement learning can elicit reasoning strategies such as reflection and verification on verifiable tasks.
  - **Experiment:** Compare an RL-reasoning baseline with supervised reasoning on held-out verifiable problems; measure accuracy, cost, and calibration.
- **[A10] [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296)** (paper; v3 2026-04-08; public source checked 2026-11-05).
  - **Technique:** Predict architecture/task alignment using capability, sequential dependency, tool density, and coordination.
  - **Experiment:** Compare one-agent, parallel, and task-coordinated routes on matched held-out tasks and equalized budgets.

### Memory and context

- **[M01] [MemGPT](https://arxiv.org/abs/2310.08560)** (paper; public source checked 2026-11-05).
  - **Technique:** Tiered virtual memory with explicit retrieval.
  - **Experiment:** Compare bounded working context to indexed durable memory.
- **[M02] [LongMemEval](https://arxiv.org/abs/2410.10813)** (benchmark; public source checked 2026-11-05).
  - **Technique:** Multi-session retrieval, update, time and abstention.
  - **Experiment:** Evaluate memory update versus stale fact and applied-claim coverage.
- **[M03] [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/)** (paper; public source checked 2026-11-05).
  - **Technique:** Position-sensitive evidence access in long contexts.
  - **Experiment:** Test relevant fact at beginning, middle and end.
- **[M04] [Effective context engineering (Anthropic)](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)** (engineering; public source checked 2026-11-05).
  - **Technique:** High-signal context and tool schemas.
  - **Experiment:** Benchmark compact source pointers against full-context flooding.
- **[M05] [GraphRAG research](https://arxiv.org/abs/2404.16130)** (paper; public source checked 2026-11-05).
  - **Technique:** Global graph-grounded corpus synthesis.
  - **Experiment:** Compare lexical retrieval, graph summarization and citation fidelity.
- **[M06] [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401)** (paper; canonical url requires live recheck).
  - **Technique:** Parametric generation plus external knowledge.
  - **Experiment:** Measure grounded citation accuracy and answer abstention.

### Tools and runtime

- **[T01] [Writing effective tools for agents (Anthropic)](https://www.anthropic.com/research/writing-tools-for-agents)** (engineering; public source checked 2026-11-05).
  - **Technique:** Clear tools, minimal overlap and trace-based evals.
  - **Experiment:** Reduce ambiguous tool signatures; measure tool-selection errors.
- **[T02] [Advanced tool use (Anthropic)](https://www.anthropic.com/research/advanced-tool-use)** (engineering; public source checked 2026-11-05).
  - **Technique:** Tool search and programmatic orchestration.
  - **Experiment:** Benchmark discovery latency and invocation precision.
- **[T03] [MCP specification release 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/)** (standard; public source checked 2026-11-05).
  - **Technique:** Stateless core and authorization hardening.
  - **Experiment:** Test current protocol compatibility and rejected unauthorized requests.
- **[T04] [Model Context Protocol specification](https://modelcontextprotocol.io/specification)** (standard; public source checked 2026-11-05).
  - **Technique:** Interoperability, transport, authorization and security.
  - **Experiment:** Check tools/list and tools/call version handling and auth boundaries.
- **[T05] [LangGraph architecture](https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph)** (documentation; public source checked 2026-11-05).
  - **Technique:** Checkpoints, durable execution and human controls.
  - **Experiment:** Crash at each boundary, resume without duplicating native effects.
- **[T06] [Deep Agents overview](https://docs.langchain.com/oss/javascript/deepagents/overview)** (documentation; public source checked 2026-11-05).
  - **Technique:** Context offloading, delegation and secure sandbox tools.
  - **Experiment:** Measure recovery after interrupted subagent/task execution.
- **[T07] [OpenAI developer agent resources](https://developers.openai.com/learn/agents)** (documentation; public source checked 2026-11-05).
  - **Technique:** SDKs, tools, tracing and sandbox workflows.
  - **Experiment:** Compare route success and readback for one real tool task.

- **[T08] [MCP authorization security considerations (2026-07-28)](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/authorization/security-considerations.mdx)** (standard; public source checked 2026-11-12).
  - **Technique:** Token audience validation and prevention of token passthrough across tools.
  - **Experiment:** Reject wrong-audience tokens and token passthrough; verify an unauthorized call changes no provider state.

- **[T09] [OpenAI prompt engineering: code-managed prompts and evaluation](https://developers.openai.com/api/docs/guides/prompt-engineering)** (documentation; public source checked 2026-11-12).
  - **Technique:** Version prompts with typed inputs, representative fixtures and eval-gated rollout.
  - **Experiment:** Ablate a versioned instruction change on held-out tasks; compare intent fidelity, regressions and measured tool outcomes.

### Evaluation

- **[E01] [SWE-bench](https://arxiv.org/abs/2310.06770)** (benchmark; public source checked 2026-11-05).
  - **Technique:** Real repository issue resolution.
  - **Experiment:** Measure accepted patch + regression suite rather than code volume.
- **[E02] [AgentBench](https://arxiv.org/abs/2308.03688)** (benchmark; public source checked 2026-11-05).
  - **Technique:** Interactive agent environment evaluation.
  - **Experiment:** Collect episode success, recovery and tool-use failures.
- **[E03] [GAIA benchmark](https://arxiv.org/abs/2311.12983)** (benchmark; canonical url requires live recheck).
  - **Technique:** Multi-step generalist assistant evaluation.
  - **Experiment:** Create multi-hop tool tasks with independently checked answers.
- **[E04] [Long-horizon agent evaluation survey](https://arxiv.org/abs/2503.16416)** (survey; public source checked 2026-11-05).
  - **Technique:** Benchmarks across planning, memory, safety and robustness.
  - **Experiment:** Build multi-axis scorecard with held-out tasks and costs.
- **[E05] [OpenAI agent improvement loop](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop)** (engineering; public source checked 2026-11-05).
  - **Technique:** Traces to evals to iterative harness improvements.
  - **Experiment:** Turn one observed failure into a replayable regression test.
- **[E06] [OpenAI evals cookbook](https://developers.openai.com/cookbook/topic/evals)** (documentation; public source checked 2026-11-05).
  - **Technique:** Evaluation design and trace-backed experiments.
  - **Experiment:** Record pass-k, latency, cost, error class and outcome receipt.
- **[E07] [Chain-of-Verification](https://aclanthology.org/2024.findings-acl.212/)** (paper; public source checked 2026-11-05).
  - **Technique:** Independent fact-check questions before response.
  - **Experiment:** Run evidence checks on disconfirming as well as favorable claims.
- **[E08] [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499)** (paper; NeurIPS 2025, v4 2026-07-10; public source checked 2026-11-05).
  - **Technique:** Estimate a task-completion time horizon from expert-timed tasks and AI success rates.
  - **Experiment:** Measure completion probability over a declared task mix and duration range; report external-validity limits and failures.

- **[E09] [tau-bench: Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045)** (benchmark; public source checked 2026-11-12).
  - **Technique:** Evaluate tool agents against end-state database goals and repeated-run pass^k reliability.
  - **Experiment:** Replay matched provider-state tasks five times; compare intended and actual end state, failure classes and repeatability.

- **[E10] [tau2-bench: Evaluating Conversational Agents in a Dual-Control Environment](https://proceedings.mlr.press/v306/barres26a.html)** (benchmark; public source checked 2026-11-12).
  - **Technique:** Evaluate coordination where user and agent each control tools in a shared environment.
  - **Experiment:** Compare agent-only against dual-control handoffs, keeping the same terminal goal and measuring missing or duplicated user actions.

- **[E11] [METR Task-Completion Time Horizons, methodology 1.1](https://metr.org/time-horizons/)** (research; public source checked 2026-11-12).
  - **Technique:** Measure agent completion probability across task durations instead of extrapolating from simple demos.
  - **Experiment:** Use expert-timed held-out tasks to compare success at multiple horizons with confidence intervals and explicit task-mix limits.

### Safety and governance

- **[S01] [AgentDojo prompt-injection benchmark](https://arxiv.org/abs/2406.13352)** (benchmark; public source checked 2026-11-05).
  - **Technique:** Adversarial tool-output injection and agent defense.
  - **Experiment:** Test malicious instructions nested in retrieved documents.
- **[S02] [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)** (standard; canonical url requires live recheck).
  - **Technique:** Governance, mapping, measurement, mitigation.
  - **Experiment:** Define audit trail, privacy, authority and rollback risk checks.
- **[S03] [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)** (standard; canonical url requires live recheck).
  - **Technique:** Prompt injection, excessive agency and insecure outputs.
  - **Experiment:** Model least-privilege and provider-native readback negative tests.
- **[S04] [Constitutional AI](https://arxiv.org/abs/2212.08073)** (paper; canonical url requires live recheck).
  - **Technique:** Preference and safety-driven model alignment.
  - **Experiment:** Test self-critique limits against external validation.

- **[S05] [OpenAI: Designing AI agents to resist prompt injection](https://openai.com/index/designing-agents-to-resist-prompt-injection/)** (engineering; public source checked 2026-11-12).
  - **Technique:** Treat external content as untrusted and constrain the consequences of socially engineered instructions.
  - **Experiment:** Insert malicious directions into a retrieved email or document; check user-authorized target and zero unauthorized sends or writes.

### Research practice

- **[R01] [Stanford CS224N](https://web.stanford.edu/class/cs224n/)** (course; canonical url requires live recheck).
  - **Technique:** Neural language representations, transformer foundations.
  - **Experiment:** Reproduce an NLP result with a clean split and ablation.
- **[R02] [Papers with Code](https://paperswithcode.com/)** (resource; canonical url requires live recheck).
  - **Technique:** Find implementations, datasets and benchmark protocols.
  - **Experiment:** Replicate one paper baseline from reproducible code.
- **[R03] [Hugging Face Papers](https://huggingface.co/papers)** (resource; canonical url requires live recheck).
  - **Technique:** Research discovery and implementation ecosystem.
  - **Experiment:** Track dated claims, code, evaluation and deployment maturity.
- **[R04] [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)** (research report; public source checked 2026-11-05).
  - **Technique:** Evolutionary code search steered by one or more evaluators.
  - **Experiment:** Compare evaluator-guided search with random and human baselines; require independent correctness checks and held-out objective tests.
- **[R05] [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292)** (paper; v3; public source checked 2026-11-05).
  - **Technique:** Automate idea generation, implementation, experimentation, writing, and review as a research pipeline.
  - **Experiment:** Blindly evaluate generated findings against human-reviewed baselines; independently reproduce results and audit novelty.

### Embodied AI

- **[B01] [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)** (technical report; public source checked 2026-11-05).
  - **Technique:** Vision-language-action and embodied-reasoning models for robot perception and control.
  - **Experiment:** Evaluate task success and safe recovery on held-out objects, environments, and embodiments before any physical deployment.

## Compounding study sequence: theory → implementation → adversarial proof

- **Cycle A, principled agent:** Implement ReAct, Reflexion, Tree of Thoughts and a deterministic no-agent baseline; compare task success, tokens, runtime, and recovery after tool failure.
- **Cycle B, memory and knowledge:** Run LongMemEval-style update and temporal checks; add middle-position retrieval, counterfactual supersession and mandatory exact source application; compare indexed memory versus raw context.
- **Cycle C, production tool use:** Build MCP/SDK adapters with typed authorization and idempotency; inject timeouts, partial effects and prompt injections; verify provider-native state before reattempting.
- **Cycle D, real research competence:** Implement one selected paper's benchmark, ablating each claimed contribution, with provenance and confidence intervals; separate research reproduction from global capability claims.
- **Cycle E, Spiral promotion:** Feed independently observed before/after states, source readbacks and regressions into the existing Spiral controller and mission improvement contract; verify replay, durable journal, HMAC when an independent secret is available, and promotion readiness.

## Research scoring, not vanity scoring

Report real task-success rate and repeatability (pass@k), artifact/readback integrity, verified memory application, robustness under injection/partial failures, privacy and authority adherence, and total cost. Repository presence, number of links, passing toy tests and headline score **do not** prove doctoral mastery. Terminal outcome must be separately grounded in a provider-readback or reproducible scientific result.

## Native project integration

Existing project phases: `phase1-foundations/`, `phase2-core-ml/`, `phase3-agentic-ai/`, `phase4-research/`, `phase5-agentic-upgrade/`. Existing paper tracker remains intact. New index has stable IDs for future ingestion and can be queried using `scripts/validate_research_library.py`. Real Spiral ownership stays in private `GlacierEQ/spiral-engine`, not copied or replaced here.
