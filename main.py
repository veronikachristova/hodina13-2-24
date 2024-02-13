#abstraktna trieda
# from abc import ABC, abstractmethod
#
# class Zviera(ABC):
#     @abstractmethod
#     def Zvuk(self):
#         pass
#
# class Pes(Zviera):
#     def Zvuk(self):
#         return "Haf"
#
# class Macka(Zviera):
#     def Zvuk(self):
#         return "Mnau"
#
# moj_pes = Pes()
# moja_macka = Macka()
#
# print(moj_pes.Zvuk())
# print(moja_macka.Zvuk())



class Shoe
    def __init__(self, id, gender, type, color, price, brand, size):
        self.id = id
        self.gender = gender
        self.type = type
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size

    def __str__(self):
        return f"Shoe:{self.id},{self.brand}, {self.type}, ({self.gender}), Color: {self.color}, Size: {self.size}, Price: {self.price}eur"


class ShoeModel:
    def __init__(self):
        self.shoes =[]

    def add(self,shoe):
        self.shoes.append(shoe)

    def delete(self, id):
        for index, shoe in enumerate(self.shoes):
            if shoe.id == id:
                del self.shoes[index]
                return True
        return False

class ShoeViewer:
    def display(self, shoes):
        print("Shoe Inventory:")
        for shoe in shoes:
            print(shoe)


class ShoeController:
    def __init__(self, model, viewer):
        self.model = model
        self.viewer = viewer

    def add(self, id, gender, type, color, price, brand, size):
        shoe = Shoe(id, gender, type, color, price, brand, size)
        self.model.add(shoe)

    def delete(self, id):
        return self.model.delete(id)

    def viewAll

    def ViewBySize

    def ViewByPrice


if __name__ == "__main__":
    # Create model, view, and controller instances
    shoe_model = ShoeModel()
    shoe_viewer = ShoeViewer()
    shoe_controller = ShoeController(shoe_model, shoe_viewer)

    # Add some shoes
    shoe_controller.add_shoe(1, "Men", "Sneakers", "Black", 50, "Nike", 10)
    shoe_controller.add_shoe(2, "Women", "Sandals", "Brown", 30, "Adidas", 8)
    shoe_controller.add_shoe(3, "Women", "Boots", "Red", 80, "Timberland", 9)

    # Display all shoes
    shoe_viewer.display_shoes(shoe_model.shoes)

    # Delete a shoe by ID
    shoe_id_to_delete = 2
    if shoe_controller.delete_shoe_by_id(shoe_id_to_delete):
        print(f"Shoe with ID {shoe_id_to_delete} deleted successfully")
    else:
        print(f"No shoe found with ID {shoe_id_to_delete}")

    # Display updated shoe inventory
    shoe_viewer.display_shoes(shoe_model.shoes)

