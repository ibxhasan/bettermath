# IB Math Instructor Kit (Cursor)

A ready-to-use workspace for teaching **IB Mathematics AA / AI (SL & HL)** with Cursor — built to sit beside [BetterMath](../README.md) (AA HL companion).

Designed for classroom use at international schools (including Yokohama contexts with English + Japanese support).

## Quick start (5 minutes)

1. Open this repo in **Cursor**.
2. Read [`START-HERE.md`](START-HERE.md).
3. Open the matching course folder under `courses/` and paste a prompt from `prompts/`.
4. Save strong outputs into `bank/` so you build a reusable library.

## What’s inside

| Folder | Purpose |
|--------|---------|
| `prompts/` | Copy-paste prompt packs (lessons, Paper 1/2, IA, differentiation, admin) |
| `templates/` | Blank structures Cursor should fill |
| `courses/` | Syllabus topic maps for AA/AI SL & HL |
| `demos/` | Starter Python visualisations for class projector use |
| `glossary/` | EN–JA math term bank for international classrooms |
| `bank/` | Your saved lessons, worksheets, assessments, IA feedback |

## Recommended Cursor habits

- **One chat per unit** — keep context focused (e.g. “AA HL Vectors”).
- **Attach syllabus + a sample** — `@courses/AA-HL/topics.md` plus one past worksheet you like.
- **Always request a markscheme** — and verify marks yourself before issuing.
- **Never paste live/secure IB exam material** into AI tools.
- **For IA** — coach structure and criteria; do not write the student’s exploration.

## Pairing with BetterMath

For AA HL, map lessons to BetterMath chapters via `courses/AA-HL/topics.md`. Example prompt:

> Using BetterMath Chapter 10 (Vectors) and `@courses/AA-HL/topics.md`, write a 40-minute lesson with Paper 1 non-GDC practice and a full markscheme.

## Guardrails

See [`.cursor/rules/ib-math-instructor.mdc`](../.cursor/rules/ib-math-instructor.mdc) — Cursor will follow these automatically in this project.
