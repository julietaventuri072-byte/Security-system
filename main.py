from system import SecuritySystem

def main():
    system = SecuritySystem()

    # Usuario inicial
    system.register_user("admin", "1234", "admin")

    print("=== SECURITY SYSTEM ===")

    username = input("Username: ")
    password = input("Password: ")

    user = system.login(username, password)

    if not user:
        print("Login failed.")
        return

    print(f"\nWelcome {user.username} ({user.role})")

    while True:
        print("\n1. Add Camera")
        print("2. View Cameras")
        print("3. Report Incident")
        print("4. View Incidents")
        print("5. View Logs")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            cam_id = input("Camera ID: ")
            location = input("Location: ")
            system.add_camera(cam_id, location, user)

        elif choice == "2":
            system.list_cameras()

        elif choice == "3":
            desc = input("Incident description: ")
            system.report_incident(desc, user)

        elif choice == "4":
            system.list_incidents()

        elif choice == "5":
            system.show_logs()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()