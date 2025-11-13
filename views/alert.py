"""
Alert UI Component
Figmaデザインに基づくアラートコンポーネント（エラー・情報・ニュートラル）
"""
import flet as ft
from utils.constants import *


def create_alert_section(colors):
    """アラートセクション（Figmaデザインに基づく）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_alert(
        alert_type="error",
        has_outline=True,
        main_text="これはアラートです。詳しくはこちらを 確認してください。",
        sub_text="アラートには補足を追加することもできます",
        show_option=True,
        show_close=True,
    ):
        """アラートを作成"""

        # アラートタイプに応じた設定
        if alert_type == "error":
            bg_color = "#ffebe7"
            border_color = colors["danger_main"]
            icon_color = colors["danger_main"]
            icon = ft.Icons.WARNING
            button_color = colors["danger_main"]
        elif alert_type == "information":
            bg_color = "#e0f2ff"
            border_color = "#0265dc"
            icon_color = "#0265dc"
            icon = ft.Icons.INFO
            button_color = "#0265dc"
        else:  # neutral
            bg_color = "#fdfdfd"
            border_color = colors["neutral_black"]
            icon_color = colors["neutral_black"]
            icon = ft.Icons.HELP
            button_color = colors["neutral_black"]

        # アイコン
        alert_icon = ft.Icon(
            icon,
            size=24,
            color=icon_color,
        )

        # テキストコンテンツ
        text_content = ft.Column([
            ft.Text(
                main_text,
                size=12,
                color=colors["neutral_black"],
                weight=ft.FontWeight.NORMAL,
            ),
            ft.Text(
                sub_text,
                size=10,
                color=colors["neutral_light"],
                weight=ft.FontWeight.NORMAL,
            ),
        ], spacing=2)

        # オプションボタン
        option_button = None
        if show_option:
            option_button = ft.Container(
                content=ft.Text(
                    "Option",
                    size=11,
                    color=button_color,
                    weight=ft.FontWeight.BOLD,
                ),
                padding=ft.padding.symmetric(horizontal=4, vertical=4),
                border_radius=100,
                height=24,
            )

        # 閉じるボタン
        close_button = None
        if show_close:
            close_button = ft.Icon(
                ft.Icons.CLOSE,
                size=16,
                color=colors["neutral_light"],
            )

        # アラート全体の行
        alert_row = ft.Row([
            alert_icon,
            ft.Container(
                content=text_content,
                expand=True,
            ),
        ], spacing=8)

        if option_button:
            alert_row.controls.append(option_button)
        if close_button:
            alert_row.controls.append(close_button)

        # アラートコンテナ
        alert_container = ft.Container(
            content=alert_row,
            bgcolor=bg_color,
            padding=ft.padding.symmetric(horizontal=16, vertical=8),
            border_radius=8,
            border=ft.border.all(1, border_color) if has_outline else None,
        )

        return alert_container

    # アラートのバリエーションを作成
    alerts_with_outline = ft.Container(
        content=ft.Column([
            ft.Text("With Outline", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
            ft.Container(height=10),

            # Error with outline
            create_alert("error", True),
            ft.Container(height=12),

            # Information with outline
            create_alert("information", True),
            ft.Container(height=12),

            # Neutral with outline
            create_alert("neutral", True),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=20,
        border_radius=8,
        border=ft.border.all(1, "#E0E0E0"),
    )

    alerts_without_outline = ft.Container(
        content=ft.Column([
            ft.Text("Without Outline", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
            ft.Container(height=10),

            # Error without outline
            create_alert("error", False),
            ft.Container(height=12),

            # Information without outline
            create_alert("information", False),
            ft.Container(height=12),

            # Neutral without outline
            create_alert("neutral", False),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=20,
        border_radius=8,
        border=ft.border.all(1, "#E0E0E0"),
    )

    # セクション全体を構築
    alert_section = ft.Container(
        content=ft.Column([
            section_title("Alert (Figma)", color=colors["primary_main"]),
            ft.Container(height=20),

            alerts_with_outline,
            ft.Container(height=20),

            alerts_without_outline,
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return alert_section
