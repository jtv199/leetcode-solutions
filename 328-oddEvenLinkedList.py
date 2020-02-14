# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val}->{self.next}'

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        self.evenHead = None
        self.evenTail = None
        self.oddHead = head
        self.oddTail = head
        i = 2
        point = head.next

        while point:
            if i == 2:
                self.evenHead = point
                self.evenTail = point
                point = point.next
            elif i % 2 == 0:
                # if even
                self.evenTail.next = point
                self.evenTail = point
                point = point.next
            else:
                self.oddTail.next = point
                self.oddTail = point
                point = point.next

            print(point)

            i += 1

        self.evenTail.next = None
        point = self.evenHead
        self.oddTail.next = self.evenHead
        return self.oddHead


if __name__ == '__main__':
    a = ListNode(1)
    point = a

    for i in range(2,6):
        point.next = ListNode(i)
        point = point.next

    print(a)

    sol = Solution()
    l = sol.oddEvenList(a)
    print(a)
