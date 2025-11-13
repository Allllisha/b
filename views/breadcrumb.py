"""
Breadcrumb Section - Breadcrumbコンポーネント（Figmaデザインに基づく）
"""
import flet as ft
from utils.constants import *


def create_breadcrumb_section(colors):
    """Breadcrumbコンポーネント（Figmaデザインに基づく）"""

    def section_title_local(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_breadcrumb_item(text, is_active=True):
        """パンくずアイテムを作成"""
        return ft.Text(
            text,
            size=12,
            weight=ft.FontWeight.BOLD,
            color="#5258E4" if is_active else "#6D6D6D",
        )

    def create_arrow_icon():
        """矢印アイコンを作成"""
        return ft.Icon(
            name="keyboard_arrow_right",
            size=16,
            color="#6D6D6D",
        )

    def create_overflow_icon():
        """Overflowアイコン（3つのドット）を作成"""
        return ft.Container(
            content=ft.Icon(
                name="more_horiz",
                size=16,
                color="#5258E4",
            ),
            padding=4,
            border_radius=100,
        )

    # 通常版Breadcrumb（全表示）
    breadcrumb_normal = ft.Row([
        create_breadcrumb_item("HOME"),
        create_arrow_icon(),
        create_breadcrumb_item("Page"),
        create_arrow_icon(),
        create_breadcrumb_item("Page"),
        create_arrow_icon(),
        create_breadcrumb_item("Page"),
        create_arrow_icon(),
        create_breadcrumb_item("Page"),
        create_arrow_icon(),
        create_breadcrumb_item("Page", is_active=False),
    ], spacing=8)

    # Overflow版Breadcrumb（省略表示）
    breadcrumb_overflow = ft.Row([
        create_breadcrumb_item("HOME"),
        create_arrow_icon(),
        create_overflow_icon(),
        create_arrow_icon(),
        create_breadcrumb_item("Page"),
        create_arrow_icon(),
        create_breadcrumb_item("Page", is_active=False),
    ], spacing=8)

    return ft.Container(
        content=ft.Column([
            section_title_local("BREADCRUMB コンポーネント", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Text(
                "Figmaデザインシステムから取得したBreadcrumb（パンくずリスト）",
                size=14,
                color="#666666",
            ),
            ft.Container(height=30),

            # 通常版
            ft.Text("通常版（全表示）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            breadcrumb_normal,
            ft.Container(height=30),

            # Overflow版
            ft.Text("Overflow版（省略表示）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            breadcrumb_overflow,
        ], spacing=5),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )
