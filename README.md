# SwarmPlug

**A Sidecar Infrastructure for Structural Clarity in ROS Systems**

SwarmPlug is a plug-and-play sidecar layer for ROS1-based systems, designed to enable **decentralized association, structured introspection, and explicit system attribution** across heterogeneous robotic devices — without modifying existing ROS hosts.

🚩 **This repository serves as the main public documentation hub and long-term reference for SwarmPlug.**

It provides architectural context, version roles, and demo references, while **intentionally excluding commercial core implementations.**

📌 This README is a **living document** and will be updated as new SwarmPlug versions are released.

# 1. What is SwarmPlug?

SwarmPlug addresses a foundational systems question in distributed robotics:

>**How can independent ROS-based systems be observed, identified, and reasoned about in a decentralized and non-intrusive way?**

SwarmPlug is **not**:

- a ROS replacement

- a multi-master framework

- a control or decision-making layer

Instead, it provides a **progressively layered infrastructure**, starting from safe association and moving toward structured coordination.

# 2. Repository Scope

This repository is **documentation-first.**

It exists to:

- Define the **overall architecture and design philosophy**

- Clarify the **role of each released version**

- Provide **references to public demos**

- Act as a **public timestamp anchor** for SwarmPlug evolution

### Included in this repository

📄 Architecture & design documentation

🧩 Version-level responsibility definitions

🎥 References to demo repositories and videos

🕒 Public release milestones

### Not included in this repository

❌ Core synchronization or coordination algorithms

❌ Internal protocols or optimizations

❌ Commercial SwarmPlug implementation

❌ Appliance images or firmware

This separation is intentional and aligned with the commercial roadmap.

## 3. Version Overview

SwarmPlug is developed as a **layered system**, where each version introduces **one clearly scoped responsibility**.

### v0.1 — Host Discovery & Safe Association

**Status**: Released (Demo)

**Purpose:**
Establish a reliable and reproducible way for independent ROS1 systems to discover and associate with each other.

**What v0.1 proves:**

✅ Cross-device association between ROS1 systems

✅ Swarm-wide discovery of:

    - ROS nodes

    - ROS topics

    - ROS parameters

✅ CLI-based introspection of distributed system state

✅ End-to-end “hello world” visibility across devices

v0.1 focuses on **connectivity and observability**, not control or task logic.

### v0.2 — Canonical Naming & Host Identity

**Status**: Released (Engineering Stable)

**Purpose:**
Make ROS system resources **explicitly attributable** to a specific host.

**What v0.2 introduces:**

- Canonical naming layer
    ```
    /sp/<host_id>/<kind>/<ros_path>
    ```
- Explicit host identity abstraction

- Read-only system introspection

- Host network self-description (preferred IP / MAC)

**What v0.2 does NOT do:**

- No control or coordination

- No cross-host synchronization

- No semantic unification

📎 A recorded v0.2 demo is available in the separate repository:
👉 **swarmplug-demo**

### v0.3 — Unified Parameter & State Schema (Planned)

**Status:** Planned

**Purpose:**
Introduce a unified, host-agnostic representation of parameters and system state.

**Planned direction:**

    - Structured parameter/state schemas (e.g. YAML / JSON)

    - Clear separation between:

        - raw ROS parameters
        
        - semantic system state

v0.3 focuses on **meaning and structure**, not transport or coordination.

### v1.x — Cross-Host Coordination & Robustness (Planned)

**Status:** Planned

**Purpose:**
Enable controlled and explicit coordination across multiple ROS hosts.

**Potential scope:**

    - Cross-host state propagation
    
    - Robustness and recovery mechanisms
    
    - Optional transport backends

v1.x is **opt-in** and strictly layered on top of earlier versions.

## 4. Architecture (High-Level)

SwarmPlug runs locally on each device, alongside the **local ROS master**.

Each instance:

    - Interfaces with its **local ROS graph**
    
    - Participates in a **decentralized association process**
    
    - Exposes a structured, system-wide view via CLI

ROS Nodes  →  Local ROS Master
                  │
                  ▼
             SwarmPlug Module
                  │
        ── Association / Structure Layer ──
                  │
             System-wide View
                  │
                  ▼
             swarmplug CLI

## 5. Demo Repositories

Public demo materials are hosted separately to avoid exposing implementation details.

    - **swarmplug-demo**
    
        - Recorded demo videos
        
        - Demo scenario descriptions
        
        - Observable CLI behavior only

These demos are **read-only and observational.**

## 6. Project Status

    - Current released versions: **v0.1, v0.2**

    - Development approach: conservative, layered, system-first

    - README policy:

>This document will be **updated with each new SwarmPlug version** to reflect scope, responsibilities, and roadmap changes.

# 7. License & Usage

This repository is provided for **demonstration and evaluation purposes only.**

   - Commercial use of SwarmPlug core requires authorization
    
   - Internal implementations are not open-sourced here

# 8. Contact

If you are evaluating SwarmPlug for research or engineering use,feel free to reach out at: 

📧 swarmplug@163.com

📧 swarmplug@gmail.com
