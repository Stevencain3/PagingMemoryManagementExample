
class paging_system:
    
    def __init__ (self, desk_size, cart_size ):
        self.desk = [] # the desk is what would be in your ram
        self.cart = [] # the cart is what would be in your Vram 
        self.library = ["Dinosour Dogs", " The Early History of Dogs", "Dogs in Mythology",
                            "Ancient Civilizations with Dogs", "Famous Dogs in Pop Culture", "Dog Breeds And Traits",
                            "Role of Dogs in Companionship"] #library would be everything in your HDD 

        self.cart_size = cart_size # cart size is how big your Vram is 
        self.desk_size = 3 # Desk size is how big your RAM is 
            
        #this would be like doing a paging request 
    def request_book(self, book):
        if book in desk:
           print ("{book} is on the desk(RAM) already!")
        elif book in cart:
            print ("moving {book} from the cart(VRAM) to the desk(RAM)")
            self.move_to_desk(book)
        elif book in library:
            print("{book} is on the libray shelves(HDD) im fetiching it now.")
            self.get_from_shelves(book)
        else: 
            print("{book} is not offered here in the library")

#getting a book from the sheves 
    def get_from_shelves(self, book):
        self.library.remove(book)
        self.move_to_desk(book)
        print("{book} is now on the desk!")

    def move_to_desk(self, book):
        if len(self.desk) >= self.desk_size:
            removed = self.desk.pop(0)
            print ("desk(RAM) is full. Moving {removed} to the cart (VRAM).")
            if len(self.cart) >= self.cart_size:
                removed_cart = self.cart.pop
                self.desk.append(removed)
                print("library cart(VRAM) is full. Moving {removed_cart} to the library shelves")
                self.library.append(removed_cart)
