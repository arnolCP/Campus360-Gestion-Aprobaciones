from app.services.sla_strategy import TramiteRegularStrategy

def test_tramite_regular_obtener_prioridad_devuelve_normal():
    estrategia = TramiteRegularStrategy()
    
    prioridad = estrategia.obtener_prioridad()
    
    assert prioridad == "NORMAL"