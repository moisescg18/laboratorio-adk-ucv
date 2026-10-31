from agente_ucv.agent import calcular_promedio, explicar_concepto


def test_explicar_concepto_existente():
    result = explicar_concepto("API")
    assert result["status"] == "success"


def test_explicar_concepto_con_tilde_y_espacios():
    result = explicar_concepto("  Función ")
    assert result["status"] == "success"


def test_explicar_concepto_no_registrado():
    assert explicar_concepto("blockchain")["status"] == "not_found"


def test_explicar_concepto_vacio():
    assert explicar_concepto("   ")["status"] == "error"


def test_calcular_promedio_correcto():
    result = calcular_promedio([10, 20, 30])
    assert result["status"] == "success"
    assert result["promedio"] == 20


def test_calcular_promedio_lista_vacia():
    assert calcular_promedio([])["status"] == "error"


def test_calcular_promedio_valores_invalidos():
    assert calcular_promedio([1, "a", 3])["status"] == "error"