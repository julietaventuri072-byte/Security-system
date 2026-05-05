from models import User, Camera, Incident
from auth import hash_password, verify_password

class SecuritySystem:
    def __init__(self):
        self.users = []
        self.cameras = []
        self.incidents = []
        self.logs = []

    def log(self, action):
        self.logs.append(action)

    # -------- USERS --------
    def register_user(self, username, password, role):
        password_hash = hash_password(password)
        self.users.append(User(username, password_hash, role))
        self.log(f"User registered: {username}")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and verify_password(password, user.password_hash):
                self.log(f"Login success: {username}")
                return user
        self.log(f"Login failed: {username}")
        return None

    # -------- CAMERAS --------
    def add_camera(self, camera_id, location, user):
        if user.role != "admin":
            print("Access denied: Only admin can add cameras.")
            return

        self.cameras.append(Camera(camera_id, location))
        self.log(f"Camera added: {camera_id}")

    def list_cameras(self):
        if not self.cameras:
            print("No cameras registered.\n")
            return

        for cam in self.cameras:
            status = "Active" if cam.active else "Inactive"
            print(f"{cam.camera_id} - {cam.location} ({status})")

    # -------- INCIDENTS --------
    def report_incident(self, description, user):
        if not description.strip():
            print("Invalid incident description.")
            return

        incident = Incident(description, user.username)
        self.incidents.append(incident)
        self.log(f"Incident reported by {user.username}")

    def list_incidents(self):
        if not self.incidents:
            print("No incidents.\n")
            return

        for inc in self.incidents:
            print(inc)

    # -------- LOGS --------
    def show_logs(self):
        if not self.logs:
            print("No logs.\n")
            return

        for log in self.logs:
            print(log)
