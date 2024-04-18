class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Khởi tạo nút giả (dummy) để bắt đầu
    dummy = ListNode(0)
    # current là con trỏ hiện tại đang trỏ đến nút cuối cùng của danh sách đã hợp nhất
    current = dummy
    
    # Duyệt qua cả hai danh sách
    while list1 and list2:
        # So sánh giá trị của nút hiện tại trong mỗi danh sách
        if list1.val < list2.val:
            # Nếu giá trị của nút trong list1 nhỏ hơn, thêm nút đó vào danh sách đã hợp nhất
            current.next = list1
            # Di chuyển con trỏ của list1 sang phần tử tiếp theo
            list1 = list1.next
        else:
            # Nếu giá trị của nút trong list2 nhỏ hơn hoặc bằng, thêm nút đó vào danh sách đã hợp nhất
            current.next = list2
            # Di chuyển con trỏ của list2 sang phần tử tiếp theo
            list2 = list2.next
        # Di chuyển con trỏ của danh sách đã hợp nhất sang phần tử tiếp theo
        current = current.next
    
    # Khi một trong hai danh sách kết thúc, nối danh sách còn lại vào danh sách đã hợp nhất
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    # Trả về nút đầu tiên của danh sách đã hợp nhất
    return dummy.next
