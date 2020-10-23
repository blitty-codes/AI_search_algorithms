# Index
1. [Information](#information)
2. [Notes](#notes)
3. [Type of Algorithms](#types-of-algorithms)
4. [Todo](#todo)
5. [Utility](#utility)
6. [Biography](#biography)

# Information
With this program you can create a random graph or
use one of your interest.

You can **test search algorithms** in a **graph**, and see if
there is a **solution**, _from a node A to another B_,
if the algorithm is **informative** then we will need a
graph with **heuristics** and **costs**. If not, you just
need **costs**.

If you choose the **random graph**, it will have _**no reflexive**_
nodes, also the **last node** is the **objective** to be searched,
if you want to **change** this objective, **it will be asked**.

# Notes
Be careful with **cyclic graphs**, some algorithms will be on a **loop**. Ex._
```
This happens in the hill climbing algorithm because we do not save the nodes
that have already been visited.

Nodes: [('4', 0), ('1', 1.81), ('2', 1.35), ('3', 0.95)]

Relations: [('4', '1', 2.73), ('1', '2', 1.68), ('2', '3', 0.37), ('3', '1', 0.67), ('3', '2', 2.65)]

When the end node is 4, and we start in node 1 we may get a loop like
this 1 -> 2 -> 3 -> 2 -> 3 -> .... and so on, this case happens in **hill climbing**
algorithm, because it takes the minimum heuristic, which the next to 3 is 2 and next
to 2 is 3, so we get a cyclic and infinite loop.
```
**This is solve removing the nodes which has been already visited in the current path.**

### A graph is formed with:
  - sources [] -> nodes where the arrow starts
  - targets [] -> nodes which the arrow points
  - heuristics [] -> the heuristic of a graph
  - weight [] -> the costs of weight reference to
      the arrow that goes from sources[x] to targets[x]

`If there is no heuristic applied then it is a non informed algorithm`

# Types of algorithms

| Non-informative | Informative |
|---|---|
| Deep search | Climb algorithm |
| Range search | First better algorithm |
| Branch & Bound | A* |

# Todo
- [x] Insert input graph
- [x] Convert into Objects
- [x] Random choice
- [x] Deep search algorithm
- [x] Range search algorithm
- [x] Climb algorithm
- [x] Branch & Bound algorithm
- [x] First better algorithm
- [x] A*
- [x] Draw graph
- [ ] Read from a file the graph
- [ ] Save a graph into a file

# Solved problems
- When on algorithms like deep_search, range_search, hill_climbing, the end was
change, the element end goes to a **str** type, on the other case, we get an **int**,
since the name can be anything, the end is going to be send as **string**

# Utility
- Heuristic
    - https://en.wikipedia.org/wiki/Heuristic
- Hill Climbing
    - https://en.wikipedia.org/wiki/Hill_climbing
    - https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/

# Biography:
  - UPM search algorithms from 1st unit AI
  - http://micaminomaster.com.co/grafo-algoritmo/libreria-grafos-dinamicos/
  - https://es.wikipedia.org/wiki/Grado_(teor%C3%ADa_de_grafos) (Lema apreton de manos)
  - https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/

**Update: blitty-codes 18-Oct-2020**