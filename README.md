💰 Bank Management System

A simple yet powerful Bank Management System built using Python and Streamlit.
This project allows users to create, manage, and delete bank accounts, perform transactions like deposit and withdrawal, and update personal details — all with a user-friendly web interface.

🚀 Features

✅ Create Account – Open a new account with name, email, age, and PIN
✅ Deposit Money – Deposit up to ₹10,000 at once
✅ Withdraw Money – Withdraw money securely using PIN
✅ Show Account Details – View account balance and user info
✅ Update Details – Modify name, email, or PIN
✅ Delete Account – Permanently close your bank account
✅ Data Persistence – All records are stored safely in a local data.json file
✅ Interactive UI – Built using Streamlit for an intuitive experience

🧠 Tech Stack
Component	Technology
Language	Python
Frontend / UI	Streamlit
Database	JSON File (data.json)
Modules Used	json, random, string, pathlib, streamlit
📂 Project Structure
📦 Bank-Management-System
 ┣ 📜 bank_app.py                # Main Streamlit Application
 ┣ 📜 data.json             # Stores all user account data
 ┣ 📜 README.md             # Project documentation

🧩 How It Works

When a new account is created, a unique account number is generated using random letters, digits, and symbols.

Account details are saved inside data.json.

Each transaction (deposit/withdraw) updates the file automatically.

PIN-based authentication ensures account security.

🧠 Future Enhancements

Add user authentication (login/signup)

Integrate with SQLite or MySQL database

Add transaction history and PDF statement download

Enable OTP/email verification for extra security

👨‍💻 Author

Nikhil Kumar Singh

🪪 License

This project is open-source under the MIT License.
Feel free to use and modify it for your learning or portfolio projects.
