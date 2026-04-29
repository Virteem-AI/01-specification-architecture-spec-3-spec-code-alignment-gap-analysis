# Exercise Guide - SPEC-3

## Goal

Compare `repo/spec.md` and `repo/app.py` to identify mismatches, undocumented behavior and ambiguous requirements.

## Steps

1. Attach `repo/spec.md` and `repo/app.py` in Copilot Chat.
2. Ask Copilot:

```text
Compare the specification and the code.
List differences: missing endpoints, wrong status codes, missing validation and missing fields.
```

3. Ask Copilot:

```text
What behaviors exist in app.py that are not documented in spec.md?
List implicit defaults, undocumented error cases and edge cases.
```

4. Review the findings.
5. Decide whether each issue belongs to the code or the specification.
6. Write the findings in `repo/alignment-report.md`.
7. Rewrite weak sections in `repo/spec-v2.md`.

## Expected Output

- `repo/alignment-report.md` with at least three findings.
- `repo/spec-v2.md` with at least two improved sections.

## Completion Criteria

The trainee can explain whether each mismatch is a code issue, a specification issue or an ambiguity.
