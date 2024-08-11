# L2JFrozen Custom Server

Bienvenido a **L2JFrozen Custom Server**, una versión personalizada y optimizada del servidor Lineage II basada en el pack L2JFrozen. Este documento proporciona una descripción general de todas las características, mejoras, balanceos y optimizaciones que se han realizado para ofrecer una experiencia de juego equilibrada y dinámica.

## Características del Servidor

### Rates del Servidor
- **Rate XP**: x5
- **Rate SP**: x5
- **Rate Party XP**: x5
- **Rate Party SP**: x5
- **Rate Drop Adena**: x5
- **Rate Drop Items**: x5
- **Rate Drop Spoil**: x5
- **Rate Drop Quest**: x5
- **Rate Drop SealStones**: x5
- **Rate Drop Herbs**:
  - **Herb of Power, Magic, Atk. Spd., Casting Spd., Critical Attack, Speed**: x15
  - **Herb of Life, Mana**: x10
  - **Greater Herb of Life, Mana**: x4
  - **Superior Herb of Life, Mana**: x0.8
  - **Herb of Warrior, Mystic, Recovery**: x0.2
- **Rates de Bosses**:
  - **Grand Boss**: x1
  - **Raid Boss**: x1
  - **Raid Minions**: x1

### Optimización y Balanceo

#### Balanceo de Clases y Combate
- **Configuración de Daños por Clase**: Habilitado para ajustar y balancear los daños infligidos por las diferentes clases en el juego, tanto en el entorno normal como en Olympiad.
- **Probabilidad de Golpe de Habilidades Blow y Backstab**: Ajustada para mejorar el equilibrio en el combate:
  - **Blow Attack**:
    - Frontal: 50%
    - Lateral: 60%
    - Trasero: 70%
  - **Backstab**:
    - Frontal: 3%
    - Lateral: 50%
    - Trasero: 90%
- **Velocidades Máximas de Ataque**:
  - **Convencional**: 1500
  - **Mágico**: 1999
- **Límite de Crítico**:
  - **Físico**: 500 (10% de probabilidad máxima)
  - **Mágico**: 300 (10% de probabilidad máxima)
- **Multiplicadores de Daño**:
  - **Mages**: Físico y Mágico ajustado a x1.0 para equilibrio.
  - **Fighters**: Físico y Mágico ajustado a x1.0 para equilibrio.
  - **Mascotas e Invocaciones**: Físico y Mágico ajustado a x1.0 para mantener un combate justo.
- **Configuración de Lethal Strike**: 
  - **Raids Protegidos contra Lethal**: Desactivado para evitar abusos en raids.
  - **Protección de Mobs contra Lethal**: Desactivado, pero algunos mobs específicos están protegidos.

#### Optimización del Sistema
- **GeoData**: Desactivada para mejorar el rendimiento general en servidores con baja concurrencia, permitiendo una experiencia de juego más fluida.
- **Pathfinding Celular**: Desactivado para reducir la carga del servidor.
- **Corrección de Z-Axis**: Activada para todos los NPCs y mobs, garantizando que aparezcan en las coordenadas correctas sin errores visuales ni de combate.
- **Configuración de la Base de Datos**:
  - **Tipo de Pool de Conexiones**: c3p0 seleccionado por su estabilidad.
  - **Número Máximo de Conexiones a la Base de Datos**: Reducido a 50 para mantener un uso eficiente de recursos.
- **Ajuste del Sistema de Almacenamiento**:
  - **Límite de Espacios en Inventario**: 
    - No-Dwarfs: 80
    - Dwarfs: 100
    - GMs: 250
  - **Límite de Espacios en Almacén**:
    - No-Dwarfs: 100
    - Dwarfs: 120 (con bono desde nivel 60)
    - Almacén de Clan: 200
    - Freight: 20
- **Regen de Raids**:
  - **Multiplicadores de Regeneración de HP/MP/CP**: x1 para mantener un desafío justo durante las batallas contra Raid Bosses.
  - **Penalización por Torre de Control Perdida durante Siege**: 45 segundos adicionales para mayor desafío estratégico.

### Configuraciones de Eventos y PvP
- **Sistema de Color PvP/PK**: Desactivado para mantener la interfaz de usuario limpia y no saturar a los jugadores con información visual innecesaria.
- **Sistema Anti-Farmeo**: Desactivado para mantener la jugabilidad fluida y sin restricciones artificiales, permitiendo un enfoque más natural en la progresión del juego.
- **Protección al Conectarse**: Configurada en 0 segundos para permitir que los jugadores entren en acción inmediatamente después de conectarse.
- **Configuración de Olympiad**:
  - **Uso de Augmentación Permitido**: Para mantener la competitividad y ofrecer más variedad en las estrategias de los jugadores.
  - **Inicio de Olympiad**: 18:00 horas (6 PM) con una duración de 6 horas para asegurar la participación máxima.
  - **Sistema de Recompensas**: Ajustado para ofrecer una cantidad justa de Gate Pass en función de la modalidad (clasificada o no clasificada).

### Configuraciones de Clan y Clan Hall
- **Límites de Clanes en Alianza**: Máximo de 3 clanes, ajustado para evitar alianzas demasiado grandes que dominen el servidor.
- **Precios de Funciones en Clan Hall**:
  - **Teletransporte**: Desde 7,000 hasta 28,000 Adena, ajustado para mantener la economía del servidor.
  - **Regeneración de HP/MP/EXP**: Ajustados para reflejar un balance adecuado entre costo y beneficio.
- **Sistema de Reputación de Clan por Raid Bosses**: Puntos de reputación ajustados para fomentar la competencia entre clanes.

### Sistema de Raid Bosses
- **Multiplicador de Poder de Raid Bosses**: x1 (Retail) para mantener el desafío original del juego.
- **Tiempo de Respawn de Raid Bosses**:
  - **Antharas**: 180 + 24 horas
  - **Valakas**: 192 + 44 horas
  - **Otros Raid Bosses**: Ajustados de acuerdo a las configuraciones originales para mantener la disponibilidad y el desafío.
- **Curación de Raid Bosses por Jugadores**: Permitida para ofrecer una capa adicional de estrategia en batallas grupales.

### Configuraciones de Enchant y Augmentación
- **Probabilidades de Enchant Personalizadas**:
  - **Scrolls Normales, Blessed y Crystal**: Desde 100% hasta 35%, ajustadas para equilibrar la progresión de los jugadores sin facilitar demasiado el proceso de enchant.
- **Augmentación**:
  - **Probabilidades de Obtener Habilidades y Glow**: Ajustadas para ofrecer un balance justo entre riesgo y recompensa.
  - **Eliminación de Efectos de Augmentación al Cambiar de Arma**: Activada para evitar abusos.

### Sistema de Red y Base de Datos
- **IP Externa e Interna Configurada para Pruebas Locales**: Ideal para desarrollo y ajustes antes de un lanzamiento público.
- **Configuraciones del Servidor de Base de Datos**:
  - **Tipo de Pool de Conexiones**: c3p0, elegido por su equilibrio entre rendimiento y estabilidad.
  - **Tiempo de Espera de Conexión Única**: 200,000 ms para evitar desconexiones prematuras en operaciones largas.

## Requisitos del Sistema
- **Java 11** o superior.
- **MySQL 5.7** o superior.
- **Conexión a Internet** para acceso de jugadores externos (opcional).

## Instalación
1. Clona este repositorio en tu servidor.
2. Configura las credenciales de la base de datos en el archivo `GameServerSettings`.
3. Configura las IPs internas y externas según tu entorno de red.
4. Ejecuta el script de base de datos para inicializar las tablas necesarias.
5. Inicia el servidor utilizando el script `startGameServer.sh`.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un `issue` o un `pull request` para discutir cualquier cambio que te gustaría hacer.

## Licencia
Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

---

© 2024 L2JFrozen Custom Server. Todos los derechos reservados.
