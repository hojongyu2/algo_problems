class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head = None):
        if head == None:
            return None
        return list_to_ll(ll_to_list(head))

def ll_to_list(curr_node):
    output = []
    while curr_node:
        output.insert(0, curr_node.val)
        curr_node = curr_node.next
    return output

def list_to_ll(reversed_list):
    ll = ListNode(reversed_list[0])
    current_head = ll
    for i in reversed_list[1:]:
        current_head.next = ListNode(i)
        current_head = current_head.next
    return ll

num_one = ListNode(1)
num_two = ListNode(2)
num_three = ListNode(3)
num_one.next = num_two
num_two.next = num_three
print(num_one.next.val)
# print(Solution.reverseList(num_one))