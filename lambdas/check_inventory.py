import json


def lambda_handler(event, context):
    print("=== INICIO check-inventory ===")
    print("Evento recibido:")
    print(json.dumps(event))

    cantidad = event.get("cantidad", 0)

    if cantidad <= 5:
        event["inventoryStatus"] = "AVAILABLE"
    else:
        event["inventoryStatus"] = "OUT_OF_STOCK"

    print("Resultado inventario:")
    print(json.dumps(event))
    print("=== FIN check-inventory ===")

    return event
