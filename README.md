# 内容管理系统用户模块

<p align="center">
  <a href="./README_cn.md">English</a> |
  <a href="./README.md">简体中文</a> 
</p>

<div align="center">
  <br>
  <img src="https://github.com/umi-AIGC-saas/umi_ai_cms_user/blob/main/assets/v1.png" alt="platform multimodal">
</div>

**体验地址**：[https://ai.umi6.com](https://ai.umi6.com)

## 准备工作

### 环境依赖
1. **Python版本**  
   必须使用 **Python 3.10**（其他版本可能导致兼容性问题）。  
   *验证命令*：`python --version`

2. **系统工具**  
   - Docker及Docker Compose（建议Docker ≥20.10，Compose ≥2.0）  
   - Supervisor（用于进程管理）  
   *安装示例（Ubuntu）*：  
   ```bash
   # 安装Docker
   curl -fsSL https://get.docker.com | sh
   # 安装Docker Compose
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose
   # 安装Supervisor
   sudo apt-get install supervisor
   ```

### 配置要求
1. **代码配置项**  
   项目中以 `TODO` 标记的配置项需补全（如API密钥、数据库连接等）。  
   *快速定位*：在PyCharm中通过左下角 `TODO` 面板查看，其他IDE可搜索关键字 `TODO`。

2. **端口放行**  
   确保以下端口可被访问（防火墙/安全组配置）：  
   `28999、28998、28060、28083、28071、8080、29090`  
   *注意*：`28060` 重复列出，已修正为单个端口。

3. **工作进程配置**  
   在 `docker-compose.yml` 或 `start` 脚本中设置工作进程数量（示例）：  
   ```yaml
   # production.yml示例
   services:
     worker:
       command: python worker.py --workers 4  # 配置工作进程数为4
   ```


### 服务准备
1. **Opensearch向量数据库**  
   - **方案选择**：  
     - 云服务（如阿里云OpenSearch，需提前创建实例）  
     - 本地部署（通过Docker）  
   - **本地部署步骤**：  
     ```bash
     # 下载安装脚本（假设项目根目录存在install_opensearch.yml）
     docker compose -f install_opensearch.yml build  # 构建镜像
     docker compose -f install_opensearch.yml up -d  # 后台运行
     ```
     *验证*：访问 `http://localhost:9200` 检查OpenSearch是否启动。

2. **Supervisor配置**  
   - 创建配置文件 `supervisord.conf`（示例路径：`/etc/supervisor/supervisord.conf`）  
   - 关键配置示例：  
     ```ini
     [program:umi-chat]
     command=/path/to/your/start_script.sh  # 启动脚本路径
     directory=/path/to/project  # 项目根目录
     autostart=true
     autorestart=true
     stdout_logfile=/var/log/umi-chat.log
     stderr_logfile=/var/log/umi-chat.err.log
     ```
   - 重启Supervisor：`sudo supervisorctl reload`


## 快速开始
```bash
# 1. 拉取项目代码
git clone https://github.com/ymzn3820/umi_platform_chat_module.git
cd umi_platform_chat_module  # 进入项目目录

# 2. 构建Docker镜像（生产环境配置）
docker compose -f production.yml build

# 3. 后台运行服务
docker compose -f production.yml up -d

# 4. 检查运行状态
# 方式1：查看容器日志（替换{service_name}为具体服务名，如web、worker）
docker logs -f $(docker compose ps -q {service_name})
# 方式2：查看所有容器状态
docker compose ps
```

**成功标志**：日志中无 `ERROR` 或 `Exception` 信息，且容器状态为 `healthy`。


## 注意事项
1. **配置优先级**：  
   生产环境配置以 `production.yml` 为准，开发环境可参考 `docker-compose.dev.yml`（若有）。

2. **安全建议**：  
   - 敏感配置项（如数据库密码）请勿直接写入代码，建议通过环境变量或配置文件管理。  
   - 生产环境需关闭OpenSearch的公网访问，或通过VPN/内网连接。

3. **常见问题**：  
   - 端口冲突：检查是否有其他进程占用指定端口（`lsof -i :端口号` 查看）。  
   - Docker权限：非root用户需加入 `docker` 组（`sudo usermod -aG docker $USER` 后重启）。






## 🎉 Stay Tuned

⭐️ Star our repository to stay up-to-date with exciting new features and improvements! Get instant notifications for new
releases! 🌟

<div align="center" style="margin-top:20px;margin-bottom:20px;">
<img src="https://github.com/umi-AIGC-saas/umi_ai_cms_user/blob/main/assets/v1.gif" width="1200"/>
</div>

## 导航
| 模块名称 | 链接 | 介绍|
| -------- | ---- |---- |
| 前端PC | [umi_platform_frontend](https://github.com/ymzn3820/umi_platform_frontend) | PC端前段代码仓库地址|
| 小程序端 | [umi_platform_mini_program](https://github.com/ymzn3820/umi_platform_mini_program) |小程序端代码仓库地址|
| H5端 | [umi_platform_h5](https://github.com/ymzn3820/umi_platform_h5) |H5端代码仓库地址|
| 支付模块 | [umi_platform_pay_module](https://github.com/ymzn3820/umi_platform_pay_module) |支付模块代码仓库地址|
| 用户模块 | [umi_platform_user_module](https://github.com/ymzn3820/umi_platform_user_module) |用户模块代码仓库地址|
| Chat模块 | [umi_platform_chat_module](https://github.com/ymzn3820/umi_platform_chat_module) |Chat模块代码仓库地址|

[返回引导页](https://github.com/ymzn3820/umi_platform_pay_module)

## License

BSD 3-Clause License
