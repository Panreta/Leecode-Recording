[[D.P.]] 

Below is **a complete, structured list** of classic problems that **can be solved by greedy**, plus an explanation of **why some problems require DP instead of greedy**.


This is meant to be your “all-in-one greedy reference”.

---

# ✅ **1. Problems That Can Be Solved by Greedy Algorithms**

Greedy algorithms work when making the **locally optimal choice** leads to the **global optimal solution**, usually because the problem has:

- **Greedy-choice property**
    
- **Optimal substructure**
    

Below is a categorized list of the most _standard, canonical, and interview-relevant_ greedy problems.

---

## **A. Scheduling / Interval Problems**![[Pasted image 20251201160355.png]]
choosing the deadlines to be monotonic,
intuition:
> **The activity that ends earliest leaves the most room for future activities.**

| Problem                             | Greedy Strategy                                |
| ----------------------------------- | ---------------------------------------------- |
| **Activity Selection**              | Pick interval with **earliest finishing time** |
| **Interval Scheduling**             | Same as above                                  |
| **Scheduling to Minimize Lateness** | Sort by **earliest deadline**                  |
| **Minimum Number of Meeting Rooms** | Sort by start time + min heap                  |
| **Merge Intervals**                 | Sort intervals by start time                   |

These work because once you choose the earliest-finish interval, it **maximizes freedom** for future choices.

---

## **B. Optimal Choice / Minimization Problems**

| Problem                                                              | Greedy Strategy                           |
| -------------------------------------------------------------------- | ----------------------------------------- |
| **Minimum Number of Coins (only canonical systems like U.S. coins)** | Largest coin first                        |
| **Rope Joining Problem**                                             | Always join two smallest ropes (min heap) |
| **Huffman Coding**                                                   | Combine two least frequencies repeatedly  |
| **Fractional Knapsack**                                              | Sort by **value/weight ratio**            |
| **Load Balancing on Two Machines**                                   | Greedy longest-job-first                  |
Remark: 0-1 Knapsack can not be solved by Greedy Algorithm, like 1,4,5 to represent 8.

---

## **C. Graph Problems**

|Problem|Greedy Strategy|
|---|---|
|**Prim's MST**|Add smallest edge that connects to tree|
|**Kruskal's MST**|Add smallest edge that doesn’t form a cycle|
|**Dijkstra**|Relax smallest-distance vertex first|
|**Topological Sorting (using indegree)**|Greedy pick node with indegree 0|
|**Bipartite graph matching with interval structure**|Always match earliest finishing interval|

---

## **D. String Problems**

|Problem|Greedy Strategy|
|---|---|
|**Reorganize String**|Always pick two most frequent chars|
|**Remove K digits**|Remove digits while the previous digit is larger|
|**Split into monotonic segments**|Pick locally optimal split|

---

## **E. Greedy Data Structure Problems**

|Problem|Greedy Strategy|
|---|---|
|**Task Scheduling with Cooldown**|Always schedule most frequent tasks first|
|**IPO / Select Projects**|Always pick project with maximum profit available|

---

# 🧠 **2. Why Some Problems Can Be Solved by DP but Not Greedy**

Greedy fails when:

### ❌ **1. Taking a local best choice destroys global optimality**

Example: **0/1 Knapsack**(NPC)

- Greedy picks highest value/weight ratio first.
    
- But the best solution may require taking **two medium items instead of one high-density item**.
    

This violates **greedy choice property**.

---

### ❌ **2. There are overlapping subproblems**

DP is required when:

- The optimal solution of a subproblem **depends on previous choices** that greedy cannot remember.
    

Example: **Longest Increasing Subsequence**

- Picking greedy local best (take whenever possible) is NOT optimal.
    
- Need DP or patience sorting.
    

---

### ❌ **3. Future decisions depend on past states**

Example: **DP on strings**

- Edit distance
    
- LCS
    
- Palindromic substrings  
    Greedy cannot "undo" previous decisions; DP can explore multiple states.
    

---

### ❌ **4. Optimal solution requires trying multiple branching paths**

Greedy only follows **one path**.  
DP tries **all possible states** and picks the best.

Example:  
**Partition equal subset sum** — must consider subsets, cannot greedy-pick numbers.

---

### ❌**5. Problem does NOT have the greedy-choice property**

Formal definition:

> A problem has greedy-choice property if a locally optimal choice leads to the global optimal.

If not, greedy cannot work.

---

# 🆚 **3. Concrete Comparison: DP vs Greedy**

|Problem|Greedy?|DP?|Why|
|---|---|---|---|
|Activity selection|✔ Yes|✖ No need|Earliest finish = optimal|
|MST (Prim, Kruskal)|✔ Yes|✖ unnecessary|Safe edge property|
|Fractional knapsack|✔ Yes|✖ unnecessary|Ratios make greedy optimal|
|0/1 Knapsack|❌ No|✔ Yes|Local best ratio fails|
|LIS|❌ No|✔ Yes|Need global comparison|
|Coin Change (U.S.)|✔ Yes|✔ Yes|Canonical coin system|
|Coin Change (general)|❌ No|✔ Yes|Greedy fails: counterexamples|
|Shortest Path (positive weights)|✔ Dijkstra|✔ Bellman-Ford|Works because weights are positive|
|Shortest Path (negative weights)|❌ Dijkstra fails|✔ Bellman-Ford|Greedy gets stuck|

---

# 🧪 **4. Quick Greedy Test Checklist (for any new problem)**

Ask:

### **1. Does picking the best local choice always leave the best future?**

If **no**, greedy fails.

### **2. Can I prove "exchange argument"?**

Meaning you can transform any optimal solution into your greedy solution without making it worse.

### **3. Does the problem have:**

- **Optimal substructure**
    
- **Greedy-choice property**
    

If both = greedy  
If only the first = usually DP

---

# 🎁 Want a concrete list of **LeetCode greedy problems**?

I can generate:

- 📘 Sorted by difficulty
    
- 📗 Sorted by topic (intervals, heap, DP vs greedy)
    
- 📙 Roadmap to master greedy in 10 days
    

Just tell me which format you want.



Not all optimization problems exhibit optimal substructure: shortest path