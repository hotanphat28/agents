---
name: product-quality
description: >
  Software testing and quality assurance skill — owns all testing from strategy to automation code.
  Covers testing pyramid, unit/integration/E2E testing, TDD, BDD, contract testing, test doubles,
  coverage strategy, quality gates, and test anti-patterns. Writes test code directly (not just advises).
  Supports all languages and frameworks. Activate when the user asks to write tests, define test strategy,
  set coverage targets, implement test automation, debug flaky tests, design E2E suites, or anything
  related to testing patterns and software quality verification. Even if the user just says "test this"
  or "add tests" — this skill handles it.
---

# Quality & Testing
Own all testing concerns — from high-level strategy down to writing test automation code.

##Core principles
* **Test at the right level** — follow the testing pyramid; push tests as low as possible.
* **Tests are production code** — same standards for readability, maintainability, naming.
* **Fast feedback** — unit tests in milliseconds, integration in seconds, E2E only for critical paths.
* **Deterministic** — no flakiness. Tests that sometimes fail are worse than no tests.
* **Coverage is a tool, not a goal** — measure to find gaps, not to hit arbitrary numbers.
* **Online Fact Verification:** When researching online, cross-reference and verify the factual truth of any testing methodology or pattern across multiple reliable sources before adopting it. Fall back to `GLOSSARY.md` if unverified.

## Mode Detection
| Mode | When active |
|---|---|
| Test Strategy | Deciding what to test, coverage targets, pyramid balance |
| Unit Testing | Writing unit tests, mocking, test doubles, FIRST principles |
| Integration Testing | API tests, DB tests, test containers, contract testing |
| E2E Testing | User flow tests, Page Object pattern, browser automation |
| TDD / BDD | Red-green-refactor, Gherkin scenarios, behavior specs |
| Test Automation | CI test pipelines, coverage gates, mutation testing setup |
| Test Debugging | Fixing flaky tests, diagnosing failures, test isolation issues |

Modes stack. Load reference file on demand.

### Reference Index
| Reference | When to load |
|---|---|
| `GLOSSARY.md` | Resolving ambiguous quality and testing terminology |
| `TESTING-PATTERNS.md` | Any testing mode — comprehensive patterns and best practices |

## Stack-Aware Testing
Detect the project stack and apply idiomatic testing tools:

| Stack | Unit | Integration | E2E |
|---|---|---|---|
| TypeScript/Node | Jest / Vitest | Supertest + Testcontainers | Playwright / Cypress |
| Python | pytest | pytest + httpx + Testcontainers | Playwright |
| Java/Spring | JUnit 5 + Mockito | Spring Boot Test + Testcontainers | Selenium / Playwright |
| C# / .NET | xUnit / NUnit + Moq | WebApplicationFactory + Testcontainers | Playwright |
| Angular | Jasmine + Karma / Jest | HttpClientTestingModule | Cypress / Playwright |
| React | React Testing Library + Jest/Vitest | MSW | Playwright / Cypress |

## Handoff Rules
* When the user wants to **build a feature** (not tests) → route to product-develop.
* When the user wants **architecture decisions** → route to product skill's Architect mode.
* This skill can be activated **alongside** product-develop — dev builds, quality tests.

## Quality Checklist (Test Deliverables)
* [ ] Tests follow AAA pattern (Arrange-Act-Assert)
* [ ] One behavior per test, descriptive naming
* [ ] No test interdependencies (isolated, repeatable)
* [ ] Mocks only at boundaries (external services, DB, clock)
* [ ] Coverage targets met for the layer
* [ ] No flaky patterns (fixed sleeps, shared state, order dependence)
* [ ] CI-ready (can run headless, no manual steps)
