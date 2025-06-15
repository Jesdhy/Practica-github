# 🌍👋 Hello world in python 

## 📘 About The Project

This is a minimal Python project using Flask that prints "Hello World" when running a local web server. It's designed as a basic introduction to web development, containerization with Docker, and CI/CD practices using GitHub.

## ⚠️ **¡IMPORTANT!** ⚠️

- The **main** branch contains the project with Docker.
- The **dev** Development/testing branch.
- The **deploy** Branch used for production deployment (via CI/CD).


## 📑 Table of Contents

- [📘 About The Project](#about-the-project)
- [🚀 Getting Started](#getting-started)
  - [🔧 Prerequisites](#prerequisites)
  - [📥 Installation](#installation)
  - [⚙️ Running](#running)
  - [🐳 Running with Docker](#running-with-docker)
- [🤝 Contributing](#contributing)

## 🚀 Getting Started
## 🔧 Prerequisites
**Python**: This project requires **Python 3.10.12**. Make sure you have this version installed on your system.
You can check your Python version by running:
```bash
python3 --version
 ```
## 📥 Installation

1.- Clone the repository

   ```sh
   git clone https://github.com/Jesdhy/Practica-github.git
  ```
2.- Create a virtual environment
 ```sh
    python -m venv .venv
   ```
 ```sh
    source .venv/bin/activate
   ```
## ⚙️ Running

  ```sh
    python app.py
   ```

## 🐳 Running with docker

1.- Making Docker Pull or Build docker image

 ```sh
   docker pull jessdhy/practica_git:latest
   ```

2.- Last make a docker run

 ```sh
   docker run -it jessdhy/practica_git
   ```

## 🤝 Contributing
Thank you for your interest in contributing to this project! Here are some guidelines for doing so:
1. **Fork the repository** and clone the project to your local machine.
2. **Create a new branch** for your changes.
3. **Commit your changes** with a clear, descriptive message.
4. **Submit a Pull Request** with a description of your changes.

Thank you for helping improve this project!