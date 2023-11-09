El planificador clasifica las operaciones involucradas en una consulta como *segura paralela*, *restringida o* *insegura paralela*. Una operación segura paralela es aquella que no entra en conflicto con  el uso de consultas paralelas. Una operación restringida paralela es  aquella que no se puede realizar en un trabajador paralelo, pero que se  puede realizar en el líder mientras se utiliza la consulta paralela. Por lo tanto, las operaciones restringidas paralelas nunca pueden ocurrir  por debajo de un  `Gather`o o  `Gather Merge`nodo, pero puede ocurrir en otra parte de un plan que contiene tal nodo. Una  operación paralela insegura es una operación insegura que no se puede  realizar mientras se utiliza la consulta paralela, ni siquiera en el  líder. Cuando una consulta contiene algo que sea paralelo inseguro, la  consulta paralela está completamente deshabilitada para esa consulta.

Las siguientes operaciones siempre están restringidas en paralelo:

- Escáneres de expresiones comunes de tabla (ETC).
- Escáneres de mesas temporales.
- Escanes de tablas extranjeras, a menos que el envoltorio de datos extraños tenga un  `IsForeignScanParallelSafe`API que indica lo contrario.
- Nodos de plan a lo que se hace un  `InitPlan`está unido.
- Plane los nodos que hacen referencia a un correlato `SubPlan`.