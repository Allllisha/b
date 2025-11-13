"""
Header Section - ヘッダーコンポーネント（Figmaデザイン準拠）
"""
import flet as ft
from utils.constants import *


def create_header_section(colors):
    """Headerセクションを作成（Figmaデザインに基づく）"""

    # ヘッダー用の色設定
    header_primary_bg = "#5258E4"  # 紫色の背景
    header_secondary_bg = "#E8E7F0"  # 灰色の背景

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_header_logo():
        """Type=Logo - ロゴヘッダーを作成"""
        return ft.Container(
            content=ft.Row(
                [
                    # 左側：ロゴ
                    ft.Text(
                        "FDS Fleet Design System®",
                        size=14,
                        weight=ft.FontWeight.BOLD,
                        color=colors["neutral_white"],
                    ),
                    # 右側：アイコンボタン群（Figmaデザイン準拠）
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.NOTIFICATIONS,
                                icon_color=colors["neutral_white"],
                                icon_size=20,
                                padding=0,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SETTINGS,
                                icon_color=colors["neutral_white"],
                                icon_size=20,
                                padding=0,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.HELP,
                                icon_color=colors["neutral_white"],
                                icon_size=20,
                                padding=0,
                            ),
                        ],
                        spacing=16,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=header_primary_bg,
            padding=ft.padding.only(left=20, right=20, top=12, bottom=12),
            height=48,
        )

    def create_header_title():
        """Type=Title - タイトルヘッダーを作成"""
        return ft.Container(
            content=ft.Row(
                [
                    # 左側：メニューアイコンとタイトル
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.MENU,
                                icon_color="#6D6D6D",
                                icon_size=20,
                                padding=0,
                            ),
                            ft.Text(
                                "Screen Title",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color="#222222",
                            ),
                        ],
                        spacing=8,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    # 右側：アイコンボタン群（Figmaデザイン準拠）
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.NOTIFICATIONS,
                                icon_color="#6D6D6D",
                                icon_size=20,
                                padding=0,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SETTINGS,
                                icon_color="#6D6D6D",
                                icon_size=20,
                                padding=0,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.HELP,
                                icon_color="#6D6D6D",
                                icon_size=20,
                                padding=0,
                            ),
                        ],
                        spacing=16,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=header_secondary_bg,
            padding=ft.padding.only(left=20, right=20, top=12, bottom=12),
            height=48,
        )

    def create_header_with_searchbox():
        """Type=Logo with Searchbox - 検索ボックス付きヘッダーを作成"""
        return ft.Container(
            content=ft.Row(
                [
                    # 左側：ロゴと検索ボックス
                    ft.Row(
                        [
                            ft.Text(
                                "FDS Fleet Design System®",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=colors["neutral_white"],
                            ),
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.Icons.SEARCH, size=16, color="#6D6D6D"),
                                        ft.Text("Search", size=14, color="#6D6D6D"),
                                    ],
                                    spacing=8,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor=colors["neutral_white"],
                                border_radius=4,
                                padding=ft.padding.symmetric(horizontal=12, vertical=4),
                                width=200,
                                height=28,
                            ),
                        ],
                        spacing=16,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    # 右側：アイコンボタン群（Figmaデザイン準拠）
                    ft.Row(
                        [
                            ft.IconButton(icon=ft.Icons.NOTIFICATIONS, icon_color=colors["neutral_white"], icon_size=20, padding=0),
                            ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=colors["neutral_white"], icon_size=20, padding=0),
                            ft.IconButton(icon=ft.Icons.HELP, icon_color=colors["neutral_white"], icon_size=20, padding=0),
                        ],
                        spacing=16,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=header_primary_bg,
            padding=ft.padding.only(left=20, right=20, top=12, bottom=12),
            height=48,
        )

    # セクション全体を構築
    header_section = ft.Container(
        content=ft.Column(
            [
                section_title("Header Components (Figma)", color=colors["primary_main"]),
                ft.Container(height=10),

                # Type=Logo
                ft.Column(
                    [
                        ft.Text("Type=Logo", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
                        ft.Container(height=5),
                        create_header_logo(),
                    ],
                    spacing=0,
                ),

                ft.Container(height=20),

                # Type=Title
                ft.Column(
                    [
                        ft.Text("Type=Title", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
                        ft.Container(height=5),
                        create_header_title(),
                    ],
                    spacing=0,
                ),

                ft.Container(height=20),

                # Type=Logo with Searchbox
                ft.Column(
                    [
                        ft.Text("Type=Logo with Searchbox", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
                        ft.Container(height=5),
                        create_header_with_searchbox(),
                    ],
                    spacing=0,
                ),
            ],
            spacing=0,
        ),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return header_section
