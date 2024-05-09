# SCA 

* SCA = Software Composition Analysis
* Search for well known vulnerabilities in project dependencies (CVE)

# SAST

* SAST = Static Application Security Testing

# DAST

* DAST = Dynamic Application Security Testing

# Amazon inspector

## Difference with Inspector Classic

* no limit on number of images or VMs to be scanned
* Support for container
* Support for multi account mgt
* Use SSM Agent
* Continual scanning (on change, not just on schedule)
* Risk score based on CVE and other parameters like Network Reachability
* More integrations : EventBridge, pushes findings to ECR, Security Hub

## Features

* Scan EC2, Lambda, ECR containers
* SCA + SAST

# DevSecOps Tools

## AWS

SCA / SAST : 
* Inspector
* CodeGuru Reviewer

Automation:
* Config
* GuardDuty
  * CloudTrail
  * VPC
  * DNS
  * K8s
* SecurityHub
  * GuardDuty
  * Config
  * Macie
  * IAM Access Analyzer
  * Inspector
  * Firewall Manager
  * System Manager (Patch)
  * AWS Health
  * IoT Device Defender

## Others

* Checkov (Terraform)

# Gitlab CI

* projects
* jobs
* stages
  * .pre
  * .post
  * build
  * test
  * deploy
  * user-defined
* script
  * list of commands

## Jobs properties

* **include** to import a yaml file from elsewhere

* **image**
* **artifact** (can be used by multiple jobs)
* **dependencies** (on other jobs). Used for artifacts
* **needs** : used to create a DAG to run as fast as possible
* **rules**: use CI_PIPELINE_SOURCE or CI_COMMIT_BRANCH to trigger job on special events (like pull request)
* **extends** : DRY (don't repeat yourself) principle
* hidden jobs : job that start with . (DOT). not executed by GITLAB. Can be used to share some configuration (with extends keyword)
* **default** : to provide default values for some job properties
* **trigger** : to launch child pipelines
* **only** and **changes** to trigger only when files under some location have changed (in mono repo)
