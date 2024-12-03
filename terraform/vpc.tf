resource "google_compute_firewall" "allow_http_8880" {
  name    = "allow-http-8880"
  network = var.network_name

  allow {
    protocol = "tcp"
    ports    = ["8880"]
  }

  source_ranges = ["0.0.0.0/0"]

  target_tags = ["web"] 
}
