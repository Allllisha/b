"""
Footer Section - フッターセクション
"""
import flet as ft
from utils.constants import *


def section_title(text, color="#333333"):
    """セクションタイトル用のテキストコンポーネント"""
    return ft.Text(
        text,
        size=24,
        weight=ft.FontWeight.BOLD,
        color=color,
    )


def create_footer_section(colors):
    """フッターセクションを作成（Figmaデザインに基づく）"""

    def create_footer_primary():
        """Color=Primary フッター（紫背景）"""
        return ft.Container(
            content=ft.Text(
                "Fleet Inc.",
                size=12,
                color=colors["neutral_white"],
                weight=ft.FontWeight.NORMAL,
                text_align=ft.TextAlign.CENTER,
            ),
            bgcolor=colors["primary_main"],
            padding=ft.padding.only(left=20, right=20, top=8, bottom=8),
            height=32,
            alignment=ft.alignment.center,
        )

    def create_footer_light():
        """Color=Light フッター（薄い背景）"""
        return ft.Container(
            content=ft.Text(
                "Fleet Inc.",
                size=12,
                color=colors["primary_main"],
                weight=ft.FontWeight.NORMAL,
                text_align=ft.TextAlign.CENTER,
            ),
            bgcolor="#F5F5F5",
            padding=ft.padding.only(left=20, right=20, top=8, bottom=8),
            height=32,
            alignment=ft.alignment.center,
        )

    # セクション全体を構築
    footer_section = ft.Container(
        content=ft.Column([
            section_title("Footer (Figma)", color=colors["primary_main"]),
            ft.Container(height=10),

            # Color=Primary
            ft.Text("Color=Primary", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_footer_primary(),

            ft.Container(height=20),

            # Color=Light
            ft.Text("Color=Light", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_footer_light(),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return footer_section
