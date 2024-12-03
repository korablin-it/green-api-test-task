provider "google" {
  credentials = file("/home/orangepi/cred.json") 
  project     = var.project_id 
  region      = var.region     
}
