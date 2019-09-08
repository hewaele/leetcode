# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# [2,4,3]
# [5,6,4]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def addTwoNumbers(self, l1, l2):
        a = []
        b = []
        temp = l1
        while temp.next != None:
            a.append(str(temp.val))
            temp = temp.next
        a.append(str(temp.val))


        temp = l2
        while temp.next != None:
            b.append(str(temp.val))
            temp = temp.next
        b.append(str(temp.val))
        a.reverse()
        b.reverse()


        a = ''.join(a)
        b = ''.join(b)
        sum = int(a)+int(b)

        sum = str(sum)
        sum = [i for i in sum]
        sum.reverse()
        #将sum拆开
        head = ListNode(sum[0])
        temp = head
        for i in sum[1:]:
            temp.next = ListNode(i)
            temp = temp.next

        return head


#创建一个链表输入
a = ListNode(2)
temp = a
for i in [4, 3]:
    temp.next = ListNode(i)
    temp = temp.next

b = ListNode(5)
temp = b
for i in [6, 4]:
    temp.next = ListNode(i)
    temp = temp.next

test = Solution()
result = test.addTwoNumbers(a, b)
print(result)

