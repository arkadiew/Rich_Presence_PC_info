import sys
import os
import time
import logging
import psutil
import platform
from datetime import datetime

# Setup logging for debugging
logging.basicConfig(
    filename="system_info.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    from pypresence import Presence
except ImportError:
    logging.error("pypresence module not found. Discord Rich Presence will not work.")
    Presence = None

try:
    import win32com.client
except ImportError:
    logging.error("win32com module not found. Some system info may be unavailable.")
    win32com = None

def get_resource_path(relative_path):
    """Get the absolute path to a resource, works for dev and PyInstaller EXE."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

# Read client_id from external file
try:
    client_id_path = get_resource_path("client_id.txt")
    with open(client_id_path, "r", encoding="utf-8") as f:
        client_id = f.read().strip()
    logging.info(f"Successfully read client_id from {client_id_path}")
except Exception as e:
    logging.error(f"Failed to read client ID from file: {e}")
    sys.exit(1)

# Initialize Rich Presence client
RPC = None
if Presence:
    try:
        RPC = Presence(client_id)
        RPC.connect()
        logging.info("Connected to Discord Rich Presence")
    except Exception as e:
        logging.error(f"Failed to connect to Discord: {e}")
        RPC = None

def get_cpu_name():
    """Get CPU name via OpenHardwareMonitor WMI, with fallback to platform."""
    cpu_name = "Unknown CPU"
    if platform.system() == "Windows" and win32com:
        try:
            wmi_ohm = win32com.client.GetObject("winmgmts:\\\\.\\root\\OpenHardwareMonitor")
            hardware_query = wmi_ohm.ExecQuery("SELECT * FROM Hardware WHERE HardwareType = 'CPU'")
            for hardware in hardware_query:
                cpu_name = hardware.Name
                break
            logging.debug(f"CPU name from OHM: {cpu_name}")
        except Exception as e:
            logging.error(f"Error retrieving CPU name from OpenHardwareMonitor: {e}")

    # Fallback to platform if OHM/WMI unavailable
    if cpu_name == "Unknown CPU":
        try:
            cpu_name = platform.processor()
            if not cpu_name:
                cpu_name = "Unknown CPU"
            logging.debug(f"CPU name from platform: {cpu_name}")
        except Exception as e:
            logging.error(f"Failed to get CPU name from platform: {e}")
            cpu_name = "Unknown CPU"

    return cpu_name

def get_os_info():
    """Get OS info via platform."""
    try:
        os_info = f"{platform.system()} {platform.release()}"
        logging.debug(f"OS info from platform: {os_info}")
        return os_info
    except Exception as e:
        logging.error(f"Failed to get OS info: {e}")
        return "Unknown OS"

def get_gpu_info():
    """Get GPU info via WMI and OpenHardwareMonitor."""
    gpu_info = "No GPU detected"
    gpu_temp = 0
    gpu_load = 0

    if platform.system() == "Windows" and win32com:
        try:
            wmi_obj = win32com.client.GetObject("winmgmts:")
            gpus = wmi_obj.InstancesOf("Win32_VideoController")
            for gpu in gpus:
                name = gpu.Properties_["Name"].Value
                if "Virtual" not in name and "spacedesk" not in name.lower():
                    gpu_info = name
                    break
            logging.debug(f"GPU name from WMI: {gpu_info}")
        except Exception as e:
            logging.error(f"Error retrieving GPU name from winmgmts: {e}")

        try:
            wmi_ohm = win32com.client.GetObject("winmgmts:\\\\.\\root\\OpenHardwareMonitor")
            sensors = wmi_ohm.ExecQuery("SELECT * FROM Sensor")
            for sensor in sensors:
                if sensor.Name.lower().startswith("gpu core"):
                    if sensor.SensorType == "Temperature":
                        gpu_temp = float(sensor.Value)
                    elif sensor.SensorType == "Load":
                        gpu_load = float(sensor.Value)
            logging.debug(f"GPU temp: {gpu_temp}°C, load: {gpu_load}%")
        except Exception as e:
            logging.error(f"OpenHardwareMonitor unavailable or not running: {e}")

    return f"{gpu_info} ({gpu_load:.1f}% load, {gpu_temp:.1f}°C)"

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = f"{memory.percent}% ({memory.used // 1024**2} MB / {memory.total // 1024**2} MB)"
    os_info = get_os_info().replace("Microsoft", "").replace("Майкрософт", "").strip()
    try:
        disk = psutil.disk_usage('C:/')
        disk_usage = f"{disk.percent}% ({disk.used // 1024**3} GB / {disk.total // 1024**3} GB)"
    except Exception as e:
        logging.error(f"Failed to get disk usage: {e}")
        disk_usage = "Disk info unavailable"
    gpu_info = get_gpu_info()
    cpu_name = get_cpu_name()
    cpu_name = cpu_name.replace("8-Core Processor", "").strip()

    return [
        {
            "state": f"CPU: {cpu_name} | {cpu_usage}%",
            "details": f"RAM: {memory_usage}",
            "large_text": f"OS: {os_info}",
            "small_text": f"Disk: {disk_usage}"
        },
        {
            "state": f"GPU: {gpu_info}",
            "details": f"OS: {os_info}",
            "large_text": f"RAM: {memory_usage}",
            "small_text": f"CPU: {cpu_usage}%"
        }
    ]

start_time = int(time.time())
while True:
    try:
        if RPC:
            for status in get_system_info():
                RPC.update(**status, start=start_time)
                logging.debug(f"Updated Discord status: {status}")
                time.sleep(10)
        else:
            logging.warning("Discord RPC not available, skipping update")
            time.sleep(10)
    except Exception as e:
        logging.error(f"Error updating status: {e}")
        time.sleep(10)  # Prevent tight loop on error