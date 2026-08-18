from datetime import datetime, timedelta
from app.services.solicitud_factory import SolicitudFactory

def test_factory_crea_tramite_regular_con_prioridad_normal_y_sla_72h():
    
    tipo_tramite = "Rectificacion de Nota"
    solicitante = "Gustavo"
    estado_inicial_id = 1

    solicitud = SolicitudFactory.crear_solicitud(
        tipo_tramite,
        solicitante,
        estado_inicial_id
    )

    # Validar prioridad
    assert solicitud.prioridad == "NORMAL"

    # Validar SLA (aproximadamente 72h)
    ahora = datetime.now()
    diferencia = solicitud.slaObjetivo - ahora

    # Permitimos margen de error de algunos segundos
    assert timedelta(hours=71, minutes=59) < diferencia < timedelta(hours=72, minutes=1)
