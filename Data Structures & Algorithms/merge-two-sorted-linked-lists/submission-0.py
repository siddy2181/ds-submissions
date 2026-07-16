# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        if not list1: return list2
        if not list2: return list1
        dummy =result = ListNode(min(list1.val,list2.val))

        while list1:
            sorted_list.append(list1.val)
            list1=list1.next
        while list2:
            sorted_list.append(list2.val)
            list2=list2.next
        
        sorted_list.sort()
        print(sorted_list)
        for i in sorted_list:
            result.next = ListNode(i)
            result = result.next

        return dummy.next