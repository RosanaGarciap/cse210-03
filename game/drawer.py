class Drawer():

    def __init__(self):
        self.estado = 1
    
    def draw(self):
        if(self.estado == 1):
            print("  ___\n /___\\ \n \\   /\n  \\ /\n   0 \n  /|\\ \n  / \\")

        elif(self.estado == 2):
            print(" \n /___\\ \n \\   /\n  \\ /\n   0 \n  /|\\ \n  / \\")

        elif(self.estado == 3):
            print(" \n \\   /\n  \\ /\n   0 \n  /|\\ \n  / \\")

        elif(self.estado == 4):
            print("\n  \\ /\n   0 \n  /|\\ \n  / \\")
        
        else:
            print("\n   x \n  /|\\ \n  / \\")
        print("^^^^^^^")