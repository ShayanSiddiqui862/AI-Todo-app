<!--
SYNC IMPACT REPORT:
Version change: N/A -> 1.0.0
Modified principles: N/A (new constitution)
Added sections: All principles and sections
Removed sections: None
Templates requiring updates: N/A
Follow-up TODOs: None
-->
# AI-Todo-app Constitution

## Core Principles

### I. Mission and Scope (Standalone Focus)
The AI-Todo-app Phase-1 is a command-line interface (CLI) Todo application using in-memory data structures. This phase has zero interaction with future phases. Do not include database connectors, web frameworks, or AI SDKs. The app must handle five basic operations: Add, Delete, Update, View, and Mark Complete.
<!-- Rationale: Focus on core CLI functionality without external dependencies -->

### II. Mandatory Technology Stack
The application must use Python 3.13+ as the runtime environment and UV as the package manager. No external persistence mechanisms (No SQL, No JSON files) are allowed; use Python dictionaries or lists for storage only.
<!-- Rationale: Maintain consistency in technology choices and avoid unnecessary complexity -->

### III. Spec-Driven Development (SDD) Protocol
The hierarchy of truth must follow Constitution > Specify > Plan > Tasks > Implement. No agent is permitted to write code without a specific Task ID from speckit.tasks. Architecture changes must be updated in speckit.plan before implementation. Every function in /src must include a comment linking it to a Task ID and Specify section.
<!-- Rationale: Ensure disciplined development process with proper documentation and traceability -->

### IV. Quality and Engineering Standards
All code must follow PEP 8 standards, use type hinting, and apply 'Clean Code' principles. Source code must reside strictly in the /src folder. Implement graceful handling for invalid IDs and empty inputs.
<!-- Rationale: Maintain code quality and consistency across the project -->

### V. Prohibited Behaviors (Failure Modes)
No agent may assume requirements not explicitly stated in speckit.specify. Do not add 'Future-Proof' features meant for web or cloud deployments. The human will not write code; the agent must refine the spec until the code is correct.
<!-- Rationale: Prevent scope creep and maintain adherence to specified requirements -->

### VI. No Vibe-Coding Policy

Never assume a requirement; if a feature isn't in speckit.specify, the agent must stop and ask. This ensures strict adherence to the specified requirements and prevents implementation of unintended features.
<!-- Rationale: Maintain strict requirement adherence and prevent assumption-based development -->

## Additional Constraints
Error handling: Implement graceful handling for invalid IDs and empty inputs. Project structure: Source code must reside strictly in the /src folder. No external persistence (No SQL, No JSON files); use Python dictionaries or lists for storage.
<!-- Technology stack requirements, compliance standards, deployment policies, etc. -->

## Development Workflow
Spec-Driven Development Protocol must be followed with Architecture changes updated in speckit.plan before implementation. Every function in /src must include a comment linking it to a Task ID and Specify section. Reference Mandatory: Every function in /src must include a comment linking it to a Task ID and Specify section.
<!-- Code review requirements, testing gates, deployment approval process, etc. -->

## Governance
This constitution supersedes all other practices. All development must comply with the SDD protocol. Amendments require documentation, approval, and migration plan if applicable. All implementations must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
<!-- Version: 1.0.0 | Ratified: 2025-12-28 | Last Amended: 2025-12-28 -->
