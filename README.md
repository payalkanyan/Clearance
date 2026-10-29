# Clearance

An agent that tells developers how hard it is to get their OAuth app approved with any provider, how long it will take, what might block them, and what they must do themselves, with every claim labelled by how it was verified.

## Architecture

```mermaid
flowchart TD
    A[1. Input and cache check<br/>Demo apps served instantly] --> B[2. Discover and scrape<br/>Firecrawl, LLM fetch fallback]
    B --> C[3. Probe developer portal<br/>Record login or paid gates]
    C --> D[4. Extract guide<br/>One LLM call, URL plus quote]
    D --> E[5. Citation check<br/>Quote must match page]
    E --> F[6. Score and Composio status<br/>Rubric rules, cached list]
    F --> G[7. Guide and UI<br/>Streamed, shareable link]

    classDef tool fill:#E1F5EE,stroke:#0F6E56,color:#085041
    classDef llm fill:#EEEDFE,stroke:#534AB7,color:#3C3489
    classDef io fill:#F1EFE8,stroke:#5F5E5A,color:#444441
    class A,G io
    class B,C,E,F tool
    class D llm
```

Only stage 4 uses an LLM. Everything else is tools or plain code.