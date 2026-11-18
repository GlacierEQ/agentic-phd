# Agentic PhD project guidance

This repository is a research curriculum and a set of educational implementations. It does not fine-tune the assistant, alter model weights, or prove that an agent has become more capable merely because a document or script was added.

For research or implementation work:

1. Read [the Agent Operating Playbook](docs/AGENT_OPERATING_PLAYBOOK.md) as an expansive orientation: understand the wider aim and relevant mesh before deciding how small or large a task is.
2. Treat [the research index](resources/research/frontier_sources.json) as the source catalog. Preserve provenance; distinguish established findings, useful hypotheses, proposed experiments, and completed reproductions.
3. Keep the user's objective as direction, not as a ceiling on relevant discovery. Bring in broad context, diverse peers, connectors, and tools when they can reveal important connections or increase capability.
4. For capability claims, compare against a meaningful baseline and test generalization. Report quality, new capability, reliability, regressions, intent fidelity, latency, cost, and uncertainty. A passing test proves the behavior it exercises, not the whole system.
5. Preserve promising ideas and open threads with clear confidence labels. Promote claims to established knowledge only when supported; do not discard exploration merely because it is not yet verified.
6. Strength and intelligence strictly outrank speed: default to `deep` / `xhigh` / frontier (`pro` / `inherit`) execution rather than fast or lightweight model shortcuts; never compress reasoning or skip empirical checks (inherits root `/Users/kcbflux/workspace/AGENTS.md` & `RULES.md` Rule 13).

Use the [AI evolution keynote briefs](docs/KEYNOTES_AI_EVOLUTION.md) for synthesis and presentation; do not treat a keynote as a substitute for reading the cited paper.

## Task-specific coding intelligence

For nontrivial repository bugs, cross-file behavior changes, concurrency, parser errors, authorization paths and independent patch evaluation, first consult [the imported coding skill](skills/code-intelligence/SKILL.md) and only the relevant part of [its evidence-backed method guide](references/code-intelligence-methods.md). Choose one method explicitly with `python scripts/code_intelligence_router.py select <mode>`, using the [original paper tracker](phase4-research/literature/tracker.py) and source catalog; do not load all research or claim selected guidance was executed. Preserve `GlacierEQ/pro-code` as the executable code owner and `GlacierEQ/spiral-engine` as the original improvement controller. Run independent tests and read back the real target when making capability claims.
