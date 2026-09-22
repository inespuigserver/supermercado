# Supermercado

## Objetivo

El objetivo del proyecto es desarrollar una simulación de la gestión de recursos de un supermercado.

El programa deberá controlar los productos disponibles, su stock y su precio, simulando la relación entre el supermercado, el almacén, los pedidos y la fábrica.

El sistema deberá tener en cuenta las dependencias entre estas partes. Por ejemplo, un pedido no podrá completarse si no existe suficiente stock en el almacén y, si el almacén se queda sin unidades de un producto, deberá solicitar nuevas unidades a la fábrica.

## Funcionamiento

El proyecto se divide en cuatro partes principales:

### Supermercado

Representa la tienda en la que se venden los productos.

Deberá:

- Contener los productos disponibles.
- Guardar el precio de cada producto.
- Controlar el stock disponible en la tienda.
- Actualizar el stock cuando se realice una compra.

### Almacén

Representa el stock utilizado para abastecer al supermercado.

Deberá:

- Guardar las unidades disponibles de cada producto.
- Comprobar si existe suficiente stock.
- Abastecer al supermercado cuando sea necesario.
- Detectar cuándo un producto está próximo a agotarse.
- Solicitar productos a la fábrica cuando sea necesario.

### Pedido

Representa una solicitud de productos.

Al realizar un pedido se deberá:

- Comprobar que el producto existe.
- Comprobar que existe suficiente stock.
- Calcular el coste del pedido.
- Descontar las unidades correspondientes del stock.
- Informar si el pedido no puede realizarse.

### Fábrica

Representa una empresa externa que suministra productos al almacén.

Para simplificar la simulación, se considera que la fábrica dispone de stock infinito.

Cuando el almacén tenga pocas unidades de un producto, podrá realizar un pedido a la fábrica para reponer su stock.

## Objetivo final

Conectar todos los elementos anteriores para simular el funcionamiento completo del sistema:

**Fábrica → Almacén → Supermercado → Pedido**

De esta forma, el programa deberá gestionar correctamente los productos, el stock, los precios, los pedidos y la reposición de mercancía teniendo en cuenta las dependencias entre cada parte del sistema.
