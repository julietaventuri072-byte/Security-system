<<<<<<< HEAD
import datetime

class User:
    def __init__(self, username, password_hash, role):
        self.username = username
        self.password_hash = password_hash
        self.role = role #"admin" / "guard"

class Camera:
    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location
        self.active = True

class Incident:
    def __init__(self, description, reported_by):
        self.description = description
        self.reported_by = reported_by
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.reported_by}: {self.description}"

        
=======
import datetime

class User:
    def __init__(self, username, password_hash, role):
        self.username = username
        self.password_hash = password_hash
        self.role = role #"admin" / "guard"

class Camera:
    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location
        self.active = True

class Incident:
    def __init__(self, description, reported_by):
        self.description = description
        self.reported_by = reported_by
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.reported_by}: {self.description}"

        
>>>>>>> f4a19c10a8f96dd3a8eccafa90551107535f6458
        