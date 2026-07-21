# Testing Patterns & Strategy
Core testing foundations, principles, and best practices for all platforms and languages.

## 1. Testing Pyramid
```
         /  E2E  \          ← Few, slow, expensive, high confidence
        /----------\
       / Integration \      ← Moderate count, test boundaries
      /----------------\
     /    Unit Tests     \  ← Many, fast, cheap, isolated
    /____________________\
```

| Layer | Count | Speed | Scope | Confidence |
|---|---|---|---|---|
| Unit | ~70% | < 10ms each | Single function/class | Logic correctness |
| Integration | ~20% | < 1s each | Component boundaries | Contracts hold |
| E2E | ~10% | Seconds-minutes | Full user flows | System works end-to-end |

### When to Violate the Pyramid
* **CRUD apps** → heavier on integration (little business logic to unit test)
* **Algorithmic code** → heavier on unit tests (pure functions, many edge cases)
* **UI-heavy apps** → add visual regression layer
* **Event-driven systems** → heavier on integration (async flows matter)

## 2. Unit Testing Principles

### The FIRST Principles
| Letter | Meaning | Rule |
|---|---|---|
| **F**ast | Tests run in milliseconds | No I/O, no network, no disk |
| **I**solated | No test depends on another | Each test sets up its own state |
| **R**epeatable | Same result every time | No randomness, no clock dependency |
| **S**elf-validating | Pass or fail — no interpretation | Assert clearly, no manual verification |
| **T**imely | Written alongside or before code | Not an afterthought |

### What to Unit Test
* Business logic and calculations
* State machines and decision trees
* Data transformations and mappings
* Validation rules
* Edge cases and boundary conditions

### What NOT to Unit Test
* Framework code (getters/setters, constructors with no logic)
* Third-party library internals
* Configuration/wiring
* Private methods directly (test through public interface)

### Test Structure: Arrange-Act-Assert (AAA)
```
// Arrange — set up preconditions
// Act — perform the action under test
// Assert — verify the outcome
```

### Naming Convention
```
[MethodUnderTest]_[Scenario]_[ExpectedBehavior]

calculateInterest_negativeRate_throwsInvalidArgumentException
formatCurrency_zeroAmount_returnsFormattedZero
```

## 3. Test Doubles
| Type | Purpose | When to Use |
|---|---|---|
| **Stub** | Returns canned data | Need predictable responses from dependencies |
| **Mock** | Verifies interactions | Need to assert a method was called with specific args |
| **Fake** | Working lightweight implementation | Need realistic behavior (in-memory DB, fake HTTP server) |
| **Spy** | Records calls for later assertion | Need real behavior but want to verify interactions |
| **Dummy** | Placeholder, never actually used | Fill required parameters that are irrelevant to test |

### Mocking Best Practices
* **Mock at boundaries** — external services, databases, file systems, clocks
* **Don't mock what you own** — if you wrote it, test it directly unless it's slow/stateful
* **Prefer fakes over mocks for complex dependencies** — more realistic, less brittle
* **Never mock value objects** — test with real instances
* **Limit mocks to 1-2 per test** — more means your design has too many dependencies
* **Verify behavior, not implementation** — mock assertions should test WHAT happened, not HOW

### Dependency Injection for Testability
* Inject dependencies through constructor (not created internally)
* Use interfaces/abstractions at boundaries
* Keep constructors simple — complex constructors = hard to test
* Favor composition over inheritance for testability

## 4. Integration Testing

### What Integration Tests Verify
* API contracts (request/response format, status codes, headers)
* Database queries work with real schemas (use test containers)
* Message queue producers/consumers serialize/deserialize correctly
* External service clients handle responses and errors properly
* Authentication/authorization flows work end-to-end

### Test Containers Pattern
Use real infrastructure in containers for integration tests:
* PostgreSQL, MongoDB, Redis — real engines, ephemeral instances
* Kafka, RabbitMQ — real brokers for event testing
* Localstack — AWS service emulation
* WireMock — HTTP API simulation with contract verification

### API Integration Test Checklist
* [ ] Happy path returns correct status and body
* [ ] Invalid input returns 400 with descriptive error
* [ ] Missing auth returns 401
* [ ] Insufficient permissions returns 403
* [ ] Not found returns 404
* [ ] Server error returns 500 with safe error message (no stack traces)
* [ ] Pagination works (first page, last page, empty page)
* [ ] Concurrency/idempotency handled (duplicate requests)

### Database Integration Test Rules
* Each test starts with a known state (truncate or rollback)
* Use migrations to set up schema (same as production)
* Test with realistic data volumes when performance matters
* Verify cascading deletes, constraints, and indexes

## 5. End-to-End Testing

### What E2E Tests Verify
* Critical user journeys work (registration, purchase, core workflow)
* Cross-service communication works
* UI renders and responds correctly

### E2E Best Practices
* **Test user outcomes, not implementation** — "user can submit a loan application" not "button click triggers POST request"
* **Minimize E2E count** — only critical paths; use lower layers for edge cases
* **Use stable selectors** — `data-testid` attributes, not CSS classes or XPaths
* **Handle async explicitly** — wait for elements/conditions, never use fixed sleeps
* **Isolate test data** — each test creates its own data, cleans up after
* **Retry flaky tests once, then fix** — flaky tests erode trust

### Page Object Pattern (UI E2E)
```
// Encapsulate page interaction in objects
LoginPage.enterEmail("user@test.com")
LoginPage.enterPassword("secure123")
LoginPage.submit()
DashboardPage.assertWelcomeMessage("Hello, User")
```

## 6. Test-Driven Development (TDD)

### Red-Green-Refactor Cycle
1. **Red** — Write a failing test that defines the desired behavior
2. **Green** — Write the minimum code to make it pass
3. **Refactor** — Clean up while keeping tests green

### When TDD Shines
* Well-defined requirements with clear inputs/outputs
* Business logic with edge cases
* Bug fixes (write the failing test first, then fix)
* API design (tests drive the interface)

### When TDD is Optional
* Exploratory/prototyping work (write tests after discovery)
* UI layout (visual regression tests instead)
* Third-party integrations (integration tests are more valuable)

## 7. Behavior-Driven Development (BDD)

### Gherkin Format
```gherkin
Feature: Loan eligibility check

  Scenario: Applicant meets all criteria
    Given an applicant with income €60,000
    And a credit score of 750
    And no existing defaults
    When the eligibility check runs
    Then the result should be "Eligible"
    And the maximum loan amount should be €300,000

  Scenario: Applicant has insufficient income
    Given an applicant with income €15,000
    When the eligibility check runs
    Then the result should be "Ineligible"
    And the reason should include "Minimum income not met"
```

### BDD Best Practices
* Write scenarios in domain language (not technical steps)
* One behavior per scenario (not a multi-step flow)
* Use backgrounds for shared preconditions
* Scenario outlines for data-driven testing
* Keep step definitions thin — delegate to page objects or service clients

## 8. Contract Testing

### Consumer-Driven Contracts
When services communicate via APIs:
1. **Consumer** defines what it expects (fields, types, status codes)
2. **Provider** verifies it satisfies all consumer contracts
3. **Broker** stores and versions contracts (e.g., Pact Broker)

### When to Use
* Microservices with multiple consumers
* API changes that could break unknown consumers
* Async messaging (Kafka, RabbitMQ) — verify schema compatibility

### Schema Compatibility Rules (Avro/Protobuf)
| Change | Backward Compatible? |
|---|---|
| Add optional field | ✅ Yes |
| Remove optional field | ✅ Yes (with default) |
| Add required field | ❌ No |
| Remove required field | ❌ No |
| Rename field | ❌ No |
| Change field type | ❌ No |

## 9. Testing Anti-Patterns
| Anti-Pattern | Problem | Fix |
|---|---|---|
| **Ice cream cone** | More E2E than unit tests | Push logic down, test at lowest possible layer |
| **Flaky tests** | Random failures erode trust | Fix root cause: async waits, test isolation, deterministic data |
| **Testing implementation** | Tests break on refactor | Test behavior/outcomes, not internal details |
| **Slow test suite** | Developers skip tests | Parallelize, use test containers, split unit from integration |
| **No assertions** | Tests pass but verify nothing | Every test must assert at least one meaningful thing |
| **Shared mutable state** | Tests interfere with each other | Isolate: fresh state per test, no global variables |
| **Over-mocking** | Tests pass but system fails | Reduce mocks, increase integration coverage |
| **God tests** | One test covers everything | One behavior per test, clear naming |
| **Testing trivial code** | Noise, no value | Only test code with logic, decisions, or transformation |

## 10. Coverage Strategy

### Meaningful Coverage Targets
| Layer | Target | Notes |
|---|---|---|
| Business logic | 90%+ | Critical path must be covered |
| API controllers | 80%+ | Happy path + error scenarios |
| Data access | 70%+ | Via integration tests |
| UI components | 60%+ | Interactive behavior, not markup |
| Configuration/wiring | Not tested | Low value, high maintenance |

### Coverage Rules
* **Coverage is a floor, not a ceiling** — 80% doesn't mean stop at 80%
* **Uncovered code isn't necessarily wrong** — but it should be intentional
* **Mutation testing > line coverage** — proves tests actually catch bugs
* **Branch coverage > line coverage** — ensures all decision paths are tested
* **Coverage gates in CI** — fail build if coverage drops below threshold
