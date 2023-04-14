from random import choices

from chromosome import Chromosome


def select_parent(generation, count):
    prob_list = get_weight_list(generation)
    origin_parents: list[Chromosome]
    origin_parents = choices(generation, prob_list, k=count)
    return [Chromosome(p.gens) for p in origin_parents]


def get_weight_list(chromosome_list: list, reverse=False):
    fittness_list = [c.get_fittness() for c in chromosome_list]
    min_fittness = min(fittness_list)
    if min_fittness < 0:
        fittness_list = [fittness - min_fittness for fittness in fittness_list]

    fittness_sum = sum(fittness_list)
    assert fittness_sum != 0

    weight_list = [p / fittness_sum for p in fittness_list]

    assert any([0 <= p <= 1 for p in weight_list])
    if reverse:
        return [1 - p for p in weight_list]
    else:
        return weight_list