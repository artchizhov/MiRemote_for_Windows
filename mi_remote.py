import time
from mi_remote_mode_switch import MiRemote
import json

def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_device_config(path="device.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    usage_buttons = {int(k): v for k, v in data.get("USAGE_BUTTONS", {}).items()}
    mask_buttons = {int(k): v for k, v in data.get("MASK_BUTTONS", {}).items()}
    vid = data.get("VID")
    pid = data.get("PID")
    return vid, pid, usage_buttons, mask_buttons


def main():
    config = load_config("config.json")
    
    vid, pid, usage_buttons, mask_buttons = load_device_config("device.json")

    remote = MiRemote(
        vid=vid,
        pid=pid,
        usage_buttons=usage_buttons,
        mask_buttons=mask_buttons,
        base_step_cursor=config.get("base_step_cursor", 1),
        max_step_cursor=config.get("max_step_cursor", 40),
        base_step_scroll=config.get("base_step_scroll", 1),
        max_step_scroll=config.get("max_step_scroll", 20),
        accel_time=config.get("accel_time", 0.03),
        scroll_accel_delay=config.get("scroll_accel_delay", 2),
        scroll_delay=config.get("scroll_delay", 0.06)
    )
    
    try:
        remote.connect()
        print("MiRemote сервис запущен. Нажмите POWER для переключения режима.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Сервис остановлен пользователем")
    finally:
        remote.disconnect()

if __name__ == "__main__":
    main()
