import flet as ft
from flet import Container, Column, Row, ResponsiveRow, Page

from module import AppDesignCT, AppSpineHtLoss, AppMean, AppVol


def main(page: ft.Page):
    # GET INDEX TAB
    def change_tab(e):
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        page.update()
    
    page.title = "Design CTER Protocol"
    page.window.min_width = 780
    # page.window_min_width = 780
    page.window.width = 780
    # page.window_width = 780
    page.window.min_height = 840
    # page.window_min_height = 840
    page.window.height = 840
    # page.window_height = 840
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
            ft.NavigationBarDestination(icon=ft.icons.BRUSH_ROUNDED, label="Design"),
            ft.NavigationBarDestination(icon=ft.icons.CALCULATE_ROUNDED, label="Calculate"),
        ]
    )
    
    tab_1 = AppDesignCT()
    tab_2 = ft.Column(controls=[AppMean(), AppVol(), AppSpineHtLoss()]) 
    ## Default
    tab_1.visible = True; tab_2.visible = False
    #ft.Text("Tab 2",size=30,visible=False)
    
    page.add(tab_1, tab_2)

def toggle_theme(page: ft.Page):
    if page.theme_mode == ft.ThemeMode.LIGHT:
        page.theme_mode = ft.ThemeMode.DARK
        page.appbar.trailing = ft.IconButton(icon=ft.icons.DARK_MODE_OUTLINED, tooltip="Toggle theme", on_click=lambda e: toggle_theme(page))
        
    else:
        page.theme_mode = ft.ThemeMode.LIGHT
        page.appbar.trailing = ft.IconButton(icon=ft.icons.BRIGHTNESS_5, tooltip="Toggle theme", on_click=lambda e: toggle_theme(page))
    # page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
