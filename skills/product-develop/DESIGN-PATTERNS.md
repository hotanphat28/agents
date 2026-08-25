# Software Design Patterns & Unit Testing

This document outlines the strict engineering standards and testing rules required when writing structural code.

## 1. Dependency Injection (DI)
* **Strict Prohibition:** Hardcoding dependencies via the `new` keyword (or equivalent) inside business logic is strictly prohibited.
* **Constructor Injection:** Inject all required dependencies through the class constructor. 
* **Configuration Injection:** Externalized configurations (database URIs, API keys) must also be injected, never accessed globally.

## 2. The Repository Pattern
* **Strict Prohibition:** Directly querying the database from business logic (services/controllers) is an anti-pattern.
* **Abstract Data Access:** All data access must be abstracted behind a Repository interface.
* **Domain Focus:** The Repository should act like an in-memory collection of domain objects. It takes and returns domain entities, not database rows.

## 3. Unit Testing & Mocking Rules (TDD)
* **Mock at boundaries** — external services, databases, file systems, clocks.
* **Don't mock what you own** — if you wrote it, test it directly unless it's slow/stateful.
* **Prefer fakes over mocks for complex dependencies** — more realistic, less brittle.
* **Never mock value objects** — test with real instances.
* **Limit mocks to 1-2 per test** — more means your design has too many dependencies.
* **Verify behavior, not implementation** — mock assertions should test WHAT happened, not HOW.
