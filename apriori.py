# apriori.py
# Simple Apriori algorithm for teaching/demo purposes.

from __future__ import annotations
from collections import Counter
from itertools import combinations
from typing import Dict, Iterable, List, Tuple, FrozenSet

Transaction = List[str]
Itemset = FrozenSet[str]

def _get_1_itemsets(transactions: List[Transaction], min_support: float) -> Dict[Itemset, float]:
    n_transactions = len(transactions)
    counter = Counter()
    for t in transactions:
        for item in set(t):
            counter[item] += 1
    frequent_1 = {}
    for item, count in counter.items():
        support = count / n_transactions
        if support >= min_support:
            frequent_1[frozenset([item])] = support
    return frequent_1

def _generate_candidates(prev_frequents: Dict[Itemset, float], k: int) -> List[Itemset]:
    prev_itemsets = list(prev_frequents.keys())
    candidates = []
    n = len(prev_itemsets)
    for i in range(n):
        for j in range(i + 1, n):
            l1 = sorted(prev_itemsets[i])
            l2 = sorted(prev_itemsets[j])
            if l1[: k - 2] == l2[: k - 2]:
                candidate = frozenset(prev_itemsets[i] | prev_itemsets[j])
                if len(candidate) == k and candidate not in candidates:
                    candidates.append(candidate)
    return candidates

def _prune_candidates(candidates: Iterable[Itemset], prev_frequents: Dict[Itemset, float], k: int) -> List[Itemset]:
    prev_sets = set(prev_frequents.keys())
    pruned = []
    for c in candidates:
        all_subsets_frequent = True
        for subset in combinations(c, k - 1):
            if frozenset(subset) not in prev_sets:
                all_subsets_frequent = False
                break
        if all_subsets_frequent:
            pruned.append(c)
    return pruned

def _count_support(transactions: List[Transaction], candidates: Iterable[Itemset], min_support: float) -> Dict[Itemset, float]:
    n_transactions = len(transactions)
    candidate_list = list(candidates)
    counts = Counter({c: 0 for c in candidate_list})
    for t in transactions:
        t_set = set(t)
        for c in candidate_list:
            if c.issubset(t_set):
                counts[c] += 1
    frequents = {}
    for c, count in counts.items():
        support = count / n_transactions
        if support >= min_support:
            frequents[c] = support
    return frequents

def apriori(transactions: List[Transaction], min_support: float) -> Dict[Itemset, float]:
    frequent_itemsets = {}
    Lk = _get_1_itemsets(transactions, min_support)
    frequent_itemsets.update(Lk)
    k = 2
    while Lk:
        Ck = _generate_candidates(Lk, k)
        Ck = _prune_candidates(Ck, Lk, k)
        if not Ck:
            break
        Lk = _count_support(transactions, Ck, min_support)
        frequent_itemsets.update(Lk)
        k += 1
    return frequent_itemsets

def generate_rules(frequent_itemsets: Dict[Itemset, float], min_confidence: float, min_lift: float):
    rules = []
    supports = frequent_itemsets
    for itemset, sup in supports.items():
        if len(itemset) < 2:
            continue
        items = list(itemset)
        for r in range(1, len(items)):
            for antecedent_tuple in combinations(items, r):
                antecedent = frozenset(antecedent_tuple)
                consequent = itemset - antecedent
                if not consequent:
                    continue
                sup_itemset = sup
                sup_ante = supports.get(antecedent)
                sup_cons = supports.get(consequent)
                if sup_ante is None or sup_cons is None:
                    continue
                confidence = sup_itemset / sup_ante
                lift = confidence / sup_cons
                if confidence >= min_confidence and lift >= min_lift:
                    rules.append((antecedent, consequent, sup_itemset, confidence, lift))
    rules.sort(key=lambda x: x[4], reverse=True)
    return rules
