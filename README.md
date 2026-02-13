# SwarmPlug ver0.1

**Host Attachment Specification**

---

## Statement

SwarmPlug ver0.1 defines a deterministic host attachment specification  
between SwarmPlug and a ROS runtime environment.

It does not normalize.  
It does not snapshot.  
It does not coordinate.  

**It attaches.**

---

## Problem

Before semantic abstraction or coordination can occur,  
a reliable host attachment layer must exist.

A ROS runtime exposes its operational surface through:

- ROS Master (XMLRPC)
- Topics
- Services
- Parameters

A sidecar infrastructure must attach and discover these interfaces consistently.

---

## Position

SwarmPlug ver0.1 defines the host attachment boundary.

`ROS Runtime → SwarmPlug Attachment`

ver0.1 completes the connection and discovery layer.

---

## Architecture (Conceptual)

```mermaid
flowchart TB

  subgraph L1["Host Runtime"]
    A1["ROS Master"]
    A2["Topics / Services / Params"]
  end

  subgraph L2["SwarmPlug ver0.1"]
    B1["Connection Layer"]
    B2["Discovery Interface"]
  end

  A1 --> B1
  A2 --> B2
```

## Determinism

Given a reachable ROS master,
ver0.1 deterministically discovers:

- Topics
- Nodes
- Services
- Parameters

No transformation, mutation, or interception is performed.

## Scope Limitation

SwarmPlug ver0.1 does not include:

- Canonical naming
- Semantic abstraction
- Snapshot generation
- Communication transport
- Coordination logic

## Version Context
| Version | Responsibility        |
|---------|----------------------|
| ver0.1  | Host attachment      |
| ver0.2  | Canonical naming     |
| ver0.3  | Semantic snapshot    |

## Principle

Attachment precedes abstraction.
Discovery precedes normalization.

ver0.1 establishes the attachment layer.


## License

This version specification is part of the SwarmPlug documentation.

Licensed under the **SwarmPlug Documentation License v1.0**.

See the root LICENSE file for details.



