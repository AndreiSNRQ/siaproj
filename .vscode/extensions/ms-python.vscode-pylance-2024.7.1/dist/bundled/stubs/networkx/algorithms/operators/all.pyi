from itertools import zip_longest

from numpy.typing import ArrayLike

__all__ = ["union_all", "compose_all", "disjoint_union_all", "intersection_all"]

def union_all(graphs, rename: bool = ...): ...
def disjoint_union_all(graphs: ArrayLike): ...
def compose_all(graphs: ArrayLike): ...
def intersection_all(graphs: ArrayLike): ...