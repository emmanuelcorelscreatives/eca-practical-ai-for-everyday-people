# Optional AI audit prompts
The text below is an instruction to try, not a logged assistant response. Use only the fictional kit records. Keep your own prompt and actual response if you try it.

“Audit this table only for percentage bases, currency labels, decimal or grouping ambiguity, and date order. Quote each suspicious entry exactly. Mark missing context. Do not invent conversions, rates or dates. Separate claims from source evidence. Tell me which values, units and assumptions I must verify; do not label generated calculations as independently verified.”

Percentage follow-up: “Review this row for percentage-format risks. Distinguish stored value, displayed value and percentage base. Do not calculate from missing assumptions.”

Locale follow-up: “Identify possible locale ambiguities in these exact strings: 1,234.56 and 1.234,56. Do not choose a meaning without source context. Ask for the decimal and grouping convention.”

Check any actual response against the supplied source notes and a separate calculator. If the assistant guesses, preserve that response as a claim and reject the unsupported interpretation.
