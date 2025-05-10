from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self._item_id = item_id           
        self._title = title               
        self._available = True            

    @abstractmethod
    def display_info(self):
        pass

    @property
    def title(self):                     
        return self._title

    @property
    def item_id(self):
        return self._item_id

    def is_available(self):
        return self._available

    def set_availability(self, status):
        self._available = status

class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.__author = author            

    def display_info(self):
        status = "Available" if self._available else "Not Available"
        print(f"[Book] ID: {self._item_id}, Title: {self._title}, Author: {self.__author}, Status: {status}")

class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self.__issue_number = issue_number  

    def display_info(self):
        status = "Available" if self._available else "Not Available"
        print(f"[Magazine] ID: {self._item_id}, Title: {self._title}, Issue: {self.__issue_number}, Status: {status}")

class Library:
    def __init__(self):
        self.__items = []                 

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.__items.append(item)
            print("Item added successfully.")
        else:
            print("Invalid item.")

    def display_items(self):
        if not self.__items:
            print("No items in the library.")
        for item in self.__items:
            item.display_info()

    def search_by_title(self, title):
        results = [item for item in self.__items if title.lower() in item.title.lower()]
        if results:
            print(f"Results for title '{title}':")
            for item in results:
                item.display_info()
        else:
            print(f"No items found with title '{title}'.")

    def search_by_id(self, item_id):
        for item in self.__items:
            if item.item_id == item_id:
                print("Item found:")
                item.display_info()
                return
        print(f"No item found with ID {item_id}.")

if __name__ == "__main__":
    lib = Library()

    b1 = Book("B001", "Python Basics", "John Doe")
    m1 = Magazine("M001", "Tech Monthly", "2025-05")

    lib.add_item(b1)
    lib.add_item(m1)

    print("\n== All Library Items ==")
    lib.display_items()

    print("\n== Search by Title ==")
    lib.search_by_title("python")

    print("\n== Search by ID ==")
    lib.search_by_id("M001")
