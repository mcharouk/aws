locals {  
  test_creator_tag = "terraform"  
}

locals {
  # Common tags to be assigned to all resources
  common_tags = {    
    Creator = local.test_creator_tag
    StackName = var.test_stack_name
  }
}