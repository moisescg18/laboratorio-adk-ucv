Laboratorio UCV – Mono-agente con Google ADK

Laboratorio de Sistemas Inteligentes – Universidad César Vallejo (Ingeniería de Sistemas).

1. Descripción

Mono-agente académico construido con Google ADK y Python. El agente responde en español y usa dos herramientas (tools):

explicar_concepto(concepto): explica 8 conceptos técnicos (api, algoritmo, base de datos, variable, función, bucle, git, recursividad). Ignora mayúsculas, espacios y tildes.
calcular_promedio(numeros): calcula el promedio de una lista de números.

Ambas tools validan la entrada y devuelven un diccionario con status.

2. Tecnologías
Tecnología	Propósito
Python 3.11+	Lenguaje principal
Google ADK	Framework de agentes IA
Poetry	Gestión de dependencias
pytest / pytest-cov	Pruebas y cobertura
GitHub Actions	Integración continua
SonarCloud	Calidad y análisis estático
3. Estructura del proyecto
text
laboratorio-adk-ucv/
├── agente_ucv/
│   ├── __init__.py
│   └── agent.py
├── tests/
│   └── test_agent.py
├── .github/workflows/ci.yml
├── sonar-project.properties
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── README.md
4. Instalación
bash
git clone https://github.com/moisescg18/laboratorio-adk-ucv.git
cd laboratorio-adk-ucv
poetry install
5. Configuración

Crear un archivo .env en la raíz (no se sube a GitHub) con tu clave de Google AI Studio:

env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=TU_API_KEY
6. Ejecución

En terminal:

bash
poetry run adk run agente_ucv

En interfaz web (abrir http://localhost:8000 y seleccionar agente_ucv):

bash
poetry run adk web --port 8000

Ejemplos de preguntas: ¿Qué es la recursividad? y Calcula el promedio de 14, 16 y 18.

7. Pruebas
bash
poetry run pytest --cov=agente_ucv --cov-report=term-missing

Resultado: 7 pruebas aprobadas y 100 % de cobertura.

8. Integración continua

El workflow .github/workflows/ci.yml se ejecuta en cada push a main: instala Poetry y las dependencias, corre las pruebas con cobertura y envía el análisis a SonarCloud (requiere el secreto SONAR_TOKEN).

Resultado en SonarCloud: Quality Gate aprobado, 0 issues, 0.0 % de duplicación y 100 % de cobertura.

9. Reto cumplido
5 conceptos nuevos agregados (8 en total).
Nueva tool calcular_promedio().
Validación de entrada en ambas tools.
Pruebas unitarias con pytest.
Proyecto publicado en GitHub.
Pipeline de GitHub Actions exitoso.
10. Preguntas de reflexión

1. ¿Qué diferencia existe entre un chatbot y un agente? Un chatbot solo conversa y responde. Un agente además razona, decide y usa herramientas (tools) para realizar acciones, como calcular un promedio o consultar datos.

2. ¿Qué función cumple Poetry? Gestiona las dependencias y el entorno virtual del proyecto, y fija las versiones exactas en poetry.lock para que cualquiera pueda reproducir la instalación.

3. ¿Por qué GitHub Actions es importante en DevOps? Porque automatiza las pruebas y validaciones en cada cambio (integración continua), detectando errores de forma temprana y evitando subir código roto.

4. ¿Qué problemas ayuda a detectar SonarQube? Bugs, vulnerabilidades de seguridad, código duplicado, malas prácticas (code smells) y falta de cobertura de pruebas.

5. ¿Qué mejoras agregarías a este agente? Más herramientas (consulta de APIs o bases de datos), memoria de conversación, más conceptos, pruebas de las respuestas del agente y manejo de errores del modelo, como los 503 por saturación.

11. Evidencias
Captura del agente funcionando en adk web.
Repositorio público en GitHub.
Pipeline de GitHub Actions exitoso.
Análisis de SonarCloud ejecutado.
Este README.