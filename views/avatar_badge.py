"""
Avatar Badge Section - 通知バッジ付きアバターセクション（Figmaデザイン準拠）
"""
import flet as ft
from utils.constants import *


def create_avatar_badge_section(colors):
    """Avatar with Badge（通知バッジ付きアバター）セクション"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_avatar_with_badge(avatar_type="photo", size=64, badge_count=22):
        """通知バッジ付きアバター"""
        # バッジサイズはアバターサイズに応じて調整
        if size >= 64:
            badge_size = 24
            badge_font_size = 12
        elif size >= 48:
            badge_size = 20
            badge_font_size = 10
        else:
            badge_size = 16
            badge_font_size = 8

        # アバター本体
        if avatar_type == "photo":
            # 写真（プレースホルダー - グレー円に人型アイコン）
            avatar = ft.Container(
                content=ft.Icon(ft.Icons.PERSON, size=size * 0.6, color="#999999"),
                width=size,
                height=size,
                bgcolor="#CCCCCC",
                border_radius=size / 2,
                alignment=ft.alignment.center,
            )
        elif avatar_type == "initial":
            # イニシャル
            avatar = ft.Container(
                content=ft.Text("F", size=size * 0.4, color=colors["neutral_white"], weight=ft.FontWeight.BOLD),
                width=size,
                height=size,
                bgcolor="#0265dc",
                border_radius=size / 2,
                alignment=ft.alignment.center,
            )
        else:  # icon
            # アイコン
            avatar = ft.Container(
                content=ft.Icon(ft.Icons.PERSON, size=size * 0.6, color=colors["neutral_white"]),
                width=size,
                height=size,
                bgcolor="#0265dc",
                border_radius=size / 2,
                alignment=ft.alignment.center,
            )

        # バッジ（通知数）
        badge_text = str(badge_count) if badge_count < 100 else "99+"
        badge = ft.Container(
            content=ft.Text(badge_text, size=badge_font_size, color=colors["neutral_white"], weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            width=badge_size,
            height=badge_size,
            bgcolor="#E53E3E",  # 赤
            border_radius=badge_size / 2,
            alignment=ft.alignment.center,
        )

        # アバターとバッジを重ねる（Stack使用）
        return ft.Container(
            content=ft.Stack([
                avatar,
                ft.Container(
                    content=badge,
                    left=size * 0.65,
                    top=0,
                ),
            ]),
            width=size + badge_size * 0.5,
            height=size + badge_size * 0.5,
        )

    return ft.Container(
        content=ft.Column([
            section_title("Avatar with Badge（Figmaデザイン）", color=colors["primary_main"]),
            ft.Container(height=20),

            # 大サイズ（64px）
            ft.Text("Large (64px)", size=14, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=12),
            ft.Row([
                create_avatar_with_badge("photo", 64, 22),
                ft.Container(width=16),
                create_avatar_with_badge("initial", 64, 22),
                ft.Container(width=16),
                create_avatar_with_badge("icon", 64, 22),
            ], spacing=0),
            ft.Container(height=24),

            # 中サイズ（48px）
            ft.Text("Medium (48px)", size=14, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=12),
            ft.Row([
                create_avatar_with_badge("photo", 48, 9),
                ft.Container(width=16),
                create_avatar_with_badge("initial", 48, 9),
                ft.Container(width=16),
                create_avatar_with_badge("icon", 48, 9),
            ], spacing=0),
            ft.Container(height=24),

            # 小サイズ（32px）
            ft.Text("Small (32px)", size=14, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=12),
            ft.Row([
                create_avatar_with_badge("photo", 32, 3),
                ft.Container(width=16),
                create_avatar_with_badge("initial", 32, 3),
                ft.Container(width=16),
                create_avatar_with_badge("icon", 32, 3),
            ], spacing=0),
            ft.Container(height=24),

            ft.Divider(height=1, color="#E0E0E0"),
            ft.Container(height=16),
            ft.Text("※ 写真アバターはプレースホルダー表示。実際には画像URLを指定可能", size=12, color="#666666"),
        ], spacing=0),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
