class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    
    return dummy.next

def parse_input(input_str):
    nums = list(map(int, input_str.split(',')))
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(','.join(res))

if __name__ == "__main__":
    list1_str = input("Nhập list1: ")
    list2_str = input("Nhập list2: ")

    list1 = parse_input(list1_str)
    list2 = parse_input(list2_str)

    merged_list = mergeTwoLists(list1, list2)
    print("Kết quả sau khi hợp nhất hai danh sách:")
    print_list(merged_list)
