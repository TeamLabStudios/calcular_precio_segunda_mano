def calcular_precio_segunda_mano(precio_original, puntuacion_amazon, condicion_producto):
    """
    Calcula el precio de un producto de segunda mano basado en su puntuación de Amazon
    y la condición del producto.
    """
    # Verificar que los valores de entrada sean válidos
    if not (1 <= puntuacion_amazon <= 5):
        raise ValueError("La puntuación de Amazon debe estar entre 1 y 5 estrellas")
    
    if precio_original <= 0:
        raise ValueError("El precio original debe ser mayor que 0")
        
    # Factores de ajuste según la condición del producto
    factores_condicion = {
        'excelente': 0.8,  # 80% del valor calculado
        'bueno': 0.6,      # 60% del valor calculado
        'aceptable': 0.4   # 40% del valor calculado
    }
    
    if condicion_producto.lower() not in factores_condicion:
        raise ValueError("La condición debe ser 'excelente', 'bueno' o 'aceptable'")
    
    # Factor base según la puntuación de Amazon
    factor_puntuacion = puntuacion_amazon / 5
    
    # Calcular precio base según la puntuación
    precio_base = precio_original * factor_puntuacion
    
    # Ajustar según la condición del producto
    precio_final = precio_base * factores_condicion[condicion_producto.lower()]
    
    # Redondear a 2 decimales
    return round(precio_final, 2)

def main():
    print("Calculadora de Precios para Productos de Segunda Mano")
    print("-" * 50)
    
    while True:
        try:
            # Obtener precio original
            precio_original = float(input("\nIngrese el precio original del producto (€): "))
            
            # Obtener puntuación de Amazon
            puntuacion_amazon = float(input("Ingrese la puntuación de Amazon (1-5 estrellas): "))
            
            # Obtener condición del producto
            print("\nCondiciones disponibles:")
            print("- excelente")
            print("- bueno")
            print("- aceptable")
            condicion_producto = input("\nIngrese la condición del producto: ").lower()
            
            # Calcular el precio
            precio_calculado = calcular_precio_segunda_mano(
                precio_original, 
                puntuacion_amazon, 
                condicion_producto
            )
            
            # Mostrar resultado
            print("\nResultado del cálculo:")
            print("-" * 20)
            print(f"Precio original: {precio_original}€")
            print(f"Puntuación Amazon: {puntuacion_amazon} estrellas")
            print(f"Condición: {condicion_producto}")
            print(f"Precio calculado: {precio_calculado}€")
            
            # Preguntar si desea calcular otro precio
            continuar = input("\n¿Desea calcular otro precio? (s/n): ").lower()
            if continuar != 's':
                break
                
        except ValueError as e:
            print(f"\nError: {str(e)}")
            print("Por favor, intente nuevamente.")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {str(e)}")
            print("Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()