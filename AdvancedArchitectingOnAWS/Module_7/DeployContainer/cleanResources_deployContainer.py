import boto3

alb_name = "ECS-CICD-ALB"


# get listener of alb that match port 80 and protocol HTTP
alb = boto3.client("elbv2")

# get arn of alb
response = alb.describe_load_balancers(Names=[alb_name])
alb_arn = response["LoadBalancers"][0]["LoadBalancerArn"]
response = alb.describe_listeners(LoadBalancerArn=alb_arn)
for listener in response["Listeners"]:
    if listener["Port"] == 80 and listener["Protocol"] == "HTTP":
        listener_arn = listener["ListenerArn"]
        break


# get target group of listener
target_group_arn = None
response = alb.describe_rules(ListenerArn=listener_arn)
for rule in response["Rules"]:
    if rule["Priority"] == "1":
        # get rule ARN
        rule_arn = rule["RuleArn"]
        field = rule["Conditions"][0]["Field"]
        path_pattern_config = rule["Conditions"][0]["PathPatternConfig"]

        if "ForwardConfig" in rule["Actions"][0]:
            forward_config_tg = rule["Actions"][0]["ForwardConfig"]["TargetGroups"]
            if len(rule["Actions"][0]["ForwardConfig"]["TargetGroups"]) > 1:
                # get target group whose name contains Deploy-Appli
                for target_group in forward_config_tg:
                    if "Deploy-Appli" in target_group["TargetGroupArn"]:
                        target_group_arn = target_group["TargetGroupArn"]
                        break

        break

if target_group_arn is not None:
    print(f"updating alb rule {rule_arn}")
    response = alb.modify_rule(
        RuleArn=rule_arn,
        Conditions=[
            {
                "Field": field,
                "PathPatternConfig": path_pattern_config,
            }
        ],
        Actions=[
            {
                "Type": "forward",
                "ForwardConfig": {
                    "TargetGroups": [{"TargetGroupArn": target_group_arn}]
                },
            }
        ],
    )
else:
    print("nothing to change in ALB")


code_pipeline_name = "BuildAndDeployPipeline"

# remove code pipeline if it exists
code_pipeline = boto3.client("codepipeline")

try:
    code_pipeline.delete_pipeline(name=code_pipeline_name)
    print("deleted pipeline " + code_pipeline_name)
except code_pipeline.exceptions.PipelineNotFoundException:
    print("pipeline " + code_pipeline_name + " does not exist")

code_pipeline.close()

code_build_name = "PushToECR"
# remove codebuild project if it exists
code_build = boto3.client("codebuild")

try:
    code_build.delete_project(name=code_build_name)
    print("deleted codebuild project " + code_build_name)
except code_build.exceptions.ResourceNotFoundException:
    print("codebuild project " + code_build_name + " does not exist")

code_build.close()

code_pipeline_role = "AWSCodePipelineServiceRole-eu-west-3-BuildAndDeployPipeline"
# delete role if it exists

iam = boto3.client("iam")

try:
    # check role exists
    iam.get_role(RoleName=code_pipeline_role)
    # list all policies to detach them one by one
    response = iam.list_attached_role_policies(RoleName=code_pipeline_role)
    for policy in response["AttachedPolicies"]:
        iam.detach_role_policy(
            RoleName=code_pipeline_role, PolicyArn=policy["PolicyArn"]
        )
        # remove policy
        iam.delete_policy(PolicyArn=policy["PolicyArn"])
        print("deleted policy " + policy["PolicyArn"])

    iam.delete_role(RoleName=code_pipeline_role)
    print("deleted role " + code_pipeline_role)
except iam.exceptions.NoSuchEntityException:
    print("role " + code_pipeline_role + " does not exist")

iam.close()
