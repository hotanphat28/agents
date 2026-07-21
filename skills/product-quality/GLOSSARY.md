# Glossary of Terms
This document provides a single source of truth for terminology used within the `product-quality` skill, ensuring context accuracy and preventing hallucinations.

## Testing Strategies
* **Testing Pyramid**: A framework that dictates you should have a large number of fast, isolated Unit Tests at the bottom, fewer Integration Tests in the middle, and a very small number of brittle E2E (UI) tests at the top.
* **E2E (End-to-End) Testing**: A methodology used to test whether the flow of an application is performing as designed from start to finish.
* **TDD (Test-Driven Development)**: A software development process relying on software requirements being converted to test cases before software is fully developed, tracking all software development by repeatedly testing the software against all test cases.
* **BDD (Behavior-Driven Development)**: An agile software development process that encourages collaboration among developers, QA and non-technical or business participants in a software project, often using Given/When/Then syntax.
* **Contract Testing**: A technique for testing an integration point by checking each application in isolation to ensure the messages it sends or receives conform to a shared understanding that is documented in a "contract".
* **Shift-Left Testing**: An approach to software testing and system testing in which testing is performed earlier in the lifecycle (moved left on the project timeline).

## Patterns & Principles
* **AAA Pattern (Arrange-Act-Assert)**: A pattern for formatting and writing unit tests. Arrange sets up the preconditions; Act executes the behavior; Assert verifies the outcome.
* **FIRST Principles**: Criteria for good unit tests: Fast, Isolated/Independent, Repeatable, Self-validating, Thorough/Timely.
* **Test Doubles**: A generic term for any case where you replace a production object for testing purposes (includes Dummies, Fakes, Stubs, Spies, and Mocks).
* **Mocking**: Creating objects that simulate the behavior of real objects in controlled ways, primarily used to isolate the unit being tested from external dependencies.
* **Page Object Pattern**: A design pattern used in test automation to create an object repository for web UI elements, improving test maintenance and reducing code duplication.
* **Red-Green-Refactor**: The core TDD cycle: Write a failing test (Red), write just enough code to pass it (Green), and then improve the code without changing behavior (Refactor).
* **Gherkin**: A domain-specific language that allows you to describe software behavior without detailing how that behavior is implemented (Given/When/Then).

## Tools
* **Testcontainers**: A library that provides lightweight, throwaway instances of common databases, Selenium web browsers, or anything else that can run in a Docker container, used for integration testing.
* **Playwright**: A framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API.
* **Cypress**: A next generation front end testing tool built for the modern web, executing tests directly inside the browser.
