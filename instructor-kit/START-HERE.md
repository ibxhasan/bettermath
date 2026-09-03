# Start here — IB Math + Cursor

You are an IB Math instructor. This kit turns Cursor into a **materials studio** for AA/AI SL & HL.

## Daily workflow

### 1. Plan a lesson (10–15 min)

Open Chat / Agent and paste from `prompts/lesson-bank.md`:

```
Course: AA HL
Topic: 5.8 / 5.9 Optimisation
Lesson length: 40 minutes
Class profile: mixed English levels, Yokohama international school
Output using templates/lesson-plan.md
Also produce a 1-page worksheet using templates/worksheet.md
```

Save the result to `bank/lessons/`.

### 2. Build Paper 1 / Paper 2 practice

Paste from `prompts/paper12-generator.md`:

```
Course: AI SL
Paper: 2 (GDC allowed)
Topic: Normal distribution
Marks: one 6-mark and one 8-mark question
Include full markscheme with method / accuracy / follow-through notes
Use IB command terms
```

Save to `bank/assessments/`.

### 3. Coach an IA (without writing it)

Paste from `prompts/ia-coach.md`:

```
Course: AA SL
Student stage: topic proposal
Interest area: sports / modelling growth
Give 5 viable exploration angles, each with: research question draft,
math toolkit, data plan, and risks for Criterion E (personal engagement)
Do NOT write sample calculations or a finished exploration
```

Save feedback drafts to `bank/ia-feedback/`.

### 4. Differentiate for language / readiness

Paste from `prompts/differentiation.md` and attach `@glossary/en-ja-math-terms.md`.

### 5. Make a classroom demo

Ask Cursor to extend something in `demos/examples/`, then run it locally or project the output.

## First-week checklist

- [ ] Skim `courses/` for your exact course(s)
- [ ] Customise class profile notes at the top of your first chat
- [ ] Generate 1 lesson + 1 worksheet + markscheme and verify accuracy
- [ ] Add 5 school-specific EN–JA terms to `glossary/en-ja-math-terms.md`
- [ ] Create empty unit folders under `bank/lessons/` (e.g. `unit-01-algebra`)

## Prompt formula that works

Always include:

1. **Course** (AA/AI + SL/HL)  
2. **Syllabus codes** (e.g. 1.2, 5.8)  
3. **Paper constraints** (GDC / non-GDC, marks, time)  
4. **Class profile** (language, prior knowledge, group size)  
5. **Output format** (which template to fill)  
6. **Quality bar** (“flag anything that may be off-syllabus”)

## Accuracy rule

Treat every AI markscheme as a **draft**. Check:

- syllabus fit (SL vs HL; AA vs AI)
- radian/degree conventions
- exact vs 3 s.f. expectations
- GDC vs analytic methods
- command-term verbs
