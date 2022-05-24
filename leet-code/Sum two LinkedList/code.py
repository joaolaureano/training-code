# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        excess = 0
        rtype = ListNode(-1)
        pointer = rtype

        while (l1 or l2 or excess):
            new_value = 0
            if l1:
                new_value += l1.val
                l1 = l1.next

            if l2:
                new_value += l2.val
                l2 = l2.next

            new_value += excess

            excess = new_value // 10
            new_value = new_value % 10

            pointer.next = ListNode(new_value)

            pointer = pointer.next
        
        return rtype.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

print(result)