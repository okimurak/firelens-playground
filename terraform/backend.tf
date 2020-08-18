terraform {
  backend "s3" {
    bucket  = "firelens-playground-terraform-backend"
    region  = "ap-northeast-1"
    key     = "terraform/terraform.tfstate"
    encrypt = true
    shared_credentials_file = "~/.aws/credentials"
    profile = "yappo"
  }
}