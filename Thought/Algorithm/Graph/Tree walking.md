
![[Pasted image 20251027133154.png]]
![[Pasted image 20251027133249.png]]

```python
def helper(root):

if not root: return True, 0

else:

r_avl, r_height = helper(root.right)

l_avl, l_height = helper(root.left)

return r_avl and l_avl and abs(r_height - l_height) <= 1, \

max(r_height, l_height) + 1
```