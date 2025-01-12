from datetime import datetime

def print_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hi shyam this is second time updates.........Current Time: {current_time}")

if __name__ == "__main__":
    print_current_time()
