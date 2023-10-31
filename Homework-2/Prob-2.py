alpha = 0.125
beta = 0.25
estimated_rtt = 100  # 初始EstimatedRTT
dev_rtt = 5  # 初始DevRTT


def calculate_timeout_interval(sample_rtt):
    global estimated_rtt, dev_rtt

    # 计算EstimatedRTT
    estimated_rtt = (1 - alpha) * estimated_rtt + alpha * sample_rtt

    # 计算DevRTT
    dev_rtt = (1 - beta) * dev_rtt + beta * abs(sample_rtt - estimated_rtt)

    # 计算TimeoutInterval
    timeout_interval = estimated_rtt + 4 * dev_rtt

    return timeout_interval


# 样本1
sample_rtt_1 = 120
timeout_interval_1 = calculate_timeout_interval(sample_rtt_1)
print("Timeout Interval for Sample 1:", timeout_interval_1)

# 样本2
sample_rtt_2 = 110
timeout_interval_2 = calculate_timeout_interval(sample_rtt_2)
print("Timeout Interval for Sample 2:", timeout_interval_2)

# 样本3
sample_rtt_3 = 130
timeout_interval_3 = calculate_timeout_interval(sample_rtt_3)
print("Timeout Interval for Sample 3:", timeout_interval_3)

# 样本4
sample_rtt_4 = 115
timeout_interval_4 = calculate_timeout_interval(sample_rtt_4)
print("Timeout Interval for Sample 4:", timeout_interval_4)

# 样本5
sample_rtt_5 = 105
timeout_interval_5 = calculate_timeout_interval(sample_rtt_5)
print("Timeout Interval for Sample 5:", timeout_interval_5)