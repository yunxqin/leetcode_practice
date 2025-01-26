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
