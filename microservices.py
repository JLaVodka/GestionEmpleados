import os
import requests


MICROSERVICIOS = [
    os.getenv("JAVA_URL"),
    os.getenv("NODE_URL"),
    os.getenv("CSHARP_URL"),
]


def solicitar_con_respaldo(endpoint, method="GET", **kwargs):
    ultimo_error = None

    for base_url in MICROSERVICIOS:

        if not base_url:
            continue

        url = f"{base_url}{endpoint}"

        try:
            respuesta = requests.request(
                method,
                url,
                timeout=5,
                **kwargs
            )

            respuesta.raise_for_status()

            print(f"Microservicio utilizado: {base_url}")

            return respuesta

        except requests.RequestException as error:
            print(f"Falló {base_url}: {error}")
            ultimo_error = error

    if ultimo_error:
        raise ultimo_error

    raise Exception("No hay microservicios configurados")