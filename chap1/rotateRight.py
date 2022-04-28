from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head.next:
        return head

    last, n = head, 1
    while last.next:
        last = last.next
        n += 1

    if k % n == 0:
        return head

    middle = head
    for _ in range(n - k % n - 1):
        middle = middle.next

    new_head = middle.next
    last.next = head
    middle.next = None
    return new_head

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
ans1 = rotateRight(head1, 2)

while ans1:
    print(ans1.val)
    ans1 = ans1.next

head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
ans2 = rotateRight(head2, 4)

while ans2:
    print(ans2.val)
    ans2 = ans2.next
