# Represent
Adjacency List

Adjacency Matrix


• Adjacency list

	• Θ( 𝑉 + 𝐸 ) space
	
	• Compact (in terms of space) representation of sparse ( 𝐸 ≪ 𝑉 ଶ) graphs
	
	• 𝑂( 𝑉 ) time to check if vertex 𝑗 is adjacent to vertex 𝑖: Need to     traverse the
	
	list 𝐴𝑑𝑗[𝑖], which may contain as many vertices as |𝑉|.

• Adjacency matrix

• 𝑂(1) time (always) to check if vertex 𝑗 is adjacent to vertex 𝑖 (if there’s an

edge from vertex 𝑖 to vertex 𝑗)

• Θ( $V^2$) space (always, even for very sparse graphs)


# BFS

First-In, First-Out (FIFO): Queue data structure suits this well!

𝑂(𝑉 + 𝐸).


# DFS
DFS, Last-Discovered, First-Explored!

```markdown
### Depth-First Search (DFS)

```text
DFS(G)

for each vertex u ∈ G.V
    u.color = WHITE
    u.π = NIL

time = 0

for each vertex u ∈ G.V
    if u.color == WHITE
        DFS-VISIT(G, u)

```

```markdown
DFS-VISIT(G, u)

time = time + 1                  // u has just been discovered
u.d = time
u.color = GRAY

for each v ∈ G.Adj[u]            // explore edge (u, v)
    if v.color == WHITE
        v.π = u
        DFS-VISIT(G, v)

u.color = BLACK                  // u is finished
time = time + 1
u.f = time
```

𝑂(𝑉 + 𝐸).


# Application:
Topological Sort

Strong Connected Components

for every pair of vertices 𝑢, 𝑣 ∈ 𝐶, they are reachable from each other.

```java
STRONGLY-CONNECTED-COMPONENTS(G)

1. Call DFS(G) to compute finishing times f[u] for each vertex u.
2. Compute Gᵀ (the transpose graph of G).
3. Call DFS(Gᵀ), but in the main DFS loop, consider the vertices
   in order of decreasing f[u] (as computed in step 1).
4. Output the vertices of each DFS tree formed in step 3
   as a separate strongly connected component.

```

- Performs **2 DFS traversals** → Θ(V + E)
- Constructing the transpose graph **Gᵀ** → O(V + E)
- **Total time complexity:** Θ(V + E)

---
MST：(Graph is **sparse** (few edges))

![[Pasted image 20251206215730.png]]

in cut, there must be a smallest edge there, like 2, but cut in the picture only has 3,4,5. 
No 2.

```markdown
## MST-KRUSKAL(G, w)

1. A = ∅
2. for each vertex v ∈ G.V
3.     MAKE-SET(v)
4. sort the edges of G.E into nondecreasing order by weight w
5. for each edge (u, v) ∈ G.E, taken in nondecreasing order by weight
6.     if FIND-SET(u) ≠ FIND-SET(v)
7.         A = A ∪ {(u, v)}
8.         UNION(u, v)
9. return A
```

$O(ElgV)$ 

```java
## MST-PRIM(G, w, r)

1. for each u ∈ G.V
2.     u.key = ∞
3.     u.π = NIL
4. r.key = 0
5. Q = G.V
6. while Q ≠ ∅
7.     u = EXTRACT-MIN(Q)
8.     for each v ∈ G.Adj[u]
9.         if v ∈ Q and w(u, v) < v.key
10.            v.π = u
11.            v.key = w(u, v) //approximaty, Dij doesn't have
```


**Time Complexity Analysis:**

- **Line 1-5**: BUILD-MIN-HEAP → O(V)
- **Line 6-7**: While loop runs |V| times, each EXTRACT-MIN → O(lg V)
    - Total for EXTRACT-MIN: O(V lg V)
- **Line 8**: For loop iterates O(E) times total (amortized across all iterations)
    - Since ∑|Adj(v)| = 2|E|
- **Line 9**: Q membership test → O(1) (with flags)
- **Line 11**: DECREASE-KEY on min-heap → O(lg V)
    - Total for DECREASE-KEY: O(E lg V)

**Total: O(V lg V + E lg V) = O(E lg V)**

(Since V ≤ E in a connected graph)

---
Non-weighted: BFS,

Weighted: Bellman-ford


A shortest path can’t have a cycle.

```python
Relaxation:
1. if v.d > u.d + w(u, v)
2.     v.d = u.d + w(u, v)
3.     v.π = u
```

```python
BELLMAN-FORD(G, w, s)
1. INITIALIZE-SINGLE-SOURCE(G, s)
2. for i = 1 to |G.V| - 1
3.     for each edge (u, v) ∈ G.E
4.         RELAX(u, v, w)
5. for each edge (u, v) ∈ G.E
6.     if v.d > u.d + w(u, v)
7.         return FALSE
8. return TRUE
```

```python
## INITIALIZE-SINGLE-SOURCE(G, s)

1. for each vertex v ∈ G.V
2.     v.d = ∞
3.     v.π = NIL
4. s.d = 0
```
1. do every point, search all the out-edges.
2. if change u.d, check all the out-edges of u.4

Directed-Acyclic Graphs:
use Topology sort first:O(V+E),and go all the subpath of starting point to find if can go to a vertex.

$O(E + V)$.


---

```python
DIJKSTRA(G, w, s)

1. INITIALIZE-SINGLE-SOURCE(G, s)
2. S = ∅
3. Q = G.V
4. while Q ≠ ∅
5.     u = EXTRACT-MIN(Q)
6.     S = S ∪ {u}
7.     for each vertex v ∈ G.Adj[u]
8.         RELAX(u, v, w)
```

```python
Time complexity analysis:

- Line 1, 3: Θ(V)

- While loop repeats |V| times

- Line 5: O(V) if using array, O(lg V) if using heap

- For loop repeats |E| times total (amortized)

- Line 8: O(1) if using array, O(lg V) if using heap (DECREASE-KEY)

- ∴ O(V² + E) = O(V²) if using array

- O(V lg V + E lg V) if using heap

- O(E lg V) if connected

- Note O(E lg V) < O(V²) iff E = o(V²/lg V)

- Don't use heap for a dense graph!
```