#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.
from collections import deque


class Node:
    def __init__(self, value, nid):
        self.val = value
        self.children = []
        self.cost = value
        self.nid = nid


def constructTree(v, e):

    l_v = len(v)
    tbl = {i: [] for i in range(l_v)}
    discovered = [None for i in range(l_v)]  # 0-based

    for src, des in e:
        src -= 1  # 1-base -> 0-base
        des -= 1  # 1-base -> 0-base
        tbl[src].append(des)
        tbl[des].append(src)

    discovered[0] = Node(v[0], 0)
    stack = deque([(False, 0)])  # (type, id_zerob)

    while stack:
        flag_agg, curr_id = stack.pop()
        if flag_agg:
            pnode = discovered[curr_id]
            for cnode in pnode.children:
                pnode.cost += cnode.cost
        else:
            stack.append((True, curr_id))
            for adj_id in tbl[curr_id]:
                if discovered[adj_id] is None:
                    tmp_newnode = discovered[adj_id] = Node(v[adj_id], adj_id)
                    discovered[curr_id].children.append(tmp_newnode)
                    stack.append((False, adj_id))
    return discovered[0]


_MAX_COST = 5 * (10 ** 13) + 1


def aux_traversal(root, size):
    best = _MAX_COST
    stack = deque([root])
    path_table = [False for _ in range(size)]
    path_table[0] = True

    while stack:
        cur_node = stack.pop()
        if type(cur_node) == int:
            path_table[cur_node] = False
        else:
            path_table[cur_node.nid] = True
            stack.append(cur_node.nid)  # Insert exit flag
            for chd_node in cur_node.children:
                target_root = root.cost - chd_node.cost
                target_split = chd_node.cost

                res_equal = target_root if target_root == target_split else _MAX_COST
                res_root = best_split(root, target_split, chd_node.nid, path_table)
                res_split = best_split(chd_node, target_root)
                best = min(best, res_equal, res_root, res_split)
                if best == 0:
                    return 0
                stack.append(chd_node)
    return best if best < _MAX_COST else -1


def best_split(root, target, exclude=None, path=None):
    whole_cost = root.cost - (target if exclude is not None else 0)

    if whole_cost > target * 2 or whole_cost <= target:
        return _MAX_COST

    best = _MAX_COST
    stack = deque([root])

    while stack:
        cur_node = stack.pop()
        for chd_node in cur_node.children:
            if chd_node.nid != exclude:
                sub_cost = chd_node.cost - (target if path and path[chd_node.nid] else 0)
                root_cost = whole_cost - sub_cost

                if root_cost == sub_cost == target:
                    return 0

                elif root_cost == target and sub_cost < target:
                    best = min(best, target - sub_cost)
                elif sub_cost == target and root_cost < target:
                    best = min(best, target - root_cost)

                stack.append(chd_node)
    return best


def balancedForest(tree_values, tree_edges):
    t = constructTree(tree_values, tree_edges)
    return aux_traversal(t, len(tree_values))


q = 1

n = 5

c = [1, 2, 2, 1, 1]

edges = [[1, 2], [1, 3], [3, 5], [1, 4]]

result = balancedForest(c, edges)

print(result)
