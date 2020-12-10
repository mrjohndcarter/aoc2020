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


def bfs(graph, search_color, current_color, path=[]) -> list:
    path.append(current_color)

    if current_color == search_color:
        # found a path, return it
        return True

    else:
        outgoing_edges = graph[current_color]
        if outgoing_edges:
            sub_path = []
            for outgoing_color in outgoing_edges:
                if bfs(graph, search_color, outgoing_color, path):
                    return path
        else:
            # end of the line, return
            return False

    return False


def main():
    rules = {}
    search_color = 'shiny gold'

    # this builds a digraph
    with open('input.p1', 'r') as f:
        for rule_string in f:
            temp_rule = parse_rule(rule_string)
            rules[temp_rule['color']] = temp_rule['contains']

    eventual_contain_count = 0

    for color in rules:
        if color != search_color:
            path = []
            if bfs(rules, search_color, color, path):
                print(f'Found: {path}')
                eventual_contain_count += 1

    print(f'Found: {eventual_contain_count} possible paths')


if __name__ == '__main__':
    main()
