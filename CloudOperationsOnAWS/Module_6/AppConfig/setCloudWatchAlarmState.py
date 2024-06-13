# set AppConfigAlarm cloudwatch alarm state to Alarm
import boto3


def set_alarm_state(alarm_name, state, stateReason):
    client = boto3.client("cloudwatch")
    response = client.set_alarm_state(
        AlarmName=alarm_name, StateValue=state, StateReason=stateReason
    )
    return response


alarm_status = "ALARM"
# alarm_status = "OK"
alarm_name = "AppConfigAlarm"

set_alarm_state(alarm_name, alarm_status, "testing appconfig rollback")
print(
    "alarm status updated to [{0}] for alarm name [{1}]".format(
        alarm_status, alarm_name
    )
)
