"""
Notification Section - 通知コンポーネントセクション（Figmaデザイン準拠）
"""
import flet as ft
from utils.constants import *


def create_notification_section(colors):
    """Notificationセクション（Figmaデザインから変換）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_notification(title="Notification Title", message="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", with_buttons=False, icon_type=None):
        """Notificationコンポーネントを作成"""

        icon_colors = {
            "error": "#d31510",
            "info": "#0265dc",
            "success": "#007a4d",
            "warning": "#ffa037"
        }

        icon_map = {
            "error": ft.Icons.ERROR,
            "info": ft.Icons.INFO,
            "success": ft.Icons.CHECK_CIRCLE,
            "warning": ft.Icons.WARNING
        }

        content_row = []

        # アイコン（オプション）
        if icon_type and icon_type in icon_map:
            content_row.append(
                ft.Icon(
                    icon_map[icon_type],
                    size=32,
                    color=icon_colors[icon_type]
                )
            )

        # タイトルと本文
        text_content = ft.Column([
            ft.Row([
                ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color="#222222", expand=True),
                ft.IconButton(icon=ft.Icons.CLOSE, icon_size=20, icon_color=colors["neutral_light"], padding=0),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Text(message, size=12, color="#222222"),
        ], spacing=8, expand=True)

        content_row.append(text_content)

        # ボタン（オプション）
        button_row = None
        if with_buttons:
            button_row = ft.Row([
                ft.Container(
                    content=ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color=colors["success_main"]),
                    height=32,
                    padding=ft.padding.symmetric(horizontal=12, vertical=4),
                    border=ft.border.all(1, colors["success_main"]),
                    border_radius=8,
                ),
                ft.Container(
                    content=ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
                    height=32,
                    padding=ft.padding.symmetric(horizontal=12, vertical=4),
                    bgcolor=colors["success_main"],
                    border_radius=8,
                ),
            ], spacing=4, alignment=ft.MainAxisAlignment.END)

        main_content = ft.Column([
            ft.Row(content_row, spacing=16, expand=True),
        ], spacing=8)

        if button_row:
            main_content.controls.append(button_row)

        return ft.Container(
            content=main_content,
            width=416,
            bgcolor=colors["neutral_white"],
            padding=ft.padding.only(left=24, right=24, top=24, bottom=16),
            border_radius=8,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=4,
                offset=ft.Offset(0, 2),
                color="rgba(34,34,34,0.08)"
            ),
        )

    return ft.Container(
        content=ft.Column([
            section_title("Notification (LV2 - Figmaデザイン)", color=colors["primary_main"]),
            ft.Container(height=10),

            ft.Text("Button無し", size=12, color="#222222"),
            ft.Container(height=5),
            create_notification(),
            ft.Container(height=30),

            ft.Text("Basic", size=12, color="#222222"),
            ft.Container(height=5),
            create_notification(with_buttons=True),
            ft.Container(height=30),

            ft.Text("With Icon / Error", size=12, color="#222222"),
            ft.Container(height=5),
            create_notification(with_buttons=True, icon_type="error"),
            ft.Container(height=30),

            ft.Text("With Icon / Information", size=12, color="#222222"),
            ft.Container(height=5),
            create_notification(with_buttons=True, icon_type="info"),
            ft.Container(height=30),

            ft.Text("With Icon / Success", size=12, color="#222222"),
            ft.Container(height=5),
            create_notification(with_buttons=True, icon_type="success"),
            ft.Container(height=30),

            ft.Text("With Icon / Warning", size=12, color="#222222"),
            ft.Container(height=5),
            create_notification(with_buttons=True, icon_type="warning"),
        ], spacing=0),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
