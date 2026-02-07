## High-level architecture (ver0.1)

```mermaid
flowchart LR
  A[ROS Device A<br/>roscore + app nodes] -->|local ROS| B[SwarmPlug Module A]
  C[ROS Device B<br/>roscore + app nodes] -->|local ROS| D[SwarmPlug Module B]

  B <-->|association link| D

  B -->|CLI introspection| E[swarmplug CLI]
  D -->|CLI introspection| E
