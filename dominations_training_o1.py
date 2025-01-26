'''
from collections import defaultdict

def greedy_schedule(units):
    """
    使用贪心算法，将所有兵种拆分为单个单位逐个分配给负载较低的可训练工厂
    :param units: dict, 形如:
        {
           "A": {"factoryA": 3, "factoryB": 4, "count": 10},
           "B": {"factoryA": 5, "count": 5},
           "C": {"factoryB": 2, "count": 8}
        }
    :return: (assignment, makespan)
        assignment: 记录每个兵种分配到两个工厂的数量
        makespan:   两个工厂完成所有任务的最短时间（估计值）
    """
    # 工厂的当前负载（总训练时间）
    loadA = 0
    loadB = 0

    # 分配结果：记录每种兵种有多少分到 A 厂、多少分到 B 厂
    assignment = defaultdict(lambda: {"factoryA": 0, "factoryB": 0})

    # 将所有兵种拆解成“单位”列表
    # 每个单位形如: (兵种名, 训练时间A, 训练时间B或None)
    tasks = []
    for unit_name, info in units.items():
        count = info["count"]
        timeA = info.get("factoryA", None)  # 可能不存在
        timeB = info.get("factoryB", None)  # 可能不存在
        for _ in range(count):
            tasks.append((unit_name, timeA, timeB))

    # 按照某种顺序处理所有单位（这里可以按“差异大”排个序也行，或直接顺序）
    # 这里简单直接按原顺序
    for (unit_name, timeA, timeB) in tasks:
        # 如果只有A厂能练，就只能给A厂
        if timeB is None:
            loadA += timeA
            assignment[unit_name]["factoryA"] += 1
        # 如果只有B厂能练，就只能给B厂
        elif timeA is None:
            loadB += timeB
            assignment[unit_name]["factoryB"] += 1
        else:
            # 两家都能练，选择当前负载更小的分配
            if loadA <= loadB:
                loadA += timeA
                assignment[unit_name]["factoryA"] += 1
            else:
                loadB += timeB
                assignment[unit_name]["factoryB"] += 1

    # 最终所需时间是 max(loadA, loadB)
    makespan = max(loadA, loadB)
    return assignment, makespan


if __name__ == "__main__":
    # 示例
    units = {
       "A": {"factoryA": 3, "factoryB": 4, "count": 10},  # A 可以在 A厂(3)或 B厂(4) 训练
       "B": {"factoryA": 5,              "count":  5},    # B 只能在 A厂 训练
       "C": {              "factoryB": 2, "count":  8},    # C 只能在 B厂 训练
    }

    assignment_greedy, makespan_greedy = greedy_schedule(units)
    print("【贪心算法】分配结果：")
    for k,v in assignment_greedy.items():
        print(f"  兵种 {k}: A厂={v['factoryA']} 个, B厂={v['factoryB']} 个")
    print("【贪心算法】完成所有训练的时间 =", makespan_greedy)

'''

###code2
'''
def dp_schedule_two_factories(units):
    """
    使用 2D 动态规划，针对两个工厂有兵种限制的情况，求最小最大完工时间。
    
    :param units: dict, 形如:
        {
           "A": {"factoryA": 3, "factoryB": 4, "count": 10},
           "B": {"factoryA": 5,              "count":  5},
           "C": {              "factoryB": 2, "count":  8}
        }
    :return: (min_makespan, best_split_info)
        min_makespan: 两工厂完成任务的最短时间
        best_split_info: 两工厂在可选兵种上的分配详情（如果想要追踪的话，可再做额外回溯）
    """

    # 1) 先将“只能在A厂”或“只能在B厂”的兵种计算出基线时间
    baseA = 0
    baseB = 0
    both_items = []  # 用来存储“可同时在 A/B 厂训练”的单位列表 (tA, tB)
    
    for unit_name, info in units.items():
        count = info["count"]
        tA = info.get("factoryA", None)
        tB = info.get("factoryB", None)

        if tA is not None and tB is not None:
            # 该兵种可以在 A 和 B 厂都训练 => 拆成 count 个单位
            for _ in range(count):
                both_items.append((tA, tB))
        elif tA is not None:  # 只能在A厂
            baseA += tA * count
        elif tB is not None:  # 只能在B厂
            baseB += tB * count
        else:
            # 理论上不会出现既不能A也不能B的情况，否则无法完成
            raise ValueError(f"兵种 {unit_name} 无法被任何工厂训练！")

    # 如果没有可选的单位（both_items为空），那结果很简单
    if not both_items:
        return max(baseA, baseB), None

    # 2) 用集合 dp 存储所有可达的 (timeA, timeB) 状态
    #    初始只有 (0, 0)
    current_states = {(0, 0)}

    # 3) 依次将 each unit (tA, tB) 扩展进来
    for (tA, tB) in both_items:
        new_states = set()
        for (curA, curB) in current_states:
            # 选择让这个单位去 A 厂
            new_states.add((curA + tA, curB))
            # 选择让这个单位去 B 厂
            new_states.add((curA, curB + tB))
        current_states = new_states

    # 4) current_states 里包含了所有可能的分配方式
    #    计算加上基线后，两厂的完工时间 = max(curA + baseA, curB + baseB)
    #    在所有状态中找最小值
    min_makespan = float("inf")
    for (curA, curB) in current_states:
        makespan = max(curA + baseA, curB + baseB)
        if makespan < min_makespan:
            min_makespan = makespan

    return min_makespan, None


if __name__ == "__main__":
    # 示例
    units = {
       "A": {"factoryA": 3, "factoryB": 4, "count": 10},  # 可以在A/B
       "B": {"factoryA": 5,              "count":  5},    # 只能在A
       "C": {              "factoryB": 2, "count":  8},    # 只能在B
    }
    result_dp, _ = dp_schedule_two_factories(units)
    print("【动态规划】完成所有训练的最短时间 =", result_dp)

'''
#详细注释版
def dp_schedule_two_factories(units):
    """
    使用 2D 动态规划，解决“两个工厂 + 兵种训练限制 + 最短完成时间”的问题。
    
    :param units: dict 形如:
        {
           "A": {"factoryA": 3, "factoryB": 4, "count": 10},  # 兵种A：在A厂3时间, 在B厂4时间, 共10个
           "B": {"factoryA": 5,              "count":  5},    # 兵种B：只能在A厂(5时间), 需要5个
           "C": {              "factoryB": 2, "count":  8}     # 兵种C：只能在B厂(2时间), 需要8个
        }
    :return: (min_makespan, state_count)
        min_makespan: 两工厂完成任务的最短时间(整型)
        state_count: 这个DP过程中产生的状态数量(仅用于观察规模大小)
    """

    # 1) 初始化 baseA, baseB, 还有一个列表 both_items
    baseA = 0  # 工厂A“只能A”兵种的总时间
    baseB = 0  # 工厂B“只能B”兵种的总时间
    both_items = []  # 用来存储“可以同时A或B”的单位训练时间 (tA, tB)

    for unit_name, info in units.items():
        count = info["count"]         # 要训练多少个
        tA = info.get("factoryA", None)  # A厂训练一个的时间 (可能None表示A厂不会)
        tB = info.get("factoryB", None)  # B厂训练一个的时间 (可能None表示B厂不会)

        if tA is not None and tB is not None:
            # 该兵种“可以在 A/B 训练”，拆成 count 个单位
            for _ in range(count):
                both_items.append((tA, tB))
        elif tA is not None:
            # 只能在 A 厂
            baseA += tA * count
        elif tB is not None:
            # 只能在 B 厂
            baseB += tB * count
        else:
            raise ValueError(f"兵种 {unit_name} 无法被任何工厂训练！")

    # 如果 both_items 为空，说明没有“可选”的兵种，结果直接比较 baseA 和 baseB 就好
    if not both_items:
        final_makespan = max(baseA, baseB)
        return final_makespan, 1

    # 2) 准备 DP 的数据结构: current_states 存所有可达的 (timeA, timeB)
    current_states = {(0, 0)}  # 初始没有可选单位分配 => (0,0)
    
    # 3) 依次把 both_items 中的单位拿出来，给它两种分配方式
    for (tA, tB) in both_items:
        new_states = set()
        # 对当前所有可达状态 (curA, curB)，扩展出两个新状态:
        #   1) 这个单位给A => (curA + tA, curB)
        #   2) 这个单位给B => (curA, curB + tB)
        for (curA, curB) in current_states:
            new_states.add((curA + tA, curB))
            new_states.add((curA, curB + tB))
        current_states = new_states

    # 4) 所有可达状态都生成后，逐一计算真正的完工时间 = max(curA+baseA, curB+baseB)
    #    取其中的最小值
    min_makespan = float("inf")
    for (curA, curB) in current_states:
        # 加上之前的基线时间
        timeA = curA + baseA
        timeB = curB + baseB
        makespan = max(timeA, timeB)
        if makespan < min_makespan:
            min_makespan = makespan

    # 也可以看一下总状态数多少（只是给你看看规模是否过大）
    return min_makespan, len(current_states)
