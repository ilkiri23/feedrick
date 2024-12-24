from dataclasses import dataclass

@dataclass
class Node:
    id: int
    name: str
    children: list['Node'] | None = None

@dataclass
class Tree:
    nodes: list[Node]