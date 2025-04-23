# User Module of Content Management System

<p align="center">
  <a href="./README_cn.md">English</a> |
  <a href="./README.md">简体中文</a> 
</p>

<div align="center">

  <br>
  <img src="https://github.com/umi-AIGC-saas/umi_ai_cms_user/blob/main/assets/v1.png" alt="platform multimodal">
</div>

**Experience Address**: [https://ai.umi6.com](https://ai.umi6.com)

## Preparation

### Environmental Dependencies
1. **Python Version**  
   You must use **Python 3.10** (other versions may cause compatibility issues).  
   *Verification Command*: `python --version`

2. **System Tools**  
   - Docker and Docker Compose (it is recommended that Docker ≥ 20.10 and Compose ≥ 2.0)  
   - Supervisor (for process management)  
   *Installation Example (Ubuntu)*:  
   ```bash
   # Install Docker
   curl -fsSL https://get.docker.com | sh
   # Install Docker Compose
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose
   # Install Supervisor
   sudo apt-get install supervisor
   ```

### Configuration Requirements
1. **Code Configuration Items**  
   The configuration items marked with `TODO` in the project need to be completed (such as API keys, database connections, etc.).  
   *Quick Location*: View through the `TODO` panel at the bottom left in PyCharm. Other IDEs can search for the keyword `TODO`.

2. **Port Release**  
   Ensure that the following ports are accessible (configured in the firewall/security group):  
   `28999, 28998, 28060, 28083, 28071, 8080, 29090`  
   *Note*: The duplicate listing of `28060` has been corrected to a single port.

3. **Worker Process Configuration**  
   Set the number of worker processes in the `docker-compose.yml` or `start` script (example):  
   ```yaml
   # Example of production.yml
   services:
     worker:
       command: python worker.py --workers 4  # Configure the number of worker processes to 4
   ```

### Service Preparation
1. **Opensearch Vector Database**  
   - **Solution Selection**:  
     - Cloud service (such as Alibaba Cloud OpenSearch, an instance needs to be created in advance)  
     - Local deployment (via Docker)  
   - **Local Deployment Steps**:  
     ```bash
     # Download the installation script (assuming there is an install_opensearch.yml in the project root directory)
     docker compose -f install_opensearch.yml build  # Build the image
     docker compose -f install_opensearch.yml up -d  # Run in the background
     ```
     *Verification*: Access `http://localhost:9200` to check if OpenSearch has started.

2. **Supervisor Configuration**  
   - Create a configuration file `supervisord.conf` (example path: `/etc/supervisor/supervisord.conf`)  
   - Key configuration example:  
     ```ini
     [program:umi-chat]
     command=/path/to/your/start_script.sh  # Path to the startup script
     directory=/path/to/project  # Project root directory
     autostart=true
     autorestart=true
     stdout_logfile=/var/log/umi-chat.log
     stderr_logfile=/var/log/umi-chat.err.log
     ```
   - Restart Supervisor: `sudo supervisorctl reload`

## Quick Start
```bash
# 1. Pull the project code
git clone https://github.com/ymzn3820/umi_platform_chat_module.git
cd umi_platform_chat_module  # Enter the project directory

# 2. Build the Docker image (production environment configuration)
docker compose -f production.yml build

# 3. Run the service in the background
docker compose -f production.yml up -d

# 4. Check the running status
# Method 1: View container logs (replace {service_name} with the specific service name, such as web, worker)
docker logs -f $(docker compose ps -q {service_name})
# Method 2: View the status of all containers
docker compose ps
```

**Success Sign**: There is no `ERROR` or `Exception` information in the logs, and the container status is `healthy`.

## Notes
1. **Configuration Priority**:  
   The production environment configuration is based on `production.yml`. The development environment can refer to `docker-compose.dev.yml` (if available).

2. **Security Recommendations**:  
   - Do not directly write sensitive configuration items (such as database passwords) into the code. It is recommended to manage them through environment variables or configuration files.  
   - In the production environment, turn off the public network access to OpenSearch, or connect through VPN/intranet.

3. **Common Problems**:  
   - Port conflict: Check if other processes are occupying the specified ports (`lsof -i :port number` to view).  
   - Docker permissions: Non-root users need to be added to the `docker` group (`sudo usermod -aG docker $USER` and then restart).

## 🎉 Stay Tuned

⭐️ Star our repository to stay up-to-date with exciting new features and improvements! Get instant notifications for new releases! 🌟

<div align="center" style="margin-top:20px;margin-bottom:20px;">
<img src="https://github.com/umi-AIGC-saas/umi_ai_cms_user/blob/main/assets/v1.gif" width="1200"/>
</div>

## Navigation
| Module Name | Link | Introduction |
| -------- | ---- | ---- |
| Front-end PC | [umi_platform_frontend](https://github.com/ymzn3820/umi_platform_frontend) | PC front-end code repository address |
| Mini Program | [umi_platform_mini_program](https://github.com/ymzn3820/umi_platform_mini_program) | Mini program code repository address |
| H5 | [umi_platform_h5](https://github.com/ymzn3820/umi_platform_h5) | H5 code repository address |
| Payment Module | [umi_platform_pay_module](https://github.com/ymzn3820/umi_platform_pay_module) | Payment module code repository address |
| User Module | [umi_platform_user_module](https://github.com/ymzn3820/umi_platform_user_module) | User module code repository address |
| Chat Module | [umi_platform_chat_module](https://github.com/ymzn3820/umi_platform_chat_module) | Chat module code repository address |

[Back to the Guide Page](https://github.com/ymzn3820/umi_platform_pay_module)

## License

BSD 3-Clause License