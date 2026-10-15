from datetime import time
from datetime import datetime
from zoneinfo import ZoneInfo

agora_local = datetime.now(ZoneInfo("America/Sao_Paulo"))
docente_ativo = True
hora_Atual = agora_local.time()
hora_PROIBIDA = time(23, 00, 00)
hora_PROIBIDAFIM = time(5, 00, 00)

if (hora_Atual >= hora_PROIBIDA or hora_Atual <= hora_PROIBIDAFIM) and docente_ativo:
    print("Erro")
    print(hora_Atual)
else:
    print("Deu bom paezão")
