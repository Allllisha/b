"""
Tab Bar Variations Section - タブバーバリエーションセクション（Figmaデザイン準拠）
"""
import flet as ft
from utils.constants import *


def create_tab_bar_variations_section(colors):
    """タブバーバリエーションセクション（LV1 / Tab Bar - Figmaデザイン）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_single_tab(label, is_selected=False):
        """単一タブを作成"""
        neutral_main_opacity_16 = "rgba(34,34,34,0.16)"

        return ft.Container(
            content=ft.Row([
                ft.Icon(
                    ft.Icons.LABEL,
                    size=16,
                    color=colors["neutral_black"] if is_selected else colors["neutral_light"],
                ),
                ft.Text(
                    label,
                    size=12,
                    weight=ft.FontWeight.BOLD,
                    color=colors["neutral_black"] if is_selected else colors["neutral_light"],
                ),
            ], spacing=8),
            height=40,
            padding=ft.padding.symmetric(horizontal=16, vertical=8),
            border=ft.border.only(
                bottom=ft.BorderSide(
                    2 if is_selected else 1,
                    colors["neutral_black"] if is_selected else neutral_main_opacity_16,
                )
            ),
        )

    def create_tab_bar_1():
        """Tab=1: 1つのタブ"""
        return ft.Row([create_single_tab("Label", is_selected=True)], spacing=0)

    def create_tab_bar_2():
        """Tab=2: 2つのタブ"""
        return ft.Row([
            create_single_tab("Label", is_selected=True),
            create_single_tab("Label", is_selected=False),
        ], spacing=0)

    def create_tab_bar_3():
        """Tab=3: 3つのタブ"""
        return ft.Row([
            create_single_tab("Label", is_selected=True),
            create_single_tab("Label", is_selected=False),
            create_single_tab("Label", is_selected=False),
        ], spacing=0)

    def create_tab_bar_4():
        """Tab=4: 4つのタブ"""
        return ft.Row([
            create_single_tab("Label", is_selected=True),
            create_single_tab("Label", is_selected=False),
            create_single_tab("Label", is_selected=False),
            create_single_tab("Label", is_selected=False),
        ], spacing=0)

    def create_tab_bar_5():
        """Tab=5: 5つのタブ"""
        return ft.Row([
            create_single_tab("Label", is_selected=True),
            create_single_tab("Label", is_selected=False),
            create_single_tab("Label", is_selected=False),
            create_single_tab("Label", is_selected=False),
            create_single_tab("Label", is_selected=False),
        ], spacing=0)

    return ft.Container(
        content=ft.Column([
            section_title("Tab Bar Variations (LV1 - Figmaデザイン)", color=colors["primary_main"]),
            ft.Container(height=10),

            ft.Text("Tab=1", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_tab_bar_1(),
            ft.Container(height=20),

            ft.Text("Tab=2", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_tab_bar_2(),
            ft.Container(height=20),

            ft.Text("Tab=3", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_tab_bar_3(),
            ft.Container(height=20),

            ft.Text("Tab=4", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_tab_bar_4(),
            ft.Container(height=20),

            ft.Text("Tab=5", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_tab_bar_5(),
        ], spacing=0),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
