import operator
import sys


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.split_node_calculated = False
        self.arrangs = None

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return '{}(c{}, a{})'.format(self.value, self.split_node_calculated, self.arrangs)

    def __repr__(self):
        return '{}(c{}, a{})'.format(self.value, self.split_node_calculated, self.arrangs)


def calculate_subtree_arrangements_optim(node, all_nodes, total_arrangs):
    print('curr', node, all_nodes, total_arrangs)

    if node.value == 0:
        return 1

    candidate_nodes_diffs = list()
    ind_diff = 1
    for candidate_node in all_nodes[:3]:
        diff = node.value - candidate_node.value

        if diff in {1, 2, 3}:
            candidate_nodes_diffs.append((candidate_node, ind_diff))

        ind_diff += 1

    if len(candidate_nodes_diffs) > 1:
        for candidate_node, ind_diff in candidate_nodes_diffs:
            if not candidate_node.split_node_calculated:
                arrangs = calculate_subtree_arrangements_optim(candidate_node, all_nodes[ind_diff:], total_arrangs)
                candidate_node.split_node_calculated = True
                candidate_node.arrangs = arrangs
            total_arrangs += candidate_node.arrangs

    else:
        candidate_node, _ = candidate_nodes_diffs[0]
        arrangs = calculate_subtree_arrangements_optim(candidate_node, all_nodes[1:], total_arrangs)
        total_arrangs += arrangs

    return total_arrangs


def calculate_subtree_arrangements_base(node, all_nodes):
    if node.value == 0:
        return 1

    candidate_nodes_diffs = list()
    ind_diff = 1
    for candidate_node in all_nodes[:3]:
        diff = node.value - candidate_node.value

        if diff in {1, 2, 3}:
            candidate_nodes_diffs.append((candidate_node, ind_diff))

        ind_diff += 1

    sum_arrangs = 0
    for candidate_node, ind_diff in candidate_nodes_diffs:
        arrangs = calculate_subtree_arrangements_base(candidate_node, all_nodes[ind_diff:])
        sum_arrangs += arrangs

    return sum_arrangs


def calculate_subtree_arrangements_o1(node, all_nodes, calculated):
    if node.value == 0:
        return 1

    candidate_nodes_diffs = list()
    ind_diff = 1
    for candidate_node in all_nodes[:3]:
        diff = node.value - candidate_node.value

        if diff in {1, 2, 3}:
            candidate_nodes_diffs.append((candidate_node, ind_diff))

        ind_diff += 1

    sum_arrangs = 0
    if not node.value in calculated:
        for candidate_node, ind_diff in candidate_nodes_diffs:
            arrangs = calculate_subtree_arrangements_o1(candidate_node, all_nodes[ind_diff:], calculated)
            sum_arrangs += arrangs

    else:
        sum_arrangs = calculated[node.value]

    calculated[node.value] = sum_arrangs

    return sum_arrangs


def calculate_total_arrangements(sorted_adapters):
    node = sorted_adapters[0]

    calculated_nodes = dict()
    total_arrangements = calculate_subtree_arrangements_o1(node, sorted_adapters, calculated_nodes)

    return total_arrangements


def read_adapters_from_stdin():
    adapters = [TreeNode(0)]
    max_rating = 0

    for line in sys.stdin:
        adapter_rating = int(line.strip())

        if adapter_rating > max_rating:
            max_rating = adapter_rating

        adapters.append(TreeNode(adapter_rating))

    adapters.append(TreeNode(max_rating + 3))
    adapters = sorted(adapters, key=operator.attrgetter('value'), reverse=True)

    return adapters


def main():
    adapters = read_adapters_from_stdin()
    total_arrangements = calculate_total_arrangements(adapters)

    print(total_arrangements)


if __name__ == '__main__':
    main()
