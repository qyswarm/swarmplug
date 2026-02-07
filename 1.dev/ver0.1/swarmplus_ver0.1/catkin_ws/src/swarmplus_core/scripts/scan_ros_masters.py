```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

ROS_MASTER_PORT = 11311

def local_ip_guess() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()

def can_connect(ip: str, port: int = ROS_MASTER_PORT, timeout: float = 0.2) -> bool:
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        return True
    except Exception:
        return False
    finally:
        s.close()

def rdns(ip: str) -> str:
    try:
        name, _, _ = socket.gethostbyaddr(ip)
        return name
    except Exception:
        return ""

def scan(subnet_prefix: str, timeout: float = 0.2, workers: int = 128):
    ips = [f"{subnet_prefix}.{i}" for i in range(1, 255)]
    found = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(can_connect, ip, ROS_MASTER_PORT, timeout): ip for ip in ips}
        for fut in as_completed(futs):
            ip = futs[fut]
            try:
                ok = fut.result()
            except Exception:
                ok = False
            if ok:
                found.append(ip)
    found.sort(key=lambda x: list(map(int, x.split("."))))
    return [(ip, rdns(ip)) for ip in found]

def main():
    ap = argparse.ArgumentParser(description="Scan subnet for ROS1 roscore (TCP 11311).")
    ap.add_argument("--subnet", default="", help="subnet prefix like 192.168.31 (auto if empty)")
    ap.add_argument("--timeout", type=float, default=0.2, help="TCP connect timeout seconds")
    ap.add_argument("--workers", type=int, default=128, help="parallel workers")
    args = ap.parse_args()

    lip = local_ip_guess()
    subnet = args.subnet or ".".join(lip.split(".")[:3])
    res = scan(subnet, timeout=args.timeout, workers=args.workers)

    # 输出：每行 "ip<TAB>hostname"
    for ip, name in res:
        print(f"{ip}\t{name}")

if __name__ == "__main__":
    main()


```