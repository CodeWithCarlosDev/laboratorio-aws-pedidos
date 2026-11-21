import json


def lambda_handler(event, context):
    print("=== INICIO validate-order ===")
    print("Evento recibido:")
    print(json.dumps(event))

    cliente = event.get("detail", {}).get("cliente")
    producto = event.get("detail", {}).get("producto")
    cantidad = event.get("detail", {}).get("cantidad", 0)
    total = event.get("detail", {}).get("total", 0)

    is_valid = all([
        cliente is not None and cliente != "",
        producto is not None and producto != "",
        cantidad > 0,
        total > 0
    ])

    result = event.get("detail", {}).copy()
    result["validationStatus"] = "VALID" if is_valid else "INVALID"

    print("Resultado de validación:")
    print(json.dumps(result))
    print("=== FIN validate-order ===")

    return result
