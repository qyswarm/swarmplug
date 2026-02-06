# SwarmPlug

**SwarmPlug** is a plug-and-play connectivity layer for **ROS1-based multi-agent systems**,  
designed to enable decentralized **association, introspection, and coordination** across heterogeneous robotic swarms.

> 🚩 This repository is a **public demo & timestamp anchor** for **SwarmPlug ver0.1**.  
> It demonstrates core capabilities and interfaces, **without exposing the commercial core implementation**.
![MyVideo_1](https://github.com/user-attachments/assets/b9444de8-d616-4299-8397-fcf16fdf4df1)

---

## 1. What does SwarmPlug do?

SwarmPlug focuses on one fundamental problem in swarm robotics:

> **How can multiple ROS-based agents, running independent ROS masters on different devices, discover each other and share selected ROS interfaces in a decentralized way?**

SwarmPlug provides:

- A lightweight **association layer** between devices
    
- Unified **introspection** of swarm-wide ROS entities
    
- A simple **CLI interface** to inspect swarm state
    

No cloud, no central server, no monolithic ROS master.

---

## 2. What ver0.1 proves

This ver0.1 demo validates the following capabilities:

- ✅ Cross-device association between multiple ROS1 nodes
    
- ✅ Swarm-wide discovery of:
    
    - ROS nodes
        
    - ROS topics
        
    - ROS parameters
        
- ✅ Command-line introspection of swarm state
    
- ✅ End-to-end “hello world” topic exchange across devices
    

This version focuses on **connectivity and observability**, not on control or task logic.

---

## 3. Repository scope

### Included in this repository

- 📄 Documentation and usage examples
    
- 🧩 High-level architecture description
    
- 🖥 CLI command demonstrations
    
- 🕒 Public release timestamp (ver0.1)
    

### Not included in this repository

- ❌ Core synchronization algorithms
    
- ❌ Commercial SwarmPlug implementation
    
- ❌ Protocol adapters and internal optimizations
    
- ❌ Appliance / firmware images
    

> This separation is intentional and aligns with the commercial roadmap.

---

## 4. Architecture overview (high level)

SwarmPlug runs **locally on each device**, alongside the local ROS master.

Each instance:

- Interfaces with its local ROS graph
    
- Participates in a decentralized association process
    
- Exposes a unified swarm view through a CLI
    

```
ROS Nodes  →  Local ROS Master
                │
                ▼
           SwarmPlug Module
                │
      ── Association Layer ──
                │
           Swarm-wide View
                │
                ▼
           swarmplug CLI

```
---

## 5. CLI demo (ver0.1)

The following commands illustrate the ver0.1 demo behavior.

### List swarm members

```
swarmplug nodes
```

### List visible ROS topics across the swarm

```
swarmplug topics
```

### Echo a topic from the swarm
```
swarmplug echo /topic1
```

### List ROS parameters discovered in the swarm

```
swarmplug parameters

```

### Read a specific parameter

```
swarmplug echo /turtlesim/background_b
```

These commands allow developers to **inspect swarm state without manually logging into each device**.

---

## 6. Typical demo scenario

A minimal demonstration setup may include:

- Device A: ROS1 node publishing `/topic1`
    
- Device B: SwarmPlug-enabled node associated with A
    
- Device C: Another ROS1 node joining later
    

After association:

- All participating devices can observe selected ROS entities
    
- CLI commands return a **swarm-consistent view**
    

This validates decentralized discovery and visibility.

---

## 7. Current status

- **Public demo release:** ver0.1
    
- **Focus:** association & introspection
    
- **Next milestone:** ver0.2 (feature expansion & stability improvements)
    

The roadmap prioritizes robustness, modularity, and compatibility with heterogeneous robotic platforms.

---

## 8. License & usage

This repository is provided **for demonstration and evaluation purposes only**.

- Commercial use of SwarmPlug core requires authorization
    
- Internal implementations are not open-sourced in this repository
    

---

## 9. Contact

For collaboration, evaluation, or commercial inquiries:

📧 **qyswarm@163.com**
