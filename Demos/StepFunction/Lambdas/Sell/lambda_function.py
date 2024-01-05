def lambda_handler(event, context):
    message = "Selling {order_quantity} items".format(order_quantity=event["quantity"])
    print(message)
    return {"message": message}
