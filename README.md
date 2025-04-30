# Virtual Machines & Compute Instances

## Description
This project is about Launching EC2, setting up Apache and Flask app to display instance metadata using Python.

### Contents:
1. **Exercise 1**: 
   - Documentation describing the type of virtualization used by the EC2 instance launched.
2. **Exercise 2**: 
   - A Python Flask application that displays EC2 instance metadata in a table format on a webpage.

## Prerequisites
- An active **AWS account** and **$100 AWS Academy credit**.
- **GitHub Desktop** for version control and repository management.
- **PuTTY** for connecting to the EC2 instance on Windows.
- Basic knowledge of **Amazon EC2**, **Linux** commands, and **Python Flask**.

## Setup Guide

### 1. Launching the EC2 Instance:
- Follow the steps in the lab instructions to set up an EC2 instance with **Ubuntu Server 18.04 LTS**.
- Ensure the necessary ports (22 for SSH, 80 for HTTP) are open in the instance’s security group.

### 2. Connecting to EC2:
- Use **PuTTY** to connect to your EC2 instance.
- Convert the PEM key to PPK format using **PuTTYgen** if required.

### 3. Install Apache Web Server:
- SSH into your EC2 instance and install **Apache2**:
    ```bash
    sudo apt-get update
    sudo apt-get install apache2
    ```

### 4. Replace Default Webpage:
- Replace the default `index.html` file with your custom HTML page located at `/var/www/html/`.

### 5. Setting Up Flask Web Application:
- Install Flask on your EC2 instance:
    ```bash
    sudo apt-get install python-pip
    sudo apt install python3-pip
    sudo pip install Flask
    ```

### 6. Display EC2 Metadata:
- Use the `ec2-metadata` library to fetch metadata and display it in a Flask app:
    ```bash
    pip install ec2-metadata
    ```

### 7. Running Flask Application:
- Create and run the `hello.py` script that fetches and displays metadata in a table format on a webpage:
    ```bash
    python3 hello.py
    ```
### Exercise 2:
- A screenshot of the running Flask application showing the EC2 metadata in a table format.

---

### 📄 License
This project was developed for educational purposes and is shared as a sample academic assignment.

