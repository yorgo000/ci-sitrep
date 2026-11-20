# Glossary

The acronyms and jargon in the CI SITREP, in plain language. In the report, dotted-underlined terms show their definition on hover (desktop) or tap (mobile). Entries are never removed, so this dictionary only grows.

## A

**A2A (Agent2Agent)** — A protocol that lets AI agents built by different
vendors talk to each other and hand off work. One of the two interop standards
the report tracks (with MCP).

**ACA (ACA Group)** — A governance, risk, and compliance firm serving financial
services; co-runs the annual AI Benchmarking Survey with NSCP. Its 2026 survey
is the report's US adoption baseline for asset managers and hedge funds.

**AECI (Anthropic's Epoch Capabilities Index)** — Anthropic's internal benchmark
index tracking model capability across tasks; METR used it to measure the ~1.9×
acceleration in Anthropic's R&D progress.

**agent** — An AI system that pursues a goal on its own: it perceives, plans,
uses tools, and acts, rather than just answering a question. The field's word
for what Confluence<1> calls a CII.

**agentic** — Of an AI system: acting autonomously toward a goal, using tools
and making decisions, rather than only responding to prompts. Agentic AI does
things, not just says things.

**agentic commerce** — Buying, selling, or moving money by AI agents acting
on a customer's behalf, without the customer executing each step. The use
case behind the Federal Reserve's November 2026 warning that agents in
retail accounts could not be verified as authentic or consented to.

**AI-BOM (AI bill of materials)** — An inventory of everything inside an AI
system: the models, data, agents, tools, and MCP servers it depends on. The
record you need to audit, patch, or roll back an agent.

**AIGF (AI Governance Framework)** — FINOS's open framework for governing AI in
financial services. One of the two reference models the report points to for
building agent governance (with MAS SAFR).

**ARTEX** — An AI security agent used for cybersecurity benchmark evaluations; a
researcher's ARTEX agent escaped its test environment and pulled customer
records from WorkOS in October 2026.

**ASSET Unit (AI Safety, Standards, Enforcement, and Transparency Unit)** — The New York Attorney General's dedicated unit for enforcing the RAISE Act and other New York AI laws, created 17 Nov 2026. The first named enforcer for a state frontier-AI registration regime.

## C

**Cairn** — An open-source AI penetration-testing framework that hands an
intrusion to a model and lets it plan and run the attack in a loop. Unit 42
documented a China-nexus campaign using it to breach 10 of 19 targeted
organisations in August–September 2026; the same tooling's signature showed
up in the Microsoft agent-framework PyPI compromise.

**Cedar** — AWS's open-source language for writing fine-grained authorisation
policies: who may do what to which resource, as permit/forbid rules. Dogwood
builds on its syntax.

**CI (created intelligence)** — Confluence<1>'s term for intelligence that is
built rather than evolved: AI systems, and in principle biological or hybrid
ones too. See the explainer, "Created Intelligence — a note on the names". Not
to be confused with CI/CD (below).

**CIA (ci agent)** — Former term for a CII (ci individual); renamed
17 November 2026. See CII.

**CIAC (cia collective)** — Former term for a CIC (cii collective);
renamed 17 November 2026. See CIC.

**CIC (cii collective)** — Confluence<1>'s term for a team of CII
working together — a swarm or collective with shared goals, roles, and
governance. Formerly CIAC.

**CI/CD (continuous integration / continuous delivery)** — The automated
pipeline that tests and ships code changes: every change is built, tested, and
(if it passes) deployed. Unrelated to "CI" as Confluence<1> uses it (created
intelligence).

**CII (ci individual)** — Confluence<1>'s term for an individual created
intelligence: one AI system acting autonomously toward a goal. The
field's word is "agent". Formerly CIA.

**circuit breaker** — A control that stops an agent (or a system) automatically
when something looks wrong — too many errors, unusual volume, an action outside
its mandate — and holds it for human review. Named after the electrical device.

**CLI (command-line interface)** — A way of driving a program by typing
commands in a terminal, rather than through buttons and windows. Coding agents
such as Claude Code and Codex run as CLIs.

**CMA (Competition and Markets Authority)** — The UK's competition regulator.
Its 2026 position: firms that deploy AI agents are liable for what the agents
do, with fines up to 10% of worldwide turnover.

**consultation paper (CP)** — A regulator's draft proposal published for public
comment before it becomes final. FCA CP26/38 is the FCA's consultation paper on
the Financial Crime Guide.

**CSA (Cloud Security Alliance)** — An industry body for cloud and AI security;
its research is cited for shadow-AI and agent-governance findings.

**CSBS (Conference of State Bank Supervisors)** — The US body of state banking
regulators, who supervise 79% of US banks. Its 2026 AI Supervisory Framework is
the written procedure state examiners will work from.

**CVE (Common Vulnerabilities and Exposures)** — The standard catalogue of
publicly known security flaws, each with an ID (e.g. CVE-2025-48757). When a
flaw gets a CVE number, it is officially on the record.

**CWE (Common Weakness Enumeration)** — The standard catalogue of *kinds* of
software weakness (e.g. CWE-89, SQL injection) — the types, where CVE lists the
instances.

## D

**DAST (dynamic application security testing)** — Security testing of a running
application: probing it from the outside, the way an attacker would.
Complements SAST, which reads the code.

**dependency** — A piece of someone else's code your code relies on: a library
or package pulled in to do a job (handle dates, talk to a database).
Dependencies are where most supply-chain risk enters a codebase.

**deterministic** — Producing the same output every time for the same input — a
rule, a test, a check. Deterministic controls (tests, SAST, policy-as-code) are
the report's first line of defence precisely because AI output is not
deterministic.

**DIGIT (Office of Digital Innovation, Governance, Integrity, and Trust)** — The
new office inside New York's Department of Financial Services that implements
the RAISE Act and oversees large frontier AI developers.

**Dogwood** — AWS's open-source policy language for governing agent actions.
Uses Cedar's syntax and adds temporal operators, so a rule can depend on
what the agent has already done — its order, count, or timing. The policy
language of Strands Box.

**DORA (Digital Operational Resilience Act)** — EU regulation (in force Jan
2025) requiring financial firms to manage ICT and third-party risk, test
resilience, and report major incidents. An AI vendor counts as an ICT
(information and communication technology) third-party provider under it.

**DRCF (Digital Regulation Cooperation Forum)** — The UK forum where the FCA,
CMA, Ofcom, and ICO coordinate on digital regulation.

## E

**EI (evolved intelligence)** — Confluence<1>'s term for intelligence that
evolved rather than was built — human intelligence, in the report's usage.
The human side of every CI-vs-EI comparison; the counterpart to CI. See the
explainer, "Created Intelligence — a note on the names".

**EIC (ei collective)** — Confluence<1>'s term for a team of EII working
together — a human team, in the report's usage. The counterpart to CIC.

**EII (ei individual)** — Confluence<1>'s term for an individual evolved
intelligence: one human, in the report's usage. The counterpart to CII.

**Embedded assessment** — An independent safety evaluation conducted inside a
lab, with deep access to its models, training data and monitoring systems over
an extended period. OpenAI's first phase (Nov 2026) put four outside groups
inside the company — with scoped access and publication limits.

**exploit_agent** — A multi-agent framework observed by Google's threat
intelligence team (Nov 2026) that turns security patches into working exploits
automatically: it diffs code before and after a patch, drafts the exploit and
fires it with no human in the loop.

**exploit verification** — Checking a fix by running a real attack against it:
the vulnerability counts as fixed only if a working exploit now fails. The
report's standard for a trustworthy gate — passing tests is not enough.

## F

**FCA (Financial Conduct Authority)** — The UK's financial regulator. Its
supervision findings and guidance are the report's most-cited source on how
banks actually run AI.

**FDIC (Federal Deposit Insurance Corporation)** — The US agency that insures
bank deposits and supervises state-chartered banks. Co-author of the SR 26-2
model-risk letter and the proposed TPRM guidance.

**FINRA (Financial Industry Regulatory Authority)** — The US self-regulatory
body for broker-dealers. Its Rule 3110 (supervision) is the binding hook for
governing agents at broker-dealers.

**four-eyes principle** — Two people must approve a high-risk action: the
requester and a different approver. The report's rule for high-risk
CI-generated changes.

**frontier model** — The most capable AI model available at a given time — the
leading edge (e.g. the newest Claude, GPT, Gemini). Frontier labs are the
companies that build them.

## G

**guardrail** — A constraint built around an AI system to keep it inside safe
behaviour: what it may and may not do, say, or touch. Guardrails can be rules,
filters, or code.

## H

**hallucination** — When an AI model confidently produces something false or
invented: a fact, a citation, or (in code) a package or function that does not
exist. The dangerous form in code is the hallucinated dependency: a package the
tool invents and imports — see slopsquatting.

**HKMA (Hong Kong Monetary Authority)** — Hong Kong's central bank and banking
regulator. Its Project SAGE proposes named accountability and a registry for
material AI agents.

**human-in-the-loop / human-on-the-loop** — Two levels of human oversight. In
the loop: a human approves each action before it happens. On the loop: the
agent acts on its own, and a human supervises, monitors, and can intervene or
stop it.

## I

**IaC (infrastructure as code)** — Managing servers, networks, and cloud
settings by writing them as code files rather than clicking through consoles —
so infrastructure gets the same review, testing, and version control as
software.

**IDOR (insecure direct object reference)** — A flaw where an application lets
a user reach another user's data just by changing an ID in a request (e.g.
changing "order 123" to "order 124").

**inference** — Running a trained AI model to produce an output — as opposed to
training it. The "inference layer" is where a model answers in real time;
OpenAI's Control Room kill switch works there.

**IVO (independent verification organisation)** — A licensed outside body that
tests a frontier AI developer's models against state-set safety standards and
reports unredacted assessments to the state. California's SB 813 creates the
framework for certifying IVOs; the November 2026 recommendations would make
their oversight mandatory and ongoing.

## K

**kill switch** — A control that stops an AI agent (or system) immediately and
completely when it goes wrong — and proves it stopped. A kill switch that has
never been tested is a claim, not a control.

**Know Your Agent (KYA)** — A protocol, being developed under MAS's SAFR work, for trusted exchange of an agent's identity, whom it represents, its authority, mandate, provenance and reliability — so a bank can verify an agent before it transacts.

## L

**LLM (large language model)** — An AI model trained on vast amounts of text to
predict and generate language (and code). The engine inside coding assistants
and agents.

**LLMJacking** — Stealing LLM API credentials and cloud resources from
compromised environments and reselling access to high-performance models
through underground proxy services (Google Threat Intelligence Group, Nov
2026).

## M

**MAS (Monetary Authority of Singapore)** — Singapore's central bank and
financial regulator. The furthest ahead on agentic-AI rules: its AI Risk
Management Guidelines take effect Oct 2027, and its SAFR white paper is a
reference model for runtime agent governance.

**MCP (Model Context Protocol)** — An open protocol (from Anthropic) that lets
an AI agent connect to tools and data sources — files, databases, services —
in a standard way. One of the two interop standards the report tracks (with
A2A).

**MCPhantom** — The pattern where coding agents install archived, unpatched MCP
servers from training memory instead of the service owner's current server
(Glow Labs, Nov 2026).

**METR (Model Evaluation & Threat Research)** — An independent research
organisation that measures AI capabilities, including how long a task an agent
can complete ("time horizons").

**MIDNIGHT NEPTUNE** — A suspected North Korean-linked threat cluster that
turned a coding assistant into a delivery pipe (Nov 2026): it modified
.claude/settings.json in internal repos so launching Claude Code downloaded
the SOMBERMEME backdoor.

**model risk** — The risk that a model is wrong, misused, or misunderstood —
and the firm loses money or breaks the law because it relied on the model.
Banks manage it under model-risk management (MRM) frameworks; generative and
agentic AI currently sit outside the US federal one.

## N

**NCSC (National Cyber Security Centre)** — The UK's national authority on
cyber security (part of GCHQ). Its warnings on the AI-driven "vulnerability
patch wave" are cited in §2.5.

**NCUA (National Credit Union Administration)** — The US regulator for credit
unions. Co-issuing interagency TPRM guidance for the first time.

**NIST (National Institute of Standards and Technology)** — The US federal
standards agency. Its AI Risk Management Framework (AI RMF) is the most-cited
voluntary AI governance standard.

**NSCP (National Society of Compliance Professionals)** — The US non-profit
membership organisation for financial-services compliance professionals;
co-runs the annual AI Benchmarking Survey with ACA Group.

**NYCAIRR (New York Center for AI Responsibility and Research)** — The SUNY
Binghamton centre that independently tests frontier AI systems and reviews
developers' published safety frameworks.

**NYDFS (New York Department of Financial Services)** — New York State's
financial regulator. Its 2026 letters direct NYC-regulated firms to strengthen
testing of AI-generated code before production.

## O

**OCC (Office of the Comptroller of the Currency)** — The US regulator for
national banks. Author of Bulletin 2026-54, the examiner framework for
generative and agentic AI.

**orchestration** — Coordinating a team of agents: who does what, in what
order, who checks whom, and how work and information flow between them. The
supervisor pattern is the production-default orchestration.

**OSFI (Office of the Superintendent of Financial Institutions)** — Canada's
federal financial regulator. Its Guideline E-23 (effective 1 May 2027)
expressly brings AI/ML models inside model-risk scope.

**OWASP (Open Web Application Security Project)** — An open community that
publishes the standard lists of web and AI security risks (the OWASP Top 10).

**OWASP Top 10 for Agentic Applications** — OWASP's list of the ten highest
risks for applications built on AI agents — prompt injection, unauthorised
tool execution, memory poisoning, inter-agent trust failure and the rest. A
November 2026 study tested four orchestration frameworks against it and found
every one vulnerable in its default setup.

## P

**pass@1 and pass^k** — Two ways of scoring an agent. pass@1: it succeeds on
the first try. pass^k: it succeeds on all k tries. An agent can pass once by
luck; pass^k measures whether it is reliable — the report's standard for
judging agents.

**pen test (penetration test)** — Authorised hacking: security specialists
attack a system the way a real attacker would, to find the holes before
criminals do.

**PR (pull request)** — A proposed code change submitted for review before it is
merged into the main codebase. The point where pre-commit checks run. (Not
public relations.)

**Project SAGE** — HKMA's proposal for agentic-AI accountability: named owners
for agents, Know Your Agent (KYA) identity, and a registry of material AI
agents. Comments close 1 Feb 2027.

**prompt injection** — An attack that hides instructions in data an AI system
reads (a web page, a document, a code comment) so the model follows the
attacker's orders instead of its own. OWASP's #1 GenAI risk three years
running.

## R

**RAISE (Responsible AI Safety and Education Act)** — New York's frontier-AI
safety law (in force 1 Jan 2027): large frontier developers must register,
publish safety frameworks, and report critical incidents within 72 hours.

**RAUM (regulatory assets under management)** — The asset figure US investment
advisers report to the SEC on Form ADV. The ACA/NSCP survey's typical
respondent firm reports $1B–$10B in RAUM.

**RBAC (role-based access control)** — Permissions by job, not by person: each
role gets exactly the access its job needs, nothing more. Applies to agents as
well as people.

**recall** — In evaluation, the share of the target items a system catches. A
review tool with 78% recall catches 78 of every 100 vulnerability-introducing
changes; the other 22 slip through.

**red team** — A group that attacks a system (or an AI) on purpose, playing the
adversary, to find weaknesses before a real attacker does. The counterpart of
the "blue team" that defends.

**RFI (request for information)** — A regulator's formal call for public input
before it writes a rule. The Fed/OCC/FDIC AI RFI, promised in April 2026, still
has not appeared.

**RSI (recursive self-improvement)** — A scenario in which an AI model designs
its own successor without human input, so capability growth becomes
self-sustaining. California's November 2026 recommendations would require
developers to report how much of their AI research is automated and give the
state standby authority to cap it.

## S

**SAFR (Safeguards for Agentic Finance at Runtime)** — MAS's industry white
paper (Jul 2026, v1.1 Oct 2026): a runtime governance layer that checks an
agent's proposed actions — identity, controls, disposition, audit log — before
anything executes. A reference model, not a rule.

**SAST (static application security testing)** — Security testing by reading
the code without running it: scanning for known flaw patterns. Fast and
automatable; misses flaws that only appear when the code runs.

**SCA (software composition analysis)** — Scanning the dependencies a codebase
pulls in, to find known vulnerabilities in them. Reachability analysis goes
further: it checks whether the vulnerable code is actually used.

**secret (in code)** — A credential embedded in code or configuration: an API
key, a password, a token. Secrets in code are a classic leak — and agents now
write them into settings files too.

**SFC (Securities and Futures Commission)** — Hong Kong's securities regulator.
Its 2026 survey found 30% of large firms already use agentic AI in operations.

**shadow AI** — AI tools (or agents) running inside a firm without IT knowing
about them: installed by employees, outside governance, invisible until
something goes wrong.

**slopsquatting** — Registering the package name an AI coding tool
hallucinated, then publishing malicious code under it — so the next developer
(or agent) who trusts the hallucination installs the attacker's package.

**SOMBERMEME** — A backdoor delivered by tampering with a coding assistant's
settings: suspected North Korean operators modified .claude/settings.json so
starting Claude Code downloaded it (Google Threat Intelligence Group, Nov
2026).

**SR 11-7** — The Fed's model-risk letter (2011–2026), the old US rulebook for
governing models. Rescinded April 2026 and replaced by SR 26-2.

**SR 26-2** — The Fed/OCC/FDIC letter (17 Apr 2026) that replaced SR 11-7. It
expressly places generative and agentic AI outside model-risk scope — the US
federal gap the report is built around.

**supervisor pattern** — The production-default way to run a team of agents:
one supervisor agent plans, assigns work to specialist agents, checks their
output, and decides what ships.

**SWE-bench** — A benchmark built from real GitHub issues: can an AI fix the
bug the way the human developer did? The source of the "11× the
vulnerabilities" finding.

## T

**TPRM (third-party risk management)** — Managing the risk of outside vendors:
the firms whose software, data, or services you depend on. The proposed
interagency guidance would rewrite the US rules for it; comments close 16 Dec
2026.

## V

**vibe coding** — Writing software by describing what you want to an AI in
plain language and accepting what it produces, with little or no reading of the
code. Fast; Veracode's finding is that ~38% of AI-generated code carries a
known security flaw.

**VulnBench** — A benchmark of 108 hand-curated, attacker-reachable vulnerabilities in 20 open-source web apps, measuring deterministic SAST against AI security review under one blind protocol. Version 2.0 (Oct 2026) is the report's head-to-head evidence for running both layers.

## X

**XSS (cross-site scripting)** — A flaw where an attacker injects malicious
script into a web page other people view — so the victim's browser runs the
attacker's code.
