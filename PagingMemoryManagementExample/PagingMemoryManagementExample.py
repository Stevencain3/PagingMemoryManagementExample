
class paging_system:
    
    def __init__ (self, desk_size, cart_size ):
        self.desk = [] # the desk is what would be in your ram
        self.cart = [] # the cart is what would be in your Vram 
        self.library = ["Dinosour Dogs", " The Early History of Dogs", "Dogs in Mythology",
                            "Ancient Civilizations with Dogs", "Famous Dogs in Pop Culture", "Dog Breeds And Traits",
                            "Role of Dogs in Companionship"] #library would be everything in your HHD 

        self.cart_size = cart_size # cart size is how big your Vram is 
        self.desk_size = 3 # Desk size is how big your RAM is 
            
