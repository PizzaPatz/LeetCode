# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        string_lh = self.get_order_single_link_list(l1)
        string_rh = self.get_order_single_link_list(l2)
        string_lh = self.reverseString(string_lh, len(string_lh))
        string_rh = self.reverseString(string_rh, len(string_rh))
        int_lh = int(''.join(string_lh))
        int_rh = int(''.join(string_rh))
        result = int_lh + int_rh
        result = self.reverseString(list(str(result)), len(str(result)))
        result = self.string_to_linked_list(result)
        return result
    
    def get_order_single_link_list(self, single_linked_list):
        current_node = single_linked_list
        string_number = list()
        while(current_node != None):
            string_number.append(str(current_node.val))
            current_node = current_node.next
        return string_number

    def reverseString(self, s_array, l):
        for i in range(0, int(l/2)):
            s_array = self.swap(s_array, i, l-i-1)
        return s_array
    
    def swap(self, s_array, lh, rh):
        tmp = s_array[lh]
        s_array[lh] = s_array[rh]
        s_array[rh] = tmp
        return s_array

    def string_to_linked_list(self, result_list):
        root_linked_list = ListNode(int(result_list[0]))
        for i in range(1, len(result_list)):
            current_pointer = root_linked_list
            while(current_pointer.next != None):
                current_pointer = current_pointer.next
            current_pointer.next = ListNode(int(result_list[i]))
        return root_linked_list



run = Solution()

lh = ListNode(2)
lh.next = ListNode(4)
lh.next.next = ListNode(3)

rh = ListNode(5)
rh.next = ListNode(6)
rh.next.next = ListNode(4)

print(run.addTwoNumbers(lh, rh))