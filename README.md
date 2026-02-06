# swarmplug
# SwarmPlug (Public Demo Anchor)

SwarmPlug is a plug-and-play connectivity layer for ROS1-based agents, designed to help multiple ROS masters associate and share selected ROS interfaces across a swarm environment.

> This repository is a **capability demo & public timestamp anchor** for SwarmPlug ver0.1.  
> It does **NOT** contain the commercial core implementation.

## What ver0.1 proves
- Cross-device association workflow for a minimal swarm setup
- Swarm-side introspection via CLI (nodes / topics / parameters)
- End-to-end “hello world” across multiple machines running ROS1

## Quick demo (CLI examples)
```bash
# list known swarm members
swarmplug nodes

# list visible topics across the associated swarm
swarmplug topics

# echo a topic
swarmplug echo /topic1

# list ROS parameters discovered
swarmplug parameters

# read one parameter
swarmplug echo /turtlesim/background_b
