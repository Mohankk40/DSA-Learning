public class singlyLinkedList{
    
    private ListNode head;

    private static class ListNode{
        private int data;
        private ListNode next;

        public ListNode(int data){
            this.data = data;
            this.next = null; 
        }
    }

    public int length(){
        if(head == null){
            return 0;
        }
        int count = 0;
        ListNode current = head;
        while(current != null){
            count++;
            current = current.next;
        }
        return count;
    }

    public void display(ListNode head){
        ListNode current = head;

        while(current != null){
            System.out.print(current.data + "-->");
            current = current.next;
        }
        System.out.print("null");
        System.out.println();
    }

    public void insertFirst(int value){
        ListNode newNode = new ListNode(value);
        newNode.next = head;
        head = newNode;
    }

    public void insert(int position, int value){
        ListNode node = new ListNode(value);
        if(position==1){
            node.next = head;
            head = node;
        } else {
            ListNode previous = head;
            int count = 1;

            while(count < position - 1){
                previous = previous.next;
                count++;
            }

            ListNode current = previous.next;
            previous.next = node;
            node.next = current;  
        }
    }

    public void insertLast(int value){
        ListNode newNode = new ListNode(value);
        if(head == null){
            head = newNode;
            return;
        }
        ListNode current = head;
        while(current.next != null){
            current = current.next;
        }
        current.next = newNode;
    }

    public ListNode deleteFirst(){
        if(head == null){
            return null;
        }

        ListNode temp = head;
        head = head.next;
        temp.next = null;
        return temp;
    }

    public void delete(int position){
        if(position == 1){
            head = head.next;
        } else {
            ListNode previous = head;
            int count = 1;
            while(count < position - 1){
                previous = previous.next;
                count++;
            }
            ListNode current = previous.next;
            previous.next = current.next;
        }
    }

    public ListNode deleteLast(){
        if(head == null || head.next == null){
            return head;
        }
        ListNode current = head;
        ListNode previous = null;
        while(current.next != null){
            previous = current;
            current = current.next;
        }
        previous.next = null;
        return current;

    }

    public boolean find(int searchKey){

        ListNode current = head;
        while(current != null){
            if(current.data == searchKey){
                return true;
            }
            current = current.next;
        }
        return false;
    }

    public ListNode reverse(ListNode head){
        ListNode current = head;
        ListNode previous = null;
        ListNode next = null;
        while(current != null){
            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        return previous;
    }
    
    public void removeDup(){
        ListNode current = head;

        while(current != null && current.next != null){
            if(current.data == current.next.data){
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }
    }

    public ListNode insertInSortedListNode(int value){
        ListNode newNode = new ListNode(value);

        ListNode current = head;
        ListNode temp = null;
        
        while( current != null && newNode.data > current.data){
            temp = current;
            current = current.next;
        }

        temp.next = newNode;
        newNode.next = current;

        return head;
    }

    public void deleteNode(int key){
        ListNode temp = null;
        ListNode current = head;
    
        while(current != null && current.data != key){
            temp = current;
            current = current.next;
        }

        if(current == null) return;
        
        temp.next = current.next;        
    }
    public static void main(String[] args){

        singlyLinkedList sll = new singlyLinkedList();

        // sll.head = new ListNode(10);
        // ListNode second = new ListNode(1);
        // ListNode third = new ListNode(8);
        // ListNode fourth = new ListNode(11);

        // // Connecting all sll together

        // sll.head.next = second;
        // second.next = third;
        // third.next = fourth;

        
        sll.insertLast(1);
        sll.insertLast(8);
        sll.insertLast(10);
        sll.insertLast(11);
        
        sll.display(sll.head);

        // if(sll.find(0)){
        //     System.out.println("Search key found!!!");
        // } else{
        //     System.out.println("Search key not found!!!");
        // }

        sll.deleteNode(8);

        sll.display(sll.head);

    }   
}
