import boto3
from datetime import datetime, timezone

iam = boto3.client("iam")

response = iam.list_users()

print("IAM SECURITY AUDIT REPORT")
print("-------------------------")

for user in response["Users"]:
    username = user["UserName"]

    print(f"\nUser: {username}")

    # Console Access Check
    try:
        iam.get_login_profile(UserName=username)
        print("Console Access: YES")
    except iam.exceptions.NoSuchEntityException:
        print("Console Access: NO")

    # MFA Check
    mfa_devices = iam.list_mfa_devices(UserName=username)
    mfa_enabled = len(mfa_devices["MFADevices"]) > 0

    if mfa_enabled:
        print("MFA: ENABLED")
    else:
        print("MFA: DISABLED")
        print("RISK: User has no MFA")

    # Access Key Check
    access_keys = iam.list_access_keys(UserName=username)
    key_count = len(access_keys["AccessKeyMetadata"])

    print(f"Access Keys: {key_count}")

    if key_count > 0:
        print("RISK: User has active access keys")

    # Access Key Age Check
    for key in access_keys["AccessKeyMetadata"]:
        create_date = key["CreateDate"]

        age_days = (datetime.now(timezone.utc) - create_date).days

        print(f"Access Key Age: {age_days} days")

        if age_days > 90:
            print("RISK: Access key older than 90 days")
