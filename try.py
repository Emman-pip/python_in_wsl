class node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, list = node("root")):
        self.list = list

    def ___printListLogic(self, log, lst):
        while lst != None:
            if lst.next == None:
                log += f"({lst.value}) -> None"
                break
            log += f"({lst.value}) -> "
            lst = lst.next 
        return log

    def printList(self):
        log = "root -> "
        lst = self.list.next
        return self.___printListLogic(log, lst)

    def insert(self, node):
        lst = self.list
        while lst.next != None:
            lst = lst.next
        lst.next =  node

    def __findCase2(self, lst, count, index):
        while index != count:
            count += 1
            lst = lst.next
        return lst

    def find(self, index):
        count = 0
        lst = self.list
        if index < 1:
            return "INVALID INPUT: index starts at 1"
        try:
            return self.__findCase2(lst, count, index).value
        except:
            return "INVALID INPUT: index > length of the list"

def main():
    lL = LinkedList()
    node1 = node("asljkd")
    node2 = node("hahaha")
    lL.insert(node1)
    lL.insert(node2)
    lL.insert(node("dasiouhdasidhahudshdoashdioahdoashdiasdi"))
    
    print(lL.printList())
    print(lL.find(1))

if __name__ == "__main__":
    main()