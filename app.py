from datetime import datetime

def print_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hi buddy this is fifth times updates.........Current Time: {current_time}")

if __name__ == "__main__":
    print_current_time()
