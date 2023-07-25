"""datos = [5, 6, 'A', 'Pablo', True]
print(datos)"""

productos = ['notebooks', 'lentes', 'iphones', 'parlantes']

productos[0] = 'laptops'
new_productos = productos.copy()
new_productos[0] = 'PC'
productos.append('celular')
productos.insert(1,'iPad')
new_productos.extend(productos)

print(productos)
print(len(productos), ' y ', len(new_productos))
print(new_productos)