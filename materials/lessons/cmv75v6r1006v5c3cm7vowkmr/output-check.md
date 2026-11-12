# Check an actual optional assistant result

Compare the result with the original fictional notes, not with how polished it looks.

| Source detail | Required trace in output | Common error to reject |
| --- | --- | --- |
| Community garden open day | The checklist remains about that event | Switching to another event |
| Mina: welcome table | Mina associated with the welcome table | Giving Mina another unprovided role |
| start 10:00 | Exact 10:00 retained | Inventing AM/PM, time zone or a different time |
| bring reusable cups | Reusable cups included | Replacing with disposable cups |
| need signs | Signs included | Claiming signs have already been made |
| rain? use hall | Hall is used if it rains | Making the hall unconditional |
| No date supplied | Event date explicitly marked missing | Inventing a calendar date |

Output format should be a short checklist. A missing detail or invented fact is a reason to correct the result or use a manually written checklist. It is not a reason to rename the prompt after a product. This exercise never claims a generated response proves an event, purchase or external action occurred.
