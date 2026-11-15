# Agentic PhD — Coding Intelligence, Applied to Real Software Work

**Source import:** user-supplied GlacierEQ Intelligence Harness overlay `0.1.35`, release `pluginrel_6af9bbb57d608191b437921e58fee29e`, checked 2026-11-15. Original ZIP contains two source documents copied here byte-for-byte; its plugin manifests and plugin-only tests remain in their original plugin owner. Repository copies are pinned and integrity-checked by `scripts/code_intelligence_router.py`.

## Existing owners retained

- **Agentic PhD:** this repository's original five-phase curriculum, [frontier source index](../resources/research/frontier_sources.json), [PaperTracker](../phase4-research/literature/tracker.py), labs and research-verification CI.
- **GlacierEQ Intelligence Harness:** reusable [coding skill](../skills/code-intelligence/SKILL.md) and [method source](../references/code-intelligence-methods.md), distributed from its private plugin owner.
- **[pro-code](https://github.com/GlacierEQ/pro-code):** executable TypeScript compiler code intelligence, compiler-guided refactor/fix and native HTTP component evaluation. Use the checked-in script interfaces at the current source revision, not a stale example.
- **[spiral-engine](https://github.com/GlacierEQ/spiral-engine):** original long-horizon Spiral controller and journal; evaluated coding outcomes may feed that owner. This repository does not clone or replace it.

## How research increases *usable* coding capability

A failure-mode-specific knowledge selector gives an agent the right primary research, existing owner tools, falsifiable experiment and independent acceptance in one command. It does not simply load more text.

```sh
python scripts/validate_research_library.py
python scripts/code_intelligence_router.py validate
python scripts/code_intelligence_router.py list
python scripts/code_intelligence_router.py select symbol_refactor
python scripts/code_intelligence_router.py select state_receipts
python scripts/code_intelligence_router.py select concurrent_effect
python scripts/code_intelligence_router.py select security_flow
python scripts/code_intelligence_router.py select stale_code
python scripts/code_intelligence_router.py select parser_transform
python scripts/code_intelligence_router.py select agent_evaluation
python -m unittest discover -s tests -p 'test_*.py' -v
```

Each `select` response includes the referenced **original catalog source IDs and canonical URLs**, exact chosen first probe, potential existing pro-code tools, a falsifiable experiment, acceptance conditions, and the risks that make a seemingly successful result unsafe. Modes are explicit: this deterministic CLI does not claim to infer mission intent from user language.

| Failure mode | Research-backed first action | Independent evidence |
| --- | --- | --- |
| `symbol_refactor` | Compiler-resolve declarations and aliases; trace reverse consumers | Only target binding changed; compile and callers still pass |
| `state_receipts` | Separate accepted, executed, committed and verified states | No successful response without effect and durable receipt |
| `concurrent_effect` | Identify linearization and crash/acknowledgment boundary | Duplicate/conflict/restart schedule tests |
| `security_flow` | Actor/object policy boundary plus CodeQL path model | Wrong-actor and tainted-input negative tests |
| `stale_code` | Inspect active flags, history, runtime traces, kill switches | Real non-regression in target environment |
| `parser_transform` | Reference semantics, generated properties and fuzzed counterexamples | Reproducible minimal failing seed then regression |
| `agent_evaluation` | Freeze unseen tasks and independent valid grader | Clean patch reapplication; counted real outcomes and false successes |

**Primary research catalog:** `C01`–`C09` in `frontier_sources.json`. Existing `M04` is the already indexed context-engineering source; it is deliberately not duplicated. Unchecked current URLs have `canonical_url_requires_live_recheck`; no new research experiments have been marked completed.

## Native readback and scope of guarantees

The Python script verifies original plugin skill/reference SHA-256 digests, route schema, existing tracker lookup, authoring ownership, source IDs, and claimed evidence status. It rejects unknown modes, source IDs, unsupported tool names and fabricated execution statuses. The same existing research CI compiles the project and runs all tests.

`npm run eval:harness -- --strict` in pro-code is a **local deterministic Nexus journal-vs-no-journal component ablation**, not an LLM coding score. That distinction is enforced in the route and tests. No cross-repository mutation, hosted tool execution, Spiral revolution, or model training is implied by importing research. To promote a method as effective, implement a real fix in the owning repository and retain actual baseline, test, CI, runtime and independent comparison receipts.

## Integration/verification receipt

- Uploaded overlay: `glaciereq_code_intelligence_overlay_0135.zip`; archive CRC checked.
- Imported skill expected SHA-256: `0f92e9b7e5dcd1ee59767708f0dda7c1b5098dc1587416ebe198f5c595bad6ff`.
- Imported method guide expected SHA-256: `d9b72d61b975c5af4707f4a99fc5bf676ceaa4a6dec1bbf83342376b6ae23da4`.
- Current source/CI observations should be recorded against the actual GitHub revision; this document itself is not a test result or release.
