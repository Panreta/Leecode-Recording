Yes! Here's a 2-column layout that fits on 2 pages:

```python
# RB-INSERT(T, z)                    # LEFT-ROTATE(T, x)
y = T.nil                            y = x.right
x = T.root                           x.right = y.left
while x != T.nil:                    if y.left != T.nil:
    y = x                                y.left.p = x
    if z.key < x.key:                y.p = x.p
        x = x.left                   if x.p == T.nil:
    else:                                T.root = y
        x = x.right                  elif x == x.p.left:
z.p = y                                  x.p.left = y
if y == T.nil:                       else:
    T.root = z                           x.p.right = y
elif z.key < y.key:                  y.left = x
    y.left = z                       x.p = y
else:
    y.right = z
z.left = T.nil
z.right = T.nil
z.color = RED
RB-INSERT-FIXUP(T, z)
```

```python
# RB-INSERT-FIXUP(T, z)              # RB-TRANSPLANT(T, u, v)
while z.p.color == RED:              if u.p == T.nil:
    if z.p == z.p.p.left:                T.root = v
        y = z.p.p.right              elif u == u.p.left:
        if y.color == RED:               u.p.left = v
            z.p.color = BLACK        else:
            y.color = BLACK              u.p.right = v
            z.p.p.color = RED        v.p = u.p
            z = z.p.p
        elif z == z.p.right:
            z = z.p
            LEFT-ROTATE(T, z)
        z.p.color = BLACK
        z.p.p.color = RED
        RIGHT-ROTATE(T, z.p.p)
    else:
        # same with "right" and 
        # "left" exchanged
T.root.color = BLACK
```

```python
# RB-DELETE(T, z)                    # RB-DELETE-FIXUP(T, x)
y = z                                while x != T.root and x.color == BLACK:
y-original-color = y.color               if x == x.p.left:
if z.left == T.nil:                          w = x.p.right
    x = z.right                              if w.color == RED:
    RB-TRANSPLANT(T, z, z.right)                 w.color = BLACK        # case 1
elif z.right == T.nil:                           x.p.color = RED        # case 1
    x = z.left                                   LEFT-ROTATE(T, x.p)    # case 1
    RB-TRANSPLANT(T, z, z.left)                  w = x.p.right          # case 1
else:                                        if w.left.color == BLACK and 
    y = TREE-MINIMUM(z.right)                   w.right.color == BLACK:
    y-original-color = y.color                   w.color = RED          # case 2
    x = y.right                                  x = x.p                # case 2
    if y.p == z:                             else if w.right.color == BLACK:
        x.p = y                                  w.left.color = BLACK   # case 3
    else:                                        w.color = RED          # case 3
        RB-TRANSPLANT(T, y, y.right)             RIGHT-ROTATE(T, w)     # case 3
        y.right = z.right                        w = x.p.right          # case 3
        y.right.p = y                        w.color = x.p.color        # case 4
    RB-TRANSPLANT(T, z, y)                   x.p.color = BLACK          # case 4
    y.left = z.left                          w.right.color = BLACK      # case 4
    y.left.p = y                             LEFT-ROTATE(T, x.p)        # case 4
    y.color = z.color                        x = T.root                 # case 4
if y-original-color == BLACK:            else:
    RB-DELETE-FIXUP(T, x)                    # same with "right" and "left" exchanged
                                     x.color = BLACK
```