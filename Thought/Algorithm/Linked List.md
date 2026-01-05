basic building way:

```python
# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next
```

Use List to build a linked list:

```python
def createList(arr):

    head = ListNode(arr[0]) # build the first node by the first value

    current = head

    for i in range(1, len(arr)):

        current.next = ListNode(arr[i]) # use the head to link to the next one

        current = current.next

    return head
```

