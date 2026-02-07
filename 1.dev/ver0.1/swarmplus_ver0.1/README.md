# SwarmPlug ver0.1

> **Plug-and-Play ROS Host Extension Module (Technical Preview)**

SwarmPlug ver0.1 是一个运行在独立设备上的 **ROS 插件模块**，用于在**不修改宿主系统、不引入多 Master、不依赖区块链或 Mesh 网络**的前提下，让外部设备以“插件”的方式安全、可控地接入指定 ROS 宿主。

本版本聚焦于 **“宿主发现 → 绑定 → 使用”** 的最小闭环验证。


## 1. 设计目标（ver0.1）

- 单 ROS Master 架构（不使用 multimaster）
    
- 插件设备 **只认一个指定宿主**
    
- 不自动启动任何业务节点
    
- 不侵入宿主系统
    
- 提供统一、产品化的 CLI 使用方式
    

> ver0.1 的定位是：**稳定、可解释、可复现的工程底座**

## 2. 系统角色定义

### 宿主（Host）

- 示例名称：`tsj-white`
    
- 系统：ROS1 Noetic
    
- 职责：
    
    - 运行业务 ROS 节点
        
    - 启动唯一的 `roscore`
        
    - 提供 Topic / Node / Parameter Server
        

宿主 **无需安装 SwarmPlug、无需任何改动**。

### SwarmPlug 模块（Plugin）

- 示例设备：`T480s-161`
    
- 系统：ROS1 Noetic
    
- 职责：
    
    - 扫描局域网中的 `roscore`
        
    - 按固定策略绑定指定宿主
        
    - 生成并维护 ROS 环境变量
        
    - 提供统一 CLI 命令入口
## 
3. 核心策略（S1：固定宿主）

ver0.1 采用 **S1 固定策略**：

> **只要发现指定宿主 IP 的 roscore，才允许绑定；  
> 即使网络中存在多个 roscore，也绝不会误连。**

示例：
```
Preferred host IP: 192.168.31.133

```

4. 项目结构
```
swarmplus_ver1.0/
├── README.md
├── swarmplug_start.sh          # 核心守护脚本（监听 / 绑定）
└── catkin_ws/
    └── src/
        └── swarmplus_core/
            └── scripts/
                └── scan_ros_masters.py

```

用户级命令：
```
~/bin/swarmplug

```

## 5. 启动方式（插件设备）

### 5.1 启动 SwarmPlug 守护进程
```
./swarmplug_start.sh

```

行为说明：

1. 周期扫描局域网内所有 roscore（TCP 11311）
    
2. 仅当发现指定宿主 IP 时才绑定
    
3. 生成并维护环境文件：
    

```
~/.swarmplug_env.sh
```

4. 进入 READY 状态并持续监听  
    （ver0.1 不自动启动任何插件节点）

## 6. 产品化 CLI：`swarmplug`

SwarmPlug 提供统一命令包装器，**无需手动 source 环境变量**。

### 6.1 基础命令
```
swarmplug topics        # 等价 rostopic list
swarmplug nodes         # 等价 rosnode list
swarmplug parameters    # 等价 rosparam list
swarmplug params        # 同上
```

### 6.2 Topic 操作
```
swarmplug echo /topic_name
swarmplug info /topic_name

```

示例：
```
swarmplug echo /topic1

```

### 6.3 Parameter 操作
```
swarmplug get /param_name
swarmplug set /param_name value

```

示例：
```
swarmplug get /turtlesim/background_b

```

### 6.4 自动启动模式（推荐）

如果 SwarmPlug 尚未 READY，可使用：
```
swarmplug --auto topics
swarmplug --auto echo /topic1

```

行为：

- 自动启动 `swarmplug_start.sh`
    
- 等待宿主绑定完成
    
- 再执行目标 ROS 命令

## 7. 状态说明

- **LISTENING**  
    未发现指定宿主 roscore，持续监听
    
- **READY**  
    已绑定指定宿主，ROS Master 可达，可正常使用 `swarmplug` 命令

## 8. 已验证能力（ver0.1）

- 多 roscore 环境下的安全选择
    
- 插件设备与宿主解耦
    
- Topic / Node / Parameter 可见与操作
    
- CLI 级产品体验验证

## 9. 已知限制（ver0.1）

- 仅支持 ROS1
    
- 单 Master 架构
    
- 不支持多宿主切换
    
- 不自动启动任何业务插件
    
- 不涉及区块链、Mesh、协同决策

## 10. 版本状态

```
Version: ver0.1
Status : DONE ✅
Type   : Technical Preview / Engineering Baseline

```