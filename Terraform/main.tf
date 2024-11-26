resource "aws_s3_bucket" "my-test-bucket" {
  bucket = var.test_bucket_name
  force_destroy = true
  tags = local.common_tags  
}