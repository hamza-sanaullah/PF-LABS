class Chair():
    a =" color"
    b = "Height"
    c = "material"
    @staticmethod
    def get_info():
        obj = Chair()
        obj.a = "red"
        obj.b = 20
        obj.c = "wood"
        print(f"The  color of the chair is {obj.a} and the height is {obj.b} and the material is {obj.c}")
chair = Chair().get_info()