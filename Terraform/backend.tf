terraform {
  backend "s3" {
    bucket = "marc-charouk-tfstate"
    key    = "state/terraform.tfstate"
    region = var.region
  }
}
