"""
Table Section - テーブルセクション（Figmaデザインから変換）
"""
import flet as ft
from utils.constants import *


def create_table_section(colors):
    """テーブルセクション（Figmaデザインから変換）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    # タイトルとボタン
    title_row = ft.Row([
        ft.Text("テーブルタイトル", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
        ft.Container(
            content=ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            bgcolor=colors["success_main"], padding=ft.padding.symmetric(horizontal=12, vertical=6),
            border_radius=6,
        ),
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # ページネーション（上部）
    top_pagination = ft.Row([
        ft.Text("1〜10件（全30件中）", size=12, color="#222222"),
        ft.Container(
            content=ft.Row([ft.Text("10", size=14, color="#222222"), ft.Icon(ft.Icons.ARROW_DROP_DOWN, size=20, color="#222222")], spacing=4),
            height=32, padding=ft.padding.symmetric(horizontal=8), border=ft.border.all(1, colors["neutral_light"]),
            border_radius=6, bgcolor=colors["neutral_white"],
        ),
        ft.Text("件表示", size=12, color="#222222"),
    ], spacing=8)

    # アクションボタン
    action_buttons = ft.Row([
        ft.Container(content=ft.Row([ft.Icon(ft.Icons.ADD_CIRCLE_OUTLINE, size=16, color=colors["success_main"]), ft.Text("行選択", size=12, color=colors["success_main"])], spacing=4), padding=ft.padding.symmetric(horizontal=8, vertical=4), border=ft.border.all(1, colors["success_main"]), border_radius=4),
        ft.Container(content=ft.Row([ft.Icon(ft.Icons.EDIT, size=16, color=colors["primary_main"]), ft.Text("編集", size=12, color=colors["primary_main"])], spacing=4), padding=ft.padding.symmetric(horizontal=8, vertical=4), border=ft.border.all(1, colors["primary_main"]), border_radius=4),
        ft.Container(content=ft.Row([ft.Icon(ft.Icons.DELETE_OUTLINE, size=16, color=colors["danger_main"]), ft.Text("削除", size=12, color=colors["danger_main"])], spacing=4), padding=ft.padding.symmetric(horizontal=8, vertical=4), border=ft.border.all(1, colors["danger_main"]), border_radius=4),
    ], spacing=8)

    # ショートカット
    shortcuts = ft.Row([
        ft.Text("ショートカット", size=12, color="#222222"),
        ft.TextButton("Header1", style=ft.ButtonStyle(color=colors["primary_main"])),
        ft.TextButton("Header2", style=ft.ButtonStyle(color=colors["primary_main"])),
        ft.TextButton("Header3", style=ft.ButtonStyle(color=colors["primary_main"])),
    ], spacing=8)

    # テーブルヘッダー
    header_row = ft.Container(
        content=ft.Row([
            ft.Checkbox(value=False),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=80),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=80),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=80),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=60),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=60),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=60),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=80),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=80),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=80),
            ft.Container(content=ft.Text("Header", size=12, weight=ft.FontWeight.BOLD, color="#222222"), width=80),
        ], spacing=8),
        bgcolor="#F5F5F5",
        padding=ft.padding.symmetric(horizontal=8, vertical=8),
    )

    # テーブル行を作成
    def create_data_row(is_even=False):
        row_bg = "#F5F5F5" if is_even else colors["neutral_white"]
        return ft.Container(
            content=ft.Row([
                ft.Checkbox(value=False),
                ft.Container(content=ft.Text("Text", size=12, color="#222222"), width=80),
                ft.Container(content=ft.Text("Text", size=12, color="#222222"), width=80),
                ft.Container(content=ft.Text("Text", size=12, color="#222222"), width=80),
                ft.Container(content=ft.Text("12,345", size=12, color="#222222"), width=60),
                ft.Container(content=ft.Text("12,345", size=12, color="#222222"), width=60),
                ft.Container(content=ft.Text("12,345", size=12, color="#222222"), width=60),
                ft.Container(
                    content=ft.Container(
                        content=ft.Row([ft.Text("Tag Label", size=10, color=colors["neutral_white"]), ft.Icon(ft.Icons.CLOSE, size=12, color=colors["neutral_white"])], spacing=4),
                        bgcolor="#9381FF", padding=ft.padding.symmetric(horizontal=8, vertical=4), border_radius=12,
                    ), width=80
                ),
                ft.Container(
                    content=ft.Container(
                        content=ft.Text("Button", size=12, weight=ft.FontWeight.BOLD, color=colors["neutral_white"], text_align=ft.TextAlign.CENTER),
                        bgcolor=colors["success_main"],
                        padding=ft.padding.symmetric(horizontal=12, vertical=6),
                        border_radius=4,
                        alignment=ft.alignment.center,
                    ), width=80
                ),
                ft.Container(
                    content=ft.Row([ft.Text("Option", size=12, color=colors["primary_main"]), ft.Icon(ft.Icons.ARROW_DROP_DOWN, size=16, color=colors["primary_main"])], spacing=4),
                    width=80
                ),
                ft.Container(content=ft.TextField(height=32, text_size=12, border_color=colors["neutral_light"]), width=150),
                ft.IconButton(icon=ft.Icons.ADD_CIRCLE_OUTLINE, icon_size=20, icon_color=colors["neutral_light"]),
            ], spacing=8),
            bgcolor=row_bg,
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
        )

    # テーブルボディ（Zebraパターン：交互に背景色を変える）
    table_body = ft.Column([create_data_row(is_even=(i % 2 == 1)) for i in range(20)], spacing=0)

    # 下部ページネーションと選択トグル
    bottom_controls = ft.Row([
        ft.Row([
            ft.Switch(value=False, width=40, height=20),
            ft.Text("選択中のみを表示", size=12, color="#222222"),
        ], spacing=8),
        ft.Row([
            ft.Text("1〜10件（全30件中）", size=12, color="#222222"),
            ft.Container(
                content=ft.Row([ft.Text("10", size=14, color="#222222"), ft.Icon(ft.Icons.ARROW_DROP_DOWN, size=20, color="#222222")], spacing=4),
                height=32, padding=ft.padding.symmetric(horizontal=8),
                border=ft.border.all(1, colors["neutral_light"]), border_radius=6,
            ),
            ft.Text("件表示", size=12, color="#222222"),
        ], spacing=8),
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    return ft.Container(
        content=ft.Column([
            title_row,
            ft.Container(height=16),
            ft.Row([top_pagination, action_buttons], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            shortcuts,
            ft.Container(height=8),
            ft.Container(
                content=ft.Column([header_row, ft.Divider(height=1, color=colors["neutral_light"]), table_body], spacing=8),
                border=ft.border.all(1, colors["neutral_light"]), border_radius=8, padding=16,
            ),
            ft.Container(height=16),
            bottom_controls,
        ], spacing=8),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
