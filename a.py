from math import sin, pi

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def producto_vectorial(self, otro_vector):
        resultado_x = self.y * otro_vector.x - self.x * otro_vector.y
        resultado_y = self.x * otro_vector.y - self.y * otro_vector.x
        return Vector2D(resultado_x, resultado_y)

# Crear dos vectores
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

# Calcular el producto vectorial
resultado = v1.producto_vectorial(v2)

# Imprimir el resultado
print(f"El producto vectorial v1 x v2 es: ({resultado.x}, {resultado.y})")