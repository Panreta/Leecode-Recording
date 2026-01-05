
# 1. What is CNF?

**CNF = Conjunctive Normal Form**

A Boolean formula is in CNF if it is:

[  
\text{(clause)} \land \text{(clause)} \land \cdots \land \text{(clause)}  
]

Each **clause** is an **OR** of **literals**:

[  
(x_1 \lor \neg x_2 \lor x_3)  
]

A **literal** = variable or its negation:

- ( x )
    
- ( \neg x )
    

---

### Example CNF formula

[  
(x \lor y \lor \neg z)  
;\land;  
(\neg x \lor y)  
;\land;  
(z)  
]

---

## k-CNF

A formula is **k-CNF** if:

> Each clause has **at most k literals**.

---

Examples:

- **2-CNF**  
    [  
    (a \lor \neg b) \land (c \lor d) \land (\neg e \lor f)  
    ]
    
- **3-CNF**  
    [  
    (x \lor y \lor z) \land (\neg x \lor a \lor b)  
    ]
    

---

---

# 2. What are 2-SAT and 3-SAT?

They are SAT restricted to k-CNF formulas:

| Problem | Input | Question |  
|---------|-------|  
| **2-SAT** | 2-CNF formula | Is it satisfiable? |  
| **3-SAT** | 3-CNF formula | Is it satisfiable? |

---

---

# 3. Why is **2-SAT in P**?

2-SAT has a beautiful **graph structure**.

---

## Implication Graph

Each clause

[  
(a \lor b)  
]

is equivalent to:

[  
(\neg a \Rightarrow b) \land (\neg b \Rightarrow a)  
]

For each clause we add **two directed edges**:

- ( \neg a \to b )
    
- ( \neg b \to a )
    

Create a **graph** with:

- One node for every literal (x, \neg x)
    
- Edges from implications
    

---

### Example

Clause:

[  
(x \lor y)  
]

Gives edges:

- ( \neg x \to y )
    
- ( \neg y \to x )
    

---

---

## Key Theorem for 2-SAT

> A 2-SAT formula is satisfiable **iff**  
> for no variable (x) do both (x) and (\neg x) lie in the **same strongly connected component (SCC)** of the implication graph.

---

### Why does this work?

- If (x) and (\neg x) imply each other via paths:
    
    [  
    x \Rightarrow \neg x \Rightarrow x  
    ]
    
    then both must be true ⇒ **contradiction**.
    

---

- SCC detection can be done by:
    
    - Kosaraju or Tarjan algorithms
        
    - **Linear time: O(V+E)**
        

---

### Result

✅ **2-SAT can be solved in polynomial (actually linear) time**

[  
\boxed{\text{2-SAT} \in \mathbf{P}}  
]

---

---

# 4. Why is **3-SAT NP-Complete?**

---

## Explosion of Logical Power

Allowing **three literals per clause** is the point where SAT becomes powerful enough to simulate any NP computation.

---

### Fundamental result:

[  
\boxed{\text{3-SAT is NP-complete}}  
]

---

### Why?

1. **SAT is NP-complete** (Cook–Levin theorem).
    
2. Any SAT formula can be converted into **3-CNF**:
    
    - Break long clauses into chains with fresh variables.
        
    
    Example:
    
    [  
    (a \lor b \lor c \lor d)  
    ]
    
    becomes:
    
    [  
    (a \lor b \lor y_1)  
    \land (\neg y_1 \lor c \lor y_2)  
    \land (\neg y_2 \lor d)  
    ]
    
3. This reduction is polynomial-time.
    

So:

[  
\text{SAT} \le_p \text{3-SAT}  
]

Hence 3-SAT is NP-hard, and since it’s also in NP:

✅ **3-SAT is NP-complete**

---

---

## Why 3-SAT is fundamentally harder than 2-SAT

### Structural difference:

|2-SAT|3-SAT|
|---|---|
|Can be modeled with a graph (implications)|No clean graph reduction|
|SCC algorithm solves it|No equivalent polynomial structure known|
|Constraints are “pairwise”|Constraints can encode **complex logical dependencies**|
|Linear-time solution exists|No known poly-time solution; NP-complete|

---

---

## Intuition

### 2-SAT

Clauses only compare **pairs of variables**.  
This limits complexity—you cannot express arbitrary computation.

It behaves like **simple implications**.

---

### 3-SAT

Clauses relate **three variables simultaneously**.  
This allows:

- Encoding **gadgets**
    
- Simulating **logic circuits**
    

Essentially:

> Three-variable interactions are enough to express all NP computations.

---

---

# 5. Visual Intuition

- **2-SAT = Graph reachability / SCC problem** ✅ easy.
    
- **3-SAT = Full Boolean satisfiability** ❌ NP-complete.
    

---

---

# 6. Summary

---

## Definitions

- **CNF:** AND of OR clauses.
    
- **k-CNF:** Clauses have ≤ k literals.
    
- **2-SAT:** SAT on 2-CNF.
    
- **3-SAT:** SAT on 3-CNF.
    

---

## Complexity

[  
\boxed{  
\begin{array}{c}  
\textbf{2-SAT} \in \mathbf{P} \  
\textbf{3-SAT} \text{ is NP-complete}  
\end{array}}  
]

---

---

## Final Intuition Answer

> 2-SAT is easy because it reduces to **graph SCC checking**.  
> 3-SAT is hard because allowing clauses of size 3 already makes it capable of **encoding arbitrary computation**, hence NP-complete.

---

If you'd like, I can also show:

- A full example of building an implication graph for 2-SAT
    
- A step-by-step reduction from SAT to 3-SAT
    
- The exact boundary proof: why k=2 is the last tractable case
    
- CSP perspective (binary vs ternary constraints)