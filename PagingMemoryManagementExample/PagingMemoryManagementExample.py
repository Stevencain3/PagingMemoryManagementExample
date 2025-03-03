class paging_system:
    
    def __init__ (self, cart_size ):
        self.desk = [] # the desk is what would be in your ram
        self.cart = [] # the cart is what would be in your Vram 
        self.library = ["Dinosour Dogs", "The Early History of Dogs", "Dogs in Mythology",
                            "Ancient Civilizations with Dogs", "Famous Dogs in Pop Culture", "Dog Breeds And Traits",
                            "Role of Dogs in Companionship"] #library would be everything in your HDD 

        self.cart_size = cart_size # cart size is how big your Vram is 
        self.desk_size = 3 # Desk size is how big your RAM is 
            
        #this would be like doing a paging request 
    def request_book(self, book):
        if book in self.desk:
           print (f"{book} is on the desk(RAM) already!")
        elif book in self.cart:
            print (f"moving {book} from the cart(VRAM) to the desk(RAM)")
            self.move_to_desk(book)
        elif book in self.library:
            print(f"{book} is on the libray shelves(HDD) im fetiching it now.")
            self.get_from_shelves(book)
        else: 
            print(f"{book} is not offered here in the library")

#getting a book from the sheves 
    def get_from_shelves(self, book):
        self.library.remove(book)
        self.move_to_desk(book)
        print(f"{book} is now on the desk!")

    def move_to_desk(self, book):
        if len(self.desk) >= self.desk_size:
            removed = self.desk.pop(0)
            print (f"desk(RAM) is full. Moving {removed} to the cart (VRAM).")
            self.cart.append(removed)
            if len(self.cart) > self.cart_size:
                removed_cart = self.cart.pop(0)
                print(f"library cart(VRAM) is full. Moving {removed_cart} to the library shelves")
                self.library.append(removed_cart)
        self.desk.append(book)





class user_interface:
    def main_menu():
        paging = paging_system( cart_size=2)  # Initialize the paging system
        
        while True:  # Loop to keep showing the menu
            print("\nWelcome to the Library Paging Example!")
            print("--------------------------------------")
            print("What would you like to do?")
            print("1.) Get the cart and desk ready for your research")
            print("2.) Request a book for your desk")
            print("3.) View current books on desk and cart")
            print("4.) Return a book to the library shelves")
            print("5.) View all available books in the library")
            print("6.) Exit")
            
            choice = input("\nEnter your choice (1-6): ")

            if choice == "1":
                print("\nInitializing your research space...")
                paging.request_book("Dinosour Dogs")
                paging.request_book("The Early History of Dogs") 
                paging.request_book("Dogs in Mythology") #fills the desk with 3 books 
                paging.request_book("Ancient Civilizations with Dogs")
                paging.request_book("Famous Dogs in Pop Culture")# overfills the desk to put 2 books into the cart
                print("Your desk (RAM) and cart (VRAM) are now filled!\n")

            elif choice == "2":
                book_name = input("Enter the book name: ")
                paging.request_book(book_name)  # Call the request_book method

            elif choice == "3":
                print("\nCurrent Desk (RAM):", paging.desk)
                print("Current Cart (VRAM):", paging.cart)

            elif choice == "4":
                book_name = input("Enter the book you want to return: ")
                if book_name in paging.desk:
                    paging.desk.remove(book_name)
                    paging.library.append(book_name)
                    print(f"{book_name} has been returned to the library shelves.")
                elif book_name in paging.cart:
                    paging.cart.remove(book_name)
                    paging.library.append(book_name)
                    print(f"{book_name} has been returned to the library shelves.")
                else:
                    print(f"{book_name} is not currently in your desk or cart.")

            elif choice == "5":
                print("\nAvailable Books in the Library:")
                for book in paging.library:
                    print(f"- {book}")

            elif choice == "6":
                print("\nExiting the Library Paging Example. Goodbye!")
                break  # Exit the loop

            else:
                print("\nInvalid choice. Please enter a number between 1-6.")

# Run the menu
user_interface.main_menu()



