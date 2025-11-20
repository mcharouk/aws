# Project Structure

## Organization

The repository is organized into two main course tracks with module-based structure:

### Architecting on AWS (Main Course)
- **Module_2 through Module_13**: Core AWS architecture modules
- Each module focuses on specific AWS service categories or architectural patterns

### Technical Essentials
- **TechEssentials/**: Foundational AWS course materials
- Simplified versions of concepts covered in the main course

## Module Structure

Each module typically contains:
- **README.md / README_DEMO.md**: Demo instructions and step-by-step guides
- **Subdirectories**: Service-specific demonstrations (e.g., `DynamoDB/`, `VPCPeering/`)
- **CDK projects**: Infrastructure as code implementations with standard structure
- **cleanResources.py**: Module-specific cleanup scripts

### Standard CDK Project Layout
```
Module_X/ServiceName/
├── cdk/
│   ├── app.py              # CDK app entry point
│   ├── cdk.json            # CDK configuration
│   ├── config.yml          # Custom configuration
│   ├── requirements.txt    # Python dependencies
│   ├── cdk/
│   │   ├── __init__.py
│   │   ├── cdk_stack.py    # Stack definitions
│   │   └── StackConfig.py  # Configuration classes
│   ├── Lambda/             # Lambda function code
│   └── tests/              # Unit tests
├── README.md               # Demo documentation
└── data/                   # Sample data files
```

## Root-Level Files

- **AIA-synopsis.md**: Detailed course synopsis with module breakdowns, analogies, and teaching notes
- **AIA-Labs.md, AIA-services-infos.md, AIA-userStories.md**: Supporting course materials
- **Links.md, Images.md**: Reference materials
- **Labs-Webapp.md**: Web application lab instructions
- **cleanAllResources.py**: Global cleanup script for all AWS resources across regions
- **requirements.txt**: Root-level Python dependencies
- ***.drawio**: Architecture diagrams and whiteboards
- **S3Assets/**: Static assets for S3 demonstrations

## Naming Conventions

- **Module folders**: `Module_X` where X is the module number
- **README files**: 
  - `README.md` for general documentation
  - `README_DEMO.md` or `README2.md` for demo-specific instructions
- **Python scripts**: Snake_case (e.g., `cleanAllResources.py`, `upload_files.py`)
- **PowerShell scripts**: camelCase with `.ps1` extension
- **CDK stacks**: PascalCase (e.g., `CdkStack`, `LambdaDynamoStack`)

## Documentation Language

- Primary documentation is in **French** (synopsis, teaching notes)
- Technical documentation and code comments are in **English**
- README files mix both languages depending on context

## Key Directories by Module

- **Module_2**: IAM and Permission Boundaries
- **Module_3**: VPC Security
- **Module_4**: DynamoDB and Lambda compute demos
- **Module_5**: S3 storage with access points and data samples
- **Module_7**: Auto Scaling Groups
- **Module_8**: CodeWhisperer automation
- **Module_9**: Fargate container demos
- **Module_10**: Advanced networking (Transit Gateway, VPC Endpoints, VPC Peering)
- **Module_11**: Serverless (API Gateway, Step Functions)
- **Module_13**: Backup and disaster recovery

## Special Considerations

- **Virtual environments**: Each CDK project has its own `.venv` directory (excluded from git)
- **CDK output**: `cdk.out/` directories contain synthesized CloudFormation templates
- **Data files**: Sample data stored in `data/`, `DataSamples/`, or `Sample-data/` subdirectories
- **Cleanup scripts**: Present at both root and module levels for resource management
