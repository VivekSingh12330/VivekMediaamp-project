# 🚀 DevOps Internship Challenge – Final Report

---

## 📌 VivekMediaamp-project

### DevOps Infrastructure Automation & Monitoring Using Proxmox, Terraform, Jenkins, and Prometheus

---

## 🔧 Overview

A real-world, end-to-end DevOps project simulating production-level infrastructure and application monitoring using open-source tools like **Proxmox**, **Terraform**, **Jenkins**, and **Prometheus**. This project automates infrastructure provisioning, deploys a Flask web application, schedules periodic tasks using Cron, and monitors system health and app availability.

---

## 📚 Key Themes

- **Infrastructure Automation** using Proxmox and Terraform  
- **CI/CD Pipeline** using Jenkins  
- **Application Deployment** using Flask  
- **Scheduled Monitoring** using Crontab  
- **Metrics Collection & Monitoring** using Prometheus  

---

## 🌐 Full-Stack DevOps Pipeline

> **Automated App Deployment with Proxmox, Jenkins, Crontab, and Prometheus**

- ✅ Infrastructure Provisioning (VMs & Containers)
- ✅ NAT Networking with Static IPs
- ✅ Flask Web App Deployment
- ✅ Cron-based Job Scheduling
- ✅ Jenkins CI/CD Integration
- ✅ Prometheus Metrics Collection

---

## 🛠️ Tools & Technologies

| Tool            | Purpose                                           |
|------------------|----------------------------------------------------|
| **Proxmox**       | Virtualization platform for VMs and LXC containers |
| **VMware**        | Used instead of Proxmox due to performance limits  |
| **Ubuntu Server** | OS for all infrastructure                         |
| **Terraform**     | Infrastructure-as-Code for provisioning           |
| **Jenkins**       | Continuous Integration and Delivery               |
| **Prometheus**    | Monitoring and metrics collection                 |
| **Flask**         | Web framework for the sample application          |
| **Crontab**       | Job scheduler for periodic tasks                  |

## 📁 Project Folder Structure
---
/home/ubuntu/flask_app/
├── flask_env/
│   ├── app.py
│   ├── compute.sh
│   └── requirements.txt
├── flask.log
├── compute_cron.log
└── README.md
---

## 🧱 Step 1: Proxmox Environment Setup

- Installed **Proxmox VE** on a physical host
- Used **NAT Networking** (`vmbr0`) due to lack of bridged access
- Enabled VM and Container internet access via NAT routing

---

## 🖥️ Step 2: VM & LXC Creation with Terraform

### ✅ Virtual Machine
- Ubuntu 22.04 installed
- Static IP: `10.0.0.100`
- Enabled SSH access and internet

### ✅ LXC Container
- Privileged Ubuntu container created
- Static IP: `10.0.0.101`
- Verified communication between LXC ↔ VM ↔ Proxmox host

---

## 🌐 Step 3: Networking Configuration

| Parameter        | Value            |
|------------------|------------------|
| Network Bridge    | `vmbr0`          |
| Proxmox Host IP   | NAT Gateway      |
| VM IP             | `10.0.0.100`     |
| LXC Container IP  | `10.0.0.101`     |

✅ Verified:
- VM ↔ LXC ↔ Host connectivity
- VM and LXC internet access

---

## 🧪 Step 4: Flask Application Setup

- Created a sample Flask app with `app.py` and `requirements.txt`
- Ran server on port `5000` inside the VM
- Flask app returns a JSON response at endpoint `/compute`

Sample Code:
```
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/compute')
def compute():
    return jsonify({"status": "success", "message": "Computation complete!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

## ⏰ Step 5: Automate Endpoint Hit Using Crontab
✅ Verify Cron is Installed & Active
```
sudo systemctl status cron
# If inactive
sudo systemctl start cron
sudo systemctl enable cron
```

## ✅ Install If Not Present
```
sudo apt update && sudo apt install cron -y
```

## 📝 Step 6: Create Crontab Script
Path: /home/ubuntu/flask_app/flask_env/compute.sh

```
#!/bin/bash
LOG_FILE="/var/log/compute_cron.log"
curl -X GET http://127.0.0.1:5000/compute >> $LOG_FILE 2>&1
```

# Make Executable:

```
chmod +x /home/ubuntu/flask_app/flask_env/compute.sh
```

✅ Schedule in Crontab
Open crontab:
```
crontab -e
```

Add:
```
* * * * * /home/ubuntu/flask_app/flask_env/compute.sh
```

Verify:
```
crontab -l
```

## 📄 Logs & Output
Check response logs:

```
cat /var/log/compute_cron.log
```

Sample Output:
```
{
  "message": "Computation complete!",
  "status": "success"
}
```

## 📈 Jenkins Integration (CI/CD)
Installed Jenkins on Ubuntu VM

Installed plugins:

Git

Pipeline

Docker

Configured a basic pipeline for Flask app (initial stage only)

🔴 Note: Jenkinsfile not fully completed due to time and environment limitations.

## 📊 Monitoring with Prometheus
Installed Prometheus on LXC container

Configured Flask VM IP as a target

Installed node_exporter for host metrics

✅ Real-time metrics visualized on Prometheus dashboard

## 🧪 Errors Faced & Solutions
```
Issue	Cause	Fix / Note
Jenkins service failed to start	Low resources or port conflict	Moved Jenkins to VM on VMware
Jenkins deployment failed	Incomplete Jenkinsfile, missing Docker	Partial CI/CD implemented
Prometheus blank page	Misconfigured target	Fixed using correct port and exporter
```

## 🧹 Limitations & Future Enhancements
Jenkins deployment is partial — Docker setup and complete pipeline needed

Proxmox setup was constrained due to hardware

Application logic was minimal (for demo only)

Dashboard integration (Grafana) can be added

## ✅ What Was Accomplished
Provisioned VM and LXC using Terraform

Configured NAT-based network on Proxmox

Deployed Flask App in VM

Hit endpoint periodically via Cron

Partially built CI/CD Pipeline with Jenkins

Collected system metrics using Prometheus

🎯 Conclusion
This DevOps internship challenge simulated a real-world DevOps lifecycle using open-source tooling. Despite hardware limitations and time constraints, key principles of automation, deployment, monitoring, and observability were successfully demonstrated.

The learning outcomes included:

Understanding of Proxmox provisioning and networking

Hands-on use of Terraform, Jenkins, and Prometheus

Debugging and system administration under realistic limitations

Building a CI/CD + Monitoring workflow end-to-end

With foundational components now working, the project can be easily extended to include Docker-based deployment, Jenkinsfile-based automation, Grafana dashboards, and real-time alerts.



## 📌 End of Report






