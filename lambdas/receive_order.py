import json
import boto3
import uuid
from datetime import datetime

eventbridge = boto3.client('events')


def lambda_handler(event, context):
    print("=== INICIO receive-order ===")
    print("Evento recibido desde API Gateway:")
    print(json.dumps(event))

    try:
        body = json.loads(event.get('body', '{}'))

        order_id = str(uuid.uuid4())

        order_detail = {
            "orderId": order_id,
            "cliente": body.get("cliente"),
            "producto": body.get("producto"),
            "cantidad": body.get("cantidad"),
            "total": body.get("total"),
            "timestamp": datetime.utcnow().isoformat()
        }

        print("Detalle del pedido a enviar a EventBridge:")
        print(json.dumps(order_detail))

        response = eventbridge.put_events(
            Entries=[
                {
                    "Source": "demo.pedidos.lc",
                    "DetailType": "NuevoPedidoLc",
                    "Detail": json.dumps(order_detail),
                    "EventBusName": "default"
                }
            ]
        )

        print("Respuesta de EventBridge:")
        print(json.dumps(response, default=str))
        print("=== FIN receive-order ===")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "mensaje": "Pedido recibido y enviado al bus de eventos",
                "orderId": order_id
            })
        }

    except Exception as e:
        print("ERROR en receive-order:")
        print(str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
