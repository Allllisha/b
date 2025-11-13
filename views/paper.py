"""
Paper Section - Paperフォームコンポーネント（Figmaデザインに基づく）
"""
import flet as ft
from utils.constants import *


def create_paper_section(colors):
    """Paperフォームコンポーネント（Figmaデザインに基づく）"""

    def create_form_label(text):
        """フォームラベルを作成"""
        return ft.Text(
            text,
            size=11,
            color="#222222",
            weight=ft.FontWeight.NORMAL,
        )

    def create_text_field(label, width=None):
        """テキストフィールドを作成"""
        return ft.Column([
            create_form_label(label),
            ft.TextField(
                hint_text="placeholder",
                hint_style=ft.TextStyle(size=14, color="#9E9E9E"),
                text_style=ft.TextStyle(size=14, color="#222222"),
                border_color="rgba(34, 34, 34, 0.16)",
                focused_border_color="#5258E4",
                border_radius=4,
                height=40,
                content_padding=ft.padding.only(left=12, right=12, top=8, bottom=8),
                width=width,
            ),
        ], spacing=4)

    def create_paper_title():
        """Paperタイトルとボタンを作成"""
        return ft.Row([
            ft.Text(
                "メインタイトルが入ります",
                size=16,
                color="#222222",
                weight=ft.FontWeight.NORMAL,
                expand=True,
            ),
            ft.Row([
                ft.TextButton(
                    "キャンセル",
                    style=ft.ButtonStyle(
                        color="#007A4D",
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    ),
                ),
                ft.Container(
                    content=ft.Text(
                        "機能情報を保存",
                        size=11,
                        color="#FFFFFF",
                        weight=ft.FontWeight.BOLD,
                    ),
                    bgcolor="#007A4D",
                    border_radius=4,
                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    height=24,
                ),
            ], spacing=4),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    def create_paper_form():
        """Paperフォームを作成"""
        return ft.Container(
            content=ft.Column([
                # タイトルとボタン
                create_paper_title(),
                ft.Container(height=8),

                # 4カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                ], spacing=24),

                # 3カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=360),
                    create_text_field("Form Label *", width=360),
                    create_text_field("Form Label *", width=360),
                ], spacing=24),

                # 2カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=552),
                    create_text_field("Form Label *", width=552),
                ], spacing=24),

                ft.Row([
                    create_text_field("Form Label *", width=552),
                    create_text_field("Form Label *", width=552),
                ], spacing=24),

                # 1カラムのテキストフィールド（複数）
                create_text_field("Form Label *", width=1128),
                create_text_field("Form Label *", width=1128),
                create_text_field("Form Label *", width=1128),

                # チェックボックス
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Checkbox(label="ラベル", value=True),
                        ft.Checkbox(label="ラベル", value=False),
                        ft.Checkbox(label="ラベル", value=False),
                        ft.Checkbox(label="ラベル", value=False),
                    ], spacing=16),
                ], spacing=4),

                # ラジオボタン
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.RadioGroup(
                        content=ft.Row([
                            ft.Radio(value="1", label="ラベル"),
                            ft.Radio(value="2", label="ラベル"),
                            ft.Radio(value="3", label="ラベル"),
                            ft.Radio(value="4", label="ラベル"),
                        ], spacing=16),
                        value="1",
                    ),
                ], spacing=4),

                # テキストエリア
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.TextField(
                        hint_text="placeholder",
                        hint_style=ft.TextStyle(size=14, color="#9E9E9E"),
                        text_style=ft.TextStyle(size=14, color="#222222"),
                        border_color="rgba(34, 34, 34, 0.16)",
                        focused_border_color="#5258E4",
                        border_radius=4,
                        multiline=True,
                        min_lines=6,
                        max_lines=6,
                        content_padding=ft.padding.all(12),
                        width=1128,
                    ),
                ], spacing=4),

                # 数値入力
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.TextField(
                            value="10",
                            text_style=ft.TextStyle(size=14, color="#222222"),
                            border_color="rgba(34, 34, 34, 0.16)",
                            focused_border_color="#5258E4",
                            border_radius=4,
                            height=40,
                            width=80,
                            content_padding=ft.padding.only(left=12, right=12, top=8, bottom=8),
                        ),
                        ft.Text("アイテム", size=14, color="#222222"),
                    ], spacing=8),
                ], spacing=4),

                # スイッチ
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Switch(value=False),
                        ft.Text("Switch Item", size=14, color="#222222"),
                    ], spacing=8),
                ], spacing=4),

                # タグ入力
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label1", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label2", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label3", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.ADD, size=12, color="#5258E4"),
                                ft.Text("Add", size=11, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                    ], spacing=8),
                ], spacing=4),

                # ファイルアップロード
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.Icons.UPLOAD_FILE, size=32, color="#5258E4"),
                            ft.Text("Click or drag file to upload", size=12, color="#5258E4"),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                        border=ft.border.all(1, "#5258E4"),
                        border_radius=4,
                        padding=ft.padding.all(24),
                        width=1128,
                        height=120,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

                # 画像プレビュー
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Icon(ft.Icons.IMAGE, size=48, color="#5258E4"),
                        bgcolor="rgba(82, 88, 228, 0.1)",
                        border_radius=4,
                        padding=ft.padding.all(24),
                        width=200,
                        height=150,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

                # ボタン
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Text(
                            "Button",
                            size=16,
                            color="#FFFFFF",
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#007A4D",
                        border_radius=8,
                        padding=ft.padding.symmetric(horizontal=8, vertical=8),
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

            ], spacing=16),
            bgcolor="#FFFFFF",
            border=ft.border.all(1, "rgba(34, 34, 34, 0.16)"),
            border_radius=8,
            padding=ft.padding.only(left=32, right=32, top=24, bottom=24),
            width=1200,
        )

    def create_paper_form_borderless():
        """Paperフォーム - Borderless（ボーダーなし）"""
        return ft.Container(
            content=ft.Column([
                # タイトルとボタン
                create_paper_title(),
                ft.Container(height=8),

                # 4カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                ], spacing=24),

                # 3カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=360),
                    create_text_field("Form Label *", width=360),
                    create_text_field("Form Label *", width=360),
                ], spacing=24),

                # 2カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=552),
                    create_text_field("Form Label *", width=552),
                ], spacing=24),

                ft.Row([
                    create_text_field("Form Label *", width=552),
                    create_text_field("Form Label *", width=552),
                ], spacing=24),

                # 1カラムのテキストフィールド（複数）
                create_text_field("Form Label *", width=1128),
                create_text_field("Form Label *", width=1128),
                create_text_field("Form Label *", width=1128),

                # チェックボックス
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Checkbox(label="ラベル", value=True),
                        ft.Checkbox(label="ラベル", value=False),
                        ft.Checkbox(label="ラベル", value=False),
                        ft.Checkbox(label="ラベル", value=False),
                    ], spacing=16),
                ], spacing=4),

                # ラジオボタン
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.RadioGroup(
                        content=ft.Row([
                            ft.Radio(value="1", label="ラベル"),
                            ft.Radio(value="2", label="ラベル"),
                            ft.Radio(value="3", label="ラベル"),
                            ft.Radio(value="4", label="ラベル"),
                        ], spacing=16),
                        value="1",
                    ),
                ], spacing=4),

                # テキストエリア
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.TextField(
                        hint_text="placeholder",
                        hint_style=ft.TextStyle(size=14, color="#9E9E9E"),
                        text_style=ft.TextStyle(size=14, color="#222222"),
                        border_color="rgba(34, 34, 34, 0.16)",
                        focused_border_color="#5258E4",
                        border_radius=4,
                        multiline=True,
                        min_lines=6,
                        max_lines=6,
                        content_padding=ft.padding.all(12),
                        width=1128,
                    ),
                ], spacing=4),

                # 数値入力
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.TextField(
                            value="10",
                            text_style=ft.TextStyle(size=14, color="#222222"),
                            border_color="rgba(34, 34, 34, 0.16)",
                            focused_border_color="#5258E4",
                            border_radius=4,
                            height=40,
                            width=80,
                            content_padding=ft.padding.only(left=12, right=12, top=8, bottom=8),
                        ),
                        ft.Text("アイテム", size=14, color="#222222"),
                    ], spacing=8),
                ], spacing=4),

                # スイッチ
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Switch(value=False),
                        ft.Text("Switch Item", size=14, color="#222222"),
                    ], spacing=8),
                ], spacing=4),

                # タグ入力
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label1", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label2", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label3", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.ADD, size=12, color="#5258E4"),
                                ft.Text("Add", size=11, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                    ], spacing=8),
                ], spacing=4),

                # ファイルアップロード
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.Icons.UPLOAD_FILE, size=32, color="#5258E4"),
                            ft.Text("Click or drag file to upload", size=12, color="#5258E4"),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                        border=ft.border.all(1, "#5258E4"),
                        border_radius=4,
                        padding=ft.padding.all(24),
                        width=1128,
                        height=120,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

                # 画像プレビュー
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Icon(ft.Icons.IMAGE, size=48, color="#5258E4"),
                        bgcolor="rgba(82, 88, 228, 0.1)",
                        border_radius=4,
                        padding=ft.padding.all(24),
                        width=200,
                        height=150,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

                # ボタン
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Text(
                            "Button",
                            size=16,
                            color="#FFFFFF",
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#007A4D",
                        border_radius=8,
                        padding=ft.padding.symmetric(horizontal=8, vertical=8),
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

            ], spacing=16),
            bgcolor="#FFFFFF",
            border_radius=8,
            padding=ft.padding.only(left=32, right=32, top=24, bottom=24),
            width=1200,
        )

    def create_paper_form_elevation():
        """Paperフォーム - Elevation（シャドウ付き）"""
        return ft.Container(
            content=ft.Column([
                # タイトルとボタン
                create_paper_title(),
                ft.Container(height=8),

                # 4カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                    create_text_field("Form Label *", width=264),
                ], spacing=24),

                # 3カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=360),
                    create_text_field("Form Label *", width=360),
                    create_text_field("Form Label *", width=360),
                ], spacing=24),

                # 2カラムのテキストフィールド
                ft.Row([
                    create_text_field("Form Label *", width=552),
                    create_text_field("Form Label *", width=552),
                ], spacing=24),

                ft.Row([
                    create_text_field("Form Label *", width=552),
                    create_text_field("Form Label *", width=552),
                ], spacing=24),

                # 1カラムのテキストフィールド（複数）
                create_text_field("Form Label *", width=1128),
                create_text_field("Form Label *", width=1128),
                create_text_field("Form Label *", width=1128),

                # チェックボックス
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Checkbox(label="ラベル", value=True),
                        ft.Checkbox(label="ラベル", value=False),
                        ft.Checkbox(label="ラベル", value=False),
                        ft.Checkbox(label="ラベル", value=False),
                    ], spacing=16),
                ], spacing=4),

                # ラジオボタン
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.RadioGroup(
                        content=ft.Row([
                            ft.Radio(value="1", label="ラベル"),
                            ft.Radio(value="2", label="ラベル"),
                            ft.Radio(value="3", label="ラベル"),
                            ft.Radio(value="4", label="ラベル"),
                        ], spacing=16),
                        value="1",
                    ),
                ], spacing=4),

                # テキストエリア
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.TextField(
                        hint_text="placeholder",
                        hint_style=ft.TextStyle(size=14, color="#9E9E9E"),
                        text_style=ft.TextStyle(size=14, color="#222222"),
                        border_color="rgba(34, 34, 34, 0.16)",
                        focused_border_color="#5258E4",
                        border_radius=4,
                        multiline=True,
                        min_lines=6,
                        max_lines=6,
                        content_padding=ft.padding.all(12),
                        width=1128,
                    ),
                ], spacing=4),

                # 数値入力
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.TextField(
                            value="10",
                            text_style=ft.TextStyle(size=14, color="#222222"),
                            border_color="rgba(34, 34, 34, 0.16)",
                            focused_border_color="#5258E4",
                            border_radius=4,
                            height=40,
                            width=80,
                            content_padding=ft.padding.only(left=12, right=12, top=8, bottom=8),
                        ),
                        ft.Text("アイテム", size=14, color="#222222"),
                    ], spacing=8),
                ], spacing=4),

                # スイッチ
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Switch(value=False),
                        ft.Text("Switch Item", size=14, color="#222222"),
                    ], spacing=8),
                ], spacing=4),

                # タグ入力
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Row([
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label1", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label2", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Text("tag Label3", size=11, color="#5258E4"),
                                ft.Icon(ft.Icons.CLOSE, size=12, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.Icons.ADD, size=12, color="#5258E4"),
                                ft.Text("Add", size=11, color="#5258E4"),
                            ], spacing=4),
                            bgcolor="rgba(82, 88, 228, 0.1)",
                            border_radius=4,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        ),
                    ], spacing=8),
                ], spacing=4),

                # ファイルアップロード
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(ft.Icons.UPLOAD_FILE, size=32, color="#5258E4"),
                            ft.Text("Click or drag file to upload", size=12, color="#5258E4"),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
                        border=ft.border.all(1, "#5258E4"),
                        border_radius=4,
                        padding=ft.padding.all(24),
                        width=1128,
                        height=120,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

                # 画像プレビュー
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Icon(ft.Icons.IMAGE, size=48, color="#5258E4"),
                        bgcolor="rgba(82, 88, 228, 0.1)",
                        border_radius=4,
                        padding=ft.padding.all(24),
                        width=200,
                        height=150,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

                # ボタン
                ft.Column([
                    create_form_label("Form Label *"),
                    ft.Container(
                        content=ft.Text(
                            "Button",
                            size=16,
                            color="#FFFFFF",
                            weight=ft.FontWeight.BOLD,
                        ),
                        bgcolor="#007A4D",
                        border_radius=8,
                        padding=ft.padding.symmetric(horizontal=8, vertical=8),
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=4),

            ], spacing=16),
            bgcolor="#FFFFFF",
            border_radius=8,
            shadow=[ELEVATIONS["level_2"]],
            padding=ft.padding.only(left=32, right=32, top=24, bottom=24),
            width=1200,
        )

    return ft.Container(
        content=ft.Column([
            ft.Text("Paper フォームコンポーネント", size=20, weight=ft.FontWeight.BOLD, color=colors["primary_main"]),
            ft.Container(height=20),

            # Paper - Default (ボーダー付き)
            ft.Text("Paper - Default (ボーダー付き)", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_paper_form(),
            ft.Divider(height=30, color="transparent"),

            # Paper - Borderless (ボーダーなし)
            ft.Text("Paper - Borderless (ボーダーなし)", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_paper_form_borderless(),
            ft.Divider(height=30, color="transparent"),

            # Paper - Elevation (シャドウ付き)
            ft.Text("Paper - Elevation (シャドウ付き)", size=16, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            create_paper_form_elevation(),
        ], spacing=5),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )
