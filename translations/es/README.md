<p>
  <a href="https://blog.bytebytego.com/?utm_source=site"><img src="../../images/banner.jpg" /> </a>
</p>

<p align="center">
  【
  <a href="https://www.youtube.com/channel/UCZgt6AzoyjslHTC9dz0UoTw">
    👨🏻‍💻 YouTube
  </a> | 
  <a href="https://blog.bytebytego.com/?utm_source=site">
    📮 Newsletter
  </a> 】
</p>

# Diseño de Sistemas 101

Explica sistemas complejos usando imágenes y términos simples.

Ya sea que te estés preparando para una Entrevista de Diseño de Sistemas o simplemente quieras entender cómo funcionan los sistemas bajo la superficie, esperamos que este repositorio te ayude a lograrlo.

## Protocolos de Comunicación

Los estilos de arquitectura definen cómo interactúan entre sí los diferentes componentes de una interfaz de programación de aplicaciones (API). Como resultado, garantizan eficiencia, confiabilidad y facilidad de integración con otros sistemas al proporcionar un enfoque estándar para diseñar y construir APIs. Aquí se presentan los estilos más utilizados:
<p>
  <img src="../../images/api-architecture-styles.png" style="width: 640px">
</p>

- SOAP:

  Maduro, completo, basado en XML

  Ideal para aplicaciones empresariales

- RESTful:

  Popular, fácil de implementar, métodos HTTP

  Ideal para servicios web

- GraphQL:

  Lenguaje de consulta, solicita datos específicos

  Reduce la sobrecarga de red, respuestas más rápidas

- gRPC:

  Moderno, alto rendimiento, Protocol Buffers

  Adecuado para arquitecturas de microservicios

- WebSocket:

  En tiempo real, conexiones bidireccionales y persistentes

  Perfecto para el intercambio de datos de baja latencia
 
- Webhook:

  Basado en eventos, llamadas HTTP asíncronas

  Notifica a los sistemas cuando ocurren eventos

### REST API vs. GraphQL

Cuando se trata del diseño de API, REST y GraphQL tienen cada uno sus propias fortalezas y debilidades.

El diagrama a continuación muestra una rápida comparación entre REST y GraphQL.

<p>
  <img src="../../images/graphQL.jpg">
</p>

REST

- Utiliza métodos HTTP estándar como GET, POST, PUT y DELETE para operaciones CRUD.
- Funciona bien cuando se necesitan interfaces simples y uniformes entre servicios/aplicaciones separados. 
- Las estrategias de almacenamiento en caché son fáciles de implementar. 
- La desventaja es que puede requerir múltiples solicitudes para ensamblar datos relacionados de puntos finales separados.

GraphQL

- Proporciona un único punto final para que los clientes consulten exactamente los datos que necesitan. 
- Los clientes especifican los campos exactos requeridos en las consultas anidadas, y el servidor devuelve paquetes optimizados que contienen solo esos campos. 
- Admite Mutaciones para modificar datos y Subscripciones para notificaciones en tiempo real. 
- Excelente para la agregación de datos de múltiples fuentes y funciona bien con requisitos de frontend en constante evolución. 
- Sin embargo, traslada la complejidad al lado del cliente y puede permitir consultas abusivas si no se protegen adecuadamente. 
- Las estrategias de almacenamiento en caché pueden ser más complicadas que en REST.

La mejor elección entre REST y GraphQL depende de los requisitos específicos de la aplicación y del equipo de desarrollo. GraphQL es una buena opción para necesidades de frontend complejas o que cambian con frecuencia, mientras que REST es adecuado para aplicaciones en las que se prefieren contratos simples y consistentes.

Ningún enfoque de API es una solución universal. Evaluar cuidadosamente los requisitos y las compensaciones es importante para elegir el estilo correcto. Tanto REST como GraphQL son opciones válidas para exponer datos y alimentar aplicaciones modernas.

### ¿Cómo funciona gRPC?

RPC (Llamada a Procedimiento Remoto) se llama "remoto" porque permite la comunicación entre servicios remotos cuando los servicios se despliegan en servidores diferentes bajo una arquitectura de microservicios. Desde el punto de vista del usuario, actúa como una llamada a función local.

El diagrama a continuación ilustra el flujo de datos general de gRPC.

<p>
  <img src="../../images/grpc.jpg">
</p>

Paso 1: El cliente realiza una llamada REST. El cuerpo de la solicitud suele estar en formato JSON.

Pasos 2-4: El servicio de pedidos (cliente gRPC) recibe la llamada REST, la transforma y realiza una llamada RPC al servicio de pagos. gRPC codifica el "stub del cliente" en un formato binario y lo envía a la capa de transporte de nivel inferior.

Paso 5: gRPC envía los paquetes a través de la red mediante HTTP2. Debido a la codificación binaria y las optimizaciones de red, se dice que gRPC es 5 veces más rápido que JSON.

Pasos 6-8: El servicio de pagos (servidor gRPC) recibe los paquetes de la red, los descodifica y llama a la aplicación del servidor.

Pasos 9-11: Se devuelve el resultado desde la aplicación del servidor, se codifica y se envía a la capa de transporte.

Pasos 12-14: El servicio de pedidos recibe los paquetes, los descodifica y envía el resultado a la aplicación del cliente.

### ¿Qué es un webhook?

El diagrama a continuación muestra una comparación entre el polling y el webhook.

<p>
  <img src="../../images/webhook.jpeg" style="width: 680px" />
</p>

Supongamos que gestionamos un sitio web de comercio electrónico. Los clientes envían pedidos al servicio de pedidos a través de la puerta de enlace API, que se comunica con el servicio de pagos para las transacciones de pago. Luego, el servicio de pagos se comunica con un proveedor de servicios de pago externo (PSP) para completar las transacciones.

Existen dos formas de manejar las comunicaciones con el PSP externo.

1. Polling corto

Después de enviar la solicitud de pago al PSP, el servicio de pagos sigue preguntando al PSP sobre el estado del pago. Después de varias rondas, el PSP finalmente devuelve el estado.

El polling corto tiene dos desventajas:
* El constante polling del estado requiere recursos del servicio de pagos. 
* El servicio externo se comunica directamente con el servicio de pagos, creando vulnerabilidades de seguridad.

2. Webhook

Podemos registrar un webhook con el servicio externo. Significa que el servicio externo nos llamará a una URL específica cuando tenga actualizaciones sobre la solicitud. Cuando el PSP haya completado el procesamiento, invocará la solicitud HTTP para actualizar el estado del pago.

De esta manera, el paradigma de programación cambia, y el servicio de pagos ya no necesita desperdiciar recursos en el polling del estado.

¿Qué sucede si el PSP nunca llama de vuelta? Podemos configurar una tarea de mantenimiento para verificar el estado del pago cada hora.

Los webhooks a menudo se denominan API inversas o API de empuje porque el servidor envía solicitudes HTTP al cliente. Deben prestarse atención a tres cosas al usar un webhook:

1. Necesitamos diseñar una API adecuada para que el servicio externo la llame. 
2. Debemos configurar reglas adecuadas en la puerta de enlace API por razones de seguridad. 
3. Debemos registrar la URL correcta en el servicio externo.

### ¿Cómo mejorar el rendimiento de una API?

El diagrama a continuación muestra 5 trucos comunes para mejorar el rendimiento de una API.

<p>
  <img src="../../images/api-performance.jpg">
</p>

Paginación

Esta es una optimización común cuando el tamaño del resultado es grande. Los resultados se transmiten de forma continua al cliente para mejorar la capacidad de respuesta del servicio.

Registro Asíncrono

El registro síncrono implica la escritura en disco en cada llamada y puede ralentizar el sistema. El registro asíncrono envía registros a un búfer sin bloqueo primero y los devuelve de inmediato. Los registros se escriben en disco periódicamente. Esto reduce significativamente la sobrecarga de E/S.

Caché

Podemos almacenar en caché los datos de acceso frecuente en una caché. El cliente puede consultar la caché primero en lugar de acceder directamente a la base de datos. Cachés como Redis almacenan datos en memoria, por lo que el acceso a los datos es mucho más rápido que acceder a la base de datos.

Compresión de Carga Útil

Las solicitudes y respuestas se pueden comprimir con gzip, u otras técnicas, para que el tamaño de los datos transmitidos sea mucho más

Pool de Conexiones

Cuando accedemos a recursos, a menudo necesitamos cargar datos desde la base de datos. Abrir y cerrar conexiones a la base de datos añade una sobrecarga significativa. Por lo tanto, debemos conectarnos a la base de datos a través de un conjunto de conexiones abiertas. El pool de conexiones se encarga de gestionar el ciclo de vida de las conexiones.

### HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)

¿Qué problema resuelve cada generación de HTTP?

El diagrama a continuación ilustra las características clave.

<p>
  <img src="../../images/http3.jpg" />
</p>

- HTTP 1.0 se finalizó y documentó por completo en 1996. Cada solicitud al mismo servidor requiere una conexión TCP por separado.

- HTTP 1.1 se publicó en 1997. Se puede dejar abierta una conexión TCP para su reutilización (conexión persistente), pero no resuelve el problema del bloqueo HOL (head-of-line).

    Bloqueo HOL: cuando se agota el número de solicitudes paralelas permitidas en el navegador, las solicitudes posteriores deben esperar a que se completen las anteriores.

- HTTP 2.0 se publicó en 2015. Aborda el problema HOL mediante la multiplexación de solicitudes, lo que elimina el bloqueo HOL en la capa de aplicación, pero el bloqueo HOL todavía existe en la capa de transporte (TCP).

    Como se puede ver en el diagrama, HTTP 2.0 introdujo el concepto de "flujos" HTTP: una abstracción que permite la multiplexación de diferentes intercambios HTTP en la misma conexión TCP. Cada flujo no necesita ser enviado en orden.

- HTTP 3.0 se publicó en borrador por primera vez en 2020. Es el sucesor propuesto de HTTP 2.0. Utiliza QUIC en lugar de TCP como protocolo de transporte subyacente, eliminando así el bloqueo HOL en la capa de transporte.

QUIC se basa en UDP. Introduce flujos como ciudadanos de primera clase en la capa de transporte. Los flujos QUIC comparten la misma conexión QUIC, por lo que no se requieren apretones de manos adicionales y comienzos lentos para crear nuevos flujos, pero los flujos QUIC se entregan de forma independiente de modo que, en la mayoría de los casos, la pérdida de paquetes que afecta a un flujo no afecta a otros.

### SOAP vs REST vs GraphQL vs RPC

El diagrama a continuación ilustra la línea de tiempo de las API y la comparación de estilos de API.

Con el tiempo, se han lanzado diferentes estilos arquitectónicos de API. Cada uno de ellos tiene sus propios patrones para estandarizar el intercambio de datos.

Puedes consultar los casos de uso de cada estilo en el diagrama.

<p>
  <img src="../../images/SOAP vs REST vs GraphQL vs RPC.jpeg" />
</p>

### Code First vs. API First

El diagrama a continuación muestra las diferencias entre el desarrollo orientado al código (Code First) y el desarrollo orientado a la API (API First). ¿Por qué queremos considerar un diseño API First?

<p>
  <img src="../../images/api_first.jpg" style="width: 680px" />
</p>

- Los microservicios aumentan la complejidad del sistema y tenemos servicios separados para servir diferentes funciones del sistema. Si bien este tipo de arquitectura facilita el desacoplamiento y la segregación de funciones, necesitamos manejar las diversas comunicaciones entre los servicios.

    Es mejor pensar en la complejidad del sistema antes de escribir el código y definir cuidadosamente los límites de los servicios.

- Los equipos funcionales separados deben hablar el mismo idioma y los equipos funcionales dedicados son responsables solo de sus propios componentes y servicios. Se recomienda que la organización hable el mismo idioma a través del diseño de la API.

    Podemos simular solicitudes y respuestas para validar el diseño de la API antes de escribir el código.

- Mejora de la calidad del software y la productividad de los desarrolladores. Dado que hemos resuelto la mayoría de las incertidumbres al comienzo del proyecto, el proceso de desarrollo en general es más fluido y la calidad del software mejora considerablemente.

    Los desarrolladores también están satisfechos con el proceso porque pueden centrarse en el desarrollo funcional en lugar de negociar cambios repentinos.

    La posibilidad de tener sorpresas hacia el final del ciclo de vida del proyecto se reduce.

    Debido a que hemos diseñado la API primero, las pruebas se pueden diseñar mientras se desarrolla el código. En cierto sentido, también tenemos un enfoque de Desarrollo Guiado por Pruebas (TDD) al utilizar el desarrollo API First.

### Códigos de Estado HTTP

<p>
  <img src="../../images/http-status-code.jpg" style="width: 540px" />
</p>

Los códigos de respuesta para HTTP se dividen en cinco categorías:

Informativos (100-199)
Éxito (200-299)
Redirección (300-399)
Error del Cliente (400-499)
Error del Servidor (500-599)

### ¿Qué hace una puerta de enlace API?

El diagrama a continuación muestra los detalles. 

<p>
  <img src="../../images/api_gateway.jpg" style="width: 520px" />
</p>

Paso 1 - El cliente envía una solicitud HTTP a la puerta de enlace API.

Paso 2 - La puerta de enlace API analiza y valida los atributos en la solicitud HTTP.

Paso 3 - La puerta de enlace API realiza comprobaciones de lista de permitidos/denegados.

Paso 4 - La puerta de enlace API se comunica con un proveedor de identidad para autenticación y autorización.

Paso 5 - Se aplican las reglas de limitación de velocidad a la solicitud. Si supera el límite, la solicitud se rechaza.

Pasos 6 y 7 - Ahora que la solicitud ha pasado las comprobaciones básicas, la puerta de enlace API encuentra el servicio relevante al que enrutar mediante la coincidencia de rutas.

Paso 8 - La puerta de enlace API transforma la solicitud en el protocolo apropiado y la envía a los microservicios de backend.

Pasos 9-12: La puerta de enlace API puede manejar errores de manera adecuada y tratar con fallos si el error lleva más tiempo en recuperarse (interrupción del circuito). También puede aprovechar la pila ELK (Elastic-Logstash-Kibana) para el registro y monitoreo. A veces, se almacenan datos en caché en la puerta de enlace API.

### ¿Cómo diseñamos API efectivas y seguras?

El diagrama a continuación muestra diseños de API típicos con un ejemplo de carrito de compras.

<p>
  <img src="../../images/safe-apis.jpg" />
</p>

Ten en cuenta que el diseño de una API no se limita al diseño de la ruta de URL. La mayoría de las veces, necesitamos elegir los nombres de recursos adecuados, identificadores y patrones de ruta apropiados. También es importante diseñar campos de encabezado HTTP adecuados o reglas de limitación de velocidad efectivas dentro de la puerta de enlace de la API.

### Encapsulación TCP/IP

¿Cómo se envían datos a través de la red? ¿Por qué necesitamos tantas capas en el modelo OSI?

<p>
  <img src="../../images/osi model.jpeg" />
</p>

El diagrama a continuación muestra cómo se encapsulan y desencapsulan los datos al transmitirse a través de la red.

Paso 1: Cuando el Dispositivo A envía datos al Dispositivo B a través de la red mediante el protocolo HTTP, primero se agrega un encabezado HTTP en la capa de aplicación.

Paso 2: Luego se agrega un encabezado TCP o UDP a los datos. Se encapsulan en segmentos TCP en la capa de transporte. El encabezado contiene el puerto de origen, el puerto de destino y el número de secuencia.

Paso 3: Los segmentos se encapsulan con un encabezado IP en la capa de red. El encabezado IP contiene las direcciones IP de origen y destino.

Paso 4: Al datagrama IP se le agrega un encabezado MAC en la capa de enlace de datos, con direcciones MAC de origen y destino.

Paso 5: Los marcos encapsulados se envían a la capa física y se envían por la red en forma de bits binarios.

Pasos 6-10: Cuando el Dispositivo B recibe los bits de la red, realiza el proceso de desencapsulación, que es un procesamiento inverso del proceso de encapsulación. Los encabezados se eliminan capa por capa y, finalmente, el Dispositivo B puede leer los datos.

Necesitamos capas en el modelo de red porque cada capa se enfoca en sus propias responsabilidades. Cada capa puede confiar en los encabezados para recibir instrucciones de procesamiento y no necesita conocer el significado de los datos de la capa anterior.

### ¿Por qué se llama a Nginx un proxy "inverso"?

El diagrama a continuación muestra las diferencias entre un proxy hacia adelante y un proxy inverso.

<p>
  <img src="../../images/Forward Proxy v.s. Reverse Proxy2x.jpg" style="width: 720px" />
</p>

Un proxy hacia adelante es un servidor que se encuentra entre los dispositivos de usuario y la internet.

Un proxy hacia adelante se utiliza comúnmente para:

1. Proteger a los clientes.
2. Evitar restricciones de navegación.
3. Bloquear el acceso a ciertos contenidos.

Un proxy inverso es un servidor que acepta una solicitud del cliente, la reenvía a servidores web y devuelve los resultados al cliente como si el servidor proxy hubiera procesado la solicitud.

Un proxy inverso es útil para:

1. Proteger servidores.
2. Equilibrar la carga.
3. Cachear contenidos estáticos.
4. Encriptar y desencriptar comunicaciones SSL.

### ¿Cuáles son los algoritmos comunes de equilibrio de carga?

El diagrama a continuación muestra 6 algoritmos comunes.

<p>
  <img src="../../images/lb-algorithms.jpg" />
</p>

- Algoritmos Estáticos

1. Round robin

    Las solicitudes de los clientes se envían a diferentes instancias de servicio en orden secuencial. Por lo general, se requiere que los servicios sean sin estado.

3. Round-robin persistente

    Esto es una mejora del algoritmo round-robin. Si la primera solicitud de Alice va al servicio A, las siguientes solicitudes también van al servicio A.

4. Round-robin ponderado

    El administrador puede especificar el peso para cada servicio. Los que tienen un peso más alto manejan más solicitudes que otros.

6. Hash

    Este algoritmo aplica una función hash a las direcciones IP o URL de las solicitudes entrantes. Las solicitudes se enrutan a las instancias relevantes según el resultado de la función hash.

- Algoritmos Dinámicos

5. Menos conexiones

    Una nueva solicitud se envía a la instancia de servicio con menos conexiones concurrentes.

7. Menor tiempo de respuesta

    Una nueva solicitud se envía a la instancia de servicio con el tiempo de respuesta más rápido.

### URL, URI, URN - ¿Conoces las diferencias?

El diagrama a continuación muestra una comparación de URL, URI y URN.

<p>
  <img src="../../images/url-uri-urn.jpg" />
</p>

- URI

URI significa Identificador de Recursos Uniforme. Identifica un recurso lógico o físico en la web. URL y URN son subtipos de URI. URL localiza un recurso, mientras que URN nombra un recurso.

Un URI se compone de las siguientes partes:
esquema:[//autoridad]ruta[?consulta][#fragmento]

- URL

URL significa Localizador de Recursos Uniforme, el concepto clave de HTTP. Es la dirección de un recurso único en la web. Se puede utilizar con otros protocolos como FTP y JDBC.

- URN

URN significa Nombre de Recurso Uniforme. Utiliza el esquema urn. Las URN no se pueden utilizar para localizar un recurso. Un ejemplo simple dado en el diagrama se compone de un espacio de nombres y una cadena específica del espacio de nombres.

Si deseas obtener más detalles sobre el tema, te recomendaría la [aclaración de W3C](https://www.w3.org/TR/uri-clarification/).

## CI/CD

### Pipeline de CI/CD explicado en términos sencillos

El diagrama a continuación muestra la explicación del pipeline de CI/CD.

<p>
  <img src="../../images/ci-cd-pipeline.jpg" style="width: 680px" />
</p>

Sección 1 - SDLC con CI/CD

El ciclo de vida del desarrollo de software (SDLC) consta de varias etapas clave: desarrollo, pruebas, implementación y mantenimiento. CI/CD automatiza e integra estas etapas para permitir lanzamientos más rápidos y confiables.

Cuando se envía código a un repositorio git, se desencadena un proceso de compilación y prueba automatizado. Se ejecutan casos de prueba de extremo a extremo (e2e) para validar el código. Si las pruebas son exitosas, el código se puede implementar automáticamente en entornos de puesta en escena o producción. Si se encuentran problemas, el código se devuelve al desarrollo para corrección de errores. Esta automatización proporciona retroalimentación rápida a los desarrolladores y reduce el riesgo de errores en producción.

Sección 2 - Diferencia entre CI y CD

La Integración Continua (CI) automatiza el proceso de compilación, prueba y fusión. Ejecuta pruebas cada vez que se confirma el código para detectar problemas de integración temprano. Esto fomenta confirmaciones de código frecuentes y retroalimentación rápida.

La Entrega Continua (CD) automatiza procesos de lanzamiento como cambios en la infraestructura e implementación. Asegura que el software se pueda lanzar de manera confiable en cualquier momento a través de flujos de trabajo automatizados. CD también puede automatizar las pruebas manuales y los pasos de aprobación necesarios antes de la implementación en producción.

Sección 3 - Pipeline de CI/CD

Un pipeline típico de CI/CD consta de varias etapas conectadas:
- El desarrollador confirma cambios de código en el control de código fuente
- El servidor de CI detecta los cambios y desencadena la compilación
- El código se compila y se prueba (pruebas unitarias, pruebas de integración)
- Se informan los resultados de las pruebas al desarrollador
- En caso de éxito, los artefactos se implementan en entornos de puesta en escena
- Puede realizarse una prueba adicional en puesta en escena antes del lanzamiento
- El sistema de CD implementa cambios aprobados en producción

### Stack Tecnológico de Netflix (Pipeline de CI/CD)

<p>
  <img src="../../images/netflix-ci-cd.jpg" style="width: 720px" />
</p>

Planificación: Netflix Engineering utiliza JIRA para la planificación y Confluence para la documentación.

Codificación: Java es el lenguaje de programación principal para el servicio backend, mientras que se utilizan otros lenguajes para diferentes casos de uso.

Construcción: Principalmente se utiliza Gradle para la compilación, y se han creado complementos de Gradle para admitir diversos casos de uso.

Empaquetado: El paquete y las dependencias se empacan en una Imagen de Máquina de Amazon (AMI) para su lanzamiento.

Pruebas: Las pruebas enfatizan la cultura de producción de herramientas de caos.

Implementación: Netflix utiliza su propia herramienta Spinnaker para la implementación de despliegues de canarios.

Monitoreo: Las métricas de monitoreo están centralizadas en Atlas, y se utiliza Kayenta para detectar anomalías.

Informe de incidentes: Los incidentes se envían según la prioridad, y se utiliza PagerDuty para el manejo de incidentes.

## Patrones de arquitectura

### MVC, MVP, MVVM, MVVM-C y VIPER
Estos patrones de arquitectura se encuentran entre los más comúnmente utilizados en el desarrollo de aplicaciones, ya sea en las plataformas iOS o Android. Los desarrolladores los han introducido para superar las limitaciones de patrones anteriores. Entonces, ¿en qué se diferencian?

<p>
  <img src="../../images/client arch patterns.png" style="width: 720px" />
</p>

- MVC, el patrón más antiguo, tiene casi 50 años.
- Cada patrón tiene una "vista" (V) responsable de mostrar contenido y recibir la entrada del usuario.
- La mayoría de los patrones incluyen un "modelo" (M) para gestionar los datos comerciales.
- "Controlador," "presentador" y "modelo de vista" son traductores que median entre la vista y el modelo ("entidad" en el patrón VIPER).

### 18 Patrones de Diseño Clave que Todo Desarrollador Debería Conocer

Los patrones son soluciones reutilizables a problemas de diseño comunes, lo que resulta en un proceso de desarrollo más fluido y eficiente. Sirven como planos para construir estructuras de software mejores. Estos son algunos de los patrones más populares:

<p>
  <img src="../../images/18-oo-patterns.png" />
</p>

- Fábrica Abstracta: Creador de Familias - Crea grupos de elementos relacionados.
- Constructor: Maestro de Lego - Construye objetos paso a paso, manteniendo separada la creación y la apariencia.
- Prototipo: Fabricante de Clones - Crea copias de ejemplos completamente preparados.
- Singleton: Único y Exclusivo - Una clase especial con solo una instancia.
- Adaptador: Enchufe Universal - Conecta cosas con diferentes interfaces.
- Puente: Conector de Funciones - Vincula cómo funciona un objeto con lo que hace.
- Compuesto: Constructor de Árboles - Forma estructuras en forma de árbol de partes simples y complejas.
- Decorador: Personalizador - Agrega características a objetos sin cambiar su núcleo.
- Fachada: Todo en Uno - Representa todo el sistema con una sola interfaz simplificada.
- Peso Ligero: Ahorrador de Espacio - Comparte elementos pequeños y reutilizables de manera eficiente.
- Proxy: Actor Sustituto - Representa otro objeto, controlando el acceso o las acciones.
- Cadena de Responsabilidad: Relé de Solicitudes - Pasa una solicitud a través de una cadena de objetos hasta que se maneja.
- Comando: Envoltura de Tarea - Convierte una solicitud en un objeto listo para la acción.
- Iterador: Explorador de Colecciones - Accede a elementos en una colección uno por uno.
- Mediador: Centro de Comunicación - Simplifica las interacciones entre diferentes clases.
- Memento: Cápsula del Tiempo - Captura y restaura el estado de un objeto.
- Observador: Difusor de Noticias - Notifica a las clases sobre cambios en otros objetos.
- Visitante: Invitado Habilidoso - Agrega nuevas operaciones a una clase sin modificarla.

## Base de datos

### Una práctica hoja de trucos de diferentes bases de datos en servicios en la nube

<p>
  <img src="../../images/cloud-dbs2.png" />
</p>

Elegir la base de datos adecuada para tu proyecto es una tarea compleja. Muchas opciones de bases de datos, cada una adecuada para casos de uso distintos, pueden llevar rápidamente a la fatiga de decisión.

Esperamos que esta hoja de trucos proporcione una dirección de alto nivel para identificar el servicio adecuado que se alinee con las necesidades de tu proyecto y evitar posibles problemas.

Nota: Google tiene una documentación limitada para sus casos de uso de bases de datos. Aunque hicimos nuestro mejor esfuerzo para examinar lo que estaba disponible y llegamos a la mejor opción, es posible que algunas de las entradas necesiten ser más precisas.

### 8 Estructuras de Datos que Impulsan tus Bases de Datos

La respuesta variará según tu caso de uso. Los datos se pueden indexar en memoria o en disco. Del mismo modo, los formatos de datos varían, como números, cadenas, coordenadas geográficas, etc. El sistema puede tener una carga de escritura pesada o de lectura pesada. Todos estos factores afectan tu elección del formato de índice de base de datos.

<p>
  <img src="../../images/8-ds-db.jpg" />
</p>

Las siguientes son algunas de las estructuras de datos más populares utilizadas para indexar datos:

- Lista de salto: un tipo común de índice en memoria. Utilizado en Redis.
- Índice hash: una implementación muy común de la estructura de datos "Mapa" (o "Colección").
- SSTable: implementación en disco inmutable del "Mapa".
- Árbol LSM: Lista de salto + SSTable. Alta capacidad de escritura.
- Árbol B: solución basada en disco. Rendimiento de lectura/escritura constante.
- Índice invertido: utilizado para la indexación de documentos. Utilizado en Lucene.
- Árbol de sufijos: para la búsqueda de patrones de cadenas.
- Árbol R: búsqueda multidimensional, como encontrar el vecino más cercano.

### ¿Cómo se ejecuta una declaración SQL en la base de datos?

El diagrama a continuación muestra el proceso. Ten en cuenta que las arquitecturas de las bases de datos son diferentes, el diagrama demuestra algunos diseños comunes.

<p>
  <img src="../../images/sql execution order in db.jpeg" style="width: 580px" />
</p>

Paso 1 - Se envía una declaración SQL a la base de datos a través de un protocolo de capa de transporte (por ejemplo, TCP).

Paso 2 - La declaración SQL se envía al analizador de comandos, donde pasa por un análisis sintáctico y semántico, y se genera un árbol de consulta después.

Paso 3 - El árbol de consulta se envía al optimizador. El optimizador crea un plan de ejecución.

Paso 4 - El plan de ejecución se envía al ejecutor. El ejecutor recupera datos de la ejecución.

Paso 5 - Los métodos de acceso proporcionan la lógica de obtención de datos necesaria para la ejecución, recuperando datos del motor de almacenamiento.

Paso 6 - Los métodos de acceso deciden si la declaración SQL es de solo lectura. Si la consulta es de solo lectura (sentencia SELECT), se pasa al administrador de búferes para su procesamiento adicional. El administrador de búferes busca los datos en la memoria caché o los archivos de datos.

Paso 7 - Si la declaración es una actualización o una inserción, se pasa al administrador de transacciones para su procesamiento adicional.

Paso 8 - Durante una transacción, los datos están en modo de bloqueo. Esto está garantizado por el administrador de bloqueo. También asegura las propiedades ACID de la transacción.

## Teorema CAP

El teorema CAP es uno de los términos más famosos en ciencias de la computación, pero apuesto a que diferentes desarrolladores tienen diferentes comprensiones. Examinemos qué es y por qué puede resultar confuso.

<p>
  <img src="../../images/cap theorem.jpeg" />
</p>

El teorema CAP establece que un sistema distribuido no puede proporcionar más de dos de estas tres garantías simultáneamente.

**Consistencia**: la consistencia significa que todos los clientes ven los mismos datos al mismo tiempo, sin importar a qué nodo se conecten.

**Disponibilidad**: la disponibilidad significa que cualquier cliente que solicite datos recibe una respuesta, incluso si algunos de los nodos están fuera de servicio.

**Tolerancia a particiones**: una partición indica una interrupción de la comunicación entre dos nodos. La tolerancia a particiones significa que el sistema continúa funcionando a pesar de las particiones de la red.

La formulación de "2 de 3" puede ser útil, **pero esta simplificación puede ser engañosa**.

1. Elegir una base de datos no es fácil. Justificar nuestra elección basada únicamente en el teorema CAP no es suficiente. Por ejemplo, las empresas no eligen Cassandra para aplicaciones de chat simplemente porque es un sistema AP. Hay una lista de buenas características que hacen que Cassandra sea una opción deseable para almacenar mensajes de chat. Necesitamos profundizar más.

2. "CAP prohíbe solo una pequeña parte del espacio de diseño: disponibilidad y consistencia perfectas en presencia de particiones, que son raras". Citado del artículo: CAP Doce Años Después: Cómo las "Reglas" Han Cambiado.

3. El teorema se trata del 100% de disponibilidad y consistencia. Una discusión más realista sería las compensaciones entre latencia y consistencia cuando no hay particiones de red. Consulta el teorema PACELC para obtener más detalles.

**¿Es realmente útil el teorema CAP?**

Creo que todavía es útil, ya que abre nuestra mente a un conjunto de discusiones sobre compensaciones, pero es solo una parte de la historia. Necesitamos profundizar más al elegir la base de datos correcta.

## Tipos de Memoria y Almacenamiento

<p>
  <img src="../../images/Types_of_Memory_and_Storage.jpeg" style="width: 420px" />
</p>

## Visualización de una consulta SQL

<p>
  <img src="../../images/sql-execution-order.jpg" style="width: 580px" />
</p>

Las declaraciones SQL se ejecutan en el sistema de base de datos en varios pasos, que incluyen:

- Análisis sintáctico de la declaración SQL y verificación de su validez.
- Transformación de la SQL en una representación interna, como el álgebra relacional.
- Optimización de la representación interna y creación de un plan de ejecución que utiliza información de índice.
- Ejecución del plan y devolución de los resultados.

La ejecución de SQL es altamente compleja e implica muchas consideraciones, como:

- El uso de índices y cachés.
- El orden de las uniones de tablas.
- Control de concurrencia.
- Gestión de transacciones.

## Lenguaje SQL

En 1986, SQL (Structured Query Language) se convirtió en un estándar. Durante los siguientes 40 años, se convirtió en el lenguaje dominante para los sistemas de gestión de bases de datos relacionales. Leer el último estándar (ANSI SQL 2016) puede llevar mucho tiempo. ¿Cómo puedo aprenderlo?

<p>
  <img src="../../images/how-to-learn-sql.jpg" />
</p>

Hay 5 componentes del lenguaje SQL:

- DDL: lenguaje de definición de datos, como CREATE, ALTER, DROP.
- DQL: lenguaje de consulta de datos, como SELECT.
- DML: lenguaje de manipulación de datos, como INSERT, UPDATE, DELETE.
- DCL: lenguaje de control de datos, como GRANT, REVOKE.
- TCL: lenguaje de control de transacciones, como COMMIT, ROLLBACK.

Para un ingeniero de backend, es posible que debas conocer la mayoría de ellos. Como analista de datos, es posible que debas tener una buena comprensión de DQL. Selecciona los temas que sean más relevantes para ti.

## Caché

### Los Datos se Cachéan en Todas Partes

Este diagrama ilustra dónde almacenamos en caché datos en una arquitectura típica.

<p>
  <img src="../../images/where do we cache data.jpeg" style="width: 720px" />
</p>

Hay **múltiples capas** a lo largo del flujo.

1. Aplicaciones cliente: las respuestas HTTP pueden almacenarse en la caché del navegador. Solicitamos datos a través de HTTP por primera vez, y se devuelven con una política de vencimiento en la cabecera HTTP; solicitamos datos nuevamente y la aplicación cliente intenta recuperar los datos primero de la caché del navegador.
2. CDN: CDN almacena en caché recursos web estáticos. Los clientes pueden recuperar datos desde un nodo de CDN cercano.
3. Balanceador de carga: el balanceador de carga también puede almacenar en caché recursos.
4. Infraestructura de mensajería: los intermediarios de mensajes almacenan mensajes en disco primero y luego los consumidores los recuperan a su propio ritmo. Dependiendo de la política de retención, los datos se almacenan en caché en clústeres Kafka durante un período de tiempo.
5. Servicios: hay múltiples capas de caché en un servicio. Si los datos no están en caché en la memoria caché de la CPU, el servicio intentará recuperar los datos de la memoria. A veces, el servicio tiene una caché de segundo nivel para almacenar datos en disco.
6. Caché distribuida: la caché distribuida como Redis almacena pares clave-valor para múltiples servicios en memoria. Ofrece un rendimiento de lectura/escritura mucho mejor que la base de datos.
7. Búsqueda de texto completo: a veces necesitamos usar búsquedas de texto completo como Elastic Search para la búsqueda de documentos o registros. Una copia de los datos también se indexa en el motor de búsqueda.
8. Base de datos: incluso en la base de datos, tenemos diferentes niveles de caché:
    - WAL (Write-ahead Log): los datos se escriben primero en el WAL antes de construir el índice del árbol B.
    - Bufferpool: un área de memoria asignada para almacenar resultados de consultas en caché.
    - Vista materializada: precalcula los resultados de la consulta y los almacena en tablas de base de datos para un mejor rendimiento en las consultas.
    - Registro de transacciones: registra todas las transacciones y actualizaciones de la base de datos.
    - Registro de replicación: se utiliza para registrar el estado de la replicación en un clúster de base de datos.

## ¿Por qué Redis es tan rápido?

Hay 3 razones principales, como se muestra en el diagrama a continuación.

<p>
  <img src="../../images/why_redis_fast.jpeg" />
</p>

1. Redis es una base de datos basada en RAM. El acceso a la RAM es al menos 1000 veces más rápido que el acceso aleatorio a disco.
2. Redis utiliza la multiplexación de E/S y un bucle de ejecución de un solo hilo para lograr eficiencia en la ejecución.
3. Redis utiliza varias estructuras de datos de nivel inferior eficientes.

Pregunta: Otro almacén en memoria popular es Memcached. ¿Conoces las diferencias entre Redis y Memcached?

Tal vez hayas notado que el estilo de este diagrama es diferente de mis publicaciones anteriores. Por favor, házmelo saber si prefieres uno u otro.

## ¿Cómo se puede utilizar Redis?

<p>
  <img src="../../images/top-redis-use-cases.jpg" style="width: 520px" />
</p>

Redis se puede utilizar en una variedad de escenarios, como se muestra en el diagrama:

- Sesión: se puede usar Redis para compartir datos de sesión de usuario entre diferentes servicios.
- Caché: se puede usar Redis para almacenar en caché objetos o páginas, especialmente para datos críticos.
- Bloqueo distribuido: se puede utilizar una cadena Redis para adquirir bloqueos entre servicios distribuidos.
- Contador: se pueden contar la cantidad de "me gusta" o la cantidad de lecturas de artículos.
- Limitador de velocidad: se puede aplicar un limitador de velocidad para ciertas direcciones IP de usuario.
- Generador de ID global: se puede usar un entero Redis para IDs globales.
- Carrito de compras: se puede usar un hash Redis para representar pares clave-valor en un carrito de compras.
- Cálculo de la retención de usuarios: se puede usar un Bitmap Redis para representar el inicio de sesión diario del usuario y calcular la retención de usuarios.
- Cola de mensajes: se puede utilizar una lista Redis como cola de mensajes.
- Clasificación: se puede usar un conjunto ordenado Redis para ordenar artículos.

## Principales estrategias de caché

El diseño de sistemas a gran escala generalmente requiere una cuidadosa consideración de la caché. A continuación se presentan cinco estrategias de caché que se utilizan con frecuencia.

<p>
  <img src="../../images/top_caching_strategy.jpeg" style="width: 680px" />
</p>

## Arquitectura de microservicios

### ¿Cómo se ve una arquitectura típica de microservicios?

<p>
  <img src="../../images/typical-microservice-arch.jpg" style="width: 520px" />
</p>

El diagrama muestra una arquitectura típica de microservicios.

- Balanceador de carga: esto distribuye el tráfico entrante entre múltiples servicios de backend.
- CDN (Red de Distribución de Contenido): un grupo de servidores distribuidos geográficamente que almacenan contenido estático para una entrega más rápida. Los clientes buscan contenido en CDN primero y luego avanzan hacia los servicios de backend.
- API Gateway: maneja las solicitudes entrantes y las dirige a los servicios relevantes. Se comunica con el proveedor de identidad y el registro y descubrimiento de servicios.
- Proveedor de Identidad: se encarga de la autenticación y autorización de los usuarios.
- Registro y Descubrimiento de Servicios: el registro y descubrimiento de microservicios ocurre en este componente, y el API Gateway busca servicios relevantes en este componente para comunicarse.
- Gestión: este componente es responsable de supervisar los servicios.
- Microservicios: los microservicios están diseñados y desplegados en diferentes dominios. Cada dominio tiene su propia base de datos. El API Gateway se comunica con los microservicios a través de una API REST u otros protocolos, y los microservicios dentro del mismo dominio se comunican entre sí utilizando RPC (Llamada a Procedimiento Remoto).

Beneficios de los microservicios:

- Pueden diseñarse, desplegarse y escalarse horizontalmente de manera rápida.
- Cada dominio puede ser mantenido de manera independiente por un equipo dedicado.
- Los requisitos comerciales pueden ser personalizados en cada dominio y mejor respaldados como resultado.

## Mejores prácticas para microservicios

Una imagen vale más que mil palabras: 9 mejores prácticas para el desarrollo de microservicios.

<p>
  <img src="../../images/microservice-best-practices.jpeg" />
</p>

Cuando desarrollamos microservicios, debemos seguir las siguientes mejores prácticas:

1. Utilizar almacenamiento de datos separado para cada microservicio.
2. Mantener el código a un nivel de madurez similar.
3. Realizar una construcción separada para cada microservicio.
4. Asignar a cada microservicio una sola responsabilidad.
5. Desplegar en contenedores.
6. Diseñar servicios sin estado.
7. Adoptar el diseño basado en dominios.
8. Diseñar microfrontends.
9. Orquestar microservicios.

## Pila tecnológica comúnmente utilizada para microservicios

A continuación, encontrarás un diagrama que muestra la pila tecnológica de microservicios, tanto para la fase de desarrollo como para la producción.

<p>
  <img src="../../images/microservice-tech.jpeg" />
</p>

▶️ **Pre-Producción**

- Definir API: esto establece un contrato entre el frontend y el backend. Podemos usar Postman o OpenAPI para esto.
- Desarrollo: Node.js o React son populares para el desarrollo frontend, y Java/Python/Go para el desarrollo backend. Además, debemos cambiar las configuraciones en la pasarela de API según las definiciones de la API.
- Integración continua: JUnit y Jenkins para pruebas automatizadas. El código se empaqueta en una imagen de Docker y se despliega como microservicios.

▶️ **Producción**

- NGinx es una opción común para balanceadores de carga. Cloudflare proporciona una red de distribución de contenido (CDN).
- Pasarela de API: podemos usar Spring Boot para la pasarela y Eureka/Zookeeper para el descubrimiento de servicios.
- Los microservicios se despliegan en la nube. Tenemos opciones entre AWS, Microsoft Azure o Google GCP.
- Caché y búsqueda de texto completo: Redis es una opción común para el almacenamiento en caché de pares clave-valor. Elasticsearch se utiliza para la búsqueda de texto completo.
- Comunicaciones: para que los servicios se comuniquen entre sí, podemos usar infraestructuras de mensajería como Kafka o RPC.
- Persistencia: podemos utilizar MySQL o PostgreSQL para una base de datos relacional y Amazon S3 para el almacenamiento de objetos. También podemos utilizar Cassandra para un almacén de columnas anchas si es necesario.
- Gestión y supervisión: para administrar tantos microservicios, las herramientas comunes de operaciones incluyen Prometheus, Elastic Stack y Kubernetes.

## ¿Por qué Kafka es rápido?

Existen muchas decisiones de diseño que contribuyen al rendimiento de Kafka. En esta publicación, nos centraremos en dos. Creemos que estas dos son las que más peso tienen.

<p>
  <img src="../../images/why_is_kafka_fast.jpeg" />
</p>

1. La primera es la dependencia de Kafka en la E/S secuencial.
2. La segunda elección de diseño que le da a Kafka su ventaja en rendimiento es su enfoque en la eficiencia: el principio de "cero copias".

El diagrama ilustra cómo se transmite la información entre el productor y el consumidor, y lo que significa "cero copia".

- Paso 1.1 - 1.3: El productor escribe datos en el disco.
- Paso 2: El consumidor lee datos sin "cero copia".

2.1 Los datos se cargan desde el disco en la caché del sistema operativo.

2.2 Los datos se copian desde la caché del sistema operativo a la aplicación Kafka.

2.3 La aplicación Kafka copia los datos en el búfer del socket.

2.4 Los datos se copian del búfer del socket a la tarjeta de red.

2.5 La tarjeta de red envía los datos al consumidor.

- Paso 3: El consumidor lee datos con "cero copia".

3.1: Los datos se cargan desde el disco en la caché del sistema operativo.
3.2 La caché del sistema operativo copia directamente los datos a la tarjeta de red a través del comando "sendfile()".
3.3 La tarjeta de red envía los datos al consumidor.

La "cero copia" es un atajo para ahorrar copias múltiples de datos entre el contexto de la aplicación y el contexto del kernel.

## Sistemas de pago

### ¿Cómo aprender sobre sistemas de pago?

<p>
  <img src="../../images/learn-payments.jpg" />
</p>

### ¿Por qué se llama a la tarjeta de crédito "el producto más rentable en los bancos"? ¿Cómo gana dinero VISA/Mastercard?

El diagrama a continuación muestra la economía del flujo de pagos con tarjeta de crédito.

<p>
  <img src="../../images/how does visa makes money.jpg" style="width: 640px" />
</p>

1. El titular de la tarjeta paga $100 a un comerciante para comprar un producto.

2. El comerciante se beneficia del uso de la tarjeta de crédito con un mayor volumen de ventas y debe compensar al emisor y a la red de tarjetas por proporcionar el servicio de pago. El banco adquirente establece una tarifa con el comerciante, llamada "tarifa de descuento del comerciante".

3 - 4. El banco adquirente se queda con $0.25 como margen de adquirente, y $1.75 se paga al banco emisor como tarifa de intercambio. La tarifa de descuento del comerciante debería cubrir la tarifa de intercambio.

   La tarifa de intercambio la establece la red de tarjetas porque es menos eficiente que cada banco emisor negocie tarifas con cada comerciante.

5. La red de tarjetas configura las tasaciones y tarifas de la red con cada banco, que paga a la red de tarjetas por sus servicios cada mes. Por ejemplo, VISA cobra una tasación del 0.11%, más una tarifa de uso de $0.0195, por cada transacción.

6. El titular de la tarjeta paga al banco emisor por sus servicios.

¿Por qué se debe compensar al banco emisor?

- El banco emisor paga al comerciante incluso si el titular de la tarjeta no paga al banco emisor.
- El banco emisor paga al comerciante antes de que el titular de la tarjeta pague al banco emisor.
- El banco emisor tiene otros costos operativos, como la gestión de cuentas de clientes, la emisión de estados de cuenta, la detección de fraudes, la gestión de riesgos, la compensación y liquidación, etc.

### ¿Cómo funciona VISA cuando pasamos una tarjeta de crédito en la tienda de un comerciante?

<p>
  <img src="../../images/visa_payment.jpeg" />
</p>

VISA, Mastercard y American Express actúan como redes de tarjetas para la compensación y liquidación de fondos. El banco adquirente de la tarjeta y el banco emisor de la tarjeta pueden ser -y a menudo son- diferentes. Si los bancos liquidaran las transacciones una por una sin un intermediario, cada banco tendría que liquidar las transacciones con todos los demás bancos, lo cual sería bastante ineficiente.

El diagrama a continuación muestra el papel de VISA en el proceso de pago con tarjeta de crédito. Hay dos flujos involucrados. El flujo de autorización ocurre cuando el cliente pasa la tarjeta de crédito. El flujo de captura y liquidación ocurre cuando el comerciante quiere recibir el dinero al final del día.

- Flujo de autorización

Paso 0: El banco emisor de la tarjeta emite tarjetas de crédito a sus clientes.

Paso 1: El titular de la tarjeta desea comprar un producto y pasa la tarjeta de crédito en el punto de venta (POS) en la tienda del comerciante.

Paso 2: El terminal POS envía la transacción al banco adquirente, que ha proporcionado el terminal POS.

Paso 3 y 4: El banco adquirente envía la transacción a la red de tarjetas, también llamada esquema de tarjetas. La red de tarjetas envía la transacción al banco emisor para su aprobación.

Paso 4.1, 4.2 y 4.3: Si la transacción es aprobada, el banco emisor bloquea el dinero. La aprobación o el rechazo se envía de vuelta al adquirente, así como al terminal POS.

- Flujo de captura y liquidación

Pasos 1 y 2: El comerciante quiere recolectar el dinero al final del día, así que selecciona "captura" en el terminal POS. Las transacciones se envían en lote al banco adquirente. El banco adquirente envía el archivo de lote con transacciones a la red de tarjetas.

Paso 3: La red de tarjetas realiza el proceso de compensación para las transacciones recolectadas de diferentes adquirentes y envía los archivos de compensación a diferentes bancos emisores.

Paso 4: Los bancos emisores confirman la corrección de los archivos de compensación y transfieren dinero a los bancos adquirentes correspondientes.

Paso 5: El banco adquirente luego transfiere el dinero al banco del comerciante.

Paso 4: La red de tarjetas compensa las transacciones de diferentes bancos adquirentes. La compensación es un proceso en el que las transacciones de compensación mutua se netean, lo que reduce el número total de transacciones.

En este proceso, la red de tarjetas se encarga de hablar con cada banco y recibe tarifas de servicio a cambio.

## Sistemas de pago en todo el mundo

### (Parte 1): Interfaz Unificada de Pagos (UPI) en India

¿Qué es UPI? UPI es un sistema de pago instantáneo en tiempo real desarrollado por la Corporación Nacional de Pagos de la India.

Representa el 60% de las transacciones minoristas digitales en la India hoy en día.

UPI = lenguaje de marcado de pago + estándar para pagos interoperables

<p>
  <img src="../../images/how-does-upi-work.png"  style="width: 600px" />
</p>

## DevOps

### DevOps vs. SRE vs. Ingeniería de Plataformas. ¿Cuál es la diferencia?

Los conceptos de DevOps, SRE e Ingeniería de Plataformas han surgido en diferentes momentos y han sido desarrollados por diversas personas y organizaciones.

<p>
  <img src="../../images/devops-sre-platform.jpg" />
</p>

DevOps como concepto fue introducido en 2009 por Patrick Debois y Andrew Shafer en la conferencia Agile. Buscaron cerrar la brecha entre el desarrollo de software y las operaciones promoviendo una cultura colaborativa y una responsabilidad compartida en todo el ciclo de desarrollo de software.

SRE, o Ingeniería de Confiabilidad del Sitio, fue pionera en Google a principios de la década de 2000 para abordar los desafíos operativos en la gestión de sistemas complejos a gran escala. Google desarrolló prácticas y herramientas de SRE, como el sistema de gestión de clúster Borg y el sistema de monitoreo Monarch, para mejorar la confiabilidad y eficiencia de sus servicios.

La Ingeniería de Plataformas es un concepto más reciente que se basa en la ingeniería SRE. Los orígenes precisos de la Ingeniería de Plataformas son menos claros, pero generalmente se entiende como una extensión de las prácticas de DevOps y SRE, con un enfoque en proporcionar una plataforma integral para el desarrollo de productos que respalde la perspectiva comercial en su totalidad.

Vale la pena señalar que, aunque estos conceptos surgieron en diferentes momentos, todos están relacionados con la tendencia general de mejorar la colaboración, la automatización y la eficiencia en el desarrollo de software y las operaciones.

### ¿Qué es k8s (Kubernetes)?

K8s es un sistema de orquestación de contenedores utilizado para la implementación y gestión de contenedores. Su diseño está fuertemente influenciado por el sistema interno de Google llamado Borg.

<p>
  <img src="../../images/k8s.jpeg" style="width: 680px" />
</p>

Un clúster de k8s consta de un conjunto de máquinas trabajadoras, llamadas nodos, que ejecutan aplicaciones en contenedores. Cada clúster tiene al menos un nodo trabajador.

Los nodos trabajadores alojan los pods que son los componentes de la carga de trabajo de la aplicación. El plano de control gestiona los nodos trabajadores y los pods en el clúster. En entornos de producción, el plano de control generalmente se ejecuta en múltiples computadoras y un clúster generalmente ejecuta múltiples nodos para proporcionar tolerancia a fallos y alta disponibilidad.

- Componentes del Plano de Control

1. Servidor de API: El servidor de API se comunica con todos los componentes en el clúster k8s. Todas las operaciones en los pods se ejecutan mediante comunicación con el servidor de API.

2. Programador: El programador supervisa las cargas de trabajo de los pods y asigna cargas en los pods recién creados.

3. Controlador de Administración: El controlador de administración ejecuta los controladores, incluyendo el Controlador de Nodos, Controlador de Trabajos, Controlador de Puntos de Extremo y Controlador de Cuentas de Servicio.

4. Etcd: Etcd es un almacén de clave-valor utilizado como almacén de respaldo de Kubernetes para todos los datos del clúster.

- Nodos

1. Pods: Un pod es un grupo de contenedores y es la unidad más pequeña que administra k8s. Los pods tienen una única dirección IP que se aplica a todos los contenedores dentro del pod.

2. Kubelet: Es un agente que se ejecuta en cada nodo del clúster. Se asegura de que los contenedores se estén ejecutando en un pod.

3. Kube Proxy: Kube-proxy es un proxy de red que se ejecuta en cada nodo de su clúster. Enrutará el tráfico que entra en un nodo desde el servicio y reenviará las solicitudes de trabajo a los contenedores correctos.

### Docker vs. Kubernetes. ¿Cuál deberíamos usar?

<p>
  <img src="../../images/docker-vs-k8s.jpg" style="width: 680px" />
</p>

¿Qué es Docker?

Docker es una plataforma de código abierto que te permite empaquetar, distribuir y ejecutar aplicaciones en contenedores aislados. Se centra en la contenerización, proporcionando entornos ligeros que encapsulan aplicaciones y sus dependencias.

¿Qué es Kubernetes?

Kubernetes, a menudo referido como K8s, es una plataforma de orquestación de contenedores de código abierto. Proporciona un marco para automatizar la implementación, escalado y gestión de aplicaciones en contenedores en un clúster de nodos.

¿Cómo son diferentes entre sí?

Docker: Docker opera a nivel de contenedor individual en un único sistema operativo anfitrión. Debes gestionar manualmente cada anfitrión y configurar redes, políticas de seguridad y almacenamiento para múltiples contenedores relacionados, lo que puede ser complejo.

Kubernetes: Kubernetes opera a nivel de clúster. Gestiona múltiples aplicaciones contenerizadas en varios nodos, automatizando tareas como el equilibrio de carga, el escalado y asegurando el estado deseado de las aplicaciones.

En resumen, Docker se centra en la contenerización y la ejecución de contenedores en hosts individuales, mientras que Kubernetes se especializa en la gestión y orquestación de contenedores a escala en un clúster de hosts.

## Cómo funciona Docker

El siguiente diagrama muestra la arquitectura de Docker y cómo funciona cuando ejecutamos "docker build", "docker pull" y "docker run".

<p>
  <img src="../../images/docker.jpg" style="width: 680px" />
</p>

Hay 3 componentes en la arquitectura de Docker:

- Cliente de Docker: El cliente de Docker se comunica con el daemon de Docker.

- Host de Docker: El daemon de Docker escucha las solicitudes de la API de Docker y administra objetos de Docker como imágenes, contenedores, redes y volúmenes.

- Registro de Docker: Un registro de Docker almacena imágenes de Docker. Docker Hub es un registro público que cualquiera puede usar.

Tomemos el comando "docker run" como ejemplo:

1. Docker descarga la imagen desde el registro.
2. Docker crea un nuevo contenedor.
3. Docker asigna un sistema de archivos de lectura/escritura al contenedor.
4. Docker crea una interfaz de red para conectar el contenedor a la red predeterminada.
5. Docker inicia el contenedor.

## GIT

### Cómo funcionan los comandos de Git

Para comenzar, es esencial identificar dónde se almacena nuestro código. La suposición común es que existen solo dos ubicaciones: una en un servidor remoto como Github y la otra en nuestra máquina local. Sin embargo, esto no es del todo preciso. Git mantiene tres almacenes locales en nuestra máquina, lo que significa que nuestro código puede encontrarse en cuatro lugares:

<p>
  <img src="../../images/git-commands.png" style="width: 600px" />
</p>

- Directorio de trabajo: donde editamos archivos.
- Área de preparación: una ubicación temporal donde se mantienen los archivos para el próximo commit.
- Repositorio local: contiene el código que se ha confirmado.
- Repositorio remoto: el servidor remoto que almacena el código.

La mayoría de los comandos de Git mueven archivos principalmente entre estas cuatro ubicaciones.

### ¿Cómo funciona Git?

El siguiente diagrama muestra el flujo de trabajo de Git.

<p>
  <img src="../../images/git-workflow.jpeg" style="width: 520px" />
</p>

Git es un sistema de control de versiones distribuido.

Cada desarrollador mantiene una copia local del repositorio principal y edita y confirma en la copia local.

La confirmación es muy rápida porque la operación no interactúa con el repositorio remoto.

Si el repositorio remoto falla, los archivos pueden recuperarse de los repositorios locales.

### Git merge vs. Git rebase

¿Cuáles son las diferencias?

![Imagen](../../images/git-merge-git-rebase.jpeg)

Cuando fusionamos cambios de una rama de Git en otra, podemos usar 'git merge' o 'git rebase'. El diagrama muestra cómo funcionan estos dos comandos.

**Git merge**

Esto crea un nuevo commit G' en la rama principal. G' une las historias de ambas ramas principales y de características.

Git merge es **no destructivo**. Ni la rama principal ni la rama de características se modifican.

**Git rebase**

Git rebase mueve las historias de la rama de características a la cabeza de la rama principal. Crea nuevos commits E', F' y G' para cada confirmación en la rama de características.

El beneficio del rebase es que tiene un historial de confirmación **lineal**.

Rebase puede ser peligroso si no se sigue "la regla de oro del rebase de Git".

**La Regla de Oro del Rebase de Git**

¡Nunca lo uses en ramas públicas!

## Servicios en la nube

### Una práctica hoja de trucos de diferentes servicios en la nube (edición 2023)

![Imagen](../../images/cloud-compare.jpg)

### ¿Qué significa nativo en la nube?

A continuación se muestra un diagrama que muestra la evolución de la arquitectura y los procesos desde la década de 1980.

![Imagen](../../images/cloud-native.jpeg)

Las organizaciones pueden construir y ejecutar aplicaciones escalables en nubes públicas, privadas e híbridas utilizando tecnologías nativas de la nube.

Esto significa que las aplicaciones están diseñadas para aprovechar las características de la nube, por lo que son resistentes a la carga y fáciles de escalar.

Lo nativo de la nube incluye 4 aspectos:

1. Proceso de desarrollo: ha progresado desde el modelo en cascada hasta la metodología ágil y DevOps.

2. Arquitectura de la aplicación: ha evolucionado de aplicaciones monolíticas a microservicios, donde cada servicio se diseña para ser pequeño y se adapta a los recursos limitados en los contenedores de la nube.

3. Implementación y empaquetado: las aplicaciones solían implementarse en servidores físicos. Luego, alrededor del año 2000, las aplicaciones que no eran sensibles a la latencia generalmente se implementaban en servidores virtuales. Con las aplicaciones nativas de la nube, se empaquetan en imágenes de Docker y se implementan en contenedores.

4. Infraestructura de la aplicación: las aplicaciones se implementan masivamente en la infraestructura de la nube en lugar de en servidores autohospedados.

### Herramientas para la productividad del desarrollador

Visualizar archivos JSON

Los archivos JSON anidados son difíciles de leer. JsonCrack genera diagramas gráficos a partir de archivos JSON y los hace fáciles de leer. Además, los diagramas generados se pueden descargar como imágenes.

<p>
  <img src="../../images/json-cracker.jpeg" />
</p>

###Convertir automáticamente código en diagramas de arquitectura

<p>
  <img src="../../images/diagrams_as_code.jpeg" style="width: 640px" />
</p>

¿Qué hace?

    Dibuja la arquitectura del sistema en la nube en código Python.
    Los diagramas también se pueden representar directamente dentro de Jupyter Notebooks.
    No se necesitan herramientas de diseño.
    Admite los siguientes proveedores: AWS, Azure, GCP, Kubernetes, Alibaba Cloud, Oracle Cloud, etc.

[Repositorio en GitHub](https://github.com/mingrammer/diagrams)

Linux

Explicación del sistema de archivos de Linux

<p>
  <img src="../../images/linux-file-systems.jpg" style="width: 680px" />
</p>

El sistema de archivos de Linux solía parecerse a un pueblo desorganizado donde las personas construían sus casas donde quisieran. Sin embargo, en 1994 se introdujo el Estándar de Jerarquía del Sistema de Archivos (FHS) para dar orden al sistema de archivos de Linux.

Al implementar un estándar como el FHS, el software puede garantizar un diseño coherente en varias distribuciones de Linux. Sin embargo, no todas las distribuciones de Linux siguen estrictamente este estándar. A menudo incorporan elementos únicos o se adaptan a requisitos específicos.

Para familiarizarse con este estándar, puede comenzar explorando. Utilice comandos como "cd" para navegar y "ls" para listar el contenido del directorio. Imagine el sistema de archivos como un árbol, comenzando desde la raíz (/). Con el tiempo, se volverá natural para usted, transformándolo en un administrador de Linux experto.

### 18 Comandos de Linux Más Utilizados que Debes Conocer 

Los comandos de Linux son instrucciones para interactuar con el sistema operativo. Ayudan a administrar archivos, directorios, procesos del sistema y muchos otros aspectos del sistema. Necesitas familiarizarte con estos comandos para navegar y mantener eficiente y efectivamente sistemas basados en Linux. 

Esta imagen a continuación muestra comandos populares de Linux: 

<p>
  <img src="../../images/18 Comandos de Linux Más Utilizados que Debes Conocer-01.jpeg" style="width: 680px" />
</p>


- ls - Listar archivos y directorios
- cd - Cambiar el directorio actual
- mkdir - Crear un nuevo directorio
- rm - Eliminar archivos o directorios
- cp - Copiar archivos o directorios
- mv - Mover o renombrar archivos o directorios
- chmod - Cambiar los permisos de archivos o directorios
- grep - Buscar un patrón en archivos
- find - Buscar archivos y directorios
- tar - Manipular archivos de archivo tarball
- vi - Editar archivos con editores de texto
- cat - Mostrar el contenido de archivos
- top - Mostrar procesos y uso de recursos
- ps - Mostrar información de procesos
- kill - Terminar un proceso enviando una señal
- du - Estimar el uso del espacio de archivos
- ifconfig - Configurar interfaces de red
- ping - Probar la conectividad de red entre hosts

## Seguridad

### ¿Cómo funciona HTTPS?

Hypertext Transfer Protocol Secure (HTTPS) es una extensión del Protocolo de Transferencia de Hipertexto (HTTP). HTTPS transmite datos cifrados utilizando Transport Layer Security (TLS). Si los datos son interceptados en línea, todo lo que el atacante obtiene es código binario.

<p>
  <img src="../../images/https.jpg" />
</p>

¿Cómo se cifran y descifran los datos?

Paso 1 - El cliente (navegador) y el servidor establecen una conexión TCP.

Paso 2 - El cliente envía un "saludo del cliente" al servidor. El mensaje contiene un conjunto de algoritmos de cifrado necesarios (cifrado) y la última versión de TLS que puede admitir. El servidor responde con un "saludo del servidor" para que el navegador sepa si puede admitir los algoritmos y la versión de TLS.

Luego, el servidor envía el certificado SSL al cliente. El certificado contiene la clave pública, el nombre del host, las fechas de vencimiento, etc. El cliente valida el certificado.

Paso 3 - Después de validar el certificado SSL, el cliente genera una clave de sesión y la cifra con la clave pública. El servidor recibe la clave de sesión cifrada y la descifra con la clave privada.

Paso 4 - Ahora que tanto el cliente como el servidor tienen la misma clave de sesión (cifrado simétrico), los datos cifrados se transmiten en un canal bidireccional seguro.

¿Por qué HTTPS cambia al cifrado simétrico durante la transmisión de datos? Hay dos razones principales:

1. Seguridad: El cifrado asimétrico va en una sola dirección. Esto significa que si el servidor intenta enviar los datos cifrados de vuelta al cliente, cualquiera puede descifrar los datos utilizando la clave pública.

2. Recursos del servidor: El cifrado asimétrico agrega bastante sobrecarga matemática. No es adecuado para transmisiones de datos en sesiones largas.

### Explicación de OAuth 2.0 en Términos Sencillos

OAuth 2.0 es un marco potente y seguro que permite que diferentes aplicaciones interactúen de manera segura entre sí en nombre de los usuarios sin compartir credenciales sensibles.

<p>
  <img src="../../images/oAuth2.jpg" />
</p>

Las entidades involucradas en OAuth son el Usuario, el Servidor y el Proveedor de Identidad (IDP).

¿Qué Puede Hacer un Token de OAuth?

Cuando utilizas OAuth, obtienes un token de OAuth que representa tu identidad y permisos. Este token puede hacer algunas cosas importantes:

Inicio de Sesión Único (SSO): Con un token de OAuth, puedes iniciar sesión en múltiples servicios o aplicaciones con solo un inicio de sesión, lo que facilita y hace más seguro tu vida.

Autorización en Sistemas Diversos: El token de OAuth te permite compartir tus derechos de autorización o acceso en varios sistemas, por lo que no tienes que iniciar sesión por separado en todas partes.

Acceso al Perfil de Usuario: Las aplicaciones con un token de OAuth pueden acceder a ciertas partes de tu perfil de usuario que permitas, pero no verán todo.

Recuerda, OAuth 2.0 se trata de mantener tu seguridad y la de tus datos mientras haces que tus experiencias en línea sean fluidas y sin complicaciones en diferentes aplicaciones y servicios.

### Las 4 Principales Formas de Mecanismos de Autenticación 

<p>
  <img src="../../images/top4-most-used-auth.jpg" />
</p>

1. Claves SSH:

    Las claves criptográficas se utilizan para acceder a sistemas y servidores remotos de manera segura.

1. Tokens de OAuth:

    Tokens que proporcionan acceso limitado a los datos del usuario en aplicaciones de terceros.

1. Certificados SSL:

    Los certificados digitales garantizan una comunicación segura y cifrada entre servidores y clientes.

1. Credenciales:

    La información de autenticación del usuario se utiliza para verificar y otorgar acceso a diversos sistemas y servicios.

### Sesión, cookie, JWT, token, SSO y OAuth 2.0: ¿qué son?

Estos términos están relacionados con la gestión de la identidad del usuario. Cuando inicias sesión en un sitio web, declaras quién eres (identificación). Tu identidad se verifica (autenticación) y se te otorgan los permisos necesarios (autorización). Se han propuesto muchas soluciones en el pasado y la lista sigue creciendo.

<p>
  <img src="../../images/session.jpeg" />
</p>

De lo simple a lo complejo, aquí está mi comprensión de la gestión de la identidad del usuario:

- WWW-Authenticate es el método más básico. El navegador te solicita el nombre de usuario y la contraseña. Debido a la incapacidad de controlar el ciclo de vida del inicio de sesión, rara vez se utiliza en la actualidad.

- Un control más fino sobre el ciclo de vida del inicio de sesión es la sesión-cookie. El servidor mantiene el almacenamiento de la sesión y el navegador conserva el ID de la sesión. Por lo general, una cookie solo funciona con navegadores y no es amigable para aplicaciones móviles.

- Para abordar el problema de compatibilidad, se puede utilizar el token. El cliente envía el token al servidor y este lo valida. El inconveniente es que el token debe cifrarse y descifrarse, lo que puede llevar tiempo.

- JWT es una forma estándar de representar tokens. Esta información puede ser verificada y confiable porque está digitalmente firmada. Dado que JWT contiene la firma, no es necesario guardar información de sesión en el lado del servidor.

- Utilizando SSO (inicio de sesión único), puedes iniciar sesión solo una vez y acceder a múltiples sitios web. Utiliza CAS (servicio de autenticación central) para mantener información entre sitios.

- Mediante OAuth 2.0, puedes autorizar a un sitio web para que acceda a tu información en otro sitio web.

### Cómo almacenar contraseñas de forma segura en la base de datos y cómo validar una contraseña

<p>
  <img src="../../images/salt.jpg" style="width: 720px" />
</p>

**Cosas que NO debes hacer**

- Almacenar contraseñas en texto sin formato no es una buena idea porque cualquiera con acceso interno puede verlas.

- Almacenar directamente los hash de las contraseñas no es suficiente, ya que está expuesto a ataques de precomputación, como tablas arcoíris.

- Para mitigar los ataques de precomputación, salamos las contraseñas.

**¿Qué es el sal?**

Según las directrices de OWASP, "una sal es una cadena única generada al azar que se agrega a cada contraseña como parte del proceso de hash".

**Cómo almacenar una contraseña y una sal**

1. El resultado del hash es único para cada contraseña.
1. La contraseña se puede almacenar en la base de datos utilizando el siguiente formato: hash(contraseña + sal).

**Cómo validar una contraseña**

Para validar una contraseña, puede pasar por el siguiente proceso:

1. Un cliente ingresa la contraseña.
1. El sistema recupera la sal correspondiente de la base de datos.
1. El sistema agrega la sal a la contraseña y la hashea. Llamémosla H1.
1. El sistema compara H1 y H2, donde H2 es el hash almacenado en la base de datos. Si son iguales, la contraseña es válida.

### Explicando JSON Web Token (JWT) a un niño de 10 años

<p>
  <img src="../../images/jwt.jpg" />
</p>

Imagina que tienes una caja especial llamada JWT. Dentro de esta caja, hay tres partes: un encabezado, una carga útil y una firma.

El encabezado es como la etiqueta en el exterior de la caja. Nos dice qué tipo de caja es y cómo está asegurada. Por lo general, está escrito en un formato llamado JSON, que es simplemente una forma de organizar información con llaves { } y dos puntos :.

La carga útil es como el mensaje o la información real que deseas enviar. Puede ser tu nombre, edad u otros datos que deseas compartir. También está escrito en formato JSON, por lo que es fácil de entender y trabajar.

Ahora, la firma es lo que hace que el JWT sea seguro. Es como un sello especial que solo el remitente sabe cómo crear. La firma se crea utilizando un código secreto, como una contraseña. Esta firma asegura que nadie pueda manipular el contenido del JWT sin que el remitente lo sepa.

Cuando deseas enviar el JWT a un servidor, colocas el encabezado, la carga útil y la firma dentro de la caja. Luego lo envías al servidor. El servidor puede leer fácilmente el encabezado y la carga útil para comprender quién eres y qué deseas hacer.

### ¿Cómo funciona Google Authenticator (u otros tipos de autenticadores de 2 factores)?

Google Authenticator se utiliza comúnmente para iniciar sesión en nuestras cuentas cuando se habilita la autenticación de 2 factores. ¿Cómo garantiza la seguridad?

Google Authenticator es un autenticador basado en software que implementa un servicio de verificación en dos pasos. El diagrama a continuación proporciona detalles.

<p>
  <img src="../../images/google_authenticate.jpeg" />
</p>

Hay dos etapas involucradas:

- Etapa 1: El usuario habilita la verificación en dos pasos de Google.
- Etapa 2: El usuario utiliza el autenticador para iniciar sesión, etc.

Veamos estas etapas.

**Etapa 1**

Pasos 1 y 2: Bob abre la página web para habilitar la verificación en dos pasos. El frontend solicita una clave secreta. El servicio de autenticación genera la clave secreta para Bob y la almacena en la base de datos.

Paso 3: El servicio de autenticación devuelve una URI al frontend. La URI está compuesta por un emisor de clave, un nombre de usuario y una clave secreta. La URI se muestra en forma de un código QR en la página web.

Paso 4: Luego, Bob utiliza Google Authenticator para escanear el código QR generado. La clave secreta se almacena en el autenticador.

**Etapa 2**

Pasos 1 y 2: Bob desea iniciar sesión en un sitio web con la verificación en dos pasos de Google. Para esto, necesita la contraseña. Cada 30 segundos, Google Authenticator genera una contraseña de 6 dígitos utilizando el algoritmo TOTP (One Time Password basado en el tiempo). Bob utiliza la contraseña para ingresar al sitio web.

Pasos 3 y 4: El frontend envía la contraseña que Bob ingresa al backend para la autenticación. El servicio de autenticación lee la clave secreta de la base de datos y genera una contraseña de 6 dígitos utilizando el mismo algoritmo TOTP que el cliente.

Paso 5: El servicio de autenticación compara las dos contraseñas generadas por el cliente y el servidor, y devuelve el resultado de la comparación al frontend. Bob solo puede continuar con el proceso de inicio de sesión si las dos contraseñas coinciden.

¿Es segur0 este mecanismo de autenticación?

- ¿Puede la clave secreta ser obtenida por otros?

    Necesitamos asegurarnos de que la clave secreta se transmita utilizando HTTPS. El cliente del autenticador y la base de datos almacenan la clave secreta, y debemos asegurarnos de que las claves secretas estén cifradas.

- ¿Puede adivinarse la contraseña de 6 dígitos por parte de hackers?

    No. La contraseña tiene 6 dígitos, por lo que la contraseña generada tiene 1 millón de combinaciones potenciales. Además, la contraseña cambia cada 30 segundos. Si los hackers quieren adivinar la contraseña en 30 segundos, deben ingresar 30,000 combinaciones por segundo.

## Casos de Estudio del Mundo Real

### La Pila Tecnológica de Netflix

Esta publicación se basa en la investigación de muchas entradas de ingeniería de Netflix y proyectos de código abierto. Si encuentras alguna inexactitud, no dudes en informarnos.

<p>
  <img src="../../images/netflix tech stack.png" style="width: 680px" />
</p>

**Móvil y web**: Netflix ha adoptado Swift y Kotlin para construir aplicaciones móviles nativas. Para su aplicación web, utiliza React.

**Comunicación frontend/servidor**: Netflix utiliza GraphQL.

**Servicios backend**: Netflix se basa en ZUUL, Eureka, el marco Spring Boot y otras tecnologías.

**Bases de datos**: Netflix utiliza EV cache, Cassandra, CockroachDB y otras bases de datos.

**Mensajería/transmisión**: Netflix emplea Apache Kafka y Flink para fines de mensajería y transmisión.

**Almacenamiento de video**: Netflix utiliza S3 y Open Connect para el almacenamiento de video.

**Procesamiento de datos**: Netflix utiliza Flink y Spark para el procesamiento de datos, que luego se visualiza con Tableau. Se utiliza Redshift para procesar información de almacén de datos estructurados.

**CI/CD**: Netflix utiliza varias herramientas como JIRA, Confluence, PagerDuty, Jenkins, Gradle, Chaos Monkey, Spinnaker, Atlas y más para procesos de CI/CD.

### Arquitectura de Twitter 2022

Sí, esta es la verdadera arquitectura de Twitter. Es publicada por Elon Musk y redibujada por nosotros para una mejor legibilidad.

<p>
  <img src="../../images/twitter-arch.jpeg" />
</p>

### Evolución de la arquitectura de microservicios de Airbnb en los últimos 15 años

La arquitectura de microservicios de Airbnb pasó por 3 etapas principales.

<p>
  <img src="../../images/airbnb_arch.jpeg" />
</p>

Monolito (2008 - 2017)

Airbnb comenzó como un mercado simple para anfitriones e invitados. Esto se construyó en una aplicación Ruby on Rails: el monolito.

¿Cuál es el desafío?

- Propiedad del equipo confusa + código sin dueño
- Implementación lenta

Microservicios (2017 - 2020)

Los microservicios apuntan a resolver esos desafíos. En la arquitectura de microservicios, los servicios clave incluyen:

- Servicio de obtención de datos
- Servicio de datos de lógica empresarial
- Servicio de flujo de trabajo de escritura
- Servicio de agregación de UI
- Cada servicio tenía un equipo propio

¿Cuál es el desafío?

Cientos de servicios y dependencias eran difíciles de gestionar para los humanos.

Micro + macroservicios (2020 - presente)

Esto es en lo que Airbnb está trabajando actualmente. El modelo híbrido de micro y macroservicios se centra en la unificación de APIs.

### Monorepo vs. Microrepo.

¿Cuál es el mejor? ¿Por qué diferentes empresas eligen diferentes opciones?

<p>
  <img src="../../images/monorepo-microrepo.jpg" />
</p>

Monorepo no es nuevo; Linux y Windows fueron creados utilizando Monorepo. Para mejorar la escalabilidad y la velocidad de compilación, Google desarrolló su herramienta interna dedicada para escalar más rápido y estándares estrictos de calidad de código para mantenerlo consistente.

Amazon y Netflix son grandes defensores de la filosofía de Microservicios. Este enfoque separa naturalmente el código del servicio en repositorios separados. Escala más rápido pero puede llevar a problemas de gobierno más adelante.

Dentro de Monorepo, cada servicio es una carpeta, y cada carpeta tiene una configuración BUILD y un control de permisos de PROPIETARIOS. Cada miembro del servicio es responsable de su propia carpeta.

Por otro lado, en Microrepo, cada servicio es responsable de su repositorio, con la configuración de compilación y permisos generalmente establecidos para todo el repositorio.

En Monorepo, las dependencias se comparten en todo el código, independientemente de tu negocio, por lo que cuando hay una actualización de versión, cada código actualiza su versión.

En Microrepo, las dependencias se controlan dentro de cada repositorio. Las empresas eligen cuándo actualizar sus versiones según sus propios horarios.

Monorepo tiene un estándar para los envíos. El proceso de revisión de código de Google es conocido por establecer un alto estándar, asegurando un estándar de calidad coherente para Monorepo, independientemente del negocio.

Microrepo puede establecer su propio estándar o adoptar un estándar compartido incorporando las mejores prácticas. Puede escalar más rápido para los negocios, pero la calidad del código podría ser un poco diferente.

Los ingenieros de Google construyeron Bazel, y Meta construyó Buck. Hay otras herramientas de código abierto disponibles, incluyendo Nix, Lerna y otras.

A lo largo de los años, Microrepo ha tenido más herramientas compatibles, incluyendo Maven y Gradle para Java, NPM para NodeJS y CMake para C/C++, entre otras.

### ¿Cómo diseñarías el sitio web de Stack Overflow?

Si tu respuesta es servidores locales y monolito (en la parte inferior de la siguiente imagen), es probable que no pases la entrevista, ¡pero así es como se construye en realidad!

<p>
  <img src="../../images/stackoverflow.jpg" />
</p>

**Lo que la gente piensa que debería parecer**

Es probable que el entrevistador espere algo similar a la parte superior de la imagen.

- Se utiliza el microservicio para descomponer el sistema en componentes pequeños.
- Cada servicio tiene su propia base de datos. Usa mucho la caché.
- El servicio se divide.
- Los servicios se comunican entre sí de manera asincrónica a través de colas de mensajes.
- El servicio se implementa utilizando Event Sourcing con CQRS.
- Muestra conocimientos en sistemas distribuidos como consistencia eventual, teorema CAP, etc.

**Lo que realmente es**

Stack Overflow atiende todo el tráfico con solo 9 servidores web locales, ¡y está en un monolito! Tiene sus propios servidores y no se ejecuta en la nube.

Esto va en contra de todas nuestras creencias populares en estos días.

### ¿Por qué Amazon Prime Video cambió de monitoreo sin servidor a monolítico? ¿Cómo puede ahorrar un 90% de costos?

El diagrama a continuación muestra la comparación de arquitectura antes y después de la migración.

<p>
  <img src="../../images/serverless-to-monolithic.jpeg" />
</p>

¿Qué es el Servicio de Monitoreo de Amazon Prime Video?

El servicio Prime Video necesita monitorear la calidad de miles de transmisiones en vivo. La herramienta de monitoreo analiza automáticamente las transmisiones en tiempo real e identifica problemas de calidad como corrupción de bloques, congelación de video y problemas de sincronización. Este es un proceso importante para la satisfacción del cliente.

Hay 3 pasos: convertidor de medios, detector de defectos y notificación en tiempo real.

- ¿Cuál es el problema con la arquitectura anterior?

  La arquitectura anterior se basaba en Amazon Lambda, que era buena para construir servicios rápidamente. Sin embargo, no era rentable cuando se ejecutaba la arquitectura a gran escala. Las dos operaciones más costosas son:

1. El flujo de orquestación: AWS Step Functions cobra a los usuarios por las transiciones de estado y la orquestación realiza múltiples transiciones de estado cada segundo.

2. Paso de datos entre componentes distribuidos: los datos intermedios se almacenan en Amazon S3 para que la siguiente etapa pueda descargarlos. La descarga puede ser costosa cuando el volumen es alto.

- La arquitectura monolítica ahorra un 90% de costos

  Una arquitectura monolítica está diseñada para abordar los problemas de costos. Todavía hay 3 componentes, pero el convertidor de medios y el detector de defectos se implementan en el mismo proceso, lo que ahorra el costo de pasar datos a través de la red. Sorprendentemente, este enfoque para el cambio de arquitectura de implementación condujo a un ahorro del 90% en los costos.

Este es un caso de estudio interesante y único porque los microservicios se han convertido en una elección común y de moda en la industria tecnológica. Es bueno ver que estamos teniendo más discusiones sobre la evolución de la arquitectura y discusiones más honestas sobre sus pros y contras. La descomposición de componentes en microservicios distribuidos tiene un costo.

- ¿Qué dijeron los líderes de Amazon al respecto?

  CTO de Amazon, Werner Vogels: "Construir sistemas de software **evolucionables** es una estrategia, no una religión. Y revisitar tu arquitectura con una mente abierta es un must."

Ex VP de Sostenibilidad de Amazon, Adrian Cockcroft: "El equipo de Prime Video había seguido un camino que yo llamo **Serverless First**... No defiendo **Solo Serverless**".

### ¿Cómo captura Disney Hotstar 5 mil millones de emojis durante un torneo?

<p>
  <img src="../../images/hotstar_emojis.jpeg" style="width: 720px" />
</p>

1. Los clientes envían emojis a través de solicitudes HTTP estándar. Puedes pensar en el servicio Golang como un servidor web típico. Se eligió Golang porque admite bien la concurrencia. Los hilos en Golang son livianos.

2. Dado que el volumen de escritura es muy alto, se utiliza Kafka (cola de mensajes) como búfer.

3. Los datos de emoji se agregan mediante un servicio de procesamiento en tiempo real llamado Spark. Agrega datos cada 2 segundos, lo que es configurable. Hay un compromiso basado en el intervalo. Un intervalo más corto significa que los emojis se entregan a otros clientes más rápido, pero también significa que se necesitan más recursos informáticos.

4. Los datos agregados se escriben en otro Kafka.

5. Los consumidores de PubSub extraen datos de emoji agregados de Kafka.

6. Los emojis se entregan a otros clientes en tiempo real a través de la infraestructura de PubSub. La infraestructura de PubSub es interesante. Hotstar consideró los siguientes protocolos: Socketio, NATS, MQTT y gRPC, y se decantó por MQTT.

Un diseño similar es adoptado por LinkedIn, que transmite un millón de "me gusta" por segundo.

### ¿Cómo almacena Discord billones de mensajes?

El diagrama a continuación muestra la evolución del almacenamiento de mensajes en Discord:

<p>
  <img src="../../images/discord-store-messages.jpg" />
</p>

MongoDB ➡️ Cassandra ➡️ ScyllaDB

En 2015, se construyó la primera versión de Discord en una réplica única de MongoDB. Alrededor de noviembre de 2015, MongoDB almacenaba 100 millones de mensajes y la RAM ya no podía contener los datos ni los índices. La latencia se volvió impredecible. La necesidad de almacenamiento de mensajes debía trasladarse a otra base de datos. Se eligió Cassandra.

En 2017, Discord tenía 12 nodos de Cassandra y almacenaba miles de millones de mensajes.

A principios de 2022, tenía 177 nodos con billones de mensajes. En este punto, la latencia era impredecible y las operaciones de mantenimiento se volvieron demasiado costosas de ejecutar.

Hay varias razones para el problema:

- Cassandra utiliza el árbol LSM para la estructura de datos internos. Las lecturas son más costosas que las escrituras. Puede haber muchas lecturas concurrentes en un servidor con cientos de usuarios, lo que provoca puntos calientes.
- Mantener clústeres, como la compactación de SSTables, afecta el rendimiento.
- Las pausas de recolección de basura causarían picos significativos de latencia.

ScyllaDB es una base de datos compatible con Cassandra escrita en C++. Discord rediseñó su arquitectura para tener una API monolítica, un servicio de datos escrito en Rust y almacenamiento basado en ScyllaDB.

La latencia de lectura p99 en ScyllaDB es de 15 ms en comparación con 40-125 ms en Cassandra. La latencia de escritura p99 es de 5 ms en comparación con 5-70 ms en Cassandra.

### ¿Cómo funcionan las transmisiones de video en vivo en YouTube, TikTok en vivo o Twitch?

La transmisión en vivo difiere de la transmisión regular porque el contenido de video se envía a través de Internet en tiempo real, generalmente con una latencia de solo unos segundos.

El diagrama a continuación explica lo que sucede detrás de escena para hacer esto posible.

<p>
  <img src="../../images/live_streaming_updated.jpg" style="width: 640px" />
</p>

Paso 1: Los datos de video en bruto son capturados por un micrófono y una cámara. Los datos se envían al lado del servidor.

Paso 2: Los datos de video se comprimen y codifican. Por ejemplo, el algoritmo de compresión separa el fondo y otros elementos de video. Después de la compresión, el video se codifica en estándares como H.264. El tamaño de los datos de video es mucho más pequeño después de este paso.

Paso 3: Los datos codificados se dividen en segmentos más pequeños, generalmente de segundos de duración, para que se tarde mucho menos en descargar o transmitir.

Paso 4: Los datos segmentados se envían al servidor de transmisión. El servidor de transmisión debe admitir diferentes dispositivos y condiciones de red. Esto se llama "Transmisión de tasa de bits adaptable". Esto significa que debemos producir múltiples archivos a diferentes tasas de bits en los pasos 2 y 3.

Paso 5: Los datos de transmisión en vivo se envían a servidores en el borde admitidos por la CDN (Red de Entrega de Contenido). Millones de espectadores pueden ver el video desde un servidor en el borde cercano. La CDN reduce significativamente la latencia de transmisión de datos.

Paso 6: Los dispositivos de los espectadores descodifican y descomprimen los datos de video y reproducen el video en un reproductor de video.

Pasos 7 y 8: Si el video necesita almacenarse para la reproducción, los datos codificados se envían a un servidor de almacenamiento, y los espectadores pueden solicitar una reproducción más tarde.

Los protocolos estándar para la transmisión en vivo incluyen:

- RTMP (Protocolo de Mensajería en Tiempo Real): originalmente desarrollado por Macromedia para transmitir datos entre un reproductor Flash y un servidor. Ahora se utiliza para transmitir datos de video por Internet. Ten en cuenta que las aplicaciones de videoconferencia como Skype utilizan el protocolo RTC (Comunicación en Tiempo Real) para menor latencia.
- HLS (Transmisión en Vivo a través de HTTP): requiere la codificación H.264 o H.265. Los dispositivos de Apple aceptan solo el formato HLS.
- DASH (Transmisión Adaptativa Dinámica a través de HTTP): DASH no es compatible con los dispositivos de Apple.
- Tanto HLS como DASH admiten la transmisión de tasa de bits adaptable.

## Licencia

<p xmlns:cc="http://creativecommons.org/ns#">Este trabajo está bajo una <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">licencia CC BY-NC-ND 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1"></a></p>
