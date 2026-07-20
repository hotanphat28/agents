# Performance Engineering

Caching, lazy loading, database optimization, network efficiency, profiling, and performance budgets.

---

## 1. Performance Principles

### The Golden Rules
1. **Measure before optimizing** — never guess where the bottleneck is
2. **Optimize the critical path** — the slowest link in the chain users experience
3. **Cache aggressively, invalidate carefully** — caching solves most read performance
4. **Reduce work** — the fastest code is code that doesn't run
5. **Reduce distance** — process data close to where it's needed
6. **Do work asynchronously** — don't block users waiting for non-critical operations
7. **Set budgets** — define acceptable limits before building

### Performance Budget
| Metric | Web Target | API Target |
|---|---|---|
| First Contentful Paint (FCP) | < 1.8s | — |
| Largest Contentful Paint (LCP) | < 2.5s | — |
| Cumulative Layout Shift (CLS) | < 0.1 | — |
| First Input Delay (FID) | < 100ms | — |
| Time to Interactive (TTI) | < 3.8s | — |
| API response (p50) | — | < 100ms |
| API response (p95) | — | < 500ms |
| API response (p99) | — | < 1s |
| Page weight (total) | < 1.5MB | — |
| JavaScript bundle | < 300KB gzipped | — |

---

## 2. Caching Strategy

### Cache Hierarchy (Closest to User → Source)
| Layer | Location | TTL | Hit Ratio | Use Case |
|---|---|---|---|---|
| **Browser cache** | Client | Hours-days | 80-95% | Static assets (CSS, JS, images, fonts) |
| **CDN cache** | Edge | Minutes-hours | 60-90% | Static + semi-dynamic content |
| **Application cache** | In-memory (local) | Seconds-minutes | 70-95% | Hot data, computed results |
| **Distributed cache** | Redis/Memcached | Minutes-hours | 60-85% | Session data, API responses, computed aggregates |
| **Database cache** | Query cache / buffer pool | Auto | Varies | Recent query results |

### Caching Patterns

| Pattern | How | Use When |
|---|---|---|
| **Cache-aside** | App checks cache → miss → fetch from DB → populate cache | General purpose, most common |
| **Read-through** | Cache fetches from DB on miss automatically | Transparent to application |
| **Write-through** | Write to cache + DB simultaneously | Strong consistency required |
| **Write-behind** | Write to cache, async flush to DB | High write throughput, eventual consistency OK |
| **Refresh-ahead** | Proactively refresh before expiry | Predictable access patterns |

### Cache Invalidation Strategies
| Strategy | When to Use |
|---|---|
| **TTL (Time-to-Live)** | Acceptable staleness window exists (most APIs) |
| **Event-driven invalidation** | Data changes must reflect immediately (Kafka event → purge) |
| **Version keys** | `user:42:v3` — increment version on write, old keys expire naturally |
| **Tag-based purge** | CDN: purge all pages tagged "product-catalog" |

### Cache Anti-Patterns
- **Cache stampede** — many requests miss simultaneously → add jitter + lock
- **Unbounded cache** — memory grows forever → set max size + eviction policy (LRU)
- **Caching errors** — 500 responses cached → cache only successful responses
- **Over-caching** — data that changes frequently → short TTL or event-driven
- **Cache without metrics** — can't optimize what you don't measure → track hit rate

---

## 3. Database Performance

### Query Optimization Hierarchy
1. **Don't query at all** — use cache or precomputed results
2. **Query less data** — select only needed columns, filter at DB level
3. **Query efficiently** — proper indexes, optimized joins, avoid N+1
4. **Query faster** — read replicas, partitioning, materialized views

### Indexing Strategy

| Index Type | Use Case | Trade-off |
|---|---|---|
| **B-tree** (default) | Equality, range, sorting, prefix search | Write overhead, storage |
| **Hash** | Exact equality only | Fast equality, no range |
| **GIN** | Full-text search, JSONB, arrays | Slow writes, fast reads |
| **GiST** | Geospatial, range types | Specialized |
| **Partial index** | Filter on subset of rows | Smaller, faster for filtered queries |
| **Composite index** | Multi-column queries | Column order matters! |
| **Covering index** | Includes all needed columns | Index-only scan (no table lookup) |

### Index Rules
- **Index columns in WHERE, JOIN, ORDER BY** — in that priority
- **Composite index column order** — most selective column first (equality before range)
- **Don't over-index** — each index slows writes and uses storage
- **Monitor unused indexes** — drop them
- **Index for your queries, not your schema** — analyze actual query patterns

### N+1 Query Problem
```
❌ Bad: Load 100 loans, then 100 separate queries for borrower details
✅ Good: JOIN in single query, or batch fetch with IN clause
✅ Good: Use DataLoader pattern for GraphQL
```

### Connection Pooling
| Setting | Guideline |
|---|---|
| Pool size | `(2 × CPU cores) + disk spindles` (PostgreSQL recommendation) |
| Max connections | Total across all instances < DB max_connections - 20% headroom |
| Idle timeout | 5-10 minutes (don't hold connections indefinitely) |
| Connection validation | Lightweight query on checkout (e.g., `SELECT 1`) |

### Database Scaling Patterns
| Pattern | When | Complexity |
|---|---|---|
| **Read replicas** | Read-heavy workload (>80% reads) | Low |
| **Connection pooling** (PgBouncer) | Many short-lived connections | Low |
| **Table partitioning** | Large tables (>10M rows), time-series data | Medium |
| **Materialized views** | Complex aggregations queried frequently | Medium |
| **Vertical sharding** | Separate concerns into different DBs | Medium |
| **Horizontal sharding** | Single table exceeds single-server capacity | High |
| **CQRS** | Very different read/write patterns | High |

---

## 4. API Performance

### Pagination
| Strategy | Use Case | Pros/Cons |
|---|---|---|
| **Offset/Limit** | Simple lists, UI pages | Simple but slow at high offsets |
| **Cursor-based** | Infinite scroll, large datasets | Fast, consistent, complex implementation |
| **Keyset** | Sorted datasets (by ID, date) | Fast, no offset skip, requires stable sort |

### Response Optimization
- **Select only needed fields** — implement sparse fieldsets or GraphQL-style field selection
- **Compress responses** — gzip/brotli (automatic in most frameworks)
- **Paginate by default** — never return unbounded lists
- **Use ETags** — return 304 Not Modified when data hasn't changed
- **Batch endpoints** — allow fetching multiple resources in one request

### Rate Limiting
| Strategy | Use Case |
|---|---|
| **Fixed window** | Simple, per-minute/hour limits |
| **Sliding window** | Smooth rate enforcement |
| **Token bucket** | Allow bursts up to capacity |
| **Leaky bucket** | Strict constant rate output |

### Async Processing Pattern
```
Request → Validate → Enqueue → Return 202 Accepted
                         ↓
              Background Worker → Process → Notify via webhook/SSE
```
Use when: processing > 2s, result not needed immediately, can retry independently.

---

## 5. Frontend Performance

### Critical Rendering Path
1. HTML downloaded and parsed → DOM
2. CSS downloaded and parsed → CSSOM
3. DOM + CSSOM → Render Tree
4. Layout → Paint → Composite

**Optimize by:** minimizing render-blocking resources, critical CSS inlining, defer non-critical JS.

### Loading Strategies
| Technique | What | When |
|---|---|---|
| **Lazy loading** | Defer off-screen content | Images, videos, below-fold components |
| **Code splitting** | Separate bundles by route/feature | SPAs with many routes |
| **Prefetching** | Load resources for likely next action | Next page, hover over link |
| **Preloading** | Load critical resources immediately | Fonts, above-fold images, critical JS |
| **Tree shaking** | Remove unused exports | Build time, reduce bundle size |
| **Dynamic imports** | Load modules on demand | Large libraries used conditionally |

### Image Optimization
| Format | Use Case |
|---|---|
| **WebP** | General photos and illustrations (30% smaller than JPEG) |
| **AVIF** | Best compression (50% smaller), limited browser support |
| **SVG** | Icons, logos, simple illustrations (scales perfectly) |
| **PNG** | Transparency needed, exact pixel rendering |

**Rules:**
- Serve responsive images (`srcset` with multiple sizes)
- Lazy load below-fold images (`loading="lazy"`)
- Set explicit width/height to prevent CLS
- Use CDN with automatic format conversion

### Web Vitals Optimization
| Metric | Fix |
|---|---|
| **LCP** | Preload hero image, inline critical CSS, fast server response |
| **FID/INP** | Break long tasks (>50ms), defer non-critical JS, use web workers |
| **CLS** | Set image dimensions, no dynamic content insertion above fold, font-display: swap |

---

## 6. Network Optimization

### HTTP/2 and HTTP/3 Best Practices
- **Multiplexing** — no need for domain sharding or sprite sheets
- **Server push** — push critical CSS/JS with initial HTML (H2)
- **Header compression** — HPACK reduces redundant header bytes
- **Connection reuse** — single connection per origin

### Payload Optimization
| Technique | Savings |
|---|---|
| Gzip compression | 60-80% for text content |
| Brotli compression | 15-25% better than gzip |
| JSON field minimization | Only return what client needs |
| Protocol Buffers/MessagePack | 30-50% smaller than JSON |
| GraphQL (precise queries) | Eliminates over-fetching |

### DNS and Connection
- **DNS prefetch** — `<link rel="dns-prefetch" href="//api.example.com">`
- **Preconnect** — `<link rel="preconnect" href="//cdn.example.com">`
- **Keep-alive** — reuse TCP connections (default in HTTP/1.1+)
- **Connection pooling** — limit concurrent connections per origin

---

## 7. Profiling & Diagnosis

### When to Profile
- Response time exceeds budget (p95 > 500ms)
- CPU/memory usage unexpectedly high
- Before and after optimization (prove impact)
- Periodic production profiling (continuous profiling)

### Profiling Approach
1. **Reproduce** — identify the slow operation reliably
2. **Measure baseline** — record current metrics
3. **Profile** — identify WHERE time is spent (not guess)
4. **Analyze** — find the biggest contributor (Pareto: 20% of code = 80% of time)
5. **Optimize** — fix the specific bottleneck
6. **Verify** — measure again, confirm improvement
7. **Monitor** — ensure it stays fast

### Common Bottleneck Patterns
| Symptom | Likely Cause | Fix |
|---|---|---|
| High CPU, fast GC | CPU-bound computation | Algorithm optimization, caching, parallelism |
| High CPU, slow GC | Memory churn (object allocation) | Object pooling, reduce allocations |
| Low CPU, high latency | I/O bound (DB, network, disk) | Async I/O, caching, connection pooling |
| Memory growing over time | Memory leak | Profile heap, find retained references |
| Sporadic high latency | GC pauses | Tune GC, reduce object creation |
| Latency spikes at scale | Thread/connection exhaustion | Pool sizing, async patterns, backpressure |

### Load Testing
| Type | Purpose | Tool |
|---|---|---|
| **Smoke test** | Verify system works under minimal load | k6, Artillery |
| **Load test** | Expected production traffic | k6, Gatling, JMeter |
| **Stress test** | Find breaking point | k6 (ramp to failure) |
| **Soak test** | Find memory leaks, resource exhaustion | 4-24 hour sustained load |
| **Spike test** | Handle sudden traffic bursts | Rapid ramp-up/down |

### Load Test Rules
- Test with realistic data (not empty responses)
- Warm up caches before measuring
- Test from outside your infrastructure (real network conditions)
- Measure at percentiles (p50, p95, p99), not averages
- Set pass/fail criteria before running

---

## 8. Performance Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| **Premature optimization** | Optimizing before measuring | Profile first, optimize bottlenecks only |
| **N+1 queries** | 1 + N database roundtrips | Batch fetch, JOIN, DataLoader |
| **Unbounded queries** | SELECT * with no LIMIT | Always paginate, always limit |
| **Synchronous I/O on hot path** | Blocks threads waiting for I/O | Async I/O, background processing |
| **Missing indexes** | Full table scans on queries | EXPLAIN ANALYZE, add targeted indexes |
| **Over-indexing** | Slow writes, wasted storage | Remove unused indexes, composite instead of multiple single |
| **No connection pooling** | New TCP/TLS handshake per query | Use pool (HikariCP, PgBouncer) |
| **Large payloads** | Excessive bandwidth, slow parsing | Paginate, field selection, compression |
| **Cache stampede** | All requests hit DB after cache expires | Jitter TTL, lock + refresh, refresh-ahead |
| **Chatty microservices** | Too many inter-service calls for one operation | Aggregate endpoint, BFF pattern, denormalize |

---

## 9. Scalability Patterns

### Horizontal Scaling Readiness Checklist
- [ ] Application is stateless (no local session, no local file storage)
- [ ] Sessions stored externally (Redis, DB)
- [ ] File uploads go to object storage (S3, Blob Storage)
- [ ] Configuration externalized (env vars, config service)
- [ ] Database connections pooled with limits
- [ ] Background jobs use distributed queue (not in-process)
- [ ] Health checks enable load balancer traffic management
- [ ] Graceful shutdown handles in-flight requests

### Backpressure
When a system is overwhelmed:
1. **Queue** — buffer requests and process at sustainable rate
2. **Shed load** — reject lowest-priority requests (429 Too Many Requests)
3. **Degrade gracefully** — disable non-critical features, serve cached/stale data
4. **Circuit breaker** — stop calling failing downstream services

### Circuit Breaker States
```
Closed → (failures exceed threshold) → Open → (timeout expires) → Half-Open → (success) → Closed
                                                                              → (failure) → Open
```
- **Closed**: Normal operation, count failures
- **Open**: Fast-fail immediately, don't call downstream
- **Half-Open**: Allow one probe request, decide based on result
