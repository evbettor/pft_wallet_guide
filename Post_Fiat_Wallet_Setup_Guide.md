
# **Comprehensive Guide to Setting Up the Post Fiat Wallet and Trustlines**

## **Table of Contents**
1. [Introduction](#introduction)
2. [Environment Setup](#environment-setup)
   - [Install Python](#install-python)
   - [Install Git](#install-git)
   - [Clone the Repository](#clone-the-repository)
   - [Set Up a Virtual Environment](#set-up-a-virtual-environment)
   - [Install Dependencies](#install-dependencies)
3. [Wallet Installation and Configuration](#wallet-installation-and-configuration)
   - [Launch the Wallet Client](#launch-the-wallet-client)
   - [Configure Trustlines](#configure-trustlines)
   - [Submit a Handshake](#submit-a-handshake)
   - [Verify on Discord](#verify-on-discord)
   - [Test Wallet Functionality](#test-wallet-functionality)
4. [Troubleshooting Common Issues](#troubleshooting-common-issues)
5. [Python Automation Scripts](#python-automation-scripts)
   - [Virtual Environment Setup](#virtual-environment-setup)
   - [Configure Trustlines](#configure-trustlines-script)
   - [Automate Wallet Updates](#automate-wallet-updates)
   - [Submit a Handshake](#submit-a-handshake-script)
6. [Conclusion](#conclusion)

## **Introduction**

This guide provides a step-by-step process for setting up the Post Fiat wallet and configuring trustlines to interact with the Post Fiat Token (PFT) on the XRP Ledger. It includes troubleshooting tips, best practices, and Python scripts to automate the setup process.

---

## **Environment Setup**

### **Install Python**
Ensure you have Python 3.11+ installed on your system.

#### Windows:
1. Download Python from [python.org](https://www.python.org/downloads/).
2. During installation, check:
   - `Add Python to PATH`
   - Install pip.
3. Verify installation:
   ```powershell
   python --version
   ```

#### macOS:
1. Install via Homebrew:
   ```bash
   brew install python
   ```
2. Verify installation:
   ```bash
   python3 --version
   ```

#### Linux:
1. Install using your package manager:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```
2. Verify installation:
   ```bash
   python3 --version
   ```

---

### **Install Git**
Git is required to clone the Post Fiat client repository.

#### Windows:
1. Download Git from [git-scm.com](https://git-scm.com/).
2. Verify installation:
   ```powershell
   git --version
   ```

#### macOS/Linux:
1. Install via Homebrew (macOS) or your package manager:
   ```bash
   brew install git  # macOS
   sudo apt install git  # Linux
   ```
2. Verify installation:
   ```bash
   git --version
   ```

---

### **Clone the Repository**
1. Navigate to the desired folder:
   ```bash
   cd /path/to/projects  # macOS/Linux
   cd C:\Projects  # Windows
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/postfiatorg/pftpyclient.git
   ```
3. Navigate into the project directory:
   ```bash
   cd pftpyclient
   ```

---

### **Set Up a Virtual Environment**
1. Create a virtual environment:
   ```bash
   python -m venv pftwalletenv
   ```
2. Activate the virtual environment:
   - Windows:
     ```powershell
     .\pftwalletenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source pftwalletenv/bin/activate
     ```
3. Verify activation:
   - The prompt should show `(pftwalletenv)`.

---

### **Install Dependencies**
1. Install the client and its dependencies:
   ```bash
   pip install -e .
   ```
2. Verify installation:
   ```bash
   pip list
   ```

---

## **Wallet Installation and Configuration**

### **Launch the Wallet Client**
1. Run the client:
   ```bash
   pft
   ```

---

### **Configure Trustlines**
1. Add a trustline for the PFT token:
   - Issuer: `rnQUEEg8yyjrwk9FhyXpKavHyCRJM9BDMW`
   - Token: `PFT`

2. Verify using [XRPL Explorer](https://livenet.xrpl.org).

---

### **Submit a Handshake**
1. Send **0.000001 XRP** to the provided node address.
2. Include the memo `HANDSHAKE`.
3. Verify the transaction via [XRPL Explorer](https://livenet.xrpl.org).

---

### **Verify on Discord**
1. Run `/pf_verify` in the Post Fiat Discord server.
2. Paste your wallet address when prompted.

---

### **Test Wallet Functionality**
1. Confirm the wallet displays your XRP balance and PFT trustline.
2. Use the **Task Request** section to request your first task.

---

## **Troubleshooting Common Issues**
### Virtual Environment Setup Issues
- **Problem**: `[WinError 5] Access is denied`.
- **Solution**: Run PowerShell/terminal as an administrator.

### Transaction Errors
- **Problem**: `tecPATH_DRY`.
- **Solution**: Ensure sufficient XRP and correct transaction details.

See the full troubleshooting guide in the Python scripts section.

---

## **Python Automation Scripts**

### **Virtual Environment Setup**
```python
# setup_env.py
# Script to automate virtual environment creation and dependency installation.
```

### **Configure Trustlines Script**
```python
# configure_trustline.py
# Script to add trustlines for PFT token programmatically.
```

### **Automate Wallet Updates**
```python
# update_client.py
# Automates Git pull and dependency reinstallation.
```

### **Submit a Handshake Script**
```python
# submit_handshake.py
# Script to send a handshake transaction programmatically.
```

## **Python Automation Scripts**

This section provides detailed descriptions of the Python scripts included in the `helper_scripts/` folder of the repository. These scripts automate common setup tasks, making it easier to configure and manage your Post Fiat wallet.

### **Virtual Environment Setup**
**File**: `helper_scripts/setup_env.py`

This script automates the creation and activation of a virtual environment and installs all necessary dependencies.

#### Usage:
1. Run the script from the project root:
   ```bash
   python helper_scripts/setup_env.py
   ```
2. Follow the printed instructions to activate the environment.

#### Features:
- Ensures a clean virtual environment.
- Automatically installs all dependencies.

---

### **Configure Trustlines Script**
**File**: `helper_scripts/configure_trustline.py`

This script adds a trustline for the PFT token programmatically, ensuring your wallet is ready to interact with the Post Fiat ecosystem.

#### Usage:
1. Open the script and replace the placeholder values (`rYourWalletAddress` and `sYourSecret`) with your wallet's address and secret.
2. Run the script:
   ```bash
   python helper_scripts/configure_trustline.py
   ```

#### Features:
- Automates trustline configuration with the PFT token issuer.
- Prevents manual entry errors.

---

### **Automate Wallet Updates**
**File**: `helper_scripts/update_client.py`

This script updates the Post Fiat wallet repository and reinstalls dependencies.

#### Usage:
1. Run the script from the project root:
   ```bash
   python helper_scripts/update_client.py
   ```

#### Features:
- Automates `git pull` to fetch the latest code.
- Reinstalls all required dependencies after updates.

---

### **Submit a Handshake Script**
**File**: `helper_scripts/submit_handshake.py`

This script automates sending a handshake transaction, ensuring you can quickly verify your wallet with the Post Fiat system.

#### Usage:
1. Open the script and replace the placeholder values (`rYourWalletAddress` and `sYourSecret`) with your wallet's address and secret.
2. Run the script:
   ```bash
   python helper_scripts/submit_handshake.py
   ```

#### Features:
- Automatically sends a handshake with the correct memo and transaction amount.
- Verifies successful submission via XRP Ledger.

---

## **Conclusion**

This guide covers the entire setup process, including troubleshooting and automation. With the included Python scripts, you can streamline your workflow and get started quickly in the Post Fiat ecosystem.

---

### **Next Steps**
- Download the scripts from the repository.
- Use the guide to set up your wallet and request your first task.
- Contribute to the community by reporting bugs or suggesting improvements.

---
