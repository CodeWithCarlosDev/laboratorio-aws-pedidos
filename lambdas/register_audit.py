import json


def lambda_handler(event, context):
    print("=== INICIO register-audit ===")
    print("Evento recibido para auditoría:")
    print(json.dumps(event))

    result = {
        "mensaje": "Proceso finalizado",
        "orderId": event.get("orderId"),
        "cliente": event.get("cliente"),
        "producto": event.get("producto"),
        "cantidad": event.get("cantidad"),
        "total": event.get("total"),
        "orderStatus": event.get("orderStatus", "FAILED"),
        "inventoryStatus": event.get("inventoryStatus"),
        "paymentStatus": event.get("paymentStatus")
    }

    print("Auditoría final:")
    print(json.dumps(result))
    print("=== FIN register-audit ===")

    return result
