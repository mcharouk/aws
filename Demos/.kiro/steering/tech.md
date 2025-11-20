# Technology Stack

## Infrastructure as Code

- **AWS CDK (Cloud Development Kit)**: Primary IaC tool using Python
- **AWS CloudFormation**: Underlying deployment mechanism for CDK stacks
- CDK projects follow standard structure with `app.py`, `cdk.json`, and stack definitions in `cdk/` folders

## Languages

- **Python**: Primary language for automation scripts, Lambda functions, and CDK infrastructure
- **Bash/Shell**: Used for EC2 user data scripts and automation
- **PowerShell**: Windows-specific automation scripts (`.ps1` files)

## AWS Services

The repository demonstrates a wide range of AWS services including:
- Compute: EC2, Lambda, ECS, EKS, Fargate
- Storage: S3, EFS, EBS
- Database: DynamoDB, RDS, ElastiCache
- Networking: VPC, Transit Gateway, VPC Peering, Direct Connect
- Serverless: API Gateway, Step Functions, SQS, SNS, Kinesis
- Security: IAM, Security Groups, NACLs, WAF, Shield
- Monitoring: CloudWatch, CloudTrail
- Edge: CloudFront, Route 53
- Automation: Systems Manager, AWS Backup

## Development Tools

- **boto3**: AWS SDK for Python used in cleanup and utility scripts
- **Flask**: Web framework (version >3.0.0)
- **Draw.io**: Architecture diagrams (`.drawio` files)
- **Rancher Desktop**: Required for container demonstrations

## Common Commands

### CDK Operations
```bash
# Deploy a CDK stack
cdk deploy

# Destroy a CDK stack
cdk destroy

# Synthesize CloudFormation template
cdk synth
```

### Python Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Resource Cleanup
```bash
# Clean all AWS resources across regions
python cleanAllResources.py

# Module-specific cleanup
python cleanResources.py
```

### S3 Operations
```powershell
# Upload files to S3
.\uploadS3Files.ps1

# Remove S3 bucket
.\removeS3Bucket.ps1
```

## Configuration

- CDK configuration stored in `cdk.json` and `config.yml` files
- AWS regions primarily used: `eu-west-3` (Paris), `eu-west-1` (Ireland), `us-east-1`
- Virtual environments (`.venv`) used for Python dependency isolation
