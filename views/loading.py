"""
Loading Section - ローディングスピナーセクション
"""
import flet as ft
from utils.constants import *


def create_spinner(size="XL", on_colored=True):
    """
    ローディングスピナーを作成

    Args:
        size: "XL" (24px) or "Medium" (14px)
        on_colored: True (白色) or False (青色)
    """
    # サイズ設定
    if size == "XL":
        spinner_size = 24
        container_size = 32
        stroke_width = 3
    else:  # Medium
        spinner_size = 14
        container_size = 18
        stroke_width = 2

    # 色設定
    color = COLORS["neutral_white"] if on_colored else COLORS["primary_main"]

    spinner = ft.Container(
        content=ft.ProgressRing(
            width=spinner_size,
            height=spinner_size,
            stroke_width=stroke_width,
            color=color,
        ),
        width=container_size,
        height=container_size,
        alignment=ft.alignment.center,
    )

    return spinner


def create_loading_button(text="Loading...", size="XL", on_colored=True, bgcolor=None):
    """
    ローディング状態のボタンを作成

    Args:
        text: ボタンのラベルテキスト
        size: スピナーのサイズ ("XL" or "Medium")
        on_colored: True (白色スピナー) or False (青色スピナー)
        bgcolor: 背景色（指定しない場合は success_main）
    """
    spinner = create_spinner(size=size, on_colored=on_colored)

    if bgcolor is None:
        bgcolor = COLORS["success_main"]

    button = ft.Container(
        content=ft.Row(
            [
                spinner,
                ft.Text(
                    text,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=COLORS["neutral_white"],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        ),
        bgcolor=bgcolor,
        padding=12,
        border_radius=8,
        width=169,
        height=56,
    )

    return button


def create_loading_button_outline(text="Loading...", size="XL", color=None):
    """
    枠だけのローディングボタンを作成

    Args:
        text: ボタンのラベルテキスト
        size: スピナーのサイズ ("XL" or "Medium")
        color: 枠とテキストとスピナーの色
    """
    spinner = create_spinner(size=size, on_colored=False)
    # スピナーの色を変更
    spinner.content.color = color

    button = ft.Container(
        content=ft.Row(
            [
                spinner,
                ft.Text(
                    text,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=color,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        ),
        bgcolor="transparent",
        border=ft.border.all(BORDER_WIDTH, color),
        padding=12,
        border_radius=8,
        width=169,
        height=56,
    )

    return button


def create_loading_button_text(text="Loading...", size="XL", color=None):
    """
    枠なし（テキストのみ）のローディングボタンを作成

    Args:
        text: ボタンのラベルテキスト
        size: スピナーのサイズ ("XL" or "Medium")
        color: テキストとスピナーの色
    """
    spinner = create_spinner(size=size, on_colored=False)
    # スピナーの色を変更
    spinner.content.color = color

    button = ft.Container(
        content=ft.Row(
            [
                spinner,
                ft.Text(
                    text,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=color,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        ),
        bgcolor="transparent",
        padding=12,
        border_radius=8,
        width=169,
        height=56,
    )

    return button


def section_title_local(text, color):
    """ローカルセクションタイトル用のテキストコンポーネント"""
    return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)


def row_title(text):
    """行タイトル用のテキストコンポーネント"""
    return ft.Text(text, size=14, weight=ft.FontWeight.BOLD, color="#333333")


def create_loading_section(colors):
    """通常のローディングスピナーセクション"""
    return ft.Container(
        content=ft.Column(
            [
                section_title_local("Loading Buttons", color=COLORS["success_main"]),
                ft.Container(height=10),

                # 背景色ありのローディングボタン
                row_title("Filled"),
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Success", size=12, color="#666666"),
                                ft.Container(height=5),
                                create_loading_button("Loading...", size="XL", on_colored=True, bgcolor=COLORS["success_main"]),
                            ],
                            spacing=0,
                        ),
                        ft.Column(
                            [
                                ft.Text("Danger", size=12, color="#666666"),
                                ft.Container(height=5),
                                create_loading_button("Loading...", size="XL", on_colored=True, bgcolor=COLORS["danger_main"]),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=15,
                ),

                ft.Container(height=20),

                # 枠だけのローディングボタン
                row_title("Outline"),
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Success", size=12, color="#666666"),
                                ft.Container(height=5),
                                create_loading_button_outline("Loading...", size="XL", color=COLORS["success_main"]),
                            ],
                            spacing=0,
                        ),
                        ft.Column(
                            [
                                ft.Text("Danger", size=12, color="#666666"),
                                ft.Container(height=5),
                                create_loading_button_outline("Loading...", size="XL", color=COLORS["danger_main"]),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=15,
                ),

                ft.Container(height=20),

                # 枠なしのローディングボタン
                row_title("Text Only"),
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Success", size=12, color="#666666"),
                                ft.Container(height=5),
                                create_loading_button_text("Loading...", size="XL", color=COLORS["success_main"]),
                            ],
                            spacing=0,
                        ),
                        ft.Column(
                            [
                                ft.Text("Danger", size=12, color="#666666"),
                                ft.Container(height=5),
                                create_loading_button_text("Loading...", size="XL", color=COLORS["danger_main"]),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=15,
                ),
            ],
            spacing=0,
        ),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )


def create_dark_bg_loading_section(colors):
    """暗い背景上のローディングボタンセクション"""
    return ft.Container(
        content=ft.Column(
            [
                section_title_local("On Dark Background", color=COLORS["neutral_white"]),
                ft.Container(height=10),

                row_title("Filled (White Background)"),
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("On Colored", size=12, color=COLORS["neutral_white"]),
                                ft.Container(height=5),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            create_spinner(size="XL", on_colored=False),
                                            ft.Text(
                                                "Loading...",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                                color=COLORS["primary_main"],
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=12,
                                    ),
                                    bgcolor=COLORS["neutral_white"],
                                    padding=12,
                                    border_radius=8,
                                    width=169,
                                    height=56,
                                ),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=15,
                ),

                ft.Container(height=20),

                row_title("Outline (White)"),
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("On Colored", size=12, color=COLORS["neutral_white"]),
                                ft.Container(height=5),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            create_spinner(size="XL", on_colored=True),
                                            ft.Text(
                                                "Loading...",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                                color=COLORS["neutral_white"],
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=12,
                                    ),
                                    bgcolor="transparent",
                                    border=ft.border.all(BORDER_WIDTH, COLORS["neutral_white"]),
                                    padding=12,
                                    border_radius=8,
                                    width=169,
                                    height=56,
                                ),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=15,
                ),

                ft.Container(height=20),

                row_title("Text Only (White)"),
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("On Colored", size=12, color=COLORS["neutral_white"]),
                                ft.Container(height=5),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            create_spinner(size="XL", on_colored=True),
                                            ft.Text(
                                                "Loading...",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                                color=COLORS["neutral_white"],
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=12,
                                    ),
                                    bgcolor="transparent",
                                    padding=12,
                                    border_radius=8,
                                    width=169,
                                    height=56,
                                ),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=15,
                ),
            ],
            spacing=0,
        ),
        bgcolor=COLORS["primary_main"],
        padding=30,
        border_radius=12,
    )
