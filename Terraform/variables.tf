variable "test_bucket_name" {
  type = string
  description = "name of test bucket"
}

variable "test_stack_name" {
  type = string
  description = "stack name"
}

variable "region" {
  type    = string
  default = "eu-west-3"
  description = "region in which resources will be created"
}
