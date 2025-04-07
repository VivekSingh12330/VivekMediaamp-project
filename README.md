# 🚀 DevOps Infrastructure Automation & Monitoring

### DevOps Internship Challenge – Final Report

## 📌 Project Title
**DevOps Infrastructure Automation & Monitoring Using Proxmox, Terraform, Jenkins, and Prometheus**

---

## 🔧 About the Project

This project simulates a real-world DevOps workflow covering:
- Infrastructure provisioning using **Proxmox** and **Terraform**
- CI/CD pipeline with **Jenkins**
- App automation and scheduled tasks via **Cron**
- Monitoring using **Prometheus**

The focus is on implementing a **full-stack DevOps solution**—from VM provisioning to observability of services.

---

## 🧰 Tools & Technologies Used

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| **Proxmox**  | Container & VM orchestration           |
| **Terraform**| Infrastructure as Code (IaC)           |
| **Ubuntu**   | OS for both VM and LXC                 |
| **Jenkins**  | CI/CD pipeline automation              |
| **Prometheus**| Monitoring & metrics collection       |
| **Crontab**  | Scheduled automation                   |
| **Flask**    | Lightweight web app framework          |
| **VMware**   | Virtualization fallback (due to hardware limits) |

---

## ⚙️ Infrastructure Overview

### 1️⃣ Proxmox Setup
- Proxmox VE installed on a local server.
- NAT configured using `vmbr0` bridge (due to hardware/network constraints).

### 2️⃣ VM & Container Provisioning (via Terraform)
- **VM**:
  - OS: Ubuntu 22.04
  - Static IP: `10.0.0.100`
  - SSH access enabled
- **LXC Container**:
  - OS: Ubuntu 22.04
  - Static IP: `10.0.0.101`
  - Privileged container for broader compatibility

### 3️⃣ Networking
- NAT networking across VM, LXC, and internet
- Verified:
  - VM ↔ LXC ↔ Proxmox ↔ Internet — ✅

---

## 🌐 Application Deployment (Flask App)

### Project Structure
```bash
flask_app/
├── app.py
├── requirements.txt
├── flask_env/
│   └── compute.sh      # Script to hit /compute endpoint
