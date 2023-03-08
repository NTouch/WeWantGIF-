from controller.appcontroller import AppController
from view.screen import Screen

console_screen = Screen()
controller = AppController(console_screen)

controller.run_app()
