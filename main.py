import flet as ft
import pyperclip
import datetime
from flet import Container, Column, Row, ResponsiveRow, Page

from module.designct_app import DesignCTApp
from designcter._utils import dash_if_blank


def main(page: ft.Page):
    # GET INDEX TAB
    def change_tab(e):
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        page.update()
    
    page.title = "Design CTER Protocol"
    page.window_min_width = 780
    page.window_width = 780
    page.window_min_height = 840
    page.window_height = 840
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        bgcolor=ft.colors.SURFACE_VARIANT,
        middle=ft.Text("Design CTER Protocol", weight=ft.FontWeight.BOLD),
        trailing=ft.IconButton(icon=ft.icons.BRIGHTNESS_2_OUTLINED, tooltip="Toggle theme", on_click=lambda e: toggle_theme(page))
    )
    
    page.navigation_bar = ft.NavigationBar( 
        selected_index = 0,
        on_change= change_tab, # KEY
        destinations=[
            ft.NavigationDestination(icon=ft.icons.BRUSH_ROUNDED, label="Design"),
            ft.NavigationDestination(icon=ft.icons.CALCULATE_ROUNDED, label="Calculate"),
        ]
    )
    
    tab_1 = DesignCTApp()
    tab_2 = ft.Text("Tab 2",size=30,visible=False)
    
    page.add(tab_1, tab_2)

def toggle_theme(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
