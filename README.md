
# SwarmPlug v0.2
> Target audience: ROS system engineers, researchers, and platform architects.

> **Canonical Naming & Host Identity Layer for ROS Systems**

SwarmPlug v0.2 is an **engineering-stable milestone** that introduces  
**canonical naming** and **explicit host identity** for ROS-based systems,  
laying the structural foundation for future cross-host coordination, replication,
and heterogeneous system integration.

This version does **not** add new communication mechanisms.  
Instead, it focuses on **making the system observable, identifiable, and manageable**.


---

## What is SwarmPlug?

**SwarmPlug** is a plug-and-play ROS extension module that runs on a separate device
and connects to an existing ROS host **without modifying the host system**.

- No ROS nodes are injected
- No Multi-Master
- No intrusion into the host
- Single, controlled ROS Master binding

SwarmPlug acts as a **sidecar system interface**, not a replacement for ROS.

---

## What’s New in v0.2

### 1. Canonical Naming (Core Feature)

v0.2 introduces a **canonical naming layer** for ROS resources:

```
/sp/<host_id>/<kind>/<ros_path>
```

Where:

- `<host_id>`: Explicit identity of the ROS host
- `<kind>`: topic / service / param / node / action
- `<ros_path>`: Original ROS name (unchanged)

Example:
```
/sp/node161/topic/turtle1/cmd_vel
```


Canonical names are **read-only structural references** and do **not** replace native ROS names.

---

### 2. Host Identity Abstraction

Each SwarmPlug instance exposes an explicit **Host ID**, used consistently across
canonical naming and system inspection.

Host ID resolution order:

1. `--host-id` CLI flag
2. `SP_HOST_ID` environment variable
3. System hostname (fallback)

This avoids ambiguity in multi-host or multi-plugin environments.

---

### 3. Host Network Self-Description

`swarmplug host info` provides a structured, explainable view of the plugin host:

- Preferred IP (RFC1918, non-virtual)
- Preferred MAC
- All IPs / MACs
- Optional raw network dump (`--all`)

Example:
```
IP preferred: 192.168.31.161 (iface=wlp3s0)  
MAC preferred: 1c:1b:b5:6a:b6:8e (iface=wlp3s0)
```


This is essential for future Mesh, appliance, and multi-NIC deployments.

---

### 4. Action Structure Inference

v0.2 adds CLI-level **ROS Action discovery**, with optional strict validation:

```bash
swarmplug actions
swarmplug actions --canon
swarmplug actions --canon --strict-action
```

This capability is preparatory and does not alter runtime behavior.

## Project Layout (v0.2)

```
swarmplug/
├── bin/
│   └── swarmplug                # Single CLI entry point
├── bootstrap/
│   ├── swarmplug_start.sh       # Host discovery & binding
│   └── scan_ros_masters.py
├── env/
│   └── swarmplug_env.sh         # Runtime-generated environment
├── README.md
├── VERSION
└── LICENSE

```

## Usage Overview

### Environment Setup (Required)

Add the following to your shell configuration:
```
export PATH="$HOME/swarmplug/bin:$PATH"
export SP_HOST_ID=node161   # example: robot001 / carA / host-alpha

```

Reload:
```
source ~/.bashrc
hash -r
```

### Basic Commands
```
swarmplug --auto topics
swarmplug topics --canon
swarmplug services --canon
swarmplug parameters --canon

```
### Host Inspection
```
swarmplug --auto host info
swarmplug --auto host info --all

```

### Actions
```
swarmplug actions
swarmplug actions --canon
swarmplug actions --canon --strict-action

```

## Design Principles (v0.2)

- **Non-intrusive**: No changes to ROS host
    
- **Structural, not behavioral**: Observe and describe, do not decide
    
- **Reversible & transparent**: Canonical names always map back to ROS names
    
- **Version-scoped**: No premature features

## What v0.2 Intentionally Does NOT Do

- No parameter semantic unification
    
- No cross-host synchronization
    
- No Mesh / blockchain / consensus
    
- No automatic control or decision-making
    

These are reserved for later versions.

## Version Status
```
Version: v0.2.0
Status : DONE
Type   : Engineering Stable / Structural Milestone

```
## License
See LICENSE file for details.

## Roadmap Context

- **v0.1**: Host discovery and safe binding
    
- **v0.2**: Canonical naming & host identity (this version)
    
- **v0.3**: Unified parameter / state schema (planned)
    
- **v1.x**: Cross-host coordination and robustness layers

> **SwarmPlug v0.2 answers one question clearly:  
> “What exists in this system, and who does it belong to?”**

Nothing more. Nothing less.
