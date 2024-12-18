'''给你两个 非空 的链表，表示两个非负的整数。
它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。'''

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # def addTwoNumbers(self, l1, l2):
        l1_list=[]
        l2_list=[]
        current=l1
        # while None:
        #     print("None ?????")
        while current:
            print(f"current.val: {current.val}")
            l1_list.append(current.val)
            current = current.next
        current=l2
        while current:
            l2_list.append(current.val)
            current = current.next
        print(l1_list)
        print(l2_list)

        result_nodes=[]
        result_nodes_=ListNode()
        flag=0
        length1=len(l1_list)
        length2=len(l2_list)

        if length1<length2:
            l1_list, l2_list = l2_list, l1_list

        for i in range(len(l1_list)):
            new_node=ListNode()
            if i<len(l2_list):
                if l1_list[i]+l2_list[i]+flag>=10:
                    new_node.val=l1_list[i]+l2_list[i]+flag-10
                    new_node.next=None
                    result_nodes.append(new_node)
                    flag=1
                else:
                    new_node.val=l1_list[i]+l2_list[i]+flag
                    new_node.next=None   
                    result_nodes.append(new_node) 
                    flag=0
            else:
                if l1_list[i]+flag>=10:
                    new_node.val=l1_list[i]+flag-10
                    new_node.next=None
                    result_nodes.append(new_node)   
                    flag=1
                else:
                    new_node.val=l1_list[i]+flag
                    new_node.next=None   
                    result_nodes.append(new_node)  
                    flag=0            
        if flag==1:
            new_node=ListNode()
            new_node.val=1
            new_node.next=None
            result_nodes.append(new_node)
        print(result_nodes)

        current = result_nodes[0] 
        for node in result_nodes[1:]:
            current.next=node
            current = current.next

        print(result_nodes[0])
        return result_nodes[0]

a=Solution()

l1=[2,4,3]
l2=[5,6,4]

l1=[9,9,9,9,9,9,9]
l2=[9,9,9,9]


def convert_list_to_node(l1,l2):
    l1n=ListNode()
    l2n=ListNode()
    l1l=[]
    l2l=[]

    for i in range(0,len(l1)):
        new_node=ListNode()
        new_node.val=l1[i]
        new_node.next=None
        l1l.append(new_node)
    for i in range(0,len(l2)):
        new_node=ListNode()
        new_node.val=l2[i]
        new_node.next=None
        l2l.append(new_node)
    print(l1l,"\n",l2l)
    current = l1l[0] 
    for node in l1l[1:]:
        current.next=node
        current = current.next    

    current = l2l[0] 
    for node in l2l[1:]:
        current.next=node
        current = current.next  

    print(l1l[0],"\n",l2l[0])
    return l1l[0] ,l2l[0] 

l1n,l2n=convert_list_to_node(l1,l2)
a.addTwoNumbers(l1n,l2n)
