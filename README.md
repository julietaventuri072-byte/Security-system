# 🛡️ Security Monitoring System (Python)

A console-based security system simulator built in Python using Object-Oriented Programming (OOP).  
It allows user authentication, camera management, incident reporting, and activity logging.

---

## 🚀 Features

- 🔐 User authentication (admin / guard roles)
- 📷 Camera management system
- 🚨 Incident reporting with timestamps
- 📋 Activity logs tracking system actions
- 🧠 Input validation and basic access control

---

## 🏗️ Project Structure

```text
auth.py       # password hashing & verification
models.py     # data models (User, Camera, Incident)
system.py     # core system logic
main.py       # interactive console interface

🔑 Default Access
Username: admin
Password: 1234
📸 Example Output
=== SECURITY SYSTEM ===
Username: admin
Password: ****

Welcome admin (admin)

1. Add Camera
2. View Cameras
3. Report Incident
4. View Incidents
5. View Logs
6. Exit
🧠 Concepts Applied
Object-Oriented Programming (OOP)
Separation of concerns (modular design)
Basic authentication logic
Data handling with lists
Timestamp management using datetime

🔐 Security Considerations
Passwords are hashed (SHA-256)
Role-based access control (admin vs guard)
Basic input validation
Activity logging for auditing

⚠️ Limitations
No persistent storage (data resets on restart)
No database integration
Basic console interface only

🚀 Future Improvements
💾 Data persistence (JSON or database)
🔒 Stronger password hashing (bcrypt)
🖥️ Graphical user interface (GUI)
🔍 Search and filtering system
🌐 Web-based version

👩‍💻 Author
Julieta Venturi
