# terminate all Provisioned Products of Service Catalog

import time

import boto3

client = boto3.client("servicecatalog")
# get all provisioned products and terminate them
response = client.scan_provisioned_products(
    AccessLevelFilter={"Key": "Role", "Value": "self"}
)

product_name = "LinuxApacheTestProductInstance"
if response["ProvisionedProducts"] == []:
    print("No provisioned products found")
else:
    for product in response["ProvisionedProducts"]:
        current_product_name = product["Name"]
        if not (current_product_name.startswith(product_name)):
            print(
                f"Product {current_product_name} does not start with {product_name}, skipping"
            )
            continue
        print("Terminating product with name" + product["Name"])
        terminate_response = client.terminate_provisioned_product(
            ProvisionedProductName=product["Name"], TerminateToken="string"
        )
        record_id = terminate_response["RecordDetail"]["RecordId"]
        # wait until it is terminated
        while True:

            response = client.describe_record(Id=record_id)
            status = response["RecordDetail"]["Status"]
            if status == "SUCCEEDED":
                break
            else:
                print(f"{product['Name']} still in status {status}")
                time.sleep(5)

        print(f"Terminated {product['Name']}")


response = client.list_portfolios(AcceptLanguage="en")

for portfolio in response["PortfolioDetails"]:
    constraints_response = client.list_constraints_for_portfolio(
        PortfolioId=portfolio["Id"]
    )
    for constraint in constraints_response["ConstraintDetails"]:
        client.delete_constraint(Id=constraint["ConstraintId"])
        print(f"Constraint {constraint['ConstraintId']} deleted")

    response = client.list_principals_for_portfolio(PortfolioId=portfolio["Id"])
    for principal in response["Principals"]:
        client.disassociate_principal_from_portfolio(
            PortfolioId=portfolio["Id"], PrincipalARN=principal["PrincipalARN"]
        )
        print(
            f"Principal {principal['PrincipalARN']} disassociated from {portfolio['DisplayName']}"
        )

    # list all tag options and disassociate them
    tag_options_response = client.list_tag_options()
    for tag_option in tag_options_response["TagOptionDetails"]:
        tag_options_portfolios = client.list_resources_for_tag_option(
            TagOptionId=tag_option["Id"],
            ResourceType="Portfolio",
        )
        for portfolio in tag_options_portfolios["ResourceDetails"]:
            client.disassociate_tag_option_from_resource(
                ResourceId=portfolio["Id"], TagOptionId=tag_option["Id"]
            )
            print(
                f"Tag option {tag_option['Id']} disassociated from {portfolio['Name']}"
            )


# list all products

response = client.search_products_as_admin(AcceptLanguage="en")
for product in response["ProductViewDetails"]:
    productViewSummary = product["ProductViewSummary"]
    response = client.list_portfolios_for_product(
        ProductId=productViewSummary["ProductId"]
    )
    for portfolios in response["PortfolioDetails"]:
        client.disassociate_product_from_portfolio(
            PortfolioId=portfolios["Id"],
            ProductId=productViewSummary["ProductId"],
        )
        print(
            f"Product {productViewSummary['Name']} disassociated from {portfolios['DisplayName']}"
        )
    client.delete_product(Id=productViewSummary["ProductId"], AcceptLanguage="en")
    print(f"Product {productViewSummary['Name']} deleted")

# delete all portfolios
response = client.list_portfolios(AcceptLanguage="en")
for portfolio in response["PortfolioDetails"]:
    client.delete_portfolio(Id=portfolio["Id"], AcceptLanguage="en")
    print(f"Portfolio {portfolio['DisplayName']} deleted")
