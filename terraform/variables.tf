variable "project_id" {
  type        = string
  default     = "utopian-bonito-443516-g4"
}

variable "region" {
  type        = string
  default     = "europe-north1"
}

variable "zone" {
  type        = string
  default     = "europe-north1-a"
}

variable "network_name" {
  type        = string
  default     = "default"
}

variable "machine_type" {
  type        = string
  default     = "e2-medium"  # 2 vCPU, 2 GB RAM
}

variable "disk_type" {
  type        = string
  default     = "pd-standard"  # Стандартный HDD
}

variable "disk_size" {
  type        = number
  default     = 10
}

variable "image" {
  type        = string
  default     = "debian-11-bullseye-v20241112"  # Debian 11
}
