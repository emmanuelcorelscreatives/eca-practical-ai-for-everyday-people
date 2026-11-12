# Estimate Before You Accept the Answer — Academy practice kit

A self-authored fictional lesson 60 kit. No records describe purchases, people or real incidents. “Units” is an unspecified unit of price, not a named currency. Nothing here is an observed AI conversation or a screenshot of software output.

Start with worksheet.md. Work without answers.md open, using paper, any ordinary calculator, or a spreadsheet. No account or internet is required. The optional Python checker uses only the standard library; arithmetic printed by it is deterministic local execution, not independent evidence that the source records are true.

Files: source-input.csv holds the narrated 48-item example; quantity-check.csv adds four clearly fictional extension records for the omitted-row exercise; mean-values.csv holds the five source-prompt values; practice-cases.csv preserves the three narrated plausibility cases. quantity-check-template.csv is an empty Total column for manual spreadsheet work; formula-map.md gives the cell plan. worksheet.md and checking-record.csv are learner workspaces; answers.md is the worked key; verify.py replays numerical checks; provenance.md explains evidence limits.

Optional check: run `python3 verify.py` from this directory. Its expected successful output is described in answers.md. It does not launch or verify Windows Calculator or LibreOffice. For spreadsheet software, enter the formulas yourself and compare the result. Keep any AI response separately with its own provenance; the supplied illustrative wrong values are authored fixtures.

The routine is: round for scale, set bounds, calculate explicitly, spot-check another way, investigate mismatches. Agreement supports a calculation on chosen inputs. It does not validate missing taxes, discounts, units or the original records.
