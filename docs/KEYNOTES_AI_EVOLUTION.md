# Keynote briefs: the evolution of AI

**Research cut:** 2026-11-05. These briefs synthesize selected primary research and official technical reports; they are not an exhaustive survey. Claims are bounded by the tasks and systems each source evaluated.

## Central thesis

AI progress is shifting from a model-only story to **evidence-bearing capability systems**: models allocate inference-time computation, use tools, retrieve and update state, collaborate when work is decomposable, and act through increasingly multimodal interfaces. The key engineering question is no longer simply “How smart is the model?” but “Which outcomes can this system reliably achieve, at what cost and risk, under what conditions—and how do we know?”

This is a synthesis, not a validated equation. A useful mental model is:

> **Capability in practice = model × context/data × tools × runtime/control × evaluation**

A weak term can dominate. A powerful model with stale context, an ambiguous tool, a poor recovery loop, or an ungrounded evaluator can still fail the user's actual objective.

## What is changing

### 1. Reasoning is becoming an allocated resource

The DeepSeek-R1 report is a prominent example of reinforcement learning eliciting longer reasoning and behaviors such as reflection and verification on verifiable math, coding, and STEM tasks. It distinguishes R1-Zero, which uses RL without initial supervised fine-tuning, from R1's multi-stage pipeline, which includes cold-start data; it also reports distilling reasoning behavior into smaller models. The important shift is that inference and training can spend compute on search and feedback, not just produce the first fluent answer.

**Limit:** self-reflection is not a truth oracle. Results on verifiable tasks do not establish equally reliable reasoning in open-ended, ambiguous, or socially consequential settings. Check the work against external evidence.

### 2. Agents are systems, not a prompt pattern

An agent is a model embedded in an action/observation loop with tools, state, permissions, and a stopping condition. Each extra action creates opportunities for recovery and for error propagation. Long-horizon ability therefore depends on reliability, environment feedback, and recovery—not just a strong single-step answer.

METR's 2025 time-horizon study illustrates a move from static question accuracy toward tasks timed against human experts. Its reported roughly 50-minute horizon for Claude 3.7 Sonnet was a dated result on a particular task mix, not a statement about today's frontier or a universal measure of work. The study itself discusses external-validity limits. The durable lesson is methodological: measure real task completion, including failures and task duration, rather than extrapolating from a headline benchmark alone.

### 3. More agents is not a scaling law

The controlled *Towards a Science of Scaling Agent Systems* study evaluates 260 configurations across six benchmarks, five architectures, and three model families. In its benchmark suite, architecture-relative changes ranged from +80.8% on decomposable financial reasoning to -70.0% on sequential planning. It reports diminishing coordination returns at stronger single-agent baselines, overhead on tool-heavy tasks, and greater error propagation without centralized verification.

**Implication:** preserve a polycentric peer mesh as the capability substrate, but choose topology per task. Keep coherent sequential work together; fan out independent work; use temporary coordination and independent verification where dependencies or risk justify them. Verification is a function, not a permanent authority.

**Limit:** the paper's predictive model has moderate cross-validated explanatory power (reported R²=0.373 overall); its results motivate conditional design, not universal guarantees.

### 4. Memory is selective state, not a larger prompt

Persistent systems need to retrieve the right fact, detect that it has changed, preserve its provenance, and avoid applying it outside its scope. More stored text does not ensure better recall. A useful memory design separates transient task context from durable user decisions and verified reusable lessons, and supports correction and supersession.

**Implication:** evaluate memory on retrieval, temporal updates, contradiction handling, and actual application—not volume written or number of summaries.

### 5. AI for science is becoming a search-and-evaluate loop

AlphaEvolve describes an evolutionary coding agent that proposes algorithm changes and uses one or more evaluators to select improvements. Its reported applications include computational infrastructure and algorithmic discovery. *The AI Scientist* explores an end-to-end loop spanning idea generation, implementation, experiments, paper writing, and automated review.

The most reusable principle is **generate candidates cheaply; let independent, task-appropriate tests decide what survives**. A benchmark, proof checker, simulator, or experiment can provide a stronger signal than a model's persuasive explanation.

**Limit:** a system that writes a paper or passes its own reviewer has not established scientific truth. Reproduction, sound measurement, novelty checks, human scrutiny, and independent validation remain essential.

### 6. AI is crossing from digital interfaces into physical action

The Gemini Robotics report describes vision-language-action systems that map multimodal input and instructions into robot actions, plus an embodied-reasoning model for spatial and temporal tasks. This illustrates an important expansion: capability must be grounded in observations and feedback from the world, where actions have physical consequences.

**Implication:** test generalization across objects, environments, embodiments, and disturbances; require safe limits and recovery. A fluent plan is not evidence that an action is safe.

### 7. Evaluation and safety are part of capability

Tool access, longer context, and autonomy make an agent more useful only if it can respect authority boundaries and handle untrusted inputs. Protocols such as [MCP](https://modelcontextprotocol.io/specification) reduce integration friction for tools and context; they do not establish user intent, authorization, or factual correctness. Evaluate exact outcomes, permission handling, robustness, recovery, latency, cost, and user-intent fidelity. Treat benchmark scores as bounded measurements, not proxies for universal competence.

## Keynote I — “The agent is the system”

**Audience:** AI builders, technical leaders, researchers. **Length:** 15–20 minutes.

1. **Opening:** A model can be brilliant and still fail because it used the wrong tool, forgot a correction, or stopped at a success-shaped response.
2. **The evolution:** pretraining builds broad priors; inference-time reasoning spends computation; tools connect the model to evidence and action; memory carries selected state; evaluation governs what we can claim.
3. **The pivotal data point:** agent architectures can help one task class and sharply harm another. Show the +80.8% to -70.0% range from the controlled scaling study, with its benchmark caveat.
4. **The new design unit:** a mission-oriented capability loop—whole-system context, possibility expansion, action, observation, recovery, integration, and external verification.
5. **The strategic choice:** use parallel agents for independent work, not as a ritual; retain a coherent single-agent path for sequential tasks; use task-local coordinators rather than universal hubs.
6. **Close:** “The next leap is not autonomy for its own sake or restraint for its own sake. It is a system with enough context, effort, reach, and feedback to realize the user's purpose.”

## Keynote II — “How an AI gets better without pretending to self-improve”

**Audience:** research teams, agent operators, product and safety teams. **Length:** 15–20 minutes.

1. Separate **model learning** (changed parameters through training) from **system improvement** (changed tools, instructions, data, memory, or runtime).
2. Start with a real failure; define a reproducible task set and a baseline.
3. Make one change, then evaluate on held-out examples with independent outcome checks.
4. Measure side effects: regressions, user corrections, latency, cost, permissions, and recovery—not only success rate.
5. Preserve source, version, uncertainty, and an undo path; promote only domain-specific repeatable gains.
6. Close: “An AI system earns the word ‘better’ by doing more of the user's intended work reliably—not by describing itself as smarter.”

## Research questions worth pursuing

1. **Topology selection:** Can task features—sequential dependency, tool density, and model baseline—predict when collaboration is worth its coordination cost?
2. **Reliable long-horizon work:** Which recovery mechanisms produce actual completion gains on held-out tasks, not merely longer trajectories?
3. **Memory quality:** Can a system update and apply user decisions without stale-memory errors, overgeneralization, or memory flooding?
4. **Scientific discovery:** Which evaluator properties (independence, proof-checkability, noise, and distribution shift) best predict real discovery rather than benchmark overfitting?
5. **Embodied generalization:** What evidence is needed to transfer a successful simulated or laboratory action policy to novel real environments safely?

For each project, preregister a baseline, data/task scope, success criterion, negative controls, cost budget, and failure analysis. Report both positive and null results.

## Primary sources

- DeepSeek-AI, [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) (2025; revised 2026-01-04; *Nature* 2025).
- Kim et al., [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (v3, 2026-04-08).
- Kwa et al. / METR, [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) (NeurIPS 2025; v4, 2026-07-10).
- Novikov et al., [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131) (2025).
- Lu et al., [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) (2024; v3).
- Gemini Robotics Team, [Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020) (2025).
- Model Context Protocol, [Specification](https://modelcontextprotocol.io/specification) (live standard; check version and authorization model).

## Epistemic boundary

These are synthesis notes from the cited papers, not independent replications. Company-authored system reports may describe selected evaluations; benchmark performance, demonstrations, and model-generated reviews are not interchangeable with broad real-world validation. Check each paper's version and methods before reusing a numerical claim.
