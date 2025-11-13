"""
Collapse UI Component
Figmaデザインに基づくアコーディオン式Collapse
"""
import flet as ft
from utils.constants import *


def create_collapse_section(colors):
    """Collapseセクション（アコーディオン式）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    # 展開/折りたたみ状態を管理
    is_open = [True]  # リストで包んで参照を保持

    # Collapseコンポーネント
    collapse_content = ft.Column([
        # タイトルと説明
        ft.Container(
            content=ft.Row([
                ft.Text(
                    "メインタイトルが入ります",
                    size=16,
                    color="#222222",
                    weight=ft.FontWeight.NORMAL,
                    expand=True,
                ),
                # ボタングループ
                ft.Row([
                    ft.Container(
                        content=ft.Text(
                            "キャンセル",
                            size=11,
                            color="#007a4d",
                            weight=ft.FontWeight.BOLD,
                        ),
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        border_radius=100,
                    ),
                    ft.Container(
                        content=ft.Text(
                            "編集内容を保存",
                            size=11,
                            color="#ffffff",
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#007a4d",
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        border_radius=4,
                    ),
                ], spacing=4),
            ]),
            padding=ft.padding.only(bottom=16),
        ),

        # フォームフィールド（例として4つ）
        ft.Row([
            ft.Column([
                ft.Text("Form Label *", size=14, color="#6d6d6d"),
                ft.TextField(
                    value="",
                    hint_text="placeholder",
                    border_color="#6d6d6d",
                    height=40,
                ),
            ], expand=True),
            ft.Column([
                ft.Text("Form Label *", size=14, color="#6d6d6d"),
                ft.TextField(
                    value="",
                    hint_text="placeholder",
                    border_color="#6d6d6d",
                    height=40,
                ),
            ], expand=True),
            ft.Column([
                ft.Text("Form Label *", size=14, color="#6d6d6d"),
                ft.TextField(
                    value="",
                    hint_text="placeholder",
                    border_color="#6d6d6d",
                    height=40,
                ),
            ], expand=True),
        ], spacing=24),

        ft.Container(height=16),

        # 2行目
        ft.Row([
            ft.Column([
                ft.Text("Form Label *", size=14, color="#6d6d6d"),
                ft.TextField(
                    value="",
                    hint_text="placeholder",
                    border_color="#6d6d6d",
                    height=40,
                ),
            ], expand=True),
            ft.Column([
                ft.Text("Form Label *", size=14, color="#6d6d6d"),
                ft.TextField(
                    value="",
                    hint_text="placeholder",
                    border_color="#6d6d6d",
                    height=40,
                ),
            ], expand=True),
        ], spacing=24),
    ], spacing=8)

    # パネルコンテナ
    panel = ft.Container(
        content=collapse_content,
        bgcolor="#ffffff",
        border=ft.border.only(
            left=ft.BorderSide(1, "rgba(34, 34, 34, 0.16)"),
            right=ft.BorderSide(1, "rgba(34, 34, 34, 0.16)"),
            bottom=ft.BorderSide(1, "rgba(34, 34, 34, 0.16)"),
        ),
        border_radius=ft.border_radius.only(bottom_left=4, bottom_right=4),
        padding=24,
        visible=is_open[0],
    )

    # アイコン
    arrow_icon = ft.Icon(
        ft.Icons.KEYBOARD_ARROW_UP if is_open[0] else ft.Icons.KEYBOARD_ARROW_DOWN,
        size=24,
        color="#6d6d6d",
    )

    # ヘッダー
    def toggle_collapse(e):
        is_open[0] = not is_open[0]
        panel.visible = is_open[0]
        arrow_icon.name = ft.Icons.KEYBOARD_ARROW_UP if is_open[0] else ft.Icons.KEYBOARD_ARROW_DOWN

        # ヘッダーの角丸を状態に応じて変更
        if is_open[0]:
            header.border_radius = ft.border_radius.only(top_left=4, top_right=4)
        else:
            header.border_radius = 4

        header.update()
        arrow_icon.update()
        panel.update()

    header = ft.Container(
        content=ft.Row([
            ft.Text(
                "Label",
                size=16,
                color="#222222",
                weight=ft.FontWeight.NORMAL,
                expand=True,
            ),
            arrow_icon,
        ]),
        bgcolor="#f8f8f8",
        border=ft.border.all(1, "rgba(34, 34, 34, 0.5)"),
        border_radius=ft.border_radius.only(top_left=4, top_right=4),
        padding=ft.padding.symmetric(horizontal=16, vertical=8),
        height=48,
        on_click=toggle_collapse,
        ink=True,
    )

    # Collapse全体
    collapse_widget = ft.Column([
        header,
        panel,
    ], spacing=0)

    return ft.Container(
        content=ft.Column([
            section_title("Collapse (アコーディオン)", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Text("クリックして展開/折りたたみ", size=12, color="#666666"),
            ft.Container(height=10),

            collapse_widget,
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )
