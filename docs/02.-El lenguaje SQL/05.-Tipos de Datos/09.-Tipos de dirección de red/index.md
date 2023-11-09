PostgreSQL ofrece tipos de datos para almacenar direcciones IPv4, IPv6 y MAC, como se muestra en el [cuadro 8.21.](https://www.postgresql.org/docs/current/datatype-net-types.html#DATATYPE-NET-TYPES-TABLE) Es mejor utilizar estos tipos en lugar de tipos de texto plano para  almacenar direcciones de red, porque estos tipos ofrecen verificación de errores de entrada y operadores y funciones especializadas (ver [Sección 9.](https://www.postgresql.org/docs/current/functions-net.html)12).

**Cuadro 8.21. Tipos de dirección de red**

| Nombre     | Tamaño de almacenamiento | Descripción                      |
| ---------- | ------------------------ | -------------------------------- |
| `cidr`     | 7 o 19 bytes             | Redes IPv4 e IPv6                |
| `inet`     | 7 o 19 bytes             | IPv4 e IPv6 hosts y redes        |
| `macaddr`  | 6 bytes                  | Direcciones MAC                  |
| `macaddr8` | 8 bytes                  | direcciones MAC (formate EUI-64) |

Al ordenar  `inet`o o  `cidr`Tipos de datos, las direcciones IPv4 siempre se ordenarán antes de las  direcciones IPv6, incluyendo direcciones IPv4 encapsuladas o mapeadas a  direcciones IPv6, como ::10.2.3.4 offff:10.4.3.2.