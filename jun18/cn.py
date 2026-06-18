cwnd = 10
ssthresh = 64

print(f"Initial: cwnd={cwnd}, ssthresh={ssthresh}")

# RTT 1
cwnd *= 2
print(f"RTT 1: cwnd={cwnd}, ssthresh={ssthresh}")

# RTT 2
cwnd *= 2
print(f"RTT 2: cwnd={cwnd}, ssthresh={ssthresh}")

# RTT 3
cwnd *= 2
if cwnd > ssthresh:
    cwnd = ssthresh
print(f"RTT 3: cwnd={cwnd}, ssthresh={ssthresh}")

# RTT 4 (Congestion Avoidance)
cwnd += 1
print(f"RTT 4: cwnd={cwnd}, ssthresh={ssthresh}")

# RTT 5 (Triple Duplicate ACK)
ssthresh = cwnd // 2
cwnd = ssthresh
print(f"RTT 5 (Triple Duplicate ACK): cwnd={cwnd}, ssthresh={ssthresh}")

# RTT 6 (Timeout)
ssthresh = cwnd // 2
cwnd = 1
print(f"RTT 6 (Timeout): cwnd={cwnd}, ssthresh={ssthresh}")