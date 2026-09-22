# Supermercado

## Objetivo

El objetivo del proyecto es desarrollar una simulación del funcionamiento y la gestión de recursos de un supermercado.

El programa deberá controlar los productos disponibles, sus precios y el stock existente tanto en el supermercado como en el almacén.

La simulación representará el ciclo de abastecimiento de un supermercado: los clientes compran productos, el supermercado repone su stock utilizando el almacén y, cuando el almacén necesita más productos, solicita nuevas unidades a la fábrica.

---

## Funcionamiento

El proyecto estará formado por cuatro elementos principales:

### Supermercado

Representa la tienda donde los clientes compran los productos.

Cada producto tendrá:

- Nombre.
- Precio.
- Stock disponible en el supermercado.

Cuando un cliente compre un producto, se descontarán las unidades correspondientes del stock del supermercado.

Si el stock de un producto se termina o baja de un determinado límite, el supermercado deberá solicitar nuevas unidades al almacén.

---

### Compras de clientes

Las compras de los clientes se generarán de manera aleatoria.

El programa seleccionará distintos productos y cantidades de forma random para simular las compras realizadas por los clientes.

De esta manera, el stock de los productos irá disminuyendo de forma diferente en cada ejecución y no siempre se agotarán los mismos productos.

Cada compra deberá:

- Seleccionar uno o varios productos.
- Comprobar que existe suficiente stock en el supermercado.
- Calcular el coste de la compra.
- Descontar los productos comprados del stock del supermercado.

---

### Almacén

El almacén será el encargado de reponer los productos del supermercado.

Cada producto tendrá también un determinado stock dentro del almacén.

Cuando el supermercado necesite reponer un producto:

1. Se comprobará si el producto existe en el almacén.
2. Se comprobará si hay suficiente stock.
3. Se enviarán las unidades necesarias al supermercado.
4. Se descontarán esas unidades del stock del almacén.

Con el paso del tiempo, el stock del almacén también irá disminuyendo.

Cuando un producto del almacén se termine o esté próximo a agotarse, será necesario solicitar nuevas unidades a la fábrica.

---

### Fábrica

La fábrica representa una empresa externa encargada de suministrar productos al almacén.

Para simplificar la simulación, se considerará que la fábrica dispone de stock infinito.

Cuando el almacén tenga pocas unidades de un producto, realizará un pedido a la fábrica.

La fábrica enviará las unidades necesarias y se actualizará el stock del almacén.

---

## Ciclo de funcionamiento

El funcionamiento general de la simulación será:

**Cliente compra productos → disminuye el stock del supermercado**

**Supermercado necesita productos → solicita productos al almacén**

**Almacén entrega productos → disminuye el stock del almacén**

**Almacén necesita productos → solicita productos a la fábrica**

**Fábrica repone el almacén**

A partir de ese momento el ciclo vuelve a comenzar.

El objetivo final es que todo este proceso funcione automáticamente mientras se realizan compras aleatorias y se actualizan los diferentes stocks.
