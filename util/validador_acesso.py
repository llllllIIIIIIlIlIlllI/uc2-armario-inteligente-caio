from zoneinfo import ZoneInfo
from datetime import datetime
from datetime import time
colaboradores = {
    "123": {
        "nome_completo": "Joazin",
        "tipo_cargo": "Docente",
        "ativo": True,
        "admin": False,
        "nm_chaves_em_uso": 0,
        "bypass_horario": False,
        "id_cracha": 123
    },

    "124": {
        "nome_completo": "Porteiro da Silva",
        "tipo_cargo": "Porteiro",
        "ativo": True,
        "admin": False,
        "nm_chaves_em_uso": 0,
        "bypass_horario": True,
        "id_cracha": 124
    }
}


agora_local = datetime.now(ZoneInfo("America/Sao_Paulo"))
docente_ativo = True
hora_Atual = agora_local.time()
hora_PROIBIDA = time(23, 00, 00)
hora_PROIBIDAFIM = time(5, 00, 00)


def validar_acesso(id_cracha: int):
    
    for dicionario in colaboradores:
        for dados_usuario in colaboradores.values():
            if dados_usuario["id_cracha"] == id_cracha:
                usuarios = dados_usuario
                break
        if usuarios is None:
            print("Usuario não encontrado.")
            break

    if usuarios is None:
        print("Usuario não encontrado.")
        return

    if usuarios.get("ativo") == False:
        print("Usuario inativo, não pode pegar chave.")
        return

    if usuarios.get("bypass_horario") == True:
        print("Usuario com bypass de horário, pode pegar a qualquer hora.")
        return
    else:
        print("Usuario sem bypass de horário")


    if (hora_Atual >= hora_PROIBIDA or hora_Atual <= hora_PROIBIDAFIM) and docente_ativo:
        print("Erro")
        print(hora_Atual)
    else:
        print("Deu bom paezão")