# set AppConfigAlarm cloudwatch alarm state to Alarm
import boto3


def set_alarm_state(alarm_name, state, stateReason):
    client = boto3.client("cloudwatch")
    response = client.set_alarm_state(
        AlarmName=alarm_name, StateValue=state, StateReason=stateReason
    )
    return response


set_alarm_state("AppConfigAlarm", "ALARM", "testing appconfig rollback")
