# Document Template Library

## General Guidance
All generated documents MUST follow a 6-dimension tabbed structure to ensure consistent coverage, unless specifically generating a 'Light' mode document (linear, no tabs).
1. **Context**: Problem/vision, scope, stakeholders, personas.
2. **Business**: Impact, metrics, cost-benefit, OKRs.
3. **Functional**: User flows, requirements, prototype handoff briefs, stories.
4. **Technical**: Architecture diagrams, data model, APIs, NFRs.
5. **Assessment**: Findings, scorecard, risks, tech debt.
6. **Action**: Roadmap, next steps, migration plan, decisions.

Dynamically choose the most appropriate components (from the snippets below) to represent the data in each tab.

## 1. Base HTML Shell
Use this shell as the foundation for the document. Insert the generated content inside `<main class="wrap">`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document Title</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #3B82F6;
            --bg-dark: #1E293B;
            --surface: #FFFFFF;
            --border: #DDDDDD;
            --text: #1E293B;
            --muted: #777777;
            --radius: 8px;
        }
        body { font-family: 'Inter', sans-serif; background: #F8FAFC; color: var(--text); line-height: 1.6; padding: 40px; }
        .wrap { max-width: 1200px; margin: 0 auto; background: var(--surface); border-radius: var(--radius); padding: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        h1, h2, h3 { color: var(--bg-dark); }
        .tabs { display: flex; gap: 8px; margin-bottom: 24px; border-bottom: 1px solid var(--border); padding-bottom: 12px; flex-wrap: wrap; }
        .tab { padding: 8px 16px; border: 1px solid var(--border); border-radius: 20px; cursor: pointer; background: var(--surface); font-weight: 500; transition: all 0.2s; }
        .tab:hover { border-color: var(--bg-dark); }
        .tab.active { background: var(--bg-dark); color: white; border-color: var(--bg-dark); }
        .panel { display: none; }
        .panel.on { display: block; animation: fadeIn 0.3s; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        .card { border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; margin-bottom: 24px; background: var(--surface); box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
        .ref-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 14px; }
        .ref-table th, .ref-table td { border: 1px solid var(--border); padding: 12px; text-align: left; }
        .ref-table th { background: #F1F5F9; color: var(--bg-dark); }
        .mock-ui { border: 2px dashed var(--border); padding: 24px; background: #FAFAFA; border-radius: var(--radius); margin-top: 16px; }
        details { border: 1px solid var(--border); padding: 16px; border-radius: var(--radius); margin-bottom: 16px; background: var(--surface); }
        summary { font-weight: 600; cursor: pointer; color: var(--bg-dark); }
    </style>
</head>
<body>
    <main class="wrap">
        <!-- HEADER / HERO GOES HERE -->
        
        <!-- TABS NAV GOES HERE -->

        <!-- PANELS GO HERE -->
    </main>

    <script>
        function go(id) {
            document.querySelectorAll('.panel').forEach(p => p.classList.remove('on'));
            document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
            document.getElementById('p-' + id).classList.add('on');
            document.getElementById('btn-' + id).classList.add('active');
        }
    </script>
</body>
</html>
```

## 2. Component Snippets

### Hero Section
```html
<div style="margin-bottom: 40px; padding-bottom: 24px; border-bottom: 1px solid var(--border);">
    <span style="background: var(--primary); color: white; padding: 4px 12px; border-radius: 4px; font-size: 12px; font-weight: 600; text-transform: uppercase;">{{TOPIC_CHIP}}</span>
    <h1 style="font-size: 36px; margin: 16px 0 8px; letter-spacing: -0.02em;">{{TITLE}}</h1>
    <p style="color: var(--muted); font-size: 18px; max-width: 800px;">{{DESCRIPTION}}</p>
</div>
```

### Tabs Navigation
```html
<nav class="tabs">
    <button id="btn-context" class="tab active" onclick="go('context')">Context</button>
    <button id="btn-business" class="tab" onclick="go('business')">Business</button>
    <button id="btn-functional" class="tab" onclick="go('functional')">Functional</button>
    <button id="btn-technical" class="tab" onclick="go('technical')">Technical</button>
    <button id="btn-assessment" class="tab" onclick="go('assessment')">Assessment</button>
    <button id="btn-action" class="tab" onclick="go('action')">Action</button>
</nav>
```

### Panel Shell
```html
<section id="p-context" class="panel on">
    <!-- Card components go here -->
</section>
<!-- Repeat for other 5 panels, removing 'on' class from the rest and changing the ID -->
```

### Generic Card
```html
<div class="card">
    <h3 style="margin-top: 0; margin-bottom: 12px; font-size: 20px;">{{CARD_TITLE}}</h3>
    <p style="color: var(--muted);">{{CARD_CONTENT}}</p>
</div>
```

### Concept Architecture Card
```html
<div class="card">
    <h3 style="margin-top: 0; margin-bottom: 16px; font-size: 20px;">Concept Architecture</h3>
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="padding: 16px; border-left: 4px solid var(--primary); background: #FAFAFA; border-radius: 0 var(--radius) var(--radius) 0;">
            <strong style="color: var(--bg-dark); display: block; margin-bottom: 4px;">Foundation (The Why)</strong>
            <span style="color: var(--muted); font-size: 14px;">{{VALUE_PROP_AND_HYPOTHESIS}}</span>
        </div>
        <div style="padding: 16px; border-left: 4px solid #10B981; background: #FAFAFA; border-radius: 0 var(--radius) var(--radius) 0;">
            <strong style="color: var(--bg-dark); display: block; margin-bottom: 4px;">Framework (The What)</strong>
            <span style="color: var(--muted); font-size: 14px;">{{DOMAIN_MODELS_AND_ENTITIES}}</span>
        </div>
        <div style="padding: 16px; border-left: 4px solid #F59E0B; background: #FAFAFA; border-radius: 0 var(--radius) var(--radius) 0;">
            <strong style="color: var(--bg-dark); display: block; margin-bottom: 4px;">Plumbing & Wiring (Logic & Flow)</strong>
            <span style="color: var(--muted); font-size: 14px;">{{BUSINESS_RULES_AND_JOURNEYS}}</span>
        </div>
        <div style="padding: 16px; border-left: 4px solid #8B5CF6; background: #FAFAFA; border-radius: 0 var(--radius) var(--radius) 0;">
            <strong style="color: var(--bg-dark); display: block; margin-bottom: 4px;">Facade & Interior (The Experience)</strong>
            <span style="color: var(--muted); font-size: 14px;">{{UI_UX_AND_TOUCHPOINTS}}</span>
        </div>
    </div>
</div>
```

### Reference Table
```html
<table class="ref-table">
    <thead>
        <tr>
            <th>{{Header 1}}</th>
            <th>{{Header 2}}</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{{Data 1}}</td>
            <td>{{Data 2}}</td>
        </tr>
    </tbody>
</table>
```

### Prototype Handoff Brief Container
```html
<div class="card">
    <h3 style="margin-top: 0;">Prototype Handoff Brief: {{SCREEN_NAME}}</h3>
    <div class="mock-ui">
        <!-- This is a written brief for product-develop to build — do NOT render the actual UI here -->
        <p><strong>Purpose:</strong> {{SCREEN_PURPOSE}}</p>
        <p><strong>States:</strong> {{STATES_LIST}} (e.g., empty, loading, populated, error)</p>
        <p><strong>Interactions / JS behavior:</strong> {{INTERACTION_BEHAVIOR}} (what happens on click, submit, hover, validation, etc. — precise enough to build without further clarification)</p>
        <p><strong>Inputs & validation:</strong> {{INPUTS_AND_VALIDATION}}</p>
        <p><strong>Data shape:</strong> {{DATA_SHAPE}}</p>
        <p><strong>Edge cases:</strong> {{EDGE_CASES}}</p>
        <p><strong>Layout notes:</strong> {{ROUGH_LAYOUT_NOTES}} (optional — bullet list of regions/hierarchy, not a built mockup)</p>
    </div>
</div>
```

### Diagram Container
```html
<div class="card">
    <h3 style="margin-top: 0;">Diagram: {{DIAGRAM_TITLE}}</h3>
    <div style="background: #FAFAFA; padding: 24px; border-radius: var(--radius); text-align: center;">
        <!-- Insert SVG or image here -->
        {{DIAGRAM_CONTENT}}
    </div>
</div>
```

### ADR / Collapsible Details
```html
<details>
    <summary>ADR-{{ID}}: {{DECISION_TITLE}}</summary>
    <div style="padding-top: 16px; font-size: 14px;">
        <p><strong>Context:</strong> {{CONTEXT}}</p>
        <p><strong>Decision:</strong> {{DECISION}}</p>
        <p><strong>Rationale:</strong> {{RATIONALE}}</p>
        <p><strong>Alternatives Considered:</strong> {{ALTERNATIVES}}</p>
    </div>
</details>
```
