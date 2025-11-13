"""
Snackbar Section - Snackbarセクション
"""
import flet as ft
from utils.constants import *


def section_title_local(text, color="#5258E4"):
    """ローカルセクションタイトル用のテキストコンポーネント"""
    return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)


def create_snackbar_section(colors):
    """Snackbarセクション（Figmaデザインに基づく）"""

    def create_snackbar(
        message="リストをアップロードしています...",
        show_spinner=True,
        show_icon=True,
        show_option=True,
        show_close=True,
        show_progress=True,
        progress_value=0.5,
    ):
        """Snackbarコンポーネントを作成"""

        # トップアイテムの構成要素
        top_items = []

        # スピナーアイコン
        if show_spinner:
            spinner = ft.ProgressRing(
                width=12,
                height=12,
                stroke_width=1.5,
                color=colors["neutral_white"],
            )
            top_items.append(spinner)

        # アップロードアイコン
        if show_icon:
            upload_icon = ft.Icon(
                ft.Icons.UPLOAD_FILE,
                size=16,
                color=colors["neutral_white"],
            )
            top_items.append(upload_icon)

        # メッセージテキスト
        message_text = ft.Text(
            message,
            size=11,
            color=colors["neutral_white"],
            weight=ft.FontWeight.NORMAL,
            expand=1,
        )
        top_items.append(message_text)

        # Optionボタン
        if show_option:
            option_button = ft.Container(
                content=ft.Container(
                    content=ft.Text(
                        "Option",
                        size=9,
                        weight=ft.FontWeight.BOLD,
                        color="#9599ff",
                    ),
                    padding=ft.padding.symmetric(horizontal=4, vertical=0),
                    height=14,
                    alignment=ft.alignment.center,
                ),
                border_radius=100,
                padding=3,
                height=20,
            )
            top_items.append(option_button)

        # 閉じるボタン
        if show_close:
            close_button = ft.IconButton(
                icon=ft.Icons.CLOSE,
                icon_size=16,
                icon_color=colors["neutral_white"],
                tooltip="閉じる",
                style=ft.ButtonStyle(
                    padding=0,
                ),
            )
            top_items.append(close_button)

        # トップ行
        top_row = ft.Container(
            content=ft.Row(
                top_items,
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(horizontal=12, vertical=0),
            expand=1,
        )

        # プログレスバー
        progress_bar = None
        if show_progress:
            progress_bar = ft.Container(
                bgcolor="#ffa037",  # オレンジ色
                height=2,
                width=336 * progress_value,  # 進捗に応じて幅を調整
            )

        # Snackbarコンテナ
        snackbar_content = [top_row]
        if progress_bar:
            snackbar_content.append(progress_bar)

        snackbar = ft.Container(
            content=ft.Column(
                snackbar_content,
                spacing=0,
            ),
            bgcolor="#333333",  # 不透明なダークグレー
            border_radius=8,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=8,
                color="rgba(34, 34, 34, 0.5)",
                offset=ft.Offset(0, 2),
            ),
            width=336,
            height=44,
        )

        return snackbar

    # バリエーションを作成
    snackbar_section = ft.Container(
        content=ft.Column([
            section_title_local("Lv2 Snackbar (Figma)", color=colors["primary_main"]),
            ft.Container(height=10),

            # すべての要素を含むSnackbar
            ft.Text("Full Snackbar (with spinner, icon, option, close, progress)", size=12, weight=ft.FontWeight.BOLD, color="#666666"),
            ft.Container(height=5),
            create_snackbar(
                message="リストをアップロードしています...",
                show_spinner=True,
                show_icon=True,
                show_option=True,
                show_close=True,
                show_progress=True,
                progress_value=0.5,
            ),
            ft.Container(height=20),

            # プログレスバー100%
            ft.Text("Snackbar with 100% progress", size=12, weight=ft.FontWeight.BOLD, color="#666666"),
            ft.Container(height=5),
            create_snackbar(
                message="アップロード完了しました",
                show_spinner=False,
                show_icon=True,
                show_option=True,
                show_close=True,
                show_progress=True,
                progress_value=1.0,
            ),
            ft.Container(height=20),

            # プログレスバーなし
            ft.Text("Snackbar without progress bar", size=12, weight=ft.FontWeight.BOLD, color="#666666"),
            ft.Container(height=5),
            create_snackbar(
                message="操作が完了しました",
                show_spinner=False,
                show_icon=False,
                show_option=True,
                show_close=True,
                show_progress=False,
            ),
            ft.Container(height=20),

            # シンプルなSnackbar
            ft.Text("Simple Snackbar (no option, no progress)", size=12, weight=ft.FontWeight.BOLD, color="#666666"),
            ft.Container(height=5),
            create_snackbar(
                message="変更を保存しました",
                show_spinner=False,
                show_icon=False,
                show_option=False,
                show_close=True,
                show_progress=False,
            ),
            ft.Container(height=20),

            # エラーメッセージ風
            ft.Text("Error message style", size=12, weight=ft.FontWeight.BOLD, color="#666666"),
            ft.Container(height=5),
            create_snackbar(
                message="エラーが発生しました。もう一度お試しください。",
                show_spinner=False,
                show_icon=False,
                show_option=False,
                show_close=True,
                show_progress=False,
            ),

        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return snackbar_section
