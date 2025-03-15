Below is a general step-by-step guide for deploying the **Social Security Claiming Simulator** on an **AWS EC2 free tier** instance. This walkthrough focuses on using an **Amazon Linux 2** t2.micro or t3.micro (depending on your free tier allowances). Adjust any commands or configurations as necessary for your environment.

---

# Deploying the Social Security Claiming Simulator to AWS EC2 (Free Tier)

## Prerequisites
1. **AWS account** with access to the free tier.
2. **SSH key pair** (either generated through the AWS console or existing).
3. Basic familiarity with AWS EC2, Linux commands, and networking.

---

## 1. Create or Select an EC2 Instance

1. **Log in** to your AWS Management Console.
2. Go to **Services** > **EC2**.
3. Click **Launch instances**.
4. **Name** your instance (e.g., `social-security-simulator`).
5. **Choose an AMI**:  
   - Select **Amazon Linux 2 AMI (Free Tier eligible)**.
6. **Choose an instance type**:  
   - Pick **t2.micro** or **t3.micro** (if your free tier allows).
7. **Key pair**:  
   - Create a new key pair or select an existing one so you can SSH into your instance.
8. **Network settings**:  
   - Make sure you allow inbound traffic on the ports you intend to use (e.g., **22** for SSH, and **8080** or **8501** if you’re running a web app).  
   - By default, AWS will create a security group with **SSH (22)** open. You may add custom **TCP** rules for your application’s port.
9. **Configure storage** (8GB is typical; free tier covers up to 30GB).
10. Click **Launch instance**.

---

## 2. Connect to the EC2 Instance

1. Once the instance is running, select it in the EC2 console, then click **Connect**.
2. Use the **EC2 Instance Connect** feature or your local terminal with SSH:
   ```bash
   ssh -i /path/to/your-key.pem ec2-user@<EC2-Public-IP-or-DNS>
   ```
3. You should now be logged into your EC2 instance.

---

## 3. Install System Dependencies

On your **Amazon Linux 2** instance, run:

```bash
# Update existing packages
sudo yum update -y

# Install Git (if not already installed)
sudo yum install git -y

# Install Python 3 (Amazon Linux 2 typically comes with Python 3.x, 
# but this ensures you have it and pip)
sudo yum install python3 -y

# (Optional) Install venv if you want to create a virtual environment
# Usually python3-venv is built-in, but if not, you can install:
# sudo yum install python3-venv -y
```

---

## 4. Clone the Repository

```bash
# Navigate to a directory where you want to store the code
cd ~
# Clone the Social Security Claiming Simulator
git clone https://github.com/jtayl222/social-security-claiming-simulator.git
```

---

## 5. (Optional) Create a Virtual Environment

Creating a virtual environment is good practice to keep dependencies isolated:

```bash
cd social-security-claiming-simulator
python3 -m venv venv
source venv/bin/activate
```

---

## 6. Install Python Dependencies

From within the repository folder (and inside the virtual environment if you created one):

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install **Streamlit**, **FastAPI**, **Uvicorn**, and other needed libraries.

---

## 7. Run Your Application

### Option A: Run the Streamlit App

```bash
# Still in the social-security-claiming-simulator directory
streamlit run src/streamlit_app.py --server.port 8080
```

- By default, Streamlit runs on port 8501. You can specify `--server.port 8080` (or any open port) if you prefer.  
- In your security group settings, ensure **Inbound** rules allow traffic on the chosen port (TCP 8080 or 8501).  

**Accessing the Streamlit App**:
- In a browser, go to `http://<EC2-Public-IP-or-DNS>:8080` (or `:8501`).

### Option B: Run the FastAPI App

```bash
uvicorn src.fastapi_app:app --host 0.0.0.0 --port 8080
```

- Make sure to open **port 8080** (or whatever you choose) in the security group.  
- In a browser or REST client, navigate to:  
  - `http://<EC2-Public-IP-or-DNS>:8080/docs` for the auto-generated Swagger documentation.  
  - `http://<EC2-Public-IP-or-DNS>:8080` for the root endpoint.

---

## 8. Keep Your App Running in the Background

To keep the application running if you disconnect from the SSH session, you can use:

- **tmux**:
  ```bash
  sudo yum install tmux -y
  tmux new -s simulator
  # run your streamlit or uvicorn command
  # press Ctrl+B then D to detach
  # reconnect using: tmux attach -t simulator
  ```
- **screen**:
  ```bash
  sudo yum install screen -y
  screen -S simulator
  # run your streamlit or uvicorn command
  # press Ctrl+A then D to detach
  # reconnect using: screen -r simulator
  ```
- **systemd service** (for a more permanent solution).

---

## 9. (Optional) Associate a Domain Name or Elastic IP

1. **Elastic IP**: You can allocate an Elastic IP in the EC2 console and associate it with your instance to ensure a stable IP address.  
2. **Custom Domain**: If you own a domain, you can create an A record pointing to your Elastic IP, so users can access your app via `https://mydomain.com`.

---

## 10. Costs and AWS Free Tier Reminders

- Ensure that you **stop** or **terminate** your instance when not in use, or monitor usage carefully to stay within free tier limits.  
- The free tier typically covers **750 hours/month** of t2.micro or t3.micro usage for the first 12 months. Verify your free tier usage and track potential costs in the **Billing & Cost Management** console.

---

# Disclaimer
This project is **not** legal, financial, or tax advice. It is purely for informational and educational purposes. The estimations and projections generated by this tool may not reflect real-world outcomes. **Always consult a qualified professional** to discuss how Social Security claiming decisions affect your unique circumstances.

---

## Conclusion

With these steps, you should have the **Social Security Claiming Simulator** up and running on an AWS EC2 instance under the free tier. From here, you can continue to fine-tune your security settings, optionally integrate with a domain name, and ensure your simulator is accessible to end-users as desired. 

If you encounter any issues, consider checking:
- EC2 **Security Groups** for open ports  
- **CloudWatch Logs** or local logs for errors  
- **AWS Billing** to ensure you remain within free-tier limits  

Good luck with your deployment!
