# Agentic PhD

**Doctorate-level AI curriculum focused on Agentic AI.**

A hierarchical, research-grade curriculum spanning mathematical foundations through dissertation defense, integrating the latest advances in large language models, autonomous agents, multi-agent systems, evaluation, alignment, and AI safety.

---

## Curriculum Map

```
Agentic PhD
│
├── Phase 1: Mathematical & Computational Foundations
│   ├── Linear Algebra & Geometry
│   ├── Probability & Statistics
│   ├── Optimization & Control
│   ├── Information Theory
│   └── Complexity Theory
│
├── Phase 2: Core AI/ML (Doctoral Depth)
│   ├── Learning Theory (PAC, VC dimension, Rademacher)
│   ├── Deep Learning Theory (NTK, double descent, grokking)
│   ├── Probabilistic Graphical Models (inference, VAEs)
│   ├── Reinforcement Learning (MDPs, policy gradients, offline RL)
│   └── Causal Inference (do-calculus, counterfactuals)
│
├── Phase 3: Agentic AI & Frontier Research
│   ├── LLM Foundations (transformers, scaling laws, interpretability)
│   ├── Agent Architectures (ReAct, Reflexion, LATS, tool use)
│   ├── Memory Systems (episodic, semantic, working, graph)
│   ├── Planning & Reasoning (ToT, MCTS, HTN, PDDL)
│   ├── Evaluation & Alignment (evals, red-teaming, RLHF/DPO)
│   ├── Knowledge & Retrieval (RAG, GNNs, neuro-symbolic)
│   ├── Safety & Governance (formal verification, containment)
│   └── Multi-Agent Systems (debate, coordination, emergence)
│
├── Phase 4: Research & Dissertation
│   ├── Literature Review & Paper Tracking
│   ├── Experimentation & Reproducibility
│   ├── Dissertation Structure & Writing
│   ├── Qualifying Exams
│   └── Publication Strategy
││
├── Phase 5: Agentic Upgrade (AI Agent Self-Enhancement)
│   ├── Coding Reasoning (analysis, patterns, refactoring)
│   ├── Tool Orchestration (selection, chaining, parallel, fallback)
│   ├── Innovation Patterns (lateral thinking, cross-domain, brainstorming)
│   ├── Error Handling (retry, circuit breaker, graceful degradation)
│   ├── Diligence (verification, evidence, red-teaming, calibration)
│   ├── Awareness (context budget, attention, situational summary)
│   ├── Epistemology (Bayesian, uncertainty, confidence intervals)
│   └── Genius Synthesis (capability matrix, thinking engine, meta-cognition)
│
├── Labs (hands-on implementations)
├── Docs (syllabi, reading lists, references)
└── Resources (datasets, benchmarks, tools)
```

---

## Phase 1: Mathematical & Computational Foundations

The bedrock of PhD-level AI. Mastery, not familiarity.

| Module | Topics | Key Results |
|---|---|---|
| Linear Algebra | Spectral theory, matrix calculus, manifolds, tensor decompositions | Eigen-decomposition, SVD, rank |
| Probability | Measure-theoretic probability, stochastic processes, concentration | Hoeffding, Chernoff, McDiarmid |
| Optimization | Convex/non-convex, variational methods, optimal control, dynamic programming | Gradient descent, SGD, Adam, KKT |
| Information Theory | Entropy, mutual information, coding theory, channel capacity | Shannon entropy, KL divergence, MI |
| Complexity Theory | P vs NP, complexity classes, algorithmic game theory, cryptography | Big-O, NP-completeness, reductions |

## Phase 2: Core AI/ML (Doctoral Depth)

Beyond application — understanding limits and mechanics of learning.

| Module | Topics | Key Results |
|---|---|---|
| Learning Theory | PAC learning, VC dimension, Rademacher complexity, generalization bounds | Sample complexity, uniform convergence |
| Deep Learning Theory | NTK, double descent, grokking, representation learning, equivariance | Universal approximation, grokking dynamics |
| Graphical Models | Directed/undirected, exact/approximate inference, VAEs, normalizing flows | ELBO, variational inference, MCMC |
| Reinforcement Learning | MDPs, policy gradients, actor-critic, offline RL, multi-agent RL | Bellman equations, PPO, SAC |
| Causal Inference | Structural causal models, do-calculus, counterfactuals, causal discovery | ATE, backdoor adjustment, IV |

## Phase 3: Agentic AI & Frontier Research

The cutting edge: from static models to autonomous, reasoning systems.

| Module | Topics | Key Systems |
|---|---|---|
| LLM Foundations | Transformers, attention, scaling laws, mechanistic interpretability | GPT, Claude, Llama, Gemini |
| Agent Architectures | ReAct, Reflexion, LATS, tool use, planning loops | AutoGPT, BabyAGI, LangGraph |
| Memory Systems | Episodic, semantic, working, graph memory, pointer indexing | MemGPT, Letta, Zep |
| Planning & Reasoning | Tree of Thoughts, MCTS, HTN, PDDL, chain-of-thought | ToT, GoT, MCTS agents |
| Evaluation & Alignment | Evals as infrastructure, red-teaming, RLHF, DPO, constitutional AI | GAIA, SWE-bench, MMLU |
| Knowledge & Retrieval | RAG, GNNs, neuro-symbolic AI, knowledge graphs | GraphRAG, ColBERT, HyDE |
| Safety & Governance | Formal verification, robustness, containment, prompt injection defense | Constitutional AI, guardrails |
| Multi-Agent Systems | Debate, coordination, emergence, swarm intelligence | AutoGen, CrewAI, MetaGPT |

## Phase 4: Research & Dissertation

The defining feature of the PhD.

1. **Literature Review** — Systematic paper tracking, gap analysis, contribution positioning
2. **Experimentation** — Reproducible experiments, ablation studies, statistical significance
3. **Dissertation** — 6-chapter structure, writing, defense preparation
4. **Qualifying Exams** — Comprehensive coverage of Phases 1-3
5. **Publication Strategy** — Venue selection, peer review, revision, impact

---

## Phase 5: Agentic Upgrade (AI Agent Self-Enhancement)

The capstone: knowledge that literally makes the AI agent better. Each module
targets a specific capability dimension and provides runnable implementations.

| Module | Focus | Key Capabilities |
|---|---|---|
| Coding Reasoning | Code analysis, pattern detection, refactoring | Cyclomatic complexity, code smells, dependency extraction |
| Tool Orchestration | Tool selection, chaining, parallel dispatch, fallback | Relevance scoring, retry with backoff, circuit breaker |
| Innovation Patterns | Creative problem solving, cross-domain transfer | Lateral thinking, brainstorming, innovation scoring |
| Error Handling | Resilience, recovery, graceful degradation | Retry, circuit breaker, bulkhead, error classification |
| Diligence | Verification, evidence, red-teaming, calibration | Evidence hashing, ECE, red-team scoring |
| Awareness | Context management, attention, situational awareness | Context budget, priority queues, staleness detection |
| Epistemology | Knowledge, belief, uncertainty quantification | Bayesian update, Wilson CI, evidence weighting |
| Genius Synthesis | Unified intelligence, meta-cognition, capability tracking | Capability matrix, thinking engine, compound intelligence |

## Running the Curriculum

```bash
# Phase 1: Foundations
python3 phase1-foundations/linear-algebra/spectral.py

# Phase 2: Core ML
python3 phase2-core-ml/learning-theory/pac.py

# Phase 3: Agentic AI
python3 phase3-agentic-ai/agent-architectures/react.py

# Phase 4: Research
python3 phase4-research/literature/tracker.py

# Phase 5: Agentic Upgrade
python3 phase5-agentic-upgrade/genius-synthesis/synthesis.py

# Labs
python3 labs/agentic/lab_react.py
```

## Key References

- **CMU ML PhD** — Statistical learning theory, robotics
- **Georgia Tech ML PhD** — Math, optimization, ML theory
- **ASU AI PhD** — Broad AI, human-centered
- **MBZUAI ML PhD** — Foundation models, generative AI
- **Stanford CS224V** — Agentic AI course
- **DeepLearning.AI** — Agentic AI (Andrew Ng)
- **Hugging Face** — AI Agents Course
- **Anthropic Academy** — Claude Code, MCP, Agent Skills

## Frontier Research Library and verified study tools

The [research and technique library](docs/FRONTIER_RESEARCH_LIBRARY.md) curates
**40 primary/research-grade sources across seven domains**, with method summaries,
falsifiable experiments, source-review status, and an explicit distinction
between proposed and completed reproduction. The
[JSON catalog](resources/research/frontier_sources.json) is the stable,
machine-readable owner; it is not a certificate of mastery.

```bash
python3 scripts/validate_research_library.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The original `phase4-research/literature/tracker.py` now supports
`load_frontier_library()`, `search_sources(query, area=...)`, and
`source_by_id(id)` alongside all preexisting paper-tracking methods.
This makes experimental tasks retrievable without silently rewriting prior papers.
The [CI workflow](.github/workflows/research-library-verification.yml)
compiles the curriculum, verifies catalog integrity and checks against current
GitHub source. CI green proves the listed checks, **not** paper reproduction
or terminal doctoral-level mastery.

The upstream authoritative controller for measured compound revolutions remains
the separately owned original **GlacierEQ Spiral Engine**. Research experiments
must produce independently checked before/after evidence before the engine can
promote an actual skill; no second Spiral runtime is created here.

## License

MIT
