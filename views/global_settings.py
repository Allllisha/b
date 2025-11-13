"""
Global Settings Section - グローバル設定の表示セクション
"""
import flet as ft
from utils.constants import *


def create_global_settings_section(colors):
    """グローバル設定の表示セクション"""

    def section_title_local(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    # カラーパレット表示
    color_items = []
    for name, value in COLORS.items():
        color_items.append(
            ft.Row([
                ft.Container(width=60, height=30, bgcolor=value, border_radius=4),
                ft.Text(f"{name}: {value}", size=12, color="#222222"),
            ], spacing=10)
        )

    # Elevation表示
    elevation_items = []
    for name, shadow in ELEVATIONS.items():
        elevation_items.append(
            ft.Column([
                ft.Text(name, size=10, color="#666666"),
                ft.Container(
                    width=100,
                    height=60,
                    bgcolor="#F3F4FB",
                    border_radius=8,
                    shadow=[shadow] if shadow else None,
                ),
            ], spacing=8)
        )

    # アイコン表示（一部のみ）
    icon_samples = ["home", "search", "settings", "person", "info", "help", "delete", "edit"]
    icon_items = []
    for icon_name in icon_samples:
        if icon_name in ICONS:
            icon_items.append(
                ft.Column([
                    ft.Icon(ICONS[icon_name], size=24, color="#222222"),
                    ft.Text(icon_name, size=8, color="#666666"),
                ], spacing=4, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            )

    # ディバイダー表示
    divider_items = []
    for name, color in DIVIDER_COLORS.items():
        divider_items.append(
            ft.Column([
                ft.Text(name, size=10, color="#666666"),
                ft.Container(
                    width=120,
                    height=1,
                    bgcolor=color,
                ),
            ], spacing=8)
        )

    return ft.Container(
        content=ft.Column([
            section_title_local("グローバルデザインシステム設定", color=colors["primary_main"]),
            ft.Container(height=20),

            # Colors
            ft.Text("COLORS", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Column(color_items, spacing=5),
            ft.Divider(height=30, color="transparent"),

            # Elevations
            ft.Text("ELEVATIONS", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Row(elevation_items, spacing=15, wrap=True),
            ft.Divider(height=30, color="transparent"),

            # Icons (サンプル)
            ft.Text("ICONS (サンプル)", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Row(icon_items, spacing=20),
            ft.Divider(height=30, color="transparent"),

            # Logo
            ft.Text("LOGO", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Text(LOGO_TEXT, size=14, color=colors["primary_main"]),
            ft.Divider(height=30, color="transparent"),

            # Link Styles
            ft.Text("LINK_STYLES", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Text(
                spans=[
                    ft.TextSpan(
                        "Link",
                        style=ft.TextStyle(
                            decoration=ft.TextDecoration.UNDERLINE,
                            color=colors["success_main"],
                            size=12,
                        ),
                    )
                ]
            ),
            ft.Divider(height=30, color="transparent"),

            # Dividers
            ft.Text("DIVIDER_COLORS", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Row(divider_items, spacing=20),
        ], spacing=5),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )
