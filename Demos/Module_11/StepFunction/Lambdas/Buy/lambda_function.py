def lambda_handler(event, context):
    message = "Buying {order_quantity} items".format(order_quantity=event["quantity"])
    print(message)
    return {"message": message}
