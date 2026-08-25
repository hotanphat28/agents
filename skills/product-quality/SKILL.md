---
name: product-quality
description: Define test strategy, write test automation, and verify software quality.
disable-model-invocation: true
---

# Quality & Testing

##Core principles
* **Test at the right level** — follow the testing pyramid; push tests as low as possible.
* **Tests are production code** — same standards for readability, maintainability, naming.
* **Fast feedback** — unit tests in milliseconds, integration in seconds, E2E only for critical paths.
* **Deterministic** — ensure tests are deterministic. Tests that sometimes fail are worse than no tests.
* **Coverage is a tool, not a goal** — measure to find gaps, not to hit arbitrary numbers.
* **Online Fact Verification:** When researching testing patterns, cross-reference reliable sources using 'site:' operators. Use the Pause and Challenge Protocol if evidence contradicts assumptions.


## Mode Detection
| Mode | When active |
|---|---|
| Test Strategy | Deciding what to test, coverage targets, pyramid balance |

| Integration Testing | API tests, DB tests, test containers, contract testing |
| E2E Testing | User flow tests, Page Object pattern, browser automation |
| BDD Automation | Automating plain text behavioral specs into E2E and Integration tests |
| Test Automation | CI test pipelines, coverage gates, mutation testing setup |
| Test Debugging | Fixing flaky tests, diagnosing failures, test isolation issues |
| Security Testing | SAST/DAST setup, dependency/secret scanning, vulnerability remediation |

Modes stack. Load reference file on demand.

### Reference Index
| Reference | When to load |
|---|---|

| `TESTING-PATTERNS.md` | Any testing mode — comprehensive patterns and best practices |

## Stack-Aware Testing
Detect the project stack and apply idiomatic testing tools:

| Stack | Unit | Integration | E2E | Security |
|---|---|---|---|---|
| TypeScript/Node | Jest / Vitest | Supertest + Testcontainers | Playwright / Cypress | ESLint, Snyk, ZAP |
| Python | pytest | pytest + httpx + Testcontainers | Playwright | Bandit, Trivy, ZAP |
| Java/Spring | JUnit 5 + Mockito | Spring Boot Test + Testcontainers | Selenium / Playwright | SonarQube, Snyk, ZAP |
| C# / .NET | xUnit / NUnit + Moq | WebApplicationFactory + Testcontainers | Playwright | SonarQube, Snyk, ZAP |
| Angular | Jasmine + Karma / Jest | HttpClientTestingModule | Cypress / Playwright | ESLint, Snyk, ZAP |
| React | React Testing Library + Jest/Vitest | MSW | Playwright / Cypress | ESLint, Snyk, ZAP |

## Handoff Rules
* When the user wants to **build a feature or write unit tests via TDD** → route to product-develop.
* When the user wants **architecture decisions** or **analysis** → route to product-analyze.
* When the user wants **design work** → route to product-design.
* This skill can be activated **alongside** product-develop — dev builds, quality verifies. Quality ensures what product-develop ships actually works correctly.

## Quality Checklist (Test Deliverables)
* [ ] Tests follow AAA pattern (Arrange-Act-Assert)
* [ ] One behavior per test, descriptive naming
* [ ] No test interdependencies (isolated, repeatable)
* [ ] Mocks only at boundaries (external services, DB, clock)
* [ ] Coverage targets met for the layer
* [ ] Avoid flaky patterns by using explicit waits, isolated state, and order independence
* [ ] Dependencies and codebase scanned for vulnerabilities (SAST/SCA)
* [ ] No exposed secrets or hardcoded credentials
* [ ] CI-ready (can run headless, no manual steps)

## Practical Workflows

### How to Test a New Feature (Step-by-Step)
1. **Pull the Behavioral Specs (BDD)** — Read the plain text behavioral specifications from `product-analyze`. Each behavior becomes an automated test (Integration or E2E). If the behavior is vague, ask for clarification.
2. **Identify the testing layers** — Ask: "Where does the logic live?"
   * Data access or external service calls → integration tests
   * User-facing flow across multiple components → E2E (only for critical paths)
   * *(Note: Unit testing is handled natively by `product-develop` during TDD)*
3. **Write the first test** — Start with the happy path at the lowest possible layer. Use this template:
   ```
   test("[method/feature]_[scenario]_[expected outcome]")
   // Arrange: set up inputs and dependencies
   // Act: call the thing
   // Assert: verify the one outcome you care about
   ```
4. **Add edge cases** — For each input, ask: "What if it's null? Empty? Negative? Huge? Malformed? Duplicate?"
5. **Add the sad path** — What should happen when things go wrong? Test error handling explicitly.
6. **Run and verify** — All tests green? Good. Now break the implementation on purpose — does your test catch it? If not, the test isn't testing what you think.

### Prioritizing Tests (When Time Is Limited)
When you can't test everything, test in this order:
1. **Money and data integrity** — anything that could corrupt data or lose money
2. **Security boundaries** — authentication, authorization, input validation
3. **Core happy path** — the primary thing users come here to do
4. **Error handling** — how the system behaves when dependencies fail
5. **Edge cases** — unusual but valid inputs
6. **Performance-sensitive paths** — only if there's a known risk

### Debugging Flaky Tests
A flaky test (passes sometimes, fails sometimes) is worse than no test — it erodes trust. Fix it immediately:

1. **Reproduce locally** — Run the failing test in isolation 10 times. If it always passes locally, the issue is environment-specific (shared state, timing, resource contention).
2. **Check for these common causes:**
   * **Shared mutable state** — tests writing to the same DB/file/variable without cleanup → isolate with fresh state per test
   * **Time dependency** — test uses `DateTime.Now` or real clocks → inject a fake clock
   * **Race condition** — async operations not properly awaited → add explicit waits/assertions on state instead of fixed sleeps
   * **Order dependency** — test passes only when run after another test → find and remove the hidden setup
   * **External service** — real HTTP calls in tests → mock the boundary
3. **Fix the root cause** — Don't just add retries. Retries hide the problem; they don't fix it.
4. **Quarantine if needed** — If the fix is complex and the flakiness is blocking CI, move the test to a quarantine suite temporarily. But set a deadline to fix it (max 1 sprint).

### Test Plan Template
Use when communicating test strategy to the team or stakeholders:

```markdown
## Test Plan: [Feature Name]

### Scope
What's being tested and what's explicitly excluded.

### Test Layers
| Layer | What's Covered | Tool | Count (approx) |
|---|---|---|---|
| Unit | [list key logic areas] | [jest/pytest/xunit] | ~X tests |
| Integration | [list boundaries being tested] | [tool] | ~X tests |
| E2E | [list critical user flows] | [playwright/cypress] | ~X tests |

### Key Risks
What could go wrong that tests should catch? (e.g., "race condition on concurrent submissions")

### Coverage Targets
| Layer | Target | Rationale |
|---|---|---|
| Unit | X% | [why this number — what's the critical logic?] |
| Integration | X% | [which boundaries are riskiest?] |

### Not Testing (and why)
* [Thing] — [reason: low risk / already covered / cost > benefit]
```
