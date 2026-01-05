**CIRCUIT-SAT (Boolean Circuit Satisfiability)** is a classic decision problem in computational complexity:

> **Given a Boolean circuit, is there an assignment of inputs that makes the circuit output `TRUE`?**

---

## Formal Definition

**Input:**  
A Boolean **circuit** built from logic gates such as:

- AND (∧)
    
- OR (∨)
    
- NOT (¬)
    

with:

- Input nodes (Boolean variables)
    
- Gate nodes
    
- One designated **output gate**
    

**Question:**  
Does there exist some assignment of `0/1` values to the input variables so that the final output evaluates to **1 (TRUE)**?

---

## Example

Suppose the circuit implements the expression:

$$
(x \land y) \lor (\neg x)  
$$

Try input assignments:

|x|y|Output|
|---|---|---|
|0|0|1|
|0|1|1|
|1|0|0|
|1|1|1|

Since **some assignments produce 1**, the circuit is **satisfiable**, so this instance of CIRCUIT-SAT returns **YES**.

---

## Why It Matters

### ✅ CIRCUIT-SAT is **NP-Complete**

- **In NP:**  
    If someone gives you an assignment, you can evaluate the circuit in **polynomial time**.
    
- **NP-hard:**  
    Every problem in NP can be reduced to CIRCUIT-SAT in polynomial time.
    
- **Cook–Levin Theorem:**  
    Originally proved SAT (CNF-SAT) is NP-complete.  
    CIRCUIT-SAT is often treated as a more **general** NP-complete problem because:
    
    ```text
    CIRCUIT-SAT ⟺ SAT
    ```
    
    Both problems are polynomial-time equivalent.
    

---

## Relationship to SAT

|Problem|Representation|
|---|---|
|**SAT**|Boolean formula (usually CNF)|
|**CIRCUIT-SAT**|Boolean circuit (DAG of gates)|

- A SAT formula can be converted into a circuit.
    
- A circuit can be converted into a SAT formula (using Tseitin transformation).
    

Thus:

> They are equally powerful from a complexity point of view.

---

## Differences at a Glance

|Feature|SAT|CIRCUIT-SAT|
|---|---|---|
|Structure|Boolean formula|Boolean circuit (DAG)|
|Size|May repeat subexpressions|Allows sharing subcircuits|
|Practical use|Standard SAT solvers|Hardware verification, synthesis|
|Complexity|NP-complete|NP-complete|

---

P can be reduced to NP in poly-time.
**TRIVIAL = {⟨x⟩ : x is any string}** (always accept — very easy, in P)

**3-SAT** (known NP-complete problem)

###  TRIVIAL ≤ₚ 3-SAT