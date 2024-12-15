public class CircularSinglyLinkedList {
  
  private ListNode Last;
  private int length;

  private class ListNode {
    private ListNode next;
    private int data;

    public ListNode(int data){
      this.data = data;

    }
  }

  public CurcularSinglyLinkedList() {
    last = null;
  }
}
