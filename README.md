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

A graph is formed with:
  - sources [] -> nodes where the arrow starts
  - targets [] -> nodes which the arrow points
  - heuristics [] -> the heuristic of a graph
  - weight [] -> the costs of weight reference to
      the arrow that goes from sources[x] to targets[x]

`If there is no heuristic applied then it is a non informed algorithm`

#### Types of algorithms:

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
- [ ] Branch & Bound algorithm
- [ ] Climb algorithm
- [ ] First better algorithm
- [ ] A*
- [ ] Draw graph
- [ ] Read from a file the graph

# Biography:
  - UPM search algorithms from 1st unit AI
  - http://micaminomaster.com.co/grafo-algoritmo/libreria-grafos-dinamicos/
  - https://es.wikipedia.org/wiki/Grado_(teor%C3%ADa_de_grafos) (Lema apreton de manos)

**Update: blitty-codes 16-Oct-2020**
