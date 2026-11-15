---
name: code-intelligence
description: Use when fixing a nontrivial repository bug, changing behavior across modules, or verifying a coding-agent patch. Selects source-backed analysis and independent tests without loading the whole curriculum.
---

# GlacierEQ Coding Intelligence — task-scoped execution skill

The Operator's latest request and current source own the task. Work within existing repository/skill owners; do not invent an orchestration layer. Read `../../references/code-intelligence-methods.md` only for the relevant failure mode. Do not bulk-load the whole research library or force a process checklist on a simple edit.

## First coding decision: where does actual behavior come from?

Find the live entrypoint and authoritative contract. Use the current commit SHA, relevant code, tests, config, and one or two representative actual outputs. Distinguish a docs snapshot from running source, a string match from a compiler-resolved symbol, and a source file from the loaded deployed artifact. Reuse the repository's existing semantic/code tools before creating new ones. In `GlacierEQ/pro-code`, check current `package.json` and prefer its existing `code:inspect`, `code:knowledge`, `code:refactor`, `code:fix` or `eval:harness` for matching tasks; the last is a local durable-journal ablation, not an LLM coding benchmark.

## Select the analytical instrument by the observed problem

- **Wrong symbol or broken multi-file refactor:** compiler/LSP definitions, aliases, references, reverse dependencies, generated API consumers; flag reflection/dynamic imports as unknown, not absent.
- **Bad state or false-success status:** state-transition invariant and independent reference model; distinguish accepted, effected, persisted, confirmed; test negative, conflicting, crash and retry paths.
- **Race or duplicate side effect:** identify linearization point, atomic commit boundary and idempotency key; test concurrent duplicates, restart and lost acknowledgement; in-process locks alone are not durable exactly-once.
- **Security flow/tenant escape:** exact actor/object authorization and CodeQL path or taint model as relevant; prove denial using negative runtime tests.
- **Stale code or flag cleanup:** inspect dynamic consumers, live configuration, protected kill-switches, runtime traces and change history before deletion. Preserve unknown production routes.
- **Complex parser/transformation:** property-based/metamorphic tests, differential oracle, fuzz/seed replay; don't assume good unit coverage means equivalence.

## Finish by independent evidence

Reproduce a relevant baseline failure when feasible; implement the smallest *complete* behavior change, including impacted contracts and callers; run the chosen adversarial checks and real build; inspect CI steps and read the actual target outcome. A test, pull request, generated text, or cached report proves only its supported stage. Repair failures in scope rather than reporting process as success.

Retain a compact proof: task + expected behavior, repo/SHA, source/invariant, baseline, change, selected independent tests/observations, actual output, remaining unknowns. If the user requested save/push/deploy, perform those stages under existing authorization and verify separately. For new or difficult tasks, prefer targeted discovery to broad repeated scans.

## Sources and examples

See `../../references/code-intelligence-methods.md` for the source map, tested questions, and method-to-failure routing. Canonical project reference: https://docs.google.com/document/d/1dL2dkIEpgM2_MmeTBAIWhTpaDoa9IcAfc9w5vH3geNk/edit
