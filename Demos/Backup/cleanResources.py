# delete all aws backup resource assignments

import boto3

# get all backup plan names and ids
backup = boto3.client("backup")


def get_backup_plans():
    response = backup.list_backup_plans()
    return response


for plan in get_backup_plans()["BackupPlansList"]:
    selections = backup.list_backup_selections(BackupPlanId=plan["BackupPlanId"])
    for selection in selections["BackupSelectionsList"]:
        backup.delete_backup_selection(
            BackupPlanId=plan["BackupPlanId"], SelectionId=selection["SelectionId"]
        )
        print("Deleted backup selection with id " + selection["SelectionId"])

        # delete backup plan
    backup.delete_backup_plan(BackupPlanId=plan["BackupPlanId"])
    print("Deleted backup plan with id " + plan["BackupPlanId"])

# delete all backup vaults
for vault in backup.list_backup_vaults()["BackupVaultList"]:
    backup.delete_backup_vault(BackupVaultName=vault["BackupVaultName"])
    print("Deleted backup vault with name " + vault["BackupVaultName"])
