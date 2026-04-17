# Detecta automaticamente o ambiente:
# ✔ Localhost
# ✔ GitHub Codespaces
# ✔ Docker
# ✔ WSL
# ✔ AWS EC2 / ECS / Elastic Beanstalk
# ✔ Railway
# ✔ Render
# ✔ Heroku

from pathlib import Path
import os
import sys

# ==========================================================
# DETECÇÃO DE AMBIENTE
# ==========================================================
def detectar_ambiente() -> str:
    """
    :param: None
    :return: str - ambiente detectado

    Detecta o ambiente de execução do Django, baseado em variáveis de ambiente e arquivos específicos de cada plataforma.
    Retorna:<br>
    <ul>
        <li><b>LOCAL</b>: ambiente local, sem indícios de estar rodando em nuvem ou container</li>
        <li><b>CODESPACE</b>: rodando no GitHub Codespaces</li>
        <li><b>RAILWAY</b>: rodando no Railway</li>
        <li><b>RENDER</b>: rodando no Render</li>
        <li><b>HEROKU</b>: rodando no Heroku</li>
        <li><b>AWS</b>: rodando em algum serviço da AWS (EC2, ECS, Elastic Beanstalk)</li>
        <li><b>DOCKER</b>: rodando dentro de um container Docker</li>
        <li><b>WSL</b>: rodando no Windows Subsystem for Linux</li>
    </ul>"""

    # ------------------------------------------------------
    # GitHub Codespaces
    # ------------------------------------------------------
    if os.getenv("CODESPACES", "").lower() == "true":
        return "CODESPACE"

    # ------------------------------------------------------
    # Railway
    # ------------------------------------------------------
    if os.getenv("RAILWAY_ENVIRONMENT"):
        return "RAILWAY"

    # ------------------------------------------------------
    # Render
    # ------------------------------------------------------
    if os.getenv("RENDER"):
        return "RENDER"

    # ------------------------------------------------------
    # Heroku
    # ------------------------------------------------------
    if os.getenv("DYNO"):
        return "HEROKU"

    # ------------------------------------------------------
    # AWS
    # ------------------------------------------------------
    if any([
        os.getenv("AWS_EXECUTION_ENV"),
        os.getenv("ECS_CONTAINER_METADATA_URI"),
        os.getenv("EC2_INSTANCE_ID"),
        os.getenv("AWS_REGION"),
    ]):
        return "AWS"

    # ------------------------------------------------------
    # Docker
    # ------------------------------------------------------
    if os.path.exists("/.dockerenv"):
        return "DOCKER"

    # ------------------------------------------------------
    # WSL
    # ------------------------------------------------------
    try:
        with open("/proc/version", "r") as f:
            if "microsoft" in f.read().lower():
                return "WSL"
    except:
        pass

    # ------------------------------------------------------
    # Padrão
    # ------------------------------------------------------
    return "LOCAL"


# ==========================================================
# PORTA
# ==========================================================
def detectar_porta() -> str:
    '''
    :param: None
    :return: str - porta detectada

    Detecta a porta de execução do Django, baseado em variáveis de ambiente e argumentos da linha de comando.
    Se nenhuma porta for detectada, retorna "8000" como padrão.
    '''
    # Cloud usa variável PORT
    if os.getenv("PORT"):
        return os.getenv("PORT")

    for arg in sys.argv:
        if ":" in arg:
            return arg.split(":")[-1]
        elif arg.isdigit():
            return arg

    return "8000"


# ==========================================================
# HOST / DOMÍNIO
# ==========================================================
def detectar_dominio() -> str:
    '''
    :param: None
    :return: str - domínio detectado

    Detecta o domínio de execução do Django, baseado no ambiente detectado.
    '''
    AMBIENTE = detectar_ambiente()
    PORTA = detectar_porta()
    if AMBIENTE == "CODESPACE":
        nome = os.getenv("CODESPACE_NAME")
        dom = os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
        return f"{nome}-{PORTA}.{dom}"

    if AMBIENTE == "HEROKU":
        return os.getenv("HEROKU_APP_NAME", "meuapp") + ".herokuapp.com"

    if AMBIENTE == "RAILWAY":
        return os.getenv("RAILWAY_STATIC_URL", "").replace("https://", "")

    if AMBIENTE == "RENDER":
        return os.getenv("RENDER_EXTERNAL_HOSTNAME")

    if AMBIENTE == "AWS":
        return os.getenv("DJANGO_DOMAIN", "meusite.com.br")

    return f"localhost:{PORTA}"


# ==========================================================
# PROTOCOLO
# ==========================================================

def detectar_protocolo() -> str:
    '''
    :param: None
    :return: str - protocolo detectado (http ou https)

    Detecta o protocolo de execução do Django, baseado no ambiente detectado.
    Ambientes em nuvem geralmente usam HTTPS, enquanto ambientes locais usam HTTP.
    '''
    AMBIENTE = detectar_ambiente()
    if AMBIENTE in [
        "CODESPACE",
        "AWS",
        "HEROKU",
        "RAILWAY",
        "RENDER",
    ]:
        return "https"

    return "http"

if __name__ == "__main__":
    print(f"Ambiente detectado: {detectar_ambiente()}")
    print(f"Domínio detectado: {detectar_dominio()}")
    print(f"Protocolo detectado: {detectar_protocolo()}")
