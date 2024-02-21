from nicegui import ui
import lirc

REMOTE = "NAD_SR6"
lirc_client = lirc.Client()


def radio_one():
    lirc_client.send_once(remote=REMOTE, key="tuner-1")
    lirc_client.send_once(remote=REMOTE, key="tuner-enter")
    ui.notify("tuning to CBC radio one Halifax")


def radio_two():
    lirc_client.send_once(remote=REMOTE, key="tuner-2")
    lirc_client.send_once(remote=REMOTE, key="tuner-enter")
    ui.notify("tuning to CBC radio 2")


def main():
    with ui.column().classes("w-full items-center"):
        ui.button("CBC Radio 1", on_click=radio_one)
        ui.button("CBC Radio 2", on_click=radio_two)
    ui.run(host="0.0.0.0", port=8080, dark=True)


if __name__ in {"__main__", "__mp_main__"}:
    main()
