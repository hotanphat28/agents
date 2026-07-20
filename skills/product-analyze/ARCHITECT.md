# Architect Mode — Full Reference

## Reverse Engineering Process

1. **Reconnaissance** — project type, language, framework, config, directory structure
2. **Structural Analysis** — component inventory, dependency graph, layer architecture, entry points
3. **Behavioral Analysis** — data flow, integration points, error handling, state management
4. **Quality Assessment** — test coverage, code smells, security, performance
5. **Tech Debt Scoring** — grade each dimension A-F (see below)

## Tech Debt Grading (A-F)

| Dimension | A (Clean) | C (Strained) | F (Rewrite) |
|---|---|---|---|
| Architecture | Clear layers, SRP | Muddled boundaries | Big ball of mud |
| Code Quality | Consistent, idiomatic | Mixed styles, duplication | Incomprehensible |
| Security | OWASP compliant | Missing auth on some endpoints | Exposed credentials |
| Performance | Optimized, monitored | Some bottlenecks | Unusable at scale |
| Tests | >80% coverage | 40-60%, gaps | No tests |
| Docs | Up to date | Outdated, gaps | None |
| Dependencies | Current, minimal | Major versions behind | Abandoned deps |
| DevOps | Full CI/CD, IaC | Basic CI only | No automation |

**Overall grade:** Weighted average. Architecture and Security weighted 2x.

---

## ADR Template

```markdown
## ADR-[N]: [Descriptive Title]
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-[M]
**Date:** [YYYY-MM-DD]
**Deciders:** [Names/roles]

### Context
[Problem, forces, constraints]

### Decision
[What change are we making?]

### Rationale
[Why? What evidence?]

### Alternatives Considered
| Option | Pros | Cons | Why rejected |

### Consequences
Positive: [...] | Negative: [...] | Risks: [...]
```

---

## Migration Planning

Process: Document AS-IS -> Define TO-BE (ADRs) -> Map Gap -> Sequence -> Strangler Boundary -> Execute -> Decommission

### Sequencing Criteria (priority order)
1. Risk — riskiest parts early
2. Value — highest business value first
3. Coupling — least-coupled components first
4. Data — data models before business logic
5. Dependencies — bottom-up (shared libs -> core -> edge)

### Strangler Fig Pattern
Proxy in front of legacy -> route new features to new code -> gradually migrate existing -> decommission old.
