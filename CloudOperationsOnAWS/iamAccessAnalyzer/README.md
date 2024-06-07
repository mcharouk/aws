Analyze identity policy

```
aws accessanalyzer validate-policy --policy-type IDENTITY_POLICY --policy-document file://identity-policy.json
```

Analyze scp

```
aws accessanalyzer validate-policy --policy-type SERVICE_CONTROL_POLICY --policy-document file://scp.json
```
