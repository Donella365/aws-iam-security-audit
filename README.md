# AWS IAM Security Audit Tool

## Overview

This project is an automated AWS IAM security auditing tool built with Python and Boto3.

The tool scans AWS IAM users and identifies common security risks, including:

- Missing MFA
- Active access keys
- Access key age
- Console access status

The goal is to automate IAM security reviews and identify potential security weaknesses within AWS environments.

---

## Technologies Used

- AWS IAM
- Python
- Boto3
- AWS CLI
- Linux

---

## Security Checks

### MFA Audit

Identifies IAM users without Multi-Factor Authentication enabled.

### Console Access Audit

Determines whether a user can log into the AWS Management Console.

### Access Key Audit

Identifies users with active access keys.

### Access Key Age Audit

Calculates access key age and flags keys older than 90 days.

---

## Example Findings

User: admin-user

- Console Access: YES
- MFA: DISABLED
- Active Access Key: YES
- Access Key Age: 1 Day

Risks:

- No MFA enabled
- Active access key in use

---

## Skills Demonstrated

- AWS IAM
- Cloud Security
- Identity & Access Management
- Security Auditing
- Python Automation
- AWS API Integration
- Boto3
- Linux Command Line

---

## Future Enhancements

- Export findings to CSV
- Generate HTML reports
- Add severity levels
- Email findings automatically
- Multi-account support
- AWS Organizations support
