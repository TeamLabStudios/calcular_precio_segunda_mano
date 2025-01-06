# Calculadora de Precios para Productos de Segunda Mano

Esta herramienta te ayuda a calcular precios justos para productos de segunda mano basándose en tres factores principales:
- Precio original del producto
- Puntuación del producto en Amazon
- Estado/condición del producto

## Características

- Interfaz interactiva por consola
- Cálculo basado en múltiples factores
- Manejo de errores robusto
- Resultados detallados
- Opción para calcular múltiples productos en una sesión

## Requisitos

- Python 3.x instalado en tu sistema

## Instalación

1. Descarga el archivo `calculadora_precios.py`
2. No se requieren dependencias adicionales

## Uso

1. Abre una terminal o línea de comandos
2. Navega hasta el directorio donde guardaste el script
3. Ejecuta el script:
```bash
python calculadora_precios.py
```

4. Sigue las instrucciones en pantalla:
   - Ingresa el precio original del producto en euros
   - Ingresa la puntuación de Amazon (1-5 estrellas)
   - Selecciona la condición del producto (excelente, bueno, aceptable)

## Fórmula de Cálculo

El precio final se calcula siguiendo estos pasos:
1. Se normaliza la puntuación de Amazon (valor entre 0 y 1)
2. Se aplica al precio original
3. Se ajusta según la condición del producto:
   - Excelente: 80% del valor calculado
   - Bueno: 60% del valor calculado
   - Aceptable: 40% del valor calculado

## Ejemplo de Uso

```
Calculadora de Precios para Productos de Segunda Mano
--------------------------------------------------

Ingrese el precio original del producto (€): 100
Ingrese la puntuación de Amazon (1-5 estrellas): 4.5

Condiciones disponibles:
- excelente
- bueno
- aceptable

Ingrese la condición del producto: excelente

Resultado del cálculo:
--------------------
Precio original: 100€
Puntuación Amazon: 4.5 estrellas
Condición: excelente
Precio calculado: 72.0€

¿Desea calcular otro precio? (s/n): 
```

## Manejo de Errores

El script incluye validaciones para:
- Precios negativos o cero
- Puntuaciones fuera del rango 1-5
- Condiciones de producto no válidas
- Entradas no numéricas

## Personalización

Puedes modificar los factores de condición en el código fuente:
```python
factores_condicion = {
    'excelente': 0.8,  # 80% del valor calculado
    'bueno': 0.6,      # 60% del valor calculado
    'aceptable': 0.4   # 40% del valor calculado
}
```

## Contribuciones

Si deseas mejorar esta herramienta, puedes:
1. Agregar nuevas condiciones de producto
2. Implementar factores adicionales (antigüedad, demanda, etc.)
3. Crear una interfaz gráfica
4. Agregar capacidad de guardar historial de cálculos

## Licencia

Este proyecto es software libre y puede ser utilizado, modificado y distribuido libremente.

## Soporte

Si encuentras algún problema o tienes sugerencias, por favor crea un issue en el repositorio.
