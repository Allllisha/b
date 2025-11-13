"""
Link Section - リンクセクション
"""
import flet as ft
from utils.constants import *


def section_title_local(text, color="#5258E4"):
    """ローカルセクションタイトル用のテキストコンポーネント"""
    return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)


def create_link_section(colors):
    """リンクセクション（Figmaデザインに基づく）"""

    # Type=Text: シンプルなテキストリンク（下線付き）
    text_link = ft.Text(
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
    )

    # Type=with Icon: アイコン付きリンク（ダウンロードアイコン + 下線付きテキスト）
    icon_link = ft.Row([
        ft.Icon(
            ft.Icons.DOWNLOAD,
            size=16,
            color=colors["success_main"],
        ),
        ft.Text(
            spans=[
                ft.TextSpan(
                    "Download",
                    style=ft.TextStyle(
                        decoration=ft.TextDecoration.UNDERLINE,
                        color=colors["success_main"],
                        size=12,
                    ),
                )
            ]
        ),
    ], spacing=4)

    # セクション全体を構築
    link_section = ft.Container(
        content=ft.Column([
            section_title_local("Link (Figma)", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Container(
                content=ft.Column([
                    ft.Text("Type=Text", size=14, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
                    ft.Container(height=10),
                    text_link,
                    ft.Container(height=20),

                    ft.Text("Type=with Icon", size=14, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
                    ft.Container(height=10),
                    icon_link,
                ], spacing=0),
                bgcolor="#FFFFFF",
                padding=20,
                border_radius=8,
                border=ft.border.all(1, "#E0E0E0"),
            ),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return link_section
