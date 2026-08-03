# Software Design Patterns

This document outlines the strict engineering standards required when writing structural code, regardless of the underlying language or framework.

## 1. SOLID Principles
All classes and modules MUST strictly adhere to the SOLID principles:

*   **Single Responsibility Principle (SRP):** A class should have one, and only one, reason to change. Separate data access, business logic, and presentation concerns into different classes.
*   **Open-Closed Principle (OCP):** Software entities should be open for extension but closed for modification. Use interfaces and abstract classes to allow new behaviors to be added without changing existing code.
*   **Liskov Substitution Principle (LSP):** Objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.
*   **Interface Segregation Principle (ISP):** No client should be forced to depend on methods it does not use. Break fat interfaces into smaller, role-specific interfaces.
*   **Dependency Inversion Principle (DIP):** Depend on abstractions, not on concretions. High-level modules should not depend on low-level modules; both should depend on abstractions.

## 2. Dependency Injection (DI)
Hardcoding dependencies via the `new` keyword (or equivalent) inside business logic is strictly prohibited.

*   **Constructor Injection:** Inject all required dependencies through the class constructor. This is the preferred method as it ensures the object is always in a valid state.
*   **IoC Containers:** Leverage the framework's Inversion of Control (IoC) container (e.g., Spring for Java, NestJS for TypeScript, generic DI containers for Go/Python) to wire dependencies automatically.
*   **Configuration Injection:** Externalized configurations (database URIs, API keys) must also be injected, never accessed globally.

## 3. The Repository Pattern
Directly querying the database from business logic (services/controllers) is an anti-pattern.

*   **Abstract Data Access:** All data access must be abstracted behind a Repository interface.
*   **Domain Focus:** The Repository should act like an in-memory collection of domain objects. It takes and returns domain entities, not database rows.
*   **Isolation:** This allows the underlying storage mechanism (SQL, NoSQL, external API) to be swapped or mocked for testing without affecting business logic.

## 4. Gang of Four (GoF) Patterns
When facing complex object creation or behavior, default to standard GoF patterns:

*   **Factory Pattern:** Use when the creation logic of an object is complex or when the exact type of the object isn't known until runtime.
*   **Strategy Pattern:** Use when you have multiple interchangeable algorithms (e.g., different payment methods or sorting algorithms) to avoid complex `if/else` or `switch` statements.
*   **Decorator Pattern:** Use to add responsibilities to individual objects dynamically and transparently, without affecting other objects.
*   **Observer Pattern:** Use for event-driven scenarios where a change in one object requires changing others, and you don't know how many objects need to be changed.
