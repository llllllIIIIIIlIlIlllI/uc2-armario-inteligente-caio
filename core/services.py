from .models import *
from django.utils import timezone
from datetime import date, datetime

class ValidadorReservaService:

    @classmethod
    def validar_direito_entrada(
        cls,
        espaco: Espaco,
        usuario: Usuario,
        dt_referencia: date = None,
        hr_referencia: datetime.time = None
    ) -> Tuple[bool, str]: