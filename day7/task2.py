import re
import sys


NONE_VAL = 'no other'


class Rule:
    def __init__(self, parent, children, children_multipliers):
        self.parent = parent
        self.children = children
        self.children_multipliers = children_multipliers

    def __str__(self):
        return 'parent: {}, children_multipliers: {}'.format(
            self.parent, self.children_multipliers)


def traverse_sub_bags(node, counter, multiplier, rules_dict, parent=False):
    siblings_sum = 0

    for child_name in node.children:
        child_multiplier = rules_dict[node.parent].children_multipliers[child_name]

        if child_name != NONE_VAL:
            temp_result = traverse_sub_bags(rules_dict[child_name], counter, child_multiplier, rules_dict)
            siblings_sum += temp_result

        else:
            print('bottom {} returning {}'.format(node, multiplier))
            return int(multiplier)

    if not parent:
        result = int(multiplier) * siblings_sum + int(multiplier)
    else:
        result = int(multiplier) * siblings_sum

    print('current {} result = {}'.format(node, result))
    return result


def query_required_bags_inside(rules, query_item, rules_dict):
    for rule in rules:
        if rule.parent == query_item:
            parent_node = rule
            break

    counter = 0
    counter += traverse_sub_bags(parent_node, counter, 1, rules_dict, parent=True)

    return counter


def create_rule(rule_descriptor):
    children = set()
    children_multipliers = dict()

    parent_desc = rule_descriptor[0]

    for child_desc in rule_descriptor[1:]:
        child_multipliers = re.findall(r'\d+', child_desc)

        assert len(child_multipliers) in {0, 1}

        if child_desc == NONE_VAL:
            child_multiplier = 1

        elif child_multipliers:
            child_multiplier = child_multipliers[0]
            child_desc = child_desc.replace(child_multipliers[0], '').strip()

        else:
            child_multiplier = 1

        children.add(child_desc)
        children_multipliers[child_desc] = child_multiplier

    rule_instance = Rule(parent_desc, list(children), children_multipliers)

    return rule_instance


def extract_rule_descriptor(line):
    line = line.replace('bags', 'bag').replace('bag', '').replace('.', '')
    rule = list(map(str.strip, re.split('contain|,', line)))

    return rule


def main():
    rules = list()
    rules_dict = dict()

    for line in sys.stdin:
        rule_desc = extract_rule_descriptor(line.strip())

        rule = create_rule(rule_desc)

        rules.append(rule)
        rules_dict[rule.parent] = rule

    counter = query_required_bags_inside(rules, 'shiny gold', rules_dict)

    print(counter)


if __name__ == '__main__':
    main()
