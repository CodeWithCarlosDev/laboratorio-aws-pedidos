import json


def lambda_handler(event, context):
    print("=== INICIO confirm-order ===")
    print("Evento recibido:")
    print(json.dumps(event))

    event["orderStatus"] = "CONFIRMED"

    print("Pedido confirmado:")
    print(json.dumps(event))
    print("=== FIN confirm-order ===")

    return event
