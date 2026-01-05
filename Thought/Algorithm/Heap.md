Heap is a complete binary tree, which means you need to fulfill the left then do the right.

---

### 🔹 Given array:

[  
[6, 25, 54, 21, 32, 19, 70]  
]

---

## 🧩 1. Building **Max Heap by _item-by-item insertion_**

This means:  
→ Start with an empty heap.  
→ Insert each element one by one, _bubbling up_ to maintain the **Max Heap** property after each insertion.

Let’s do it:

### Step 1: Insert 6

Heap = `[6]`

---

### Step 2: Insert 25

Heap array before reheapify: `[6, 25]`  
→ Compare 25 with its parent 6.  
25 > 6 ⇒ swap.

Heap = `[25, 6]`

---

### Step 3: Insert 54

Heap before fix: `[25, 6, 54]`  
→ 54 > parent(25), so swap.

Heap = `[54, 6, 25]`

---

### Step 4: Insert 21

Heap before fix: `[54, 6, 25, 21]`  
→ Parent of 21 is 6. 21 > 6 ⇒ swap.

Heap = `[54, 21, 25, 6]`

---

### Step 5: Insert 32

Heap before fix: `[54, 21, 25, 6, 32]`  
→ Parent of 32 is 21. 32 > 21 ⇒ swap.

Heap = `[54, 32, 25, 6, 21]`

---

### Step 6: Insert 19

Heap before fix: `[54, 32, 25, 6, 21, 19]`  
→ Parent of 19 is 25. 19 < 25 ⇒ no swap.

Heap = `[54, 32, 25, 6, 21, 19]`

---

### Step 7: Insert 70

Heap before fix: `[54, 32, 25, 6, 21, 19, 70]`  
→ Parent of 70 is 25. 70 > 25 ⇒ swap → `[54, 32, 70, 6, 21, 19, 25]`  
→ Now 70 > parent(54) ⇒ swap again.

✅ Final heap (item-by-item):  
[  
[70, 32, 54, 6, 21, 19, 25]  
]

---

## 🧩 2. Building **Max Heap using heapify** (bottom-up)

This means:  
→ Start with the full array `[6, 25, 54, 21, 32, 19, 70]`  
→ Treat it as a complete binary tree  
→ Then _heapify_ from the last non-leaf node up to the root.

---

### Step 1: Original array

Indexing (0-based):

```
        6
     /     \
   25       54
  /  \     /  \
21  32   19   70
```

---

### Step 2: Last non-leaf node = index ⌊n/2⌋−1 = 2
It is because leaves are almost half of node, want to start from an interior point

(heapify from 2, then 1, then 0)

#### i = 2 (value = 54)

Children: 19, 70 → largest child = 70  
→ swap 54 ↔ 70  
Array = `[6, 25, 70, 21, 32, 19, 54]`

---

#### i = 1 (value = 25)

Children: 21, 32 → largest child = 32  
→ swap 25 ↔ 32  
Array = `[6, 32, 70, 21, 25, 19, 54]`

---

#### i = 0 (value = 6)

Children: 32, 70 → largest child = 70  
→ swap 6 ↔ 70  
Array = `[70, 32, 6, 21, 25, 19, 54]`

→ Now heapify index 2 (value = 6)  
Children: 19, 54 → largest = 54  
→ swap 6 ↔ 54  
Array = `[70, 32, 54, 21, 25, 19, 6]`

✅ Final heap (heapify method):  
[  
[70, 32, 54, 21, 25, 19, 6]  
]

---

## 🧮 Summary

|Method|Final Max Heap|Time Complexity|
|:--|:--|:--|
|**Item-by-item insertion**|`[70, 32, 54, 6, 21, 19, 25]`|**O(n log n)**|
|**Heapify (bottom-up)**|`[70, 32, 54, 21, 25, 19, 6]`|**O(n)**|

---

✅ **Key difference:**

- _Item-by-item insertion_ simulates dynamic heap growth — elements are inserted one at a time with repeated bubbling up.
    
- _Heapify_ works bottom-up — adjusts in-place more efficiently, resulting in a slightly different structure but still a valid max heap.
    

Would you like me to draw both heaps as binary trees to visually compare their structure?