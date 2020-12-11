import re
import sys


NONE_VAL = 'no other'


class Rule:
    def __init__(self, parent, children, children_multipliers):
        self.parent = parent
        self.children = children
        self.children_multipliers = children_multipliers

    def __str__(self):
        return 'parent: {}, children: {}, children_multipliers: {}'.format(
            self.parent, self.children, self.children_multipliers)


def query_carry_atleast_one(rules, query_item):
    counter = 0
    query_items = [query_item]
    unique_containers = set()

    while len(query_items) > 0:
        query_item = query_items[0]

        for rule in rules:
            if query_item in rule.children:
                if rule.parent not in unique_containers:
                    counter += 1
                    unique_containers.add(rule.parent)
                    query_items.append(rule.parent)

        print('end of iter query_items {} unique_containers {} removing {}'.format(
            query_items, unique_containers, query_item))
        query_items.remove(query_item)

    print(len(unique_containers))
    return counter


def create_rule(rule_descriptor):
    children = set()
    children_multipliers = dict()

    parent_desc = rule_descriptor[0]

    for child_desc in rule_descriptor[1:]:
        child_multipliers = re.findall(r'\d+', child_desc)

        assert len(child_multipliers) in {0, 1}

        if child_multipliers:
            child_multiplier = child_multipliers[0]
            child_desc = child_desc.replace(child_multipliers[0], '').strip()

        else:
            child_multiplier = 1

        children.add(child_desc)
        children_multipliers[child_desc] = child_multiplier

    rule_instance = Rule(parent_desc, children, children_multipliers)

    return rule_instance


def extract_rule_descriptor(line):
    line = line.replace('bags', 'bag').replace('bag', '').replace('.', '')
    rule = list(map(str.strip, re.split('contain|,', line)))

    return rule


def main():
    rules = list()

    for line in sys.stdin:
        rule_desc = extract_rule_descriptor(line.strip())

        rule = create_rule(rule_desc)

        rules.append(rule)

    counter = query_carry_atleast_one(rules, 'shiny gold')

    print(counter)


if __name__ == '__main__':
    main()
