import pywinusb.hid as hid
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyController, Key
import threading
import time

class MiRemote:
    VID = 0x2717
    PID = 0x32B9

    USAGE_BUTTONS = {
        0x0020: "POWER",
        0x0040: "ASSIST",
        0x0001: "OK",
        0x0002: "UP",
        0x0004: "DOWN",
        0x0008: "LEFT",
        0x0010: "RIGHT",
        0x0200: "MENU",
        0x0400: "NETFLIX",
        0x2000: "PRIME_VIDEO",
        0x0080: "VOL_UP",
        0x0100: "VOL_DOWN",
    }

    MASK_BUTTONS = {
        0x08: "BACK",
        0x04: "HOME",
    }

    '''def __init__(self, base_step=10, max_step=50, accel_time=0.15):
        self.device = None
        self._last_button = None
        self.mouse = MouseController()
        self.keyboard = KeyController()

        self.base_step = base_step
        self.max_step = max_step
        self.accel_time = accel_time

        # Для удержания кнопок
        self._hold_flags = {}
        self._threads = {}

        # Режим: True = мышь, False = клавиатура/медиа
        self.mouse_mode = True'''
        
    '''def __init__(self,
                 base_step_cursor=10,
                 max_step_cursor=50,
                 base_step_scroll=1,
                 max_step_scroll=10,
                 accel_time=0.15,
                 scroll_accel_delay=3,
                 scroll_delay=0.20):
        self.device = None
        self._last_button = None
        self.mouse = MouseController()
        self.keyboard = KeyController()

        # Раздельные шаги для курсора и прокрутки
        self.base_step_cursor = base_step_cursor
        self.max_step_cursor = max_step_cursor
        self.base_step_scroll = base_step_scroll
        self.max_step_scroll = max_step_scroll
        self.accel_time = accel_time
        self.scroll_accel_delay = scroll_accel_delay
        self.scroll_delay = scroll_delay'''
    def __init__(self, vid=VID, pid=PID,
                 usage_buttons=USAGE_BUTTONS,
                 mask_buttons=MASK_BUTTONS,
                 base_step_cursor=1, max_step_cursor=40,
                 base_step_scroll=1, max_step_scroll=20,
                 accel_time=0.03,
                 scroll_accel_delay=2, scroll_delay=0.06):
        # Аппаратные параметры
        self.VID = vid
        self.PID = pid
        self.USAGE_BUTTONS = usage_buttons
        self.MASK_BUTTONS = mask_buttons

        # Настройки ускорения
        self.base_step_cursor = base_step_cursor
        self.max_step_cursor = max_step_cursor
        self.base_step_scroll = base_step_scroll
        self.max_step_scroll = max_step_scroll
        self.accel_time = accel_time
        self.scroll_accel_delay = scroll_accel_delay
        self.scroll_delay = scroll_delay

        # Внутренние переменные
        self.device = None
        self._last_button = None
        self.mouse = MouseController()
        self.keyboard = KeyController()

        self._hold_flags = {}
        self._threads = {}
        self.mouse_mode = True

        # Настройка действий для обоих режимов
        '''self.BUTTON_ACTIONS_MOUSE = {
            "UP": lambda step: self.mouse.move(0, -step),
            "DOWN": lambda step: self.mouse.move(0, step),
            "LEFT": lambda step: self.mouse.move(-step, 0),
            "RIGHT": lambda step: self.mouse.move(step, 0),
            "OK": lambda step=None: self.mouse.click(Button.left),
            "MENU": lambda step=None: self.mouse.click(Button.right),
            "ASSIST": lambda step=None: self.mouse.click(Button.middle),
            "NETFLIX": lambda step: self.mouse.scroll(0, 1),
            "PRIME_VIDEO": lambda step: self.mouse.scroll(0, -1),
            "BACK": lambda step=None: print("BACK pressed"),
            "HOME": lambda step=None: print("HOME pressed"),
            "VOL_UP": lambda step=None: print("VOL_UP pressed"),
            "VOL_DOWN": lambda step=None: print("VOL_DOWN pressed"),
            "POWER": self.toggle_mode
        }'''
        self.BUTTON_ACTIONS_MOUSE = {
            "UP": lambda step: self.mouse.move(0, -step),
            "DOWN": lambda step: self.mouse.move(0, step),
            "LEFT": lambda step: self.mouse.move(-step, 0),
            "RIGHT": lambda step: self.mouse.move(step, 0),
            "OK": lambda step=None: self.mouse.click(Button.left),
            "MENU": lambda step=None: self.mouse.click(Button.right),
            "ASSIST": lambda step=None: self.mouse.click(Button.middle),
            "NETFLIX": lambda step: self.mouse.scroll(0, step),
            "PRIME_VIDEO": lambda step: self.mouse.scroll(0, -step),
            "BACK": lambda step=None: print("BACK pressed"),
            "HOME": lambda step=None: print("HOME pressed"),
            "VOL_UP": lambda step=None: print("VOL_UP pressed"),
            "VOL_DOWN": lambda step=None: print("VOL_DOWN pressed"),
            "POWER": self.toggle_mode
        }

        # Пример действий в клавиатурном режиме
        self.BUTTON_ACTIONS_KEYBOARD = {
            "UP": lambda step=None: self.keyboard.press(Key.up),
            "DOWN": lambda step=None: self.keyboard.press(Key.down),
            "LEFT": lambda step=None: self.keyboard.press(Key.left),
            "RIGHT": lambda step=None: self.keyboard.press(Key.right),
            "OK": lambda step=None: self.keyboard.press(Key.enter),
            "MENU": lambda step=None: self.keyboard.press(Key.menu),
            "ASSIST": lambda step=None: self.keyboard.press(Key.space),
            "NETFLIX": lambda step=None: self.keyboard.press(Key.page_up),
            "PRIME_VIDEO": lambda step=None: self.keyboard.press(Key.page_down),
            "BACK": lambda step=None: self.keyboard.press(Key.backspace),
            "HOME": lambda step=None: self.keyboard.press('h'),
            "VOL_UP": lambda step=None: self.keyboard.press(Key.media_volume_up),
            "VOL_DOWN": lambda step=None: self.keyboard.press(Key.media_volume_down),
            "POWER": self.toggle_mode
        }

    # Переключение режима
    def toggle_mode(self):
        self.mouse_mode = not self.mouse_mode
        mode_name = "Мышь" if self.mouse_mode else "Клавиатура/Медиа"
        print(f"Режим переключен на: {mode_name}")

    # ----------------------------------------
    # Подключение к устройству
    # ----------------------------------------
    def connect(self):
        devices = hid.HidDeviceFilter(
            vendor_id=self.VID,
            product_id=self.PID
        ).get_devices()

        if not devices:
            raise RuntimeError("Xiaomi Mi RC not found")

        self.device = devices[0]
        self.device.open()
        self.device.set_raw_data_handler(self._on_raw_data)
        print("MiRemote подключен. По умолчанию режим Мышь.")

    def disconnect(self):
        for btn in self._hold_flags:
            self._hold_flags[btn] = False
        for t in self._threads.values():
            t.join(timeout=0.1)
        if self.device:
            self.device.close()
            self.device = None
            print("MiRemote отключен.")

    # ----------------------------------------
    # Цикл удержания кнопок с ускорением
    # ----------------------------------------
    '''def _hold_loop(self, button, direction=True):
        step = self.base_step
        while self._hold_flags.get(button, False):
            action = self._get_current_actions().get(button)
            if action:
                action(step)
            step = min(step + self.base_step, self.max_step)
            time.sleep(self.accel_time)'''
    # ----------------------------------------
    # Поток удержания кнопки с раздельным шагом
    # ----------------------------------------
    '''def _hold_loop(self, button):
        # Определяем стартовый шаг в зависимости от кнопки
        if button in ["UP", "DOWN", "LEFT", "RIGHT"]:
            step = self.base_step_cursor
            max_step = self.max_step_cursor
        elif button in ["NETFLIX", "PRIME_VIDEO"]:
            step = self.base_step_scroll
            max_step = self.max_step_scroll
        else:
            step = None
            max_step = None

        while self._hold_flags.get(button, False):
            action = self._get_current_actions().get(button)
            if action:
                if step is not None:
                    action(step)
                else:
                    action()
            if step is not None:
                step = min(step + (self.base_step_cursor if button in ["UP","DOWN","LEFT","RIGHT"] else self.base_step_scroll), max_step)
            time.sleep(self.accel_time)'''
    def _hold_loop(self, button):
        # Определяем стартовый шаг в зависимости от кнопки
        if button in ["UP", "DOWN", "LEFT", "RIGHT"]:
            step = self.base_step_cursor
            max_step = self.max_step_cursor
            accel_counter = 1  # ускорение каждую итерацию
        elif button in ["NETFLIX", "PRIME_VIDEO"]:
            step = self.base_step_scroll
            max_step = self.max_step_scroll
            accel_counter = 0  # счётчик циклов удержания
        else:
            step = None
            max_step = None
            accel_counter = None

        while self._hold_flags.get(button, False):
            action = self._get_current_actions().get(button)
            if action:
                if step is not None:
                    action(step)
                else:
                    action()

            # Ускорение
            if step is not None:
                if button in ["UP", "DOWN", "LEFT", "RIGHT"]:
                    step = min(step + self.base_step_cursor, max_step)
                elif button in ["NETFLIX", "PRIME_VIDEO"]:
                    accel_counter += 1
                    time.sleep(self.scroll_delay)
                    if accel_counter >= self.scroll_accel_delay:
                        step = min(step + self.base_step_scroll, max_step)
                        accel_counter = 0  # сброс счетчика
            time.sleep(self.accel_time)

    # Получение текущих действий в зависимости от режима
    def _get_current_actions(self):
        return self.BUTTON_ACTIONS_MOUSE if self.mouse_mode else self.BUTTON_ACTIONS_KEYBOARD

    # ----------------------------------------
    # Обработка входных данных
    # ----------------------------------------
    def _on_raw_data(self, data):
        usage = data[1] | (data[2] << 8)
        mask = data[3]

        button = None
        if usage:
            button = self.USAGE_BUTTONS.get(usage, f"UNKNOWN_{hex(usage)}")
        elif mask:
            button = self.MASK_BUTTONS.get(mask, f"UNKNOWN_MASK_{hex(mask)}")

        if button:
            action_dict = self._get_current_actions()
            # Кнопки с удержанием
            if button in ["UP", "DOWN", "LEFT", "RIGHT", "NETFLIX", "PRIME_VIDEO"]:
                if not self._hold_flags.get(button, False):
                    self._hold_flags[button] = True
                    t = threading.Thread(target=self._hold_loop, args=(button,))
                    t.daemon = True
                    t.start()
                    self._threads[button] = t
            else:
                # Однократное действие
                action = action_dict.get(button)
                if action:
                    action()
            self._last_button = button
        else:
            # RELEASE
            if self._last_button in self._hold_flags:
                self._hold_flags[self._last_button] = False
            self._last_button = None
