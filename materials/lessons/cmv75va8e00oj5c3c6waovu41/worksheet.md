# Lesson 149 — Create a Chart for a Clear Question

Emmanuel Corels Academy · Practical AI for Everyday People

This self-created fictional community-event table records counts of cups served. It contains no real event, personal data or external activity. All records are supplied; an AI assistant is optional. No generated answer, imported workbook or live chart result is claimed until you actually execute and check it.

## Source and setup

Open Community Event Refreshments.xlsx in your spreadsheet or import refreshments.csv. In Google Sheets, name the data tab Refreshments. Verify A1:B5 exactly: header Refreshment table | Cups served; Water station | 84; Tea table | 61; Coffee table | 47; Juice table | 72. There are four records, not five; the first row is a header. Preserve this source before experimenting. The workbook's Checks tab includes SUM and MAX formulas without cached results, so your actual application must calculate them. Expected results are supplied separately and are not execution evidence.

## Define the question before choosing a chart

Write: Which refreshment table served the most cups? These are discrete categories, not ordered time. A horizontal bar chart or readable column chart suits the comparison. A line between these labels suggests a progression the data does not establish. A pie can communicate shares, but common-baseline bars make the largest category easier to compare. There is no need to infer litres, percentages or monetary values.

If using an available assistant, copy question-and-prompt.txt and the exact four records. Label its recommendation a suggestion, not verified analysis. Independently compare its chart type, range, units and assumptions with the source; do not accept fluent prose as proof it read the cells.

## Build and inspect the chart in the real spreadsheet

Select A1:B5, including headers. Use the real Insert > Chart command and choose a horizontal bar chart. In the actual chart editor verify the exact range Refreshments!A1:B5, first-row headers and first-column category labels. Interface controls vary; inspect the current application rather than relying on a screenshot of a different version.

Set title Cups served by refreshment table. Use Cups served for the numeric axis and Refreshment table for the category axis. Start the numeric scale at zero. Display all four full category names and values. Check Water station 84, Tea table 61, Coffee table 47, Juice table 72 against their original cells. Use a consistent high-contrast bar color, no 3-D decoration, readable labels and a size appropriate to its real destination. Verify it again after resizing or copying.

## Diagnose two deliberately wrong ranges

1. In a separate practice chart change the range to A1:B4. The source still has four records but the chart has three categories: Juice table (72) is omitted. Water may still look largest; a plausible conclusion does not excuse incomplete evidence. Restore A1:B5 and recount.
2. In a separate copy import error-example-total-row.csv. The additional Total row is 264, but Total is a sum, not a fifth refreshment table. A1:B6 puts the whole beside its parts. Restore the correct four-category range, retaining any useful total outside that comparison.

## Independent checks and manual fallback

Ignore bar lengths and compare source numbers directly: 84 > 72 > 61 > 47. The row for 84 is Water station, confirming the chart's largest bar. Independently add 84 + 61 + 47 + 72 = 264. Check the calculated SUM and MAX on the Checks tab against those manual results.

Use review-checklist.csv to record actual observations, not just ticks copied from the answer key. Explain any repair. On a phone check source range, category count, labels, units and scale; if controls are cramped, complete editing on a larger screen. No AI feature is necessary for any of these steps.

## Exercise

Produce one correct chart and two clearly identified practice error charts. Record the exact correct range, omitted category in the first error and why the Total bar is inappropriate in the second. Explain why the same number 84 changes meaning if labeled litres, percent or currency. Finally, export or copy your correct chart into a document and check the actual final reading size. Keep the original data unchanged for Lesson 150.

The included chart-source.svg is a self-authored conceptual illustration of the expected numbers, not a Google Sheets screenshot or proof of execution. Actual course UI captures must come from genuine Google Sheets. All software results need functional QA and independent review before publication.
