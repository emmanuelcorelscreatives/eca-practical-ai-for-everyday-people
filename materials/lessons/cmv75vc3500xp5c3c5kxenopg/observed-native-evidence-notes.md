# Recorded native example and limits

The supplied workflow was tested in an isolated n8n 2.47.5 instance with a synthetic Test fixture operator. Complete-approved input produced one row; rejected and approved-incomplete inputs produced no additional row (1/0/0). `observed-native-case-results.json` and `observed-native-test-log.xlsx` retain that recorded example, not a fresh run or your own baseline. The three included form-submission screenshots show submission only, not workbook success or human approval.

For your own test, inspect the actual execution history and independently open your actual saved workbook. Start from a new empty workbook, preserve your own timestamps, and check exactly one control row and no rejected/incomplete rows. A selected option, submitted form or success message alone does not establish the destination result.

The local Python exercise is a separate offline model, not a vendor execution. No example here grants real-world approval or permission to send, publish, purchase or delete.
