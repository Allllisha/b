"""
Account Menu Section - アカウントメニューセクション
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


def create_account_menu_section(colors):
    """アカウントメニューセクションを作成（Figmaデザインに基づく）"""

    def create_account_menu_icon_label(on_colored=False):
        """Icon + Label スタイルのアカウントメニュー"""
        if on_colored:
            # 色付き背景用（白テキスト）
            return ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.PERSON, size=20, color=colors["neutral_white"]),
                    ft.Text("ログイン", size=14, color=colors["neutral_white"], weight=ft.FontWeight.BOLD),
                ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                bgcolor="transparent",
                border=ft.border.all(1, colors["neutral_white"]),
                border_radius=8,
                padding=ft.padding.only(left=16, right=16, top=8, bottom=8),
                width=120,
                height=40,
            )
        else:
            # 通常背景用（青テキスト）
            return ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.PERSON, size=20, color=colors["primary_main"]),
                    ft.Text("ログイン", size=14, color=colors["primary_main"], weight=ft.FontWeight.BOLD),
                ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                bgcolor="transparent",
                border=ft.border.all(1, colors["primary_main"]),
                border_radius=8,
                padding=ft.padding.only(left=16, right=16, top=8, bottom=8),
                width=120,
                height=40,
            )

    def create_account_menu_avatar_label(on_colored=False):
        """Avatar + Label スタイルのアカウントメニュー"""
        if on_colored:
            # 色付き背景用（白テキスト）
            return ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Icon(ft.Icons.PERSON, size=16, color=colors["primary_main"]),
                        bgcolor=colors["neutral_white"],
                        border_radius=100,
                        width=24,
                        height=24,
                        alignment=ft.alignment.center,
                    ),
                    ft.Text("ログイン", size=14, color=colors["neutral_white"], weight=ft.FontWeight.BOLD),
                ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                bgcolor="transparent",
                border=ft.border.all(1, colors["neutral_white"]),
                border_radius=8,
                padding=ft.padding.only(left=12, right=16, top=8, bottom=8),
                width=120,
                height=40,
            )
        else:
            # 通常背景用（青テキスト）
            return ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Icon(ft.Icons.PERSON, size=16, color=colors["neutral_white"]),
                        bgcolor=colors["primary_main"],
                        border_radius=100,
                        width=24,
                        height=24,
                        alignment=ft.alignment.center,
                    ),
                    ft.Text("ログイン", size=14, color=colors["primary_main"], weight=ft.FontWeight.BOLD),
                ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                bgcolor="transparent",
                border=ft.border.all(1, colors["primary_main"]),
                border_radius=8,
                padding=ft.padding.only(left=12, right=16, top=8, bottom=8),
                width=120,
                height=40,
            )

    def create_account_menu_icon_only(on_colored=False):
        """Icon only スタイルのアカウントメニュー"""
        if on_colored:
            # 色付き背景用（白アイコン）
            return ft.Container(
                content=ft.Icon(ft.Icons.PERSON, size=20, color=colors["neutral_white"]),
                bgcolor="transparent",
                border=ft.border.all(1, colors["neutral_white"]),
                border_radius=8,
                padding=6,
                width=32,
                height=32,
                alignment=ft.alignment.center,
            )
        else:
            # 通常背景用（青アイコン）
            return ft.Container(
                content=ft.Icon(ft.Icons.PERSON, size=20, color=colors["primary_main"]),
                bgcolor="transparent",
                border=ft.border.all(1, colors["primary_main"]),
                border_radius=8,
                padding=6,
                width=32,
                height=32,
                alignment=ft.alignment.center,
            )

    def create_account_menu_avatar_only(on_colored=False):
        """Avatar only スタイルのアカウントメニュー"""
        if on_colored:
            # 色付き背景用（白背景のアバター）
            return ft.Container(
                content=ft.Icon(ft.Icons.PERSON, size=16, color=colors["primary_main"]),
                bgcolor=colors["neutral_white"],
                border_radius=100,
                width=32,
                height=32,
                alignment=ft.alignment.center,
            )
        else:
            # 通常背景用（青背景のアバター）
            return ft.Container(
                content=ft.Icon(ft.Icons.PERSON, size=16, color=colors["neutral_white"]),
                bgcolor=colors["primary_main"],
                border_radius=100,
                width=32,
                height=32,
                alignment=ft.alignment.center,
            )

    # セクション全体を構築
    account_menu_section = ft.Container(
        content=ft.Column([
            section_title("Account Menu (Figma)", color=colors["primary_main"]),
            ft.Container(height=10),

            # 通常背景バージョン
            ft.Text("Normal Background", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Row([
                ft.Column([
                    ft.Text("Icon + Label", size=12, color="#666666"),
                    ft.Container(height=5),
                    create_account_menu_icon_label(on_colored=False),
                ], spacing=0),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Avatar + Label", size=12, color="#666666"),
                    ft.Container(height=5),
                    create_account_menu_avatar_label(on_colored=False),
                ], spacing=0),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Icon Only", size=12, color="#666666"),
                    ft.Container(height=5),
                    create_account_menu_icon_only(on_colored=False),
                ], spacing=0),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Avatar Only", size=12, color="#666666"),
                    ft.Container(height=5),
                    create_account_menu_avatar_only(on_colored=False),
                ], spacing=0),
            ], spacing=0),

            ft.Container(height=20),

            # 色付き背景バージョン
            ft.Text("Colored Background", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text("Icon + Label", size=12, color=colors["neutral_white"]),
                        ft.Container(height=5),
                        create_account_menu_icon_label(on_colored=True),
                    ], spacing=0),
                    ft.Container(width=20),
                    ft.Column([
                        ft.Text("Avatar + Label", size=12, color=colors["neutral_white"]),
                        ft.Container(height=5),
                        create_account_menu_avatar_label(on_colored=True),
                    ], spacing=0),
                    ft.Container(width=20),
                    ft.Column([
                        ft.Text("Icon Only", size=12, color=colors["neutral_white"]),
                        ft.Container(height=5),
                        create_account_menu_icon_only(on_colored=True),
                    ], spacing=0),
                    ft.Container(width=20),
                    ft.Column([
                        ft.Text("Avatar Only", size=12, color=colors["neutral_white"]),
                        ft.Container(height=5),
                        create_account_menu_avatar_only(on_colored=True),
                    ], spacing=0),
                ], spacing=0),
                bgcolor=colors["primary_main"],
                padding=20,
                border_radius=8,
            ),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return account_menu_section
