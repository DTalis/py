import math

class Pagination:
    """
    A class to simulate a basic pagination system.
    It breaks a list of items into smaller, manageable pages.
    """
    def __init__(self, items=None, page_size=10):
        """
        Initializes the Pagination object.

        Args:
            items (list, optional): The list of items to paginate. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.
        """
        # If no items are provided, initialize with an empty list.
        if items is None:
            self.items = []
        else:
            self.items = items
        
        # Store the page size.
        self.page_size = page_size
        
        # The internal page index (0-based).
        self.current_idx = 0
        
        # Calculate the total number of pages.
        # Handle the case where page_size is 0 to avoid ZeroDivisionError.
        if self.page_size <= 0:
            self.total_pages = 1 if self.items else 0
        else:
            self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        """
        Returns the list of items visible on the current page.

        Returns:
            list: A slice of the items list for the current page.
        """
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        """
        Navigates to a specified page number (1-based index).

        Args:
            page_num (int): The page number to go to.
        
        Raises:
            ValueError: If the page number is out of range.
        """
        # Type cast the input to an integer to be safe.
        try:
            page_num = int(page_num)
        except (ValueError, TypeError):
            raise ValueError("Page number must be an integer.")

        # Check if the requested page number is valid.
        if not 1 <= page_num <= self.total_pages:
            raise ValueError(f"Page number {page_num} is out of range. Must be between 1 and {self.total_pages}.")
        
        # Update the internal index to the requested page.
        self.current_idx = page_num - 1

    def first_page(self):
        """
        Navigates to the first page (index 0).
        Returns self for method chaining.
        """
        self.current_idx = 0
        return self

    def last_page(self):
        """
        Navigates to the last page.
        Returns self for method chaining.
        """
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        """
        Moves to the next page if not already on the last page.
        Returns self for method chaining.
        """
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """
        Moves to the previous page if not already on the first page.
        Returns self for method chaining.
        """
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        """
        Returns a string representation of the visible items on the current page.
        """
        visible_items = self.get_visible_items()
        return "\n".join(str(item) for item in visible_items)

# --- Test Cases ---

# Create a list of all lowercase letters.
alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
# Create a Pagination object with the list and a page size of 4.
p = Pagination(alphabet_list, 4)

# Test case 1: Get visible items on the first page.
print("Test 1: Initial visible items")
print(p.get_visible_items())
print("-" * 20)

# Test case 2: Move to the next page and get visible items.
p.next_page()
print("Test 2: After calling next_page()")
print(p.get_visible_items())
print("-" * 20)

# Test case 3: Move to the last page and get visible items.
p.last_page()
print("Test 3: After calling last_page()")
print(p.get_visible_items())
print("-" * 20)

# Test case 4: Go to a specific page number and check the index.
# The internal index (current_idx) should be 6, which corresponds to page 7.
p.go_to_page(7)
print("Test 4: After calling go_to_page(7)")
print(f"Current page index (0-based): {p.current_idx}")
print(f"Items on page 7: {p.get_visible_items()}")
print("-" * 20)

# Test case 5: Try to go to an invalid page number (0).
print("Test 5: Trying to go to an invalid page (0)")
try:
    p.go_to_page(0)
except ValueError as e:
    print(f"Caught expected error: {e}")
print("-" * 20)

# Test case 6: Demonstrate the __str__ method.
print("Test 6: Using the __str__ method")
# Go back to the first page for this test.
p.first_page()
print(str(p))
