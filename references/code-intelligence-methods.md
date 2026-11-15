# Code intelligence: active knowledge and method-to-problem map

**Purpose:** high-value information an agent can actually apply when writing and repairing code. Select only the small relevant section for the task. Reviewed: 2026-11-15. Research and vendor reports are evidence about their studied systems, not proof of a GlacierEQ deployment.

## 1. Context engineering (retrieval precision > loaded volume)

**Evidence:** OpenAI's *Harness engineering* describes a short AGENTS.md as a navigation map into canonical repo docs, with mechanical checks for stale guidance. Anthropic's *Effective context engineering* recommends just-in-time references and task-specific retrieval. OpenAI's Sept. 11, 2026 skills analysis warns that overlong descriptions and repetitive instructions can reduce agent selection quality.

**Action:** establish a live revision and task outcome; retrieve entrypoint, contract, exact related symbol, callers and tests. Carry file+SHA+line with each excerpt. Expand only on a contradictory finding. Don't require blanket repo reading for a trivial edit.

Sources: https://openai.com/index/harness-engineering/ ; https://www.anthropic.com/research/effective-context-engineering-for-ai-agents ; https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

## 2. Semantic localization (symbols over spelling)

**Evidence:** official compiler/typechecker and CodeQL documentation distinguish parsed structure, references and dataflow. Tree-sitter is useful for incremental syntax, not necessarily type binding or effect proof. The existing GlacierEQ/pro-code tools are historical but specifically include TypeScript impact and semantic symbol inventory; verify current runtime before use.

**Action:** for multi-file changes use symbol identity, imported aliases, call/reference graphs, build/type diagnostics and reverse dependents. Audit dynamic imports/reflection/generated code separately. Do not treat a grep match as a unique binding.

Sources: https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API ; https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/ ; https://tree-sitter.github.io/tree-sitter/

**Known existing CLI at 2026-10-29 (recheck):** `npm run code:inspect -- --impact src/workers.ts --out .pro-code/runtime/impact.json` and `npm run code:knowledge -- --symbol workersManager --definition-file src/workers.ts --out .pro-code/runtime/symbols.json` in https://github.com/GlacierEQ/pro-code .

## 2A. LIVE `GlacierEQ/pro-code` semantic capabilities — refreshed 2026-11-15

Authenticated current GitHub `main` source checked: `package.json` blob SHA `5500b9df3e0f4a722a7fb9941293e2b8f04a000b`, plus `scripts/code-refactor.mjs`, `scripts/code-fix.mjs`, `scripts/harness-eval.mjs`. A Git blob SHA identifies file content, not the complete commit/head; check current branch revision before any write. This is source verification, not a successful tool execution in this run.

- `npm run code:inspect -- --impact src/workers.ts --out .pro-code/runtime/impact.json` — TypeScript project import graph/impact and compiler diagnostics.
- `npm run code:knowledge -- --symbol workersManager --definition-file src/workers.ts --out .pro-code/runtime/symbols.json` — compiler-backed binding/reference query.
- `npm run code:refactor -- --file src/workers.ts --line <line> --column <col> --new-name <identifier>` — preview compiler-guided rename. `--apply` performs SHA-guarded write and rollback-aware transaction. Replace position/name with an inspected real symbol; never run this example unmodified as a production mutation.
- `npm run code:fix -- --file src/workers.ts` — inspect compiler-supported fixes. To preview a selected diagnostic, add `--code <TS-diagnostic-number>` and optionally `--occurrence`/`--fix-index`; `--apply` mutates through the guarded transaction after a valid preview. Do not fabricate diagnostic codes or choose an action blindly.
- `npm run eval:harness -- --strict` — real local HTTP comparison of bare Nexus against durable-journal Nexus with 7 deterministic scenarios, including replay/restart/unsupported capability and foreign origin. Script explicitly classifies this as **local fixture component ablation, not LLM agent coding intelligence evaluation**.

All commands above were checked against live `package.json` scripts and the three module CLI parsers. Scripts are present, but execution, CI and deployment behavior were not rerun in this source review. Use current repo tests `npm run test:code-intelligence`, `npm run test:code-knowledge`, `npm run test:code-refactor`, `npm run test:code-fix`, `npm run test:harness-evaluation` or scoped `npm test` as risk warrants.

Source: https://github.com/GlacierEQ/pro-code/blob/main/package.json ; https://github.com/GlacierEQ/pro-code/blob/main/scripts/code-refactor.mjs ; https://github.com/GlacierEQ/pro-code/blob/main/scripts/code-fix.mjs ; https://github.com/GlacierEQ/pro-code/blob/main/scripts/harness-eval.mjs

## 3. Falsification, not test-count theater

**Evidence:** generated stateful testing can seek unexpected sequences; fuzzing and differential or metamorphic oracles expose different classes of faults. Randomized and fuzz tests are reproducible only when seeds, harness versions and minimized cases are kept. Real distributed correctness also requires specifying crash and storage assumptions.

**Action choices:** parser → property + corruption + shrink; state machine → reference model + invalid transition; idempotency → 100 duplicates + conflicting payload + restart; transformation → compiler + differential tests; security → wrong actor/object negative test. Pick a small high-signal set, not all methods every time.

Sources: https://hypothesis.readthedocs.io/en/latest/stateful.html ; https://google.github.io/oss-fuzz/ ; https://pdos.csail.mit.edu/6.5840/ ; https://lamport.azurewebsites.net/tla/book.html

## 4. Evidence-backed runtime maintenance

**Evidence:** OpenAI's Oct. 14, 2026 maintenance case study reports using code history, live experiment configuration, profiling and reviewers to identify genuine dead code and costly flags; static analysis alone misses runtime/dynamic consumers. This is one team's report, not a universal benchmark.

**Action:** no code deletion on static non-reference alone. Look for dynamic resolution, feature flags, override paths, kill switches, generated wiring, live data, and existing functionality before removal. Prove system-level no-regression; use telemetry for impact estimates when actually available.

Source: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family

## 5. Evaluation quality, not leaderboard mimicry

**Evidence:** OpenAI's July 8, 2026 audit retracted its earlier SWE-bench Pro recommendation, estimating ~30% task defects. In engineering evals, wrong prompt/hidden tests and underspecified requirements can make both successes and failures uninformative.

**Action:** for comparative agent runs freeze the task+SHA, keep reference patch and grader blind, run independent contract tests in clean environment, inspect false successes and evaluator failures, compare same tools/budget. Score actual functional outcome, not answer polish or copied CI text.

Sources: https://openai.com/index/separating-signal-from-noise-coding-evaluations/ ; https://arxiv.org/abs/2405.15793

## 6. Tiny diagnostic examples to adapt

1. API returns `SUCCEEDED` but native storage has no mutation receipt. Strongest first probe: trace status mapping through handler/commit boundary and assert `SUCCEEDED => matching receipt and effect` with a negative no-handler test.
2. Rename `transform` affects two unrelated symbols. Strongest first probe: compiler-resolved declaration identity and aliased imports, not replace-all string search.
3. Retry duplicates a payment or task effect. Strongest first probe: identify atomic business commit + durable idempotency boundary; concurrent duplicates plus process-restart test.
4. Clean-up proposal deletes an apparently unreferenced feature flag. Strongest first probe: actual runtime evaluation, overrides and emergency-killswitch status; static absence is insufficient.
5. Parser reports `EMPTY_IN_SCOPE` for malformed data. Strongest first probe: separate true empty evidence from parse failure via discriminated variants and fuzzed malformed inputs.

Each example is a method to select, *not* a claim that a particular bug is present in the current repository.
