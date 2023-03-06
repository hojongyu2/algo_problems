# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_head = list1
        list2_head = list2
        list_arr = []
        while list1:
            list_arr.append(list1.val)
            list1 = list1.next
        while list2:
            list_arr.append(list2.val)
            list2 = list2.next
        sorted_arr = sorted(list_arr)
        if len(sorted_arr) == 0:
            return ListNode().next

        linklist = ListNode(sorted_arr[0])
        head = linklist
        for num in sorted_arr[1:]:
            head.next = ListNode(num)
            head = head.next
        return linklist