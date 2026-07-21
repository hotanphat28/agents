# Glossary of Terms
This document provides a single source of truth for terminology used within the `product-develop` skill, ensuring context accuracy and preventing hallucinations.

## Architecture & APIs
* **REST (Representational State Transfer)**: An architectural style for designing networked applications based on stateless, client-server communication, usually over HTTP.
* **GraphQL**: A query language for APIs and a runtime for fulfilling those queries with existing data, allowing clients to request exactly what they need and nothing more.
* **gRPC**: A high-performance, open-source universal RPC framework developed by Google, heavily utilizing HTTP/2 and Protocol Buffers for structured data serialization.
* **WebSocket**: A computer communications protocol providing full-duplex communication channels over a single TCP connection, ideal for real-time applications.
* **OpenAPI**: A specification for machine-readable interface files for describing, producing, consuming, and visualizing RESTful web services.
* **SPA (Single Page Application)**: A web application or website that interacts with the user by dynamically rewriting the current web page with new data from the web server, instead of the default method of a web browser loading entire new pages.
* **Microservices**: An architectural style that structures an application as a collection of loosely coupled, independently deployable services organized around business capabilities.

## AI Engineering
* **LLM (Large Language Model)**: A computational model designed to understand and generate human language, trained on vast amounts of text data (e.g., GPT-4, Gemini).
* **RAG (Retrieval-Augmented Generation)**: An AI architecture that enhances an LLM's responses by dynamically retrieving facts from an external knowledge base before generating an answer.
* **Embeddings**: Mathematical representations (vectors) of text, images, or audio that capture their semantic meaning, allowing AI systems to measure similarity between concepts.
* **Vector DB**: A database designed specifically to store, manage, and search embedding vectors efficiently using similarity search (e.g., pgvector, Chroma).
* **LangGraph**: A library for building stateful, multi-actor applications with LLMs, used to create cyclical graphs for autonomous agents.

## DevOps & Infrastructure
* **CI/CD (Continuous Integration / Continuous Deployment)**: The practice of automating the building, testing, and deployment of code changes to reduce manual effort and improve delivery speed.
* **IaC (Infrastructure as Code)**: The process of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration.
* **Observability**: A measure of how well internal states of a system can be inferred from knowledge of its external outputs (metrics, logs, traces).
* **Telemetry**: The automated communication process by which measurements and other data are collected at remote or inaccessible points and transmitted to receiving equipment for monitoring.
