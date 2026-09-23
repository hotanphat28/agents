# Testing Patterns & Strategy

This document outlines the strict quality and testing rules for the ecosystem.

## 1. Test Strategy Rules
* **Testing Pyramid Exceptions**:
  * **CRUD apps** → heavier on integration (little business logic to unit test).
  * **Algorithmic code** → heavier on unit tests (pure functions, many edge cases).
  * **UI-heavy apps** → add visual regression layer.
  * **Event-driven systems** → heavier on integration (async flows matter).

## 2. Integration Testing Rules
* **Test Containers Pattern**: Use real infrastructure in containers (e.g., PostgreSQL, Redis, Localstack, WireMock) for integration tests.
* **API Integration Test Checklist**:
  * Happy path returns correct status and body.
  * Invalid input returns 400 with descriptive error.
  * Missing auth returns 401; Insufficient permissions returns 403.
  * Not found returns 404; Server error returns 500 with safe error message (no stack traces).
  * Pagination works (first page, last page, empty page).
  * Concurrency/idempotency handled (duplicate requests).
* **Database Integration**: Each test starts with a known state (truncate or rollback). Use real migrations.

## 3. End-to-End Testing Rules
* **Test user outcomes, not implementation** — "user can submit a loan application" not "button click triggers POST request".
* **Minimize E2E count** — only critical paths; use lower layers for edge cases.
* **Use stable selectors** — `data-testid` attributes, not CSS classes or XPaths.
* **Handle async explicitly** — wait for elements/conditions, never use fixed sleeps.
* **Isolate test data** — each test creates its own data, cleans up after.

## 4. BDD Automation Rules
* Write scenarios in domain language (not technical steps).
* One behavior per scenario (not a multi-step flow).
* Keep step definitions thin — delegate to page objects or service clients.

## 5. Contract Testing Rules
* **Schema Compatibility Rules (Avro/Protobuf)**:
  * Add optional field: ✅ Yes
  * Remove optional field: ✅ Yes (with default)
  * Add required field: ❌ No
  * Remove required field: ❌ No
  * Rename field: ❌ No
  * Change field type: ❌ No

## 6. Coverage Strategy
* **Meaningful Coverage Targets**:
  * Business logic: 90%+ (Critical path must be covered)
  * API controllers: 80%+ (Happy path + error scenarios)
  * Data access: 70%+ (Via integration tests)
  * UI components: 60%+ (Interactive behavior, not markup)
* **Coverage Rules**:
  * Coverage is a floor, not a ceiling.
  * Mutation testing > line coverage.
  * Branch coverage > line coverage.
  * Uncovered code isn't necessarily wrong, but it should be intentional.

## 7. Security Testing Integration
* **Shift-Left**: Integrate SAST and secret scanning locally (IDE or pre-commit) to catch issues before they reach the repository.
* **Fail the Build**: Treat critical/high security vulnerabilities just like failing unit tests—they should block the deployment.
