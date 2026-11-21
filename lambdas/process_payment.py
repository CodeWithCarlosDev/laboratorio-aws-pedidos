import json


def lambda_handler(event, context):
    print("=== INICIO process-payment ===")
    print("Evento recibido:")
    print(json.dumps(event))

    total = event.get("total", 0)

    if total <= 1000:
        event["paymentStatus"] = "APPROVED"
    else:
        event["paymentStatus"] = "REJECTED"

    print("Resultado pago:")
    print(json.dumps(event))
    print("=== FIN process-payment ===")

    return event
