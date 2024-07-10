import flet as ft
import pyperclip
import datetime
from flet import Container, Column, Row, ResponsiveRow, Page

from designct_app import DesignCTApp
from designcter._utils import dash_if_blank


def main(page: ft.Page):
    page.title = "Design CTER Protocol"
    page.window_min_width = 780
    page.window_width = 780
    page.window_min_height = 800
    page.window_height = 800
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        bgcolor=ft.colors.SURFACE_VARIANT,
        middle=ft.Text("Design CTER Protocol", weight=ft.FontWeight.BOLD),
        trailing=ft.IconButton(icon=ft.icons.BRIGHTNESS_2_OUTLINED, tooltip="Toggle theme", on_click=lambda e: toggle_theme(page))
    )

    app = DesignCTApp()
    page.add(app)

def toggle_theme(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
