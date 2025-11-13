"""
Divider Section - Dividerコンポーネント（Figmaデザインに基づく）
"""
import flet as ft
from utils.constants import *


def create_divider_section(colors):
    """Dividerコンポーネント（Figmaデザインに基づく）"""

    def section_title_local(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_color_chip(chip_color, gradient_color):
        """カラーチップを作成（Figmaデザイン通り）"""
        return ft.Container(
            content=ft.Row([
                # 左側: 濃い色
                ft.Container(
                    width=16,
                    height=32,
                    bgcolor=chip_color,
                    border_radius=ft.border_radius.only(top_left=8, bottom_left=8),
                ),
                # 右側: グラデーション風（薄い色）
                ft.Container(
                    width=16,
                    height=32,
                    bgcolor=gradient_color,
                    border_radius=ft.border_radius.only(top_right=8, bottom_right=8),
                ),
            ], spacing=0),
            width=32,
            height=32,
        )

    # Primary Divider行
    primary_row = ft.Row([
        # カラーチップ
        create_color_chip("#4046ca", "rgba(64, 70, 202, 0.12)"),
        ft.Container(width=16),
        # Divider（Containerで直接描画）
        ft.Container(
            width=120,
            height=32,
            alignment=ft.alignment.center,
            content=ft.Container(
                width=120,
                height=1,
                bgcolor=DIVIDER_COLORS["primary"],
            ),
        ),
        ft.Container(width=16),
        # ラベル
        ft.Container(
            content=ft.Text("Primary", size=10, color="rgba(0, 0, 0, 0.6)"),
            width=50,
            height=32,
            alignment=ft.alignment.center_left,
        ),
    ], spacing=0)

    # Neutral Divider行
    neutral_row = ft.Row([
        # カラーチップ
        create_color_chip("#000000", "rgba(0, 0, 0, 0.12)"),
        ft.Container(width=16),
        # Divider（Containerで直接描画）
        ft.Container(
            width=120,
            height=32,
            alignment=ft.alignment.center,
            content=ft.Container(
                width=120,
                height=1,
                bgcolor=DIVIDER_COLORS["neutral"],
            ),
        ),
        ft.Container(width=16),
        # ラベル
        ft.Container(
            content=ft.Text("Neutral", size=10, color="rgba(0, 0, 0, 0.6)"),
            width=50,
            height=32,
            alignment=ft.alignment.center_left,
        ),
    ], spacing=0)

    # Static Divider行（カラー背景上）
    static_row = ft.Row([
        # カラーチップ
        create_color_chip("#FFFFFF", "rgba(255, 255, 255, 0.25)"),
        ft.Container(width=16),
        # Divider（カラー背景上、Containerで直接描画）
        ft.Container(
            width=120,
            height=32,
            bgcolor="#898ddc",
            alignment=ft.alignment.center,
            content=ft.Container(
                width=120,
                height=1,
                bgcolor=DIVIDER_COLORS["on_colored"],
            ),
        ),
        ft.Container(width=16),
        # ラベル
        ft.Container(
            content=ft.Text("Static", size=10, color="rgba(0, 0, 0, 0.6)"),
            width=50,
            height=32,
            alignment=ft.alignment.center_left,
        ),
        ft.Container(width=10),
        # 注釈
        ft.Container(
            content=ft.Text(
                "OnColored(Primary, NeutralのBoolean)",
                size=10,
                color="rgba(0, 0, 0, 0.6)"
            ),
            height=32,
            alignment=ft.alignment.center_left,
        ),
    ], spacing=0)

    return ft.Container(
        content=ft.Column([
            section_title_local("DIVIDER コンポーネント", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Text(
                "Figmaデザインシステムから取得した3種類のDivider（区切り線）",
                size=14,
                color="#666666",
            ),
            ft.Container(height=30),

            # 3つのDivider行
            primary_row,
            ft.Container(height=16),
            neutral_row,
            ft.Container(height=16),
            static_row,
        ], spacing=5),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )
