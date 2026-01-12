variable "allowed_instance_types" {
  description = "Allowed EC2 instance types to control costs"
  type        = list(string)
  default     = ["t3.micro", "t3.small", "t3.medium"]
}

variable "environment" {
  description = "Environment name"
  type        = string
}

resource "aws_instance" "example" {
  ami           = "ami-1234567890abcdef0"
  instance_type = var.allowed_instance_types[0]

  tags = {
    Environment = var.environment
    CostCenter  = "engineering"
  }
}
