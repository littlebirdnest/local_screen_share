# 🖥️ Py-Screen-Share
### Ultra-light LAN Screen Sharing / 极简局域网屏幕分享

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

**English:**
A lightweight Python tool for sharing your screen over a Local Area Network (LAN). 
No client installation is required on the receiver's side—just a web browser is needed to view the screen in real-time.

**中文:**
一个基于 Python 的超轻量级屏幕分享工具。
接收端无需安装任何软件，**只要有浏览器，就能实时观看电脑屏幕**。

---

## ✨ Features / 特性

- **🌐 Zero Client**: Just use a web browser (Mobile/PC/Tablet).
  - **零客户端**：接收端只需浏览器（手机/平板/电脑均可）。
- **⚡ Ultra Low Latency**: Powered by MJPEG streaming, nearly zero latency in LAN.
  - **超低延迟**：基于 MJPEG 流媒体技术，局域网内几乎无感知延迟。
- **📝 Minimal Code**: Core logic is under 50 lines, perfect for learning Flask & OpenCV.
  - **极简代码**：核心逻辑不足 50 行，适合学习 Flask 和 OpenCV。
- **💻 Cross-Platform**: Works on Windows, macOS, and Linux.
  - **跨平台**：支持 Windows, macOS, Linux。

---

## 🛠️ Tech Stack / 技术栈

- **Flask**: Lightweight Web Server / 构建轻量级 Web 服务器
- **MSS**: High-performance Screen Capture / 高性能屏幕截取
- **OpenCV**: Image Processing & Compression / 图像处理与压缩
- **NumPy**: Data manipulation / 矩阵数据处理

---

## 🚀 Quick Start / 快速开始

### 1. Clone the repository / 克隆项目
```bash
git clone [https://github.com/littlebirdnest/local_screen_share.git)
cd local_screen_share
