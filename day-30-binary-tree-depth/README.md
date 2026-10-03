# Day 30 — Binary Tree Depth

## 1. Problem

An organization hierarchy can be represented as a binary tree.

Each employee can have at most two direct reports:

- left child
- right child

The objective is to find the maximum number of employee levels
from the root employee to the deepest employee.

---

## 2. Depth Definition

This implementation measures depth using the number of nodes.

Therefore:

```text
Empty tree → 0
One node → 1
Two nodes → 2
Three nodes → 3