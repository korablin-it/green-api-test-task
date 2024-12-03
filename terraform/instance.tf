resource "google_compute_instance" "greenapi" {
  name         = "green-api"
  machine_type = var.machine_type
  zone         = var.zone
  tags         = ["web", "terraform"]

  boot_disk {
    initialize_params {
      image = var.image
      size  = var.disk_size
      type  = var.disk_type
    }
  }

  network_interface {
    network       = var.network_name
    access_config {
    }
  }

  metadata_startup_script = <<-EOT
    #!/bin/bash
    set -e  

    apt update

    apt install -y docker.io

    apt install -y docker-compose

    mkdir -p /opt/app

    useradd -m -s /bin/bash ansible

    mkdir -p /home/ansible/.ssh
    echo "${file("${path.module}/id_rsa.pub")}" > /home/ansible/.ssh/authorized_keys
    chown -R ansible:ansible /home/ansible/.ssh
    chmod 700 /home/ansible/.ssh
    chmod 600 /home/ansible/.ssh/authorized_keys
    echo 'ansible ALL=(ALL) NOPASSWD: ALL' | tee -a /etc/sudoers > /dev/null
    usermod -aG docker ansible
  EOT
}

