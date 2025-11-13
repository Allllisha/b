"""
Test Layout Templates - レイアウトテンプレートのみを表示
"""
import flet as ft
from utils.constants import COLORS
from views.layout_templates import create_layout_templates_section

def main(page: ft.Page):
    """レイアウトテンプレートセクションのみを表示"""
    page.title = "Layout Templates Test"
    page.padding = 40
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = "#F5F5F5"

    # フォント設定
    page.fonts = {
        "Noto Sans JP": "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100;300;400;500;700;900&display=swap"
    }
    page.theme = ft.Theme(font_family="Noto Sans JP")

    # レイアウトテンプレートセクションを表示
    content = ft.Column([
        ft.Text("Layout Templates Test", size=32, weight=ft.FontWeight.BOLD, color="#222222"),
        ft.Divider(height=40, color="transparent"),
        create_layout_templates_section(COLORS),
    ], spacing=10, scroll=ft.ScrollMode.AUTO)

    page.add(content)

if __name__ == "__main__":
    ft.app(target=main)
