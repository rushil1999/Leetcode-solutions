import ("fmt")

type LRUCache struct {
    head *Node
    tail *Node
    cache map[int]*Node
    capacity int
    size int
}

type Node struct {
    value int
    key int
    next *Node
    prev *Node
}

func Constructor(capacity int) LRUCache {
    cache := make(map[int]*Node)
    tail := &Node{value: -2, key: -2, next: nil, prev: nil}
    head := &Node{value: -1, key: -1, next: tail, prev: nil}
    head.next = tail
    tail.prev = head
    lruCache := LRUCache{cache: cache, head: head, tail: tail, size: 0, capacity: capacity}
    return lruCache
}

func (this * LRUCache) printLinkedList() {
    fmt.Println("--------------------------")
    ptr := this.head
    for ptr != nil {
        fmt.Println(ptr.key, ptr.value)
        ptr = ptr.next
    }
} 


func (this *LRUCache) addFirst(node *Node) {
    currentFirstElement := this.head.next
    this.head.next = node
    node.prev = this.head
    node.next = currentFirstElement
    currentFirstElement.prev = node
}

func (this *LRUCache) removeElement(node *Node) {
    nextElement := node.next
    prevElement := node.prev
    prevElement.next = nextElement
    nextElement.prev = prevElement
    node.next = nil
    node.prev = nil
}

func (this *LRUCache) removeLast() {
    lastElement := this.tail.prev
    lastElement.prev.next = this.tail
    this.tail.prev = lastElement.prev
    lastElement.prev = nil
    lastElement.next = nil
    delete(this.cache, lastElement.key)
}

func (this *LRUCache) Get(key int) int {
    if node, ok := this.cache[key]; ok {
        this.removeElement(node)
        delete(this.cache, key)
        newNode := &Node{value: node.value, key: node.key}
        this.addFirst(newNode)
        this.cache[key] = newNode
        return this.cache[key].value
    } else {
        return -1
    }
}


func (this *LRUCache) Put(key int, value int)  {

    if node, ok := this.cache[key]; ok {
        this.removeElement(node)
        delete(this.cache, key)
        newNode := &Node{value: value, key: key}
        this.addFirst(newNode)
        this.cache[key] = newNode
    } else {
            if this.size == this.capacity {
                this.removeLast()
                this.size -= 1
            }
        newNode := &Node{value: value, next: nil, prev: nil, key: key}
        this.cache[key] = newNode
        this.addFirst(newNode)
        this.size += 1
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */