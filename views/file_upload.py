"""
File Upload Section - ファイルアップロードセクション（Figmaデザイン準拠）
"""
import flet as ft
from utils.constants import *


def create_file_upload_section(colors):
    """File Uploadセクション（実際にファイルアップロード可能）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    # 選択されたファイル情報を表示するテキスト
    selected_files_text = ft.Text("ファイルが選択されていません", size=12, color="#666666")
    uploaded_files_list = ft.Column([], spacing=8)

    # FilePicker設定
    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files:
            file_names = [f.name for f in e.files]
            selected_files_text.value = f"選択されたファイル: {', '.join(file_names)}"

            # ファイルリストを表示
            uploaded_files_list.controls.clear()
            for file in e.files:
                uploaded_files_list.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.INSERT_DRIVE_FILE, size=20, color="#0265dc"),
                            ft.Text(file.name, size=12, color="#222222"),
                            ft.Text(f"({file.size} bytes)", size=10, color="#999999"),
                        ], spacing=8),
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        bgcolor="#F5F5F5",
                        border_radius=4,
                    )
                )
            uploaded_files_list.update()
        else:
            selected_files_text.value = "ファイルが選択されていません"
            uploaded_files_list.controls.clear()
            uploaded_files_list.update()

        selected_files_text.update()

    file_picker = ft.FilePicker(on_result=on_file_picked)

    # ファイル選択ボタン（実際に機能する）
    file_button = ft.Row([
        ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.Icons.ATTACH_FILE, size=20, color="#0265dc"),
                ft.Text("ファイル選択", size=14, color="#0265dc", weight=ft.FontWeight.BOLD),
            ], spacing=8, tight=True),
            on_click=lambda _: file_picker.pick_files(allow_multiple=True),
            style=ft.ButtonStyle(
                bgcolor=colors["neutral_white"],
                padding=ft.padding.symmetric(horizontal=16, vertical=8),
                shape=ft.RoundedRectangleBorder(radius=4),
                side=ft.BorderSide(1, "#CCCCCC"),
            ),
        )
    ])

    # ドラッグ&ドロップエリア（クリックでファイル選択）
    drag_drop_area = ft.Container(
        content=ft.Column([
            ft.Icon(ft.Icons.CLOUD_UPLOAD_OUTLINED, size=48, color="#0265dc"),
            ft.Container(height=16),
            ft.Text("Click or drag file to upload", size=14, color="#222222", text_align=ft.TextAlign.CENTER),
            ft.Text("複数ファイルを選択できます", size=11, color="#999999", text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, spacing=0),
        width=480,
        height=160,
        bgcolor=colors["neutral_white"],
        border=ft.border.all(2, "#CCCCCC"),
        border_radius=8,
        alignment=ft.alignment.center,
        on_click=lambda _: file_picker.pick_files(allow_multiple=True),
        ink=True,
    )

    # ホバー効果
    def on_hover(e):
        if e.data == "true":
            drag_drop_area.bgcolor = "#E8F0FE"
            drag_drop_area.border = ft.border.all(2, "#0265dc")
        else:
            drag_drop_area.bgcolor = colors["neutral_white"]
            drag_drop_area.border = ft.border.all(2, "#CCCCCC")
        drag_drop_area.update()

    drag_drop_area.on_hover = on_hover

    return ft.Container(
        content=ft.Column([
            file_picker,  # FilePickerを追加（非表示で動作）
            section_title("File Upload (実際にアップロード可能)", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Text("ボタン形式のファイル選択", size=14, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=16),
            file_button,
            ft.Container(height=8),
            selected_files_text,
            ft.Container(height=40),

            ft.Text("ドラッグ&ドロップエリア（クリックで選択）", size=14, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=16),
            drag_drop_area,
            ft.Container(height=16),

            ft.Text("選択されたファイル一覧:", size=12, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=8),
            uploaded_files_list,
        ], spacing=0),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
