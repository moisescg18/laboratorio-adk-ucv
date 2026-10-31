"""Agente académico UCV construido con Google ADK."""

import unicodedata

from google.adk.agents.llm_agent import Agent

CONCEPTOS = {
    "api": "Una API permite comunicación entre sistemas.",
    "algoritmo": "Un algoritmo es una secuencia de pasos.",
    "base de datos": "Una base de datos almacena información.",
    "variable": "Una variable guarda un valor en memoria con un nombre.",
    "funcion": "Una función es un bloque de código reutilizable.",
    "bucle": "Un bucle repite instrucciones mientras se cumpla una condición.",
    "git": "Git es un sistema que controla las versiones del código.",
    "recursividad": "La recursividad es cuando una función se llama a sí misma.",
}


def _normalizar(texto: str) -> str:
    """Pasa a minúsculas, quita espacios y elimina tildes."""
    texto = texto.lower().strip()
    descompuesto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


def explicar_concepto(concepto: str) -> dict:
    """Explica un concepto técnico básico.

    Args:
        concepto: nombre del concepto (por ejemplo, "api").

    Returns:
        Diccionario con status y explicacion.
    """
    if not isinstance(concepto, str) or not concepto.strip():
        return {"status": "error", "explicacion": "Debes ingresar un concepto válido."}

    clave = _normalizar(concepto)
    if clave in CONCEPTOS:
        return {"status": "success", "explicacion": CONCEPTOS[clave]}

    return {"status": "not_found", "explicacion": "Concepto no registrado."}


def calcular_promedio(numeros: list[float]) -> dict:
    """Calcula el promedio de una lista de números.

    Args:
        numeros: lista de números (enteros o decimales).

    Returns:
        Diccionario con status y promedio.
    """
    if not isinstance(numeros, list) or len(numeros) == 0:
        return {"status": "error", "mensaje": "Debes enviar una lista con al menos un número."}

    for n in numeros:
        if isinstance(n, bool) or not isinstance(n, (int, float)):
            return {"status": "error", "mensaje": "Todos los valores deben ser numéricos."}

    return {"status": "success", "promedio": sum(numeros) / len(numeros)}


root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    Usa la herramienta explicar_concepto para definir conceptos técnicos.
    Usa la herramienta calcular_promedio cuando te pidan un promedio.
    """,
    tools=[explicar_concepto, calcular_promedio],
)