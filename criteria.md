# Provenance Guard — Unit 7 acceptance criteria (student review draft)


1. **Protect human writers:** Across ten personally selected genuinely human
   writing samples, **no more than one** may receive the `ai` label in each of
   three evaluation runs.

   **Why:** A false accusation on a creative-writing site can damage a writer's
   reputation. This target deliberately prioritizes avoiding false positives.

2. **Meaningful score separation:** On five clearly human and five clearly
   AI-authored test pieces, the median combined score for the latter must be
   **at least 0.12 greater** than the former, in all three runs.

   **Why:** A system that returns nearly the same number for every kind of text
   is not useful, even when every request returns HTTP 200.

3. **All three reader labels are reachable:** Direct score-to-label checks at
   **0.15, 0.55, and 0.95** must yield `human`, `unsure`, and `ai`
   respectively (**3/3**).

   **Why:** A label advertised to users but impossible to obtain is a broken
   feature. This tests the threshold mapping itself, not detector accuracy.

4. **Appeal auditability:** For **five submitted and appealed items**, 5/5
   `POST /appeal` calls must change the latest status to `under_review`, while
   the original logged model score, style score, and label remain unchanged.

   **Why:** Reconsideration is only fair if a reviewer can compare the
   challenge against the exact original decision.

5. **Invalid requests are rejected, not judged:** Across **five malformed
   cases** (missing text, blank text, non-string text, absent creator ID,
   text over 20,000 characters), all **5/5** must produce a 4xx response
   without a successful attribution decision in the log.

   **Why:** A malformed request should never result in a credible-looking
   authorship verdict, even if the system remains available.

**Unit 8 reminder:** Preserve these originals even if a criterion is missed.
Only add a revised criterion when the original genuinely cannot be measured;
do not quietly lower the threshold after seeing the outcome.
