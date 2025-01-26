
'''
from collections import defaultdict
import heapq

def minimize_training_time(factory1, factory2, task_list):
    """
    :param factory1: 工厂1的兵种及训练时间，例如 {'A': 3, 'B': 5}
    :param factory2: 工厂2的兵种及训练时间，例如 {'A': 4, 'C': 2}
    :param task_list: 需要训练的兵种及数量，例如 {'A': 10, 'B': 5, 'C': 8}
    :return: 分配结果以及最短总时间
    """
    # 工厂能力
    factories = [
        {'name': 'factory1', 'training_time': factory1, 'total_time': 0},
        {'name': 'factory2', 'training_time': factory2, 'total_time': 0},
    ]

    # 记录每种兵种的分配情况
    assignment = defaultdict(lambda: {'factory1': 0, 'factory2': 0})

    for task, count in task_list.items():
        while count > 0:
            # 可训练当前兵种的工厂
            possible_factories = [
                f for f in factories if task in f['training_time']
            ]
            if not possible_factories:
                raise ValueError(f"No factory can train unit {task}!")

            # 按当前总时间+训练时间排序，优先选择负载最低的工厂
            possible_factories.sort(
                key=lambda f: f['total_time'] + f['training_time'][task]
            )

            # 分配兵种到负载最低的工厂
            chosen_factory = possible_factories[0]
            chosen_factory_name = chosen_factory['name']

            # 贪心分配数量，尽量减少一次分配的影响
            chosen_time_per_unit = chosen_factory['training_time'][task]
            chosen_factory['total_time'] += chosen_time_per_unit
            assignment[task][chosen_factory_name] += 1
            count -= 1

    # 计算总时间
    total_time = max(f['total_time'] for f in factories)

    return assignment, total_time


# 示例输入
factory1 = {'A': 3, 'B': 5}
factory2 = {'A': 4, 'C': 2}
task_list = {'A': 10, 'B': 5, 'C': 8}

# 调用函数
assignment, total_time = minimize_training_time(factory1, factory2, task_list)

print("兵种分配情况：", assignment)
print("所有训练完成的最短时间：", total_time)
'''
###code 2
'''
from collections import defaultdict

def minimize_training_time(factory_units, task_list):
    """
    :param factory_units: 工厂可以训练的兵种列表，例如 ['A', 'B', 'C']
    :param task_list: 需要训练的兵种及数量，以及每种兵种的训练时间，例如 {'A': (10, 3), 'B': (5, 5), 'C': (8, 2)}
                      格式为 {兵种: (数量, 训练时间)}
    :return: 分配结果以及最短总时间
    """
    # 初始化两个工厂的任务时间和任务分配
    factory1_time = 0
    factory2_time = 0
    assignment = defaultdict(lambda: {'factory1': 0, 'factory2': 0})

    # 按每种兵种逐一分配
    for unit, (count, training_time) in task_list.items():
        # 将每个兵种逐个分配到时间较短的工厂
        for _ in range(count):
            if factory1_time <= factory2_time:
                factory1_time += training_time
                assignment[unit]['factory1'] += 1
            else:
                factory2_time += training_time
                assignment[unit]['factory2'] += 1

    # 返回分配情况和两个工厂的最大时间
    total_time = max(factory1_time, factory2_time)
    return assignment, total_time


# 示例输入
factory_units = ['A', 'B', 'C']  # 工厂可以训练的兵种
task_list = {
    'A': (10, 3),  # 兵种 A 需要训练 10 个，每个训练时间为 3
    'B': (5, 5),   # 兵种 B 需要训练 5 个，每个训练时间为 5
    'C': (8, 2),   # 兵种 C 需要训练 8 个，每个训练时间为 2
}

# 调用函数
assignment, total_time = minimize_training_time(factory_units, task_list)

print("兵种分配情况：", assignment)
print("所有训练完成的最短时间：", total_time)

'''
#code 3
'''
def minimize_training_time_dp_optimized(factory1_tasks, factory2_tasks, task_list):
    """
    动态规划优化版本，考虑工厂的训练能力限制
    :param factory1_tasks: 工厂1能训练的兵种列表，例如 ['A', 'B']
    :param factory2_tasks: 工厂2能训练的兵种列表，例如 ['A', 'C']
    :param task_list: {兵种: (数量, 训练时间)}，例如 {'A': (10, 3), 'B': (5, 5), 'C': (8, 2)}
    :return: 最短总时间
    """
    # 工厂1的总任务时间上限
    total_time = sum(count * time for unit, (count, time) in task_list.items())
    
    # 初始化 dp 数组：dp[j] 表示工厂1达到时间 j 是否可行
    dp = [False] * (total_time + 1)
    dp[0] = True

    # 工厂1能训练的兵种及其任务
    for unit in factory1_tasks:
        if unit not in task_list:
            continue
        count, training_time = task_list[unit]

        # 逐个单位处理，更新 dp
        for _ in range(count):
            for t in range(total_time, training_time - 1, -1):
                if dp[t - training_time]:
                    dp[t] = True

    # 寻找最优分割点（接近总时间的一半）
    half = total_time // 2
    best_time_for_factory1 = 0
    for t in range(half, -1, -1):
        if dp[t]:
            best_time_for_factory1 = t
            break

    # 工厂2的时间为剩余时间
    best_time_for_factory2 = total_time - best_time_for_factory1
    return max(best_time_for_factory1, best_time_for_factory2)


# 示例输入
factory1_tasks = ['A', 'B']  # 工厂1能训练的兵种
factory2_tasks = ['A', 'C']  # 工厂2能训练的兵种
task_list = {
    'A': (10, 3),  # A 需要训练 10 个，每个训练时间 3
    'B': (5, 5),   # B 需要训练 5 个，每个训练时间 5
    'C': (8, 2),   # C 需要训练 8 个，每个训练时间 2
}

# 调用函数
total_time_dp_optimized = minimize_training_time_dp_optimized(factory1_tasks, factory2_tasks, task_list)

print("【动态规划优化】所有训练完成的最短时间：", total_time_dp_optimized)
'''