import re


def parse_rule(string) -> dict:
    rem = re.match(r'(.+)bags contain (.+)\.', string)

    if not rem:
        return None

    # parse contents
    re_contents = re.findall(r'(\d+)([^,]+)bag[s]?', rem[2])

    rule = {
        'color': rem[1].strip(),
        'contains': {}
    }

    if re_contents:
        for bag_rule in re_contents:
            rule['contains'][bag_rule[1].strip()] = int(bag_rule[0])

    return rule


def bfs_sum(graph, current_color, count_of_color=1):

    sum_of_children = 0
    for child_color, count in graph[current_color].items():
        sum_of_children += bfs_sum(graph, child_color, count)

    return sum_of_children * count_of_color + count_of_color


def main():
    rules = {}
    search_color = 'shiny gold'

    # this builds a digraph
    with open('input.p1', 'r') as f:
        for rule_string in f:
            temp_rule = parse_rule(rule_string)
            rules[temp_rule['color']] = temp_rule['contains']

    print(bfs_sum(rules, search_color) - 1) # need to subtract the shiny gold bag since we only care about contents


if __name__ == '__main__':
    main()
