class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class BrowserHistory:
    def __init__(self,homepage_url):
        self.current_page=Node(homepage_url)
    
    def visit(self,url):
        new_page=Node(url)

        #Link backward
        new_page.prev=self.current_page

        #Clear forward history
        self.current_page.next=None

        #Link new page and move to it
        self.current_page.next=new_page
        self.current_page=new_page

    def back(self):
        if self.current_page.prev:
            self.current_page=self.current_page.prev
        return self.current_page.data
    
    def forward(self):
        if self.current_page.next:
            self.current_page=self.current_page.next
        return self.current_page.data
    
    def full_history(self):
        node=self.current_page
        while node.prev:
            node=node.prev
        
        result=[]

        while node:
            result.append(node.data)
            node=node.next
        return result
    
    def current(self):
        return self.current_page.data

if __name__ == "__main__":
    bh=BrowserHistory("home.com")
    print("Start:",bh.current())

    print("\nVisit a.com")
    bh.visit("a.com")

    print("Current:",bh.current())
    print("History:",bh.full_history())

    print("\nvisit b.com")
    bh.visit("b.com")
    print("Current:",bh.current())
    print("History:",bh.full_history())

    print("\nBack")
    print("Page:",bh.back())

    print("\n Forward")
    print("Page:",bh.forward())

    print("\nVisit c.com (wipes forward history)")
    bh.visit("c.com")
    print("Current:",bh.current())
    print("History:",bh.full_history())

    print("\nForward (should not move)")
    print("Page:",bh.forward() )



