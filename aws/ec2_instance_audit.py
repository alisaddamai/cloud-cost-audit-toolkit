import boto3
from datetime import datetime, timezone

def get_ec2_instances():
    ec2 = boto3.client("ec2")
    response = ec2.describe_instances()
    instances = []

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            launch_time = instance["LaunchTime"]
            age_days = (datetime.now(timezone.utc) - launch_time).days

            instances.append({
                "InstanceId": instance["InstanceId"],
                "InstanceType": instance["InstanceType"],
                "State": instance["State"]["Name"],
                "AgeDays": age_days
            })

    return instances


def main():
    instances = get_ec2_instances()

    print("EC2 Instance Audit Report")
    print("-------------------------")

    for inst in instances:
        print(
            f"{inst['InstanceId']} | "
            f"{inst['InstanceType']} | "
            f"{inst['State']} | "
            f"{inst['AgeDays']} days old"
        )


if __name__ == "__main__":
    main()
