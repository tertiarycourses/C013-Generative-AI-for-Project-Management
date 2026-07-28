# BeaconWorks Delivery Events

Use only the event range named by the lab. All evidence is synthetic.

## E01 — Work Evidence at Day 9

- WP-01 Requirements confirmation: complete on day 3. Evidence `REQ-APP-01`
  records Service Operations Lead approval of the priority journeys.
- WP-02 Content inventory and approval: complete on day 7. Evidence `CONT-APP-01`
  records 30 approved English article outlines.
- WP-03 Experience and accessibility design: complete on day 8. Evidence
  `DES-REV-01` records the reviewed pilot design and two follow-up checks.
- WP-04 Portal configuration: owner confirmed and inputs `CONT-APP-01` and
  `DES-REV-01` are available. Environment `PORTAL-NP-01` is available.
- WP-05 interface work has an owner, but sandbox access is not confirmed.

## E02 — Pending Environment Decision

Question: should non-production interface testing wait for supplier sandbox access
or use the approved stub while access is escalated? The IT Integration Lead owns the
recommendation; the Project Manager owns the project decision within the existing
baseline. No decision is confirmed in this event.

## E03 — Feature Request

The Service Operations Lead asks whether the pilot can include bilingual FAQ content.
The authorised baseline contains English content only. No scope, date or budget
decision has been made.

## E04 — Capacity Evidence

| Resource role | Planned effort in window | Available effort | Affected work |
|---|---:|---:|---|
| Accessibility Specialist | 5 days | 3 days | WP-03, WP-08 |
| Integration Engineer | 8 days | 8 days | WP-05, WP-07 |
| Content Lead | 6 days | 4 days | WP-02, WP-04 |
| Support Lead | 4 days | 5 days | WP-08, WP-09 |

The values describe role capacity for the project window. They are not individual
performance measures.

## E05 — Confirmed Meeting Note

Date: week 6 Tuesday. Participants: Project Manager, Service Operations Lead, IT
Integration Lead and two support-agent representatives.

- Decision: the pilot content will use the existing BeaconWorks plain-language style
  guide. Decision owner: Service Operations Lead.
- Action: IT Integration Lead will confirm sandbox access or invoke the stub
  escalation by week 6 Friday.
- Question: who will approve any bilingual content and what acceptance evidence would
  be needed?
- Assumption for validation: the accessibility supplier review can start in week 9.
- Risk raised: sandbox access after the Friday trigger may delay integration testing.
- Lesson observed: sharing the acceptance checklist before design review reduced
  repeated clarification and rework.
- The meeting did not approve bilingual scope or a baseline change.

## E06 — Quality Evidence

Design verification `QV-03` checked the agreed layout, navigation, contrast and
alternative-text criteria. Layout, navigation and contrast met the criteria. Two
illustrative images lack approved alternative text. Defect `DEF-07` is severity 2;
Content Lead owns correction by week 7 Thursday.

## E07 — Acceptance Evidence

The Service Operations Lead records internal design verification as complete with
action `DEF-07`. Sponsor acceptance remains `Pending` until integration evidence,
user review and accessibility evidence are available. No event in this file records
final pilot acceptance.
