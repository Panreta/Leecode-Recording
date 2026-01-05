If you want to walk on the whole tree it will be $2^n$ .
```
CUT-ROD(p, n)
1  if n == 0
2      return 0
3  q = -∞
4  for i = 1 to n
5      q = max(q, p[i] + CUT-ROD(p, n - i))
6  return q
```


Top-down:
If you want MEMOIZED-CUT-ROD-AUX(\*,10,\*), you will need 9, then 8, then 7, until the
first element that didn't write on the table.
```markdown
MEMOIZED-CUT-ROD(p, n)
1  let r[0..n] be a new array
2  for i = 0 to n
3      r[i] = -∞
4  return MEMOIZED-CUT-ROD-AUX(p, n, r)

MEMOIZED-CUT-ROD-AUX(p, n, r)
1  if r[n] ≥ 0
2      return r[n]
3  if n == 0
4      q = 0
5  else q = -∞
6  for i = 1 to n
7      q = max(q, p[i] + MEMOIZED-CUT-ROD-AUX(p, n - i, r))
8  r[n] = q
9  return q
```


Or, just start from the first element to fulfill all.
And j is for in 1 -> j, go through all the ways of cutting to find the best.
```Bottom-up
BOTTOM-UP-CUT-ROD(p, n)
1  let r[0..n] be a new array
2  r[0] = 0
3  for j = 1 to n
4      q = -∞
5      for i = 1 to j
6          q = max(q, p[i] + r[j - i])
7      r[j] = q
8  return r[n]
```


Extended, we will see where we do the cutting.

```markdown
EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
1  let r[0..n] and s[1..n] be new arrays
2  r[0] = 0
3  for j = 1 to n
4      q = -∞
5      for i = 1 to j
6          if q < p[i] + r[j - i]
7              q = p[i] + r[j - i]
8              s[j] = i
9      r[j] = q
10 return r and s

PRINT-CUT-ROD-SOLUTION(p, n)
1  (r, s) = EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
2  while n > 0
3      print s[n]
4      n = n - s[n]
```
Here's the table in markdown form:

|i|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|s[i]|1|2|1|1|2|1|2|1|1|5|

**Question:** After running the dynamic programming algorithm (Extended-Bottom-Up-Cut-Rod method) for some input of the rod-cutting problem, the following array s[i] is produced. What is the optimal cutting for a rod with length 10 retrieved from this table?

**Answer:** 1, 2, 2, 5 ✓

according to 
n = 10
while n > 0:
  输出 s[n]
  n = n - s[n]

# Matrix Multiplication

```markdown
## MEMOIZED-MATRIX-CHAIN(p)

1. n = p.length - 1
2. let m[1..n, 1..n] be a new table
3. for i = 1 to n
4.     for j = i to n
5.         m[i, j] = ∞
6. return LOOKUP-CHAIN(m, p, 1, n)
```

```markdown
## RECURSIVE-MATRIX-CHAIN(p, i, j)

1. if i == j
2.     return 0
3. m[i, j] = ∞
4. for k = i to j - 1
5.     q = RECURSIVE-MATRIX-CHAIN(p, i, k)
           + RECURSIVE-MATRIX-CHAIN(p, k + 1, j)
           + p_{i-1}p_k p_j
6.     if q < m[i, j]
7.         m[i, j] = q
8. return m[i, j]
```

```markdown
## LOOKUP-CHAIN(m, p, i, j)

1. if m[i, j] < ∞
2.     return m[i, j]
3. if i == j
4.     m[i, j] = 0
5. else for k = i to j - 1
6.     q = LOOKUP-CHAIN(m, p, i, k)
           + LOOKUP-CHAIN(m, p, k + 1, j) + p_{i-1}p_k p_j
7.     if q < m[i, j]
8.         m[i, j] = q
9. return m[i, j]
```


# LCS:
```markdown
## LCS-LENGTH(X, Y)

1. m = X.length
2. n = Y.length
3. let b[1..m, 1..n] and c[0..m, 0..n] be new tables
4. for i = 1 to m
5.     c[i, 0] = 0
6. for j = 0 to n
7.     c[0, j] = 0
8. for i = 1 to m
9.     for j = 1 to n
10.        if x_i == y_j
11.            c[i, j] = c[i - 1, j - 1] + 1
12.            b[i, j] = "↖"
13.        elseif c[i - 1, j] ≥ c[i, j - 1]
14.            c[i, j] = c[i - 1, j]
15.            b[i, j] = "↑"
16.        else c[i, j] = c[i, j - 1]
17.            b[i, j] = "←"
18. return c and b
```

best: Θ min(𝑚, 𝑛) one is a suffix of the other.


Match:
```markdown
def Match(s, p):

m, n = len(s), len(p)

dp = [[None] * (n + 1) for _ in range(m + 1)]

dp[0][0] = True

for i in range(1, m + 1):

dp[i][0] = False

for i in range(m + 1):

for j in range(1, n + 1):

if p[j - 1] == ’*’:

dp[i][j] = dp[i][j - 1] or (i > 0 and dp[i - 1][j])

elif i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == ’?’):

dp[i][j] = dp[i - 1][j - 1]

else:

dp[i][j] = False

return dp[m][n]
```
# Optimal Binary Search Tree