# Observability & Operational Excellence
Structured logging, distributed tracing, metrics, health checks, and alerting patterns for production systems.

## 1. The Three Pillars of Observability
| Pillar | What | Answers | Tools |
|---|---|---|---|
| **Logs** | Discrete events with context | "What happened?" | ELK, Loki, CloudWatch |
| **Metrics** | Aggregated numerical measurements | "How is it performing?" | Prometheus, Datadog, CloudWatch |
| **Traces** | Request journey across services | "Where did it go?" | Jaeger, Zipkin, OpenTelemetry |

### The Missing Pillar: Events
Structured domain events that capture business-meaningful occurrences. Not just errors — also "loan approved", "payment processed", "user upgraded".

## 2. Structured Logging

### Log Format (JSON)
Every log entry must be machine-parseable:
```json
{
  "timestamp": "2026-01-15T10:30:45.123Z",
  "level": "ERROR",
  "service": "loan-service",
  "traceId": "abc123def456",
  "spanId": "span789",
  "correlationId": "req-001",
  "userId": "usr-42",
  "tenantId": "tenant-acme",
  "message": "Failed to process disbursement",
  "error": {
    "type": "InsufficientFundsException",
    "message": "Account balance below required amount",
    "stackTrace": "..."
  },
  "context": {
    "loanId": "loan-123",
    "amount": 50000,
    "currency": "EUR"
  }
}
```

### Log Levels
| Level | When | Example |
|---|---|---|
| **TRACE** | Extremely detailed debugging (disabled in prod) | Method entry/exit, variable values |
| **DEBUG** | Development-time details | SQL queries, request/response bodies |
| **INFO** | Normal business operations | "Loan application submitted", "User logged in" |
| **WARN** | Unexpected but recoverable | Retry triggered, deprecated API used, slow query |
| **ERROR** | Operation failed, needs attention | Unhandled exception, external service down |
| **FATAL** | System cannot continue | Database unreachable, out of memory |

### Logging Rules
* **Always structured** — JSON in production, human-readable in development
* **Always include correlation IDs** — traceId, correlationId, tenantId, userId
* **Never log secrets** — passwords, tokens, API keys, PII (mask or omit)
* **Log at boundaries** — incoming requests, outgoing calls, state transitions
* **Include context** — entity IDs, amounts, operation names (not just "error occurred")
* **Don't log for debugging** — use a debugger. Logs are for production operations.
* **Rate-limit repetitive logs** — if the same error fires 1000x/sec, log the first + count

### Sensitive Data Handling
| Data Type | Action |
|---|---|
| Passwords, tokens | Never log |
| SSN, national IDs | Never log |
| Email addresses | Mask: `p***@example.com` |
| Phone numbers | Mask: `***-***-1234` |
| Bank accounts | Mask: `****5678` |
| Loan amounts, dates | OK to log (business context) |
| Entity IDs | OK to log |

## 3. Distributed Tracing

### Core Concepts
| Term | Definition |
|---|---|
| **Trace** | The complete journey of a request across all services |
| **Span** | A single operation within a trace (e.g., one HTTP call, one DB query) |
| **Context propagation** | Passing traceId/spanId across service boundaries (headers) |
| **Baggage** | Key-value pairs propagated with the trace (tenantId, userId) |

### What to Trace
* All HTTP requests (inbound and outbound)
* Database queries (with query type, duration, table)
* Message queue publish/consume
* Cache hits and misses
* External API calls
* Long-running business operations (multi-step workflows)

### Span Attributes (Standard)
```
http.method = "POST"
http.url = "/api/loans"
http.status_code = 201
db.system = "postgresql"
db.statement = "SELECT..."  (parameterized — no values)
db.operation = "SELECT"
messaging.system = "kafka"
messaging.destination = "loan-events"
```

### Context Propagation Headers
```
traceparent: 00-{traceId}-{spanId}-{flags}
tracestate: vendor=value
baggage: tenantId=acme,userId=42
```

### OpenTelemetry (Standard)
* Use OpenTelemetry SDK for instrumentation (vendor-neutral)
* Auto-instrumentation for HTTP, gRPC, database clients
* Manual spans for business logic boundaries
* Export to any backend: Jaeger, Zipkin, Datadog, Azure Monitor

## 4. Metrics

### The Four Golden Signals (Google SRE)
| Signal | Measures | Example Metric |
|---|---|---|
| **Latency** | Time to serve a request | `http_request_duration_seconds` |
| **Traffic** | Demand on the system | `http_requests_total` |
| **Errors** | Rate of failed requests | `http_errors_total` |
| **Saturation** | How full/utilized resources are | `cpu_usage_percent`, `queue_depth` |

### RED Method (Request-focused)
For every service:
* **R**ate — requests per second
* **E**rrors — errors per second
* **D**uration — latency distribution (p50, p95, p99)

### USE Method (Resource-focused)
For every resource (CPU, memory, disk, network):
* **U**tilization — % of capacity used
* **S**aturation — queue length / backlog
* **E**rrors — error count

### Metric Types
| Type | Use | Example |
|---|---|---|
| **Counter** | Always increasing values | Total requests, total errors |
| **Gauge** | Values that go up and down | Current connections, queue depth, temperature |
| **Histogram** | Distribution of values | Response time buckets (p50, p95, p99) |
| **Summary** | Pre-calculated quantiles | Client-side latency percentiles |

### Business Metrics (Don't Forget These)
* Loan applications submitted / hour
* Approval rate (approved / total)
* Average processing time (submission → decision)
* Revenue per transaction
* User activation / retention rates

## 5. Health Checks

### Standard Endpoints
| Endpoint | Purpose | Response |
|---|---|---|
| `GET /health` | Basic liveness — process is running | `200 OK` / `503 Service Unavailable` |
| `GET /ready` | Readiness — can handle traffic | `200 OK` / `503 Not Ready` |
| `GET /health/details` | Detailed status (internal only) | JSON with dependency statuses |

### Liveness vs. Readiness
| Check | Liveness (`/health`) | Readiness (`/ready`) |
|---|---|---|
| Purpose | "Should we restart this?" | "Should we send traffic?" |
| Fails when | Process is deadlocked/crashed | Dependencies unavailable |
| Action on failure | Container restart | Remove from load balancer |
| Checks | Minimal — can respond to HTTP | DB connection, cache, external services |

### Health Check Response Format
```json
{
  "status": "healthy",
  "version": "2.3.1",
  "uptime": "4d 12h 30m",
  "checks": {
    "database": { "status": "healthy", "latency_ms": 3 },
    "redis": { "status": "healthy", "latency_ms": 1 },
    "kafka": { "status": "degraded", "message": "1 of 3 brokers unreachable" },
    "external-credit-api": { "status": "healthy", "latency_ms": 120 }
  }
}
```

### Health Check Rules
* Liveness should NEVER check external dependencies (or restarts cascade)
* Readiness checks should have timeouts (2-5s max per dependency)
* Cache dependency health independently (don't check on every request)
* Include version in health response for deployment verification
* Protect `/health/details` — internal network only, not public

## 6. Alerting Strategy

### Alert Severity Levels
| Level | Response Time | Example |
|---|---|---|
| **Critical (P1)** | Immediate (page on-call) | Service down, data loss, security breach |
| **High (P2)** | Within 1 hour | Error rate > 5%, latency > 5s, degraded service |
| **Medium (P3)** | Within business hours | Disk 80% full, certificate expiring, dependency slow |
| **Low (P4)** | Next sprint | Tech debt metric degraded, non-critical warning |

### Alerting Best Practices
* **Alert on symptoms, not causes** — "users getting errors" not "CPU at 90%"
* **Alert on SLO burn rate** — "at this rate, we'll breach SLO in 2 hours"
* **Every alert must be actionable** — if you can't act on it, it's noise
* **Include runbook link in every alert** — what to check, how to mitigate
* **Set proper thresholds** — alert on sustained anomalies, not single spikes
* **Avoid alert fatigue** — fewer, better alerts > many ignored alerts

### SLO-Based Alerting
```
SLI: 99.9% of requests complete in < 500ms
Error budget: 0.1% = ~43 minutes/month of breaches

Alert when:
* 5% of error budget consumed in 1 hour (fast burn) → page
* 10% of error budget consumed in 6 hours (slow burn) → ticket
```

## 7. Error Handling & Reporting

### Error Classification
| Category | Action | Alert |
|---|---|---|
| **Expected errors** | Handle gracefully, return user-friendly message | No alert (maybe metric) |
| **Transient errors** | Retry with backoff, then fail | Alert if retry exhausted |
| **Permanent errors** | Fail fast, clear error message | Alert on new error types |
| **System errors** | Circuit breaker, fallback | Alert immediately |

### Error Context (What to Capture)
* Exception type and message
* Stack trace (first occurrence, then deduplicate)
* Request context (URL, method, user, tenant)
* Correlation IDs (trace, request, session)
* Input that caused the error (sanitized)
* Retry count (if applicable)
* Timestamp and service/instance

### Error Reporting Rules
* **Group by root cause** — don't create noise for the same underlying issue
* **Track error rate, not just count** — 10 errors at 100 RPS is fine; 10 at 10 RPS is not
* **First-seen / last-seen timestamps** — identify new vs. recurring issues
* **Auto-resolve when recovered** — don't leave stale alerts open
* **Link to deployment** — correlate new errors with recent deployments

## 8. Operational Runbooks

### Runbook Template
```markdown
# [Alert Name] Runbook

## What this means
[Plain-language explanation of the alert and its impact]

## Likely causes
1. [Most common cause]
2. [Second most common]
3. [Edge case]

## Diagnosis steps
1. Check [metric/log/dashboard] for [pattern]
2. Run [command] to verify [state]
3. Look for [symptom] in [location]

## Mitigation
* Immediate: [Quick fix to restore service]
* Permanent: [Root cause fix]

## Escalation
* If not resolved in [time]: contact [team/person]
* If data loss suspected: follow [incident process]
```

### Required Runbooks (Minimum)
* Service won't start
* High error rate
* High latency
* Database connection exhaustion
* Disk space full
* Certificate expiry
* Dependency unreachable
* Memory leak suspected
* Deployment rollback procedure

## 9. Dashboard Design

### Service Dashboard (Per Service)
| Section | Content |
|---|---|
| **Status** | Current health, last deployment, version |
| **Traffic** | RPS, active connections, queue depth |
| **Latency** | p50, p95, p99 over time |
| **Errors** | Error rate, top error types, recent errors |
| **Resources** | CPU, memory, disk, connections |
| **Dependencies** | Status and latency of each dependency |
| **Business** | Domain-specific KPIs (applications/hour, etc.) |

### Dashboard Rules
* **One dashboard per service** — don't mix concerns
* **Show SLO compliance prominently** — remaining error budget
* **Time-aligned graphs** — all panels share the same time range
* **Annotations for deployments** — vertical lines on graphs at deploy time
* **Sensible defaults** — last 6 hours, auto-refresh every 30s
