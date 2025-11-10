import flet as ft
import math
import time
import asyncio

def main(page: ft.Page):
    page.title = "Flet UI Customization - Advanced Demo"
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO

    # テーマのカスタマイズ（Material3）
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#6750A4",
            secondary="#625B71",
            tertiary="#7D5260",
            surface="#FFFBFE",
            background="#FFFBFE",
            error="#B3261E",
        ),
        use_material3=True,
    )

    # ダークテーマの設定
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#D0BCFF",
            secondary="#CCC2DC",
            tertiary="#EFB8C8",
            surface="#1C1B1F",
            background="#1C1B1F",
            error="#F2B8B5",
        ),
        use_material3=True,
    )

    page.theme_mode = ft.ThemeMode.LIGHT

    # カスタムフォントの登録
    page.fonts = {
        "TsukuhouMincho": "fonts/TsukuhouMincho-Regular.ttf",
    }

    # ダークモードスイッチの参照
    dark_mode_switch = ft.Ref[ft.Switch]()

    # 通知切り替えハンドラー
    def toggle_notification(e):
        if e.control.value:
            snack_bar = ft.SnackBar(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.NOTIFICATIONS_ACTIVE, color="#FFFFFF", size=24),
                        ft.Text("通知が有効になりました", color="#FFFFFF", size=get_subsection_title_size(), weight=ft.FontWeight.W_500),
                    ],
                    spacing=12,
                ),
                bgcolor="#43E97B",
                elevation=8,
                behavior=ft.SnackBarBehavior.FLOATING,
                margin=20,
                padding=20,
            )
        else:
            snack_bar = ft.SnackBar(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.NOTIFICATIONS_OFF, color="#FFFFFF", size=24),
                        ft.Text("通知が無効になりました", color="#FFFFFF", size=get_subsection_title_size(), weight=ft.FontWeight.W_500),
                    ],
                    spacing=12,
                ),
                bgcolor="#F5576C",
                elevation=8,
                behavior=ft.SnackBarBehavior.FLOATING,
                margin=20,
                padding=20,
            )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    # テーマに応じた色を取得するヘルパー関数
    def is_dark():
        return page.theme_mode == ft.ThemeMode.DARK

    def get_surface_color():
        return "#2B2930" if is_dark() else "#FFFFFF"

    def get_container_color():
        return "#2B2930" if is_dark() else "#F5F5F5"

    def get_text_color():
        return "#E6E1E5" if is_dark() else "#1C1B1F"

    def get_secondary_text_color():
        return "#CAC4D0" if is_dark() else "#49454F"

    def get_border_color():
        return "#49454F" if is_dark() else "#E7E0EC"

    # ========================================
    # レスポンシブヘルパー関数
    # ========================================
    def get_responsive_padding():
        """画面幅に応じてパディングを返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 10
        elif width <= 600:
            return 15
        elif width <= 900:
            return 30
        else:
            return 50

    def get_responsive_content_width():
        """画面幅に応じてコンテンツ最大幅を返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return width - 20
        elif width <= 600:
            return width - 30
        elif width <= 900:
            return width - 60
        else:
            return min(width - 100, 1400)

    def get_datatable_width():
        """DataTableの幅を画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return width - 40
        elif width <= 600:
            return width - 60
        else:
            return 700

    def get_chart_width():
        """チャートの幅を画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return width - 60
        elif width <= 600:
            return width - 80
        else:
            return 500

    def get_header_title_size():
        """ヘッダータイトルのフォントサイズを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 20
        elif width <= 600:
            return 24
        else:
            return 32

    def get_header_subtitle_size():
        """ヘッダーサブタイトルのフォントサイズを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 11
        elif width <= 600:
            return 12
        else:
            return 14

    def get_header_padding():
        """ヘッダーのパディングを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return ft.padding.only(left=15, right=15, top=20, bottom=20)
        elif width <= 600:
            return ft.padding.only(left=25, right=25, top=25, bottom=25)
        else:
            return ft.padding.only(left=40, right=40, top=30, bottom=30)

    def get_section_title_size():
        """セクションタイトルのフォントサイズを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 16
        elif width <= 600:
            return 18
        else:
            return 20

    def get_subsection_title_size():
        """サブセクションタイトルのフォントサイズを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 13
        elif width <= 600:
            return 14
        else:
            return 16

    def get_section_padding():
        """セクションのパディングを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 15
        elif width <= 600:
            return 25
        else:
            return 40

    def get_container_padding():
        """コンテナ内パディングを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 10
        elif width <= 600:
            return 15
        else:
            return 20

    def get_datatable_column_spacing():
        """DataTableのカラムスペーシングを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 20
        elif width <= 600:
            return 40
        else:
            return 100

    def get_text_size():
        """通常テキストのフォントサイズを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 12
        elif width <= 600:
            return 13
        else:
            return 14

    def get_small_text_size():
        """小さいテキストのフォントサイズを画面幅に応じて返す"""
        width = page.width if page.width else 800
        if width <= 400:
            return 9
        elif width <= 600:
            return 10
        else:
            return 10

    # ========================================
    # UI構築関数
    # ========================================
    def build_ui():
        # ページの背景色を設定
        page.bgcolor = "#FAFAFA" if not is_dark() else "#121212"

        # ========================================
        # 1. グラデーション & 影付きカード
        # ========================================
        def create_stats_card(title: str, value: str, icon: str, gradient_colors: list):
            return ft.Container(
                width=280,
                height=160,
                padding=24,
                border_radius=20,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=gradient_colors,
                ),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color="#00000015" if not is_dark() else "#00000040",
                    offset=ft.Offset(0, 10),
                ),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(name=icon, color="#FFFFFF", size=32),
                                ft.Container(expand=True),
                                ft.Container(
                                    width=8,
                                    height=8,
                                    border_radius=4,
                                    bgcolor="#FFFFFF50",
                                ),
                            ],
                        ),
                        ft.Container(height=12),
                        ft.Text(
                            value,
                            size=36,
                            weight=ft.FontWeight.W_700,
                            color="#FFFFFF",
                        ),
                        ft.Text(
                            title,
                            size=14,
                            weight=ft.FontWeight.W_400,
                            color="#FFFFFFCC",
                        ),
                    ],
                    spacing=0,
                ),
                animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
                on_hover=lambda e: animate_card_hover(e),
            )

        def animate_card_hover(e):
            if e.data == "true":
                e.control.scale = 1.03
                e.control.shadow = ft.BoxShadow(
                    spread_radius=2,
                    blur_radius=30,
                    color="#00000025" if not is_dark() else "#00000050",
                    offset=ft.Offset(0, 15),
                )
            else:
                e.control.scale = 1.0
                e.control.shadow = ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color="#00000015" if not is_dark() else "#00000040",
                    offset=ft.Offset(0, 10),
                )
            e.control.update()

        # ========================================
        # 2. 状態別スタイリングボタン
        # ========================================
        def create_custom_button(text: str, icon: str, primary: bool = True):
            if is_dark():
                return ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(icon, size=20),
                            ft.Text(text, size=15, weight=ft.FontWeight.W_600),
                        ],
                        spacing=8,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12),
                        bgcolor={
                            ft.ControlState.DEFAULT: "#D0BCFF" if primary else "#4A4458",
                            ft.ControlState.HOVERED: "#E8DEF8" if primary else "#625B71",
                            ft.ControlState.PRESSED: "#B69DF8" if primary else "#3B3841",
                        },
                        color={
                            ft.ControlState.DEFAULT: "#1C1B1F" if primary else "#E6E1E5",
                        },
                        elevation={
                            ft.ControlState.DEFAULT: 2,
                            ft.ControlState.HOVERED: 6,
                            ft.ControlState.PRESSED: 1,
                        },
                        padding=20,
                        animation_duration=200,
                    ),
                    width=200,
                )
            else:
                return ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Icon(icon, size=20),
                            ft.Text(text, size=15, weight=ft.FontWeight.W_600),
                        ],
                        spacing=8,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=12),
                        bgcolor={
                            ft.ControlState.DEFAULT: "#6750A4" if primary else "#E8DEF8",
                            ft.ControlState.HOVERED: "#7F67BE" if primary else "#D0BCFF",
                            ft.ControlState.PRESSED: "#5A3D99" if primary else "#B69DF8",
                        },
                        color={
                            ft.ControlState.DEFAULT: "#FFFFFF" if primary else "#6750A4",
                        },
                        elevation={
                            ft.ControlState.DEFAULT: 2,
                            ft.ControlState.HOVERED: 6,
                            ft.ControlState.PRESSED: 1,
                        },
                        padding=20,
                        animation_duration=200,
                    ),
                    width=200,
                )

        # ========================================
        # 3. カスタムTextField（高度なスタイリング）
        # ========================================
        def create_custom_textfield(label: str, icon: str):
            return ft.Container(
                content=ft.TextField(
                    label=label,
                    prefix_icon=icon,
                    border_radius=12,
                    filled=True,
                    bgcolor=get_container_color(),
                    border_color=get_border_color(),
                    focused_border_color="#D0BCFF" if is_dark() else "#6750A4",
                    focused_bgcolor=get_surface_color(),
                    text_style=ft.TextStyle(size=16, color=get_text_color()),
                    label_style=ft.TextStyle(size=14, color=get_secondary_text_color()),
                    color=get_text_color(),
                ),
                width=300,
            )

        # ========================================
        # 4. バリデーション機能付きフォーム
        # ========================================
        import re

        # Validation state storage
        form_errors = {}
        form_values = {}
        form_refs = {}

        def validate_required(value: str, field_name: str) -> tuple[bool, str]:
            """必須フィールドのバリデーション"""
            if not value or value.strip() == "":
                return False, f"{field_name}は必須項目です"
            return True, ""

        def validate_email(value: str) -> tuple[bool, str]:
            """メールアドレスのバリデーション"""
            if not value:
                return False, "メールアドレスは必須項目です"
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, value):
                return False, "有効なメールアドレスを入力してください"
            return True, ""

        def validate_password(value: str) -> tuple[bool, str]:
            """パスワードのバリデーション"""
            if not value:
                return False, "パスワードは必須項目です"
            if len(value) < 8:
                return False, "パスワードは8文字以上必要です"
            if not any(c.isupper() for c in value):
                return False, "大文字を1文字以上含める必要があります"
            if not any(c.isdigit() for c in value):
                return False, "数字を1文字以上含める必要があります"
            return True, ""

        def validate_phone(value: str) -> tuple[bool, str]:
            """電話番号のバリデーション"""
            if not value:
                return True, ""  # Optional field
            phone_pattern = r'^0\d{9,10}$'
            if not re.match(phone_pattern, value.replace("-", "")):
                return False, "有効な電話番号を入力してください（例: 090-1234-5678）"
            return True, ""

        def validate_age(value: str) -> tuple[bool, str]:
            """年齢のバリデーション"""
            if not value or value == "選択してください":
                return False, "年齢を選択してください"
            return True, ""

        def create_validated_field(
            label: str,
            icon: str,
            field_key: str,
            validator,
            password: bool = False,
            multiline: bool = False
        ):
            """バリデーション付きテキストフィールド"""
            error_text = ft.Text(
                "",
                size=12,
                color="#F5576C",
                visible=False,
            )

            def on_change(e):
                value = e.control.value
                form_values[field_key] = value
                is_valid, error_msg = validator(value)

                if is_valid:
                    e.control.border_color = "#43E97B"
                    error_text.value = ""
                    error_text.visible = False
                    form_errors[field_key] = None
                else:
                    e.control.border_color = "#F5576C"
                    error_text.value = error_msg
                    error_text.visible = True
                    form_errors[field_key] = error_msg

                page.update()

            textfield = ft.TextField(
                label=label,
                prefix_icon=icon,
                border_radius=12,
                filled=True,
                bgcolor=get_container_color(),
                border_color=get_border_color(),
                focused_border_color="#D0BCFF" if is_dark() else "#6750A4",
                focused_bgcolor=get_surface_color(),
                text_style=ft.TextStyle(size=16, color=get_text_color()),
                label_style=ft.TextStyle(size=14, color=get_secondary_text_color()),
                color=get_text_color(),
                on_change=on_change,
                password=password,
                multiline=multiline,
                min_lines=3 if multiline else 1,
                max_lines=5 if multiline else 1,
                can_reveal_password=password,
            )

            form_refs[field_key] = textfield

            return ft.Column(
                [
                    ft.Container(
                        content=textfield,
                        width=None,
                    ),
                    error_text,
                ],
                spacing=4,
            )

        def create_dropdown_field(label: str, options: list, field_key: str, validator):
            """バリデーション付きドロップダウン"""
            error_text = ft.Text(
                "",
                size=12,
                color="#F5576C",
                visible=False,
            )

            def on_change(e):
                value = e.control.value
                form_values[field_key] = value
                is_valid, error_msg = validator(value)

                if is_valid:
                    e.control.border_color = "#43E97B"
                    error_text.value = ""
                    error_text.visible = False
                    form_errors[field_key] = None
                else:
                    e.control.border_color = "#F5576C"
                    error_text.value = error_msg
                    error_text.visible = True
                    form_errors[field_key] = error_msg

                page.update()

            dropdown = ft.Dropdown(
                label=label,
                options=[ft.dropdown.Option(opt) for opt in options],
                border_radius=12,
                filled=True,
                bgcolor=get_container_color(),
                border_color=get_border_color(),
                focused_border_color="#D0BCFF" if is_dark() else "#6750A4",
                text_style=ft.TextStyle(size=16, color=get_text_color()),
                label_style=ft.TextStyle(size=14, color=get_secondary_text_color()),
                on_change=on_change,
            )

            form_refs[field_key] = dropdown

            return ft.Column(
                [
                    ft.Container(
                        content=dropdown,
                        width=None,
                    ),
                    error_text,
                ],
                spacing=4,
            )

        # Submit result display
        submit_result = ft.Container(
            visible=False,
            padding=16,
            border_radius=12,
            bgcolor=get_container_color(),
        )

        def submit_form(e):
            """フォーム送信"""
            # Validate all fields
            all_valid = True

            # Trigger validation for all fields
            for field_key, field_ref in form_refs.items():
                if hasattr(field_ref, 'value'):
                    value = field_ref.value or ""

                    # Get appropriate validator
                    if field_key == "name":
                        is_valid, _ = validate_required(value, "お名前")
                    elif field_key == "email":
                        is_valid, _ = validate_email(value)
                    elif field_key == "password":
                        is_valid, _ = validate_password(value)
                    elif field_key == "phone":
                        is_valid, _ = validate_phone(value)
                    elif field_key == "age":
                        is_valid, _ = validate_age(value)
                    else:
                        is_valid = True

                    if not is_valid:
                        all_valid = False

            # Check if any errors exist
            if any(err is not None for err in form_errors.values()):
                all_valid = False

            # Display result
            if all_valid:
                submit_result.bgcolor = "#E8F5E9"
                submit_result.content = ft.Row(
                    [
                        ft.Icon(ft.Icons.CHECK_CIRCLE, color="#43E97B", size=24),
                        ft.Text(
                            "フォームが正常に送信されました",
                            size=14,
                            color="#2E7D32",
                            weight=ft.FontWeight.W_500,
                        ),
                    ],
                    spacing=12,
                )
                submit_result.visible = True
            else:
                submit_result.bgcolor = "#FFEBEE"
                submit_result.content = ft.Row(
                    [
                        ft.Icon(ft.Icons.ERROR, color="#F5576C", size=24),
                        ft.Text(
                            "エラーがあります。入力内容を確認してください",
                            size=14,
                            color="#C62828",
                            weight=ft.FontWeight.W_500,
                        ),
                    ],
                    spacing=12,
                )
                submit_result.visible = True

            page.update()

        # ========================================
        # 5. プログレスインジケーター（カスタム）
        # ========================================
        def create_progress_card(title: str, percentage: float, color: str):
            return ft.Container(
                padding=20,
                border_radius=16,
                bgcolor=get_surface_color(),
                border=ft.border.all(1, get_border_color()),
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=10,
                    color="#00000008" if not is_dark() else "#00000020",
                ),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(title, size=get_text_size(), weight=ft.FontWeight.W_500, color=get_text_color()),
                                ft.Container(expand=True),
                                ft.Text(
                                    f"{int(percentage * 100)}%",
                                    size=get_text_size(),
                                    weight=ft.FontWeight.W_600,
                                    color=color,
                                ),
                            ],
                        ),
                        ft.Container(height=8),
                        ft.Stack(
                            [
                                ft.Container(
                                    height=8,
                                    border_radius=4,
                                    bgcolor=get_border_color(),
                                ),
                                ft.Container(
                                    height=8,
                                    width=250 * percentage,
                                    border_radius=4,
                                    bgcolor=color,
                                ),
                            ],
                        ),
                    ],
                    spacing=4,
                ),
                width=290,
            )

        # ========================================
        # 5. ダッシュボードヘッダー
        # ========================================
        header = ft.Container(
            bgcolor="#6750A4" if not is_dark() else "#4A4458",
            padding=get_header_padding(),
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                "Flet UI カスタマイズデモ",
                                size=get_header_title_size(),
                                weight=ft.FontWeight.W_700,
                                color="#FFFFFF",
                            ),
                            ft.Text(
                                "高度なスタイリング・アニメーション・レスポンシブ対応",
                                size=get_header_subtitle_size(),
                                color="#FFFFFFCC",
                            ),
                        ],
                        spacing=4,
                    ),
                    ft.Container(expand=True),
                    ft.IconButton(
                        icon=ft.Icons.BRIGHTNESS_6,
                        icon_color="#FFFFFF",
                        icon_size=28,
                        on_click=lambda _: toggle_theme(),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )

        # ========================================
        # 6. 統計カードセクション
        # ========================================
        stats_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "統計カード - グラデーション & 影 & ホバーアニメーション",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                create_stats_card(
                                    "Total Users", "12,458", ft.Icons.PEOPLE, ["#667EEA", "#764BA2"]
                                ),
                                col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
                            ),
                            ft.Container(
                                create_stats_card(
                                    "Revenue", "¥2.4M", ft.Icons.ATTACH_MONEY, ["#F093FB", "#F5576C"]
                                ),
                                col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
                            ),
                            ft.Container(
                                create_stats_card(
                                    "Products", "856", ft.Icons.SHOPPING_BAG, ["#4FACFE", "#00F2FE"]
                                ),
                                col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
                            ),
                            ft.Container(
                                create_stats_card(
                                    "Growth", "+24%", ft.Icons.TRENDING_UP, ["#43E97B", "#38F9D7"]
                                ),
                                col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
                            ),
                        ],
                        spacing=20,
                        run_spacing=20,
                    ),
                ],
            ),
        )

        # ========================================
        # テーブルとグラフセクション
        # ========================================
        table_and_chart_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "テーブルとグラフ",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),

                    # DataTable（テーブル）
                    ft.Container(
                        bgcolor=get_container_color(),
                        border_radius=15,
                        padding=get_container_padding(),
                        content=ft.Column(
                            [
                                ft.Text("データテーブル", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                                ft.Container(height=10),
                                ft.Row(
                                    [
                                        ft.DataTable(
                                            columns=[
                                                ft.DataColumn(ft.Text("商品名", weight=ft.FontWeight.W_600, color=get_text_color(), no_wrap=True)),
                                                ft.DataColumn(ft.Text("カテゴリ", weight=ft.FontWeight.W_600, color=get_text_color(), no_wrap=True)),
                                                ft.DataColumn(ft.Text("価格", weight=ft.FontWeight.W_600, color=get_text_color(), no_wrap=True), numeric=True),
                                                ft.DataColumn(ft.Text("在庫", weight=ft.FontWeight.W_600, color=get_text_color(), no_wrap=True), numeric=True),
                                            ],
                                            rows=[
                                                ft.DataRow(
                                                    cells=[
                                                        ft.DataCell(ft.Text("ノートPC", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("電子機器", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("¥128,000", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("15", color=get_text_color(), no_wrap=True)),
                                                    ],
                                                ),
                                                ft.DataRow(
                                                    cells=[
                                                        ft.DataCell(ft.Text("マウス", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("周辺機器", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("¥3,200", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("48", color=get_text_color(), no_wrap=True)),
                                                    ],
                                                ),
                                                ft.DataRow(
                                                    cells=[
                                                        ft.DataCell(ft.Text("キーボード", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("周辺機器", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("¥8,900", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("32", color=get_text_color(), no_wrap=True)),
                                                    ],
                                                ),
                                                ft.DataRow(
                                                    cells=[
                                                        ft.DataCell(ft.Text("モニター", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("電子機器", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("¥42,000", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("22", color=get_text_color(), no_wrap=True)),
                                                    ],
                                                ),
                                                ft.DataRow(
                                                    cells=[
                                                        ft.DataCell(ft.Text("ヘッドセット", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("周辺機器", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("¥12,500", color=get_text_color(), no_wrap=True)),
                                                        ft.DataCell(ft.Text("28", color=get_text_color(), no_wrap=True)),
                                                    ],
                                                ),
                                            ],
                                            width=get_datatable_width(),
                                            border=ft.border.all(1, get_border_color()),
                                            border_radius=10,
                                            heading_row_color=get_surface_color(),
                                            column_spacing=get_datatable_column_spacing(),
                                            horizontal_lines=ft.border.BorderSide(1, get_border_color()),
                                        ),
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                ),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # バーグラフ
                    ft.Container(
                        bgcolor=get_container_color(),
                        border_radius=15,
                        padding=get_container_padding(),
                        content=ft.Column(
                            [
                                ft.Text("売上グラフ（月別）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                                ft.Container(height=10),
                                # 横スクロール可能なコンテナで囲む
                                ft.Row(
                                    [
                                        ft.Container(
                                            padding=get_container_padding(),
                                            bgcolor=get_surface_color(),
                                            border_radius=10,
                                            content=ft.Column(
                                                [
                                                    # グリッドラインとバーを重ねる
                                                    ft.Stack(
                                                        [
                                                            # 背景グリッドライン
                                                            ft.Column(
                                                                [
                                                                    ft.Row([
                                                                        ft.Text("180", size=get_small_text_size(), color=get_secondary_text_color(), width=30),
                                                                        ft.Container(height=1, bgcolor=get_border_color(), width=400),
                                                                    ]),
                                                                    ft.Container(height=59),
                                                                    ft.Row([
                                                                        ft.Text("120", size=get_small_text_size(), color=get_secondary_text_color(), width=30),
                                                                        ft.Container(height=1, bgcolor=get_border_color(), width=400),
                                                                    ]),
                                                                    ft.Container(height=59),
                                                                    ft.Row([
                                                                        ft.Text("60", size=get_small_text_size(), color=get_secondary_text_color(), width=30),
                                                                        ft.Container(height=1, bgcolor=get_border_color(), width=400),
                                                                    ]),
                                                                    ft.Container(height=59),
                                                                    ft.Row([
                                                                        ft.Text("0", size=get_small_text_size(), color=get_secondary_text_color(), width=30),
                                                                        ft.Container(height=1, bgcolor=get_border_color(), width=400),
                                                                    ]),
                                                                ],
                                                            ),
                                                            # バーグラフ（Y軸ラベルの幅を考慮して配置）
                                                            ft.Container(
                                                                padding=ft.padding.only(left=40, top=0),
                                                                content=ft.Row(
                                                                    [
                                                                        ft.Column(
                                                                            [
                                                                                ft.Container(
                                                                                    width=60,
                                                                                    height=180,
                                                                                    alignment=ft.alignment.bottom_center,
                                                                                    content=ft.Container(
                                                                                        width=60,
                                                                                        height=120,
                                                                                        bgcolor="#43E97B",
                                                                                        border_radius=5,
                                                                                    ),
                                                                                ),
                                                                                ft.Container(height=5),
                                                                                ft.Text("1月", size=12, color=get_secondary_text_color()),
                                                                            ],
                                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                        ),
                                                                        ft.Column(
                                                                            [
                                                                                ft.Container(
                                                                                    width=60,
                                                                                    height=180,
                                                                                    alignment=ft.alignment.bottom_center,
                                                                                    content=ft.Container(
                                                                                        width=60,
                                                                                        height=140,
                                                                                        bgcolor="#4FACFE",
                                                                                        border_radius=5,
                                                                                    ),
                                                                                ),
                                                                                ft.Container(height=5),
                                                                                ft.Text("2月", size=12, color=get_secondary_text_color()),
                                                                            ],
                                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                        ),
                                                                        ft.Column(
                                                                            [
                                                                                ft.Container(
                                                                                    width=60,
                                                                                    height=180,
                                                                                    alignment=ft.alignment.bottom_center,
                                                                                    content=ft.Container(
                                                                                        width=60,
                                                                                        height=100,
                                                                                        bgcolor="#F093FB",
                                                                                        border_radius=5,
                                                                                    ),
                                                                                ),
                                                                                ft.Container(height=5),
                                                                                ft.Text("3月", size=12, color=get_secondary_text_color()),
                                                                            ],
                                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                        ),
                                                                        ft.Column(
                                                                            [
                                                                                ft.Container(
                                                                                    width=60,
                                                                                    height=180,
                                                                                    alignment=ft.alignment.bottom_center,
                                                                                    content=ft.Container(
                                                                                        width=60,
                                                                                        height=160,
                                                                                        bgcolor="#FEC163",
                                                                                        border_radius=5,
                                                                                    ),
                                                                                ),
                                                                                ft.Container(height=5),
                                                                                ft.Text("4月", size=12, color=get_secondary_text_color()),
                                                                            ],
                                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                        ),
                                                                        ft.Column(
                                                                            [
                                                                                ft.Container(
                                                                                    width=60,
                                                                                    height=180,
                                                                                    alignment=ft.alignment.bottom_center,
                                                                                    content=ft.Container(
                                                                                        width=60,
                                                                                        height=130,
                                                                                        bgcolor="#667EEA",
                                                                                        border_radius=5,
                                                                                    ),
                                                                                ),
                                                                                ft.Container(height=5),
                                                                                ft.Text("5月", size=12, color=get_secondary_text_color()),
                                                                            ],
                                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                        ),
                                                                    ],
                                                                    spacing=20,
                                                                    alignment=ft.MainAxisAlignment.START,
                                                                ),
                                                            ),
                                                        ],
                                                        height=220,
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                ),
                                ft.Container(height=10),
                                ft.Text("各月の売上推移を視覚的に表示", size=12, color=get_secondary_text_color(), italic=True),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 折れ線グラフ
                    ft.Container(
                        bgcolor=get_container_color(),
                        border_radius=15,
                        padding=get_container_padding(),
                        content=ft.Column(
                            [
                                ft.Text("折れ線グラフ（売上推移）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                                ft.Container(height=10),
                                # 横スクロール可能にする
                                ft.Row(
                                    [
                                        ft.Container(
                                            width=500,
                                            height=300,
                                            padding=get_container_padding(),
                                            bgcolor=get_surface_color(),
                                            border_radius=10,
                                    content=ft.Stack(
                                        [
                                            # Y軸ラベル
                                            ft.Container(
                                                top=40,
                                                left=5,
                                                content=ft.Column(
                                                    [
                                                        ft.Text("180", size=get_small_text_size(), color=get_secondary_text_color()),
                                                        ft.Container(height=32),
                                                        ft.Text("120", size=get_small_text_size(), color=get_secondary_text_color()),
                                                        ft.Container(height=32),
                                                        ft.Text("60", size=get_small_text_size(), color=get_secondary_text_color()),
                                                        ft.Container(height=32),
                                                        ft.Text("0", size=get_small_text_size(), color=get_secondary_text_color()),
                                                    ],
                                                    spacing=0,
                                                ),
                                            ),
                                            # グリッド線（横）
                                            ft.Container(
                                                top=40,
                                                left=40,
                                                right=40,
                                                content=ft.Column(
                                                    [
                                                        ft.Container(height=40, border=ft.border.only(bottom=ft.BorderSide(1, get_border_color()))),
                                                        ft.Container(height=40, border=ft.border.only(bottom=ft.BorderSide(1, get_border_color()))),
                                                        ft.Container(height=40, border=ft.border.only(bottom=ft.BorderSide(1, get_border_color()))),
                                                        ft.Container(height=40, border=ft.border.only(bottom=ft.BorderSide(1, get_border_color()))),
                                                    ],
                                                    spacing=0,
                                                ),
                                            ),
                                            # データポイント
                                            ft.Container(
                                                left=80, top=140,
                                                width=12, height=12,
                                                bgcolor="#43E97B",
                                                border_radius=6,
                                            ),
                                            ft.Container(
                                                left=160, top=120,
                                                width=12, height=12,
                                                bgcolor="#4FACFE",
                                                border_radius=6,
                                            ),
                                            ft.Container(
                                                left=240, top=160,
                                                width=12, height=12,
                                                bgcolor="#F093FB",
                                                border_radius=6,
                                            ),
                                            ft.Container(
                                                left=320, top=100,
                                                width=12, height=12,
                                                bgcolor="#FEC163",
                                                border_radius=6,
                                            ),
                                            ft.Container(
                                                left=400, top=130,
                                                width=12, height=12,
                                                bgcolor="#667EEA",
                                                border_radius=6,
                                            ),
                                            # 月ラベル
                                            ft.Container(
                                                bottom=25,
                                                left=40,
                                                content=ft.Row(
                                                    [
                                                        ft.Container(width=80, content=ft.Text("1月", size=11, color=get_secondary_text_color(), text_align=ft.TextAlign.CENTER)),
                                                        ft.Container(width=80, content=ft.Text("2月", size=11, color=get_secondary_text_color(), text_align=ft.TextAlign.CENTER)),
                                                        ft.Container(width=80, content=ft.Text("3月", size=11, color=get_secondary_text_color(), text_align=ft.TextAlign.CENTER)),
                                                        ft.Container(width=80, content=ft.Text("4月", size=11, color=get_secondary_text_color(), text_align=ft.TextAlign.CENTER)),
                                                        ft.Container(width=80, content=ft.Text("5月", size=11, color=get_secondary_text_color(), text_align=ft.TextAlign.CENTER)),
                                                    ],
                                                    spacing=0,
                                                ),
                                            ),
                                        ],
                                    ),
                                        ),
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                ),
                                ft.Container(height=10),
                                ft.Text("時系列データの変化を線で表示", size=12, color=get_secondary_text_color(), italic=True),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 円グラフ
                    ft.Container(
                        bgcolor=get_container_color(),
                        border_radius=15,
                        padding=get_container_padding(),
                        content=ft.Column(
                            [
                                ft.Text("円グラフ（カテゴリ別売上）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                                ft.Container(height=10),
                                # 横スクロール可能にする
                                ft.Row(
                                    [
                                        # 円グラフ
                                        ft.Container(
                                            width=200,
                                            height=200,
                                            content=ft.Stack(
                                                [
                                                    # セグメント1: 40% (緑)
                                                    ft.Container(
                                                        width=200,
                                                        height=200,
                                                        border_radius=100,
                                                        bgcolor="#43E97B",
                                                    ),
                                                    # セグメント2: 30% (青)
                                                    ft.Container(
                                                        width=200,
                                                        height=200,
                                                        border_radius=100,
                                                        bgcolor="#4FACFE",
                                                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                                        gradient=ft.SweepGradient(
                                                            center=ft.alignment.center,
                                                            colors=["#4FACFE", "#4FACFE", get_container_color(), get_container_color()],
                                                            stops=[0, 0.3, 0.3, 1],
                                                            start_angle=0,
                                                            end_angle=6.28,
                                                        ),
                                                    ),
                                                    # セグメント3: 20% (ピンク)
                                                    ft.Container(
                                                        width=200,
                                                        height=200,
                                                        border_radius=100,
                                                        bgcolor="#F093FB",
                                                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                                        gradient=ft.SweepGradient(
                                                            center=ft.alignment.center,
                                                            colors=["#F093FB", "#F093FB", get_container_color(), get_container_color()],
                                                            stops=[0, 0.2, 0.2, 1],
                                                            start_angle=1.88,
                                                            end_angle=8.16,
                                                        ),
                                                    ),
                                                    # セグメント4: 10% (オレンジ)
                                                    ft.Container(
                                                        width=200,
                                                        height=200,
                                                        border_radius=100,
                                                        bgcolor="#FEC163",
                                                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                                        gradient=ft.SweepGradient(
                                                            center=ft.alignment.center,
                                                            colors=["#FEC163", "#FEC163", get_container_color(), get_container_color()],
                                                            stops=[0, 0.1, 0.1, 1],
                                                            start_angle=3.14,
                                                            end_angle=9.42,
                                                        ),
                                                    ),
                                                    # 中央の円（ドーナツ風）
                                                    ft.Container(
                                                        width=120,
                                                        height=120,
                                                        border_radius=60,
                                                        bgcolor=get_surface_color(),
                                                    ),
                                                ],
                                                alignment=ft.alignment.center,
                                            ),
                                        ),
                                        ft.Container(width=30),
                                        # 凡例
                                        ft.Column(
                                            [
                                                ft.Row(
                                                    [
                                                        ft.Container(width=20, height=20, bgcolor="#43E97B", border_radius=4),
                                                        ft.Text("電子機器 40%", size=get_text_size(), color=get_text_color()),
                                                    ],
                                                    spacing=10,
                                                ),
                                                ft.Container(height=8),
                                                ft.Row(
                                                    [
                                                        ft.Container(width=20, height=20, bgcolor="#4FACFE", border_radius=4),
                                                        ft.Text("周辺機器 30%", size=get_text_size(), color=get_text_color()),
                                                    ],
                                                    spacing=10,
                                                ),
                                                ft.Container(height=8),
                                                ft.Row(
                                                    [
                                                        ft.Container(width=20, height=20, bgcolor="#F093FB", border_radius=4),
                                                        ft.Text("ソフトウェア 20%", size=get_text_size(), color=get_text_color()),
                                                    ],
                                                    spacing=10,
                                                ),
                                                ft.Container(height=8),
                                                ft.Row(
                                                    [
                                                        ft.Container(width=20, height=20, bgcolor="#FEC163", border_radius=4),
                                                        ft.Text("その他 10%", size=get_text_size(), color=get_text_color()),
                                                    ],
                                                    spacing=10,
                                                ),
                                            ],
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    scroll=ft.ScrollMode.AUTO,
                                ),
                                ft.Container(height=10),
                                ft.Text("全体に占める各カテゴリの割合を表示", size=12, color=get_secondary_text_color(), italic=True),
                            ],
                        ),
                    ),
                ],
            ),
        )

        # ========================================
        # 7. インタラクティブコントロール
        # ========================================
        controls_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "インタラクティブコントロール - 状態別スタイリング",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Text("カスタムボタン", size=get_subsection_title_size(), weight=ft.FontWeight.W_500, color=get_text_color()),
                                        ft.Container(height=12),
                                        create_custom_button("Primary Action", ft.Icons.SEND, True),
                                        ft.Container(height=12),
                                        create_custom_button("Secondary", ft.Icons.BOOKMARK, False),
                                    ],
                                ),
                                col={"xs": 12, "md": 6},
                            ),
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Text(
                                            "カスタムフォーム - バリデーション機能付き",
                                            size=get_subsection_title_size(),
                                            weight=ft.FontWeight.W_500,
                                            color=get_text_color(),
                                        ),
                                        ft.Container(height=16),
                                        # Name field (required, min 2 chars)
                                        create_validated_field(
                                            "お名前",
                                            ft.Icons.PERSON,
                                            "name",
                                            lambda v: validate_required(v, "お名前"),
                                        ),
                                        ft.Container(height=12),
                                        # Email field (required, email format)
                                        create_validated_field(
                                            "メールアドレス",
                                            ft.Icons.EMAIL,
                                            "email",
                                            validate_email,
                                        ),
                                        ft.Container(height=12),
                                        # Password field (required, 8+ chars, uppercase + digit)
                                        create_validated_field(
                                            "パスワード",
                                            ft.Icons.LOCK,
                                            "password",
                                            validate_password,
                                            password=True,
                                        ),
                                        ft.Container(height=12),
                                        # Phone field (optional, format validation)
                                        create_validated_field(
                                            "電話番号（任意）",
                                            ft.Icons.PHONE,
                                            "phone",
                                            validate_phone,
                                        ),
                                        ft.Container(height=12),
                                        # Age dropdown (required)
                                        create_dropdown_field(
                                            "年齢層",
                                            ["選択してください", "18-24歳", "25-34歳", "35-44歳", "45-54歳", "55歳以上"],
                                            "age",
                                            validate_age,
                                        ),
                                        ft.Container(height=12),
                                        # Message field (multiline, optional)
                                        create_validated_field(
                                            "メッセージ（任意）",
                                            ft.Icons.MESSAGE,
                                            "message",
                                            lambda v: (True, ""),
                                            multiline=True,
                                        ),
                                        ft.Container(height=20),
                                        # Submit button
                                        ft.ElevatedButton(
                                            "送信する",
                                            icon=ft.Icons.SEND,
                                            on_click=submit_form,
                                            style=ft.ButtonStyle(
                                                bgcolor="#6750A4",
                                                color="white",
                                                padding=ft.padding.symmetric(horizontal=40, vertical=16),
                                                shape=ft.RoundedRectangleBorder(radius=12),
                                            ),
                                        ),
                                        ft.Container(height=12),
                                        # Submit result display
                                        submit_result,
                                    ],
                                ),
                                col={"xs": 12, "md": 6},
                            ),
                        ],
                        spacing=30,
                    ),
                ],
            ),
        )

        # ========================================
        # 8. プログレスセクション
        # ========================================
        progress_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "プログレス表示 - カスタムデザイン",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),
                    ft.ResponsiveRow(
                        [
                            ft.Container(
                                create_progress_card("UI Design", 0.85, "#667EEA"),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                            ft.Container(
                                create_progress_card("Development", 0.62, "#F5576C"),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                            ft.Container(
                                create_progress_card("Testing", 0.43, "#43E97B"),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                        ],
                        spacing=20,
                        run_spacing=20,
                    ),
                ],
            ),
        )

        # ========================================
        # 9. 高度なコンテナ装飾デモ
        # ========================================
        neumorph_bg = "#E0E5EC" if not is_dark() else "#2B2930"
        neumorph_shadow_dark = "#A3B1C6" if not is_dark() else "#1C1B1F"
        neumorph_shadow_light = "#FFFFFF" if not is_dark() else "#3B3841"

        decoration_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "高度な装飾 - Neumorphism & Multi-Shadow",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),
                    ft.ResponsiveRow(
                        [
                            # ネオモーフィズム（本格実装）
                            ft.Container(
                                ft.Container(
                                    width=250,
                                    height=180,
                                    border_radius=30,
                                    bgcolor=neumorph_bg,
                                    padding=get_container_padding(),
                                    shadow=[
                                        # 暗い影（右下）
                                        ft.BoxShadow(
                                            spread_radius=1,
                                            blur_radius=15,
                                            color=neumorph_shadow_dark,
                                            offset=ft.Offset(8, 8),
                                        ),
                                        # 明るい影（左上）
                                        ft.BoxShadow(
                                            spread_radius=1,
                                            blur_radius=15,
                                            color=neumorph_shadow_light,
                                            offset=ft.Offset(-8, -8),
                                        ),
                                    ],
                                    content=ft.Column(
                                        [
                                            ft.Container(
                                                width=60,
                                                height=60,
                                                border_radius=30,
                                                bgcolor=neumorph_bg,
                                                shadow=[
                                                    ft.BoxShadow(
                                                        spread_radius=0,
                                                        blur_radius=10,
                                                        color=neumorph_shadow_dark,
                                                        offset=ft.Offset(5, 5),
                                                    ),
                                                    ft.BoxShadow(
                                                        spread_radius=0,
                                                        blur_radius=10,
                                                        color=neumorph_shadow_light,
                                                        offset=ft.Offset(-5, -5),
                                                    ),
                                                ],
                                                content=ft.Icon(name=ft.Icons.LAYERS, size=32, color="#D0BCFF" if is_dark() else "#6750A4"),
                                                alignment=ft.alignment.center,
                                            ),
                                            ft.Container(height=12),
                                            ft.Text(
                                                "Neumorphism",
                                                size=18,
                                                weight=ft.FontWeight.W_700,
                                                color="#D0BCFF" if is_dark() else "#6750A4",
                                            ),
                                            ft.Text(
                                                "ソフトな凹凸感",
                                                size=12,
                                                color=get_secondary_text_color(),
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                            # マルチレイヤーシャドウ
                            ft.Container(
                                ft.Container(
                                    width=250,
                                    height=150,
                                    border_radius=20,
                                    bgcolor=get_surface_color(),
                                    padding=get_container_padding(),
                                    shadow=[
                                        ft.BoxShadow(
                                            spread_radius=0,
                                            blur_radius=10,
                                            color="#6750A440",
                                            offset=ft.Offset(0, 4),
                                        ),
                                        ft.BoxShadow(
                                            spread_radius=0,
                                            blur_radius=30,
                                            color="#6750A420",
                                            offset=ft.Offset(0, 15),
                                        ),
                                    ],
                                    content=ft.Column(
                                        [
                                            ft.Icon(ft.Icons.AUTO_AWESOME, size=40, color="#D0BCFF" if is_dark() else "#6750A4"),
                                            ft.Container(height=8),
                                            ft.Text(
                                                "Multi-Shadow",
                                                size=get_subsection_title_size(),
                                                weight=ft.FontWeight.W_600,
                                                color=get_text_color(),
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                        ],
                        spacing=20,
                        run_spacing=20,
                    ),
                ],
            ),
        )

        # ========================================
        # 10. 全スタイリング手法デモ
        # ========================================
        styling_demo_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "全スタイリング手法デモ - Fletで利用可能な全機能",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),

                    # 1. Containerプロパティの包括デモ
                    ft.Text("1. Container プロパティ", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.ResponsiveRow(
                        [
                            # パディング・マージン
                            ft.Container(
                                ft.Container(
                                    width=200,
                                    height=120,
                                    padding=ft.padding.only(left=20, top=10, right=20, bottom=10),
                                    margin=10,
                                    bgcolor="#E8DEF8" if not is_dark() else "#4A4458",
                                    border_radius=15,
                                    content=ft.Text(
                                        "Padding & Margin",
                                        color="#6750A4" if not is_dark() else "#D0BCFF",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 3},
                            ),
                            # ボーダー
                            ft.Container(
                                ft.Container(
                                    width=200,
                                    height=120,
                                    padding=get_container_padding(),
                                    border=ft.border.all(3, "#6750A4" if not is_dark() else "#D0BCFF"),
                                    border_radius=15,
                                    content=ft.Text(
                                        "Border",
                                        color="#6750A4" if not is_dark() else "#D0BCFF",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 3},
                            ),
                            # 角丸バリエーション
                            ft.Container(
                                ft.Container(
                                    width=200,
                                    height=120,
                                    padding=get_container_padding(),
                                    bgcolor="#F093FB",
                                    border_radius=ft.border_radius.only(
                                        top_left=30,
                                        top_right=5,
                                        bottom_left=5,
                                        bottom_right=30,
                                    ),
                                    content=ft.Text(
                                        "Custom Radius",
                                        color="#FFFFFF",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 3},
                            ),
                            # 透明度
                            ft.Container(
                                ft.Container(
                                    width=200,
                                    height=120,
                                    padding=get_container_padding(),
                                    bgcolor="#6750A480",
                                    border_radius=15,
                                    content=ft.Text(
                                        "Opacity (50%)",
                                        color="#FFFFFF",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 3},
                            ),
                        ],
                        spacing=15,
                        run_spacing=15,
                    ),

                    ft.Container(height=30),

                    # 2. グラデーション
                    ft.Text("2. Gradient（グラデーション）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.ResponsiveRow(
                        [
                            # Linear Gradient
                            ft.Container(
                                ft.Container(
                                    width=200,
                                    height=120,
                                    padding=get_container_padding(),
                                    border_radius=15,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_left,
                                        end=ft.alignment.bottom_right,
                                        colors=["#667EEA", "#764BA2", "#F093FB"],
                                    ),
                                    content=ft.Text(
                                        "Linear Gradient",
                                        color="#FFFFFF",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                            # Radial Gradient
                            ft.Container(
                                ft.Container(
                                    width=200,
                                    height=120,
                                    padding=get_container_padding(),
                                    border_radius=15,
                                    gradient=ft.RadialGradient(
                                        colors=["#FF6B9D", "#C44569", "#FEC163"],
                                    ),
                                    content=ft.Text(
                                        "Radial Gradient",
                                        color="#FFFFFF",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                            # Sweep Gradient
                            ft.Container(
                                ft.Container(
                                    width=200,
                                    height=120,
                                    padding=get_container_padding(),
                                    border_radius=15,
                                    gradient=ft.SweepGradient(
                                        center=ft.alignment.center,
                                        colors=["#43E97B", "#38F9D7", "#667EEA", "#F093FB", "#43E97B"],
                                    ),
                                    content=ft.Text(
                                        "Sweep Gradient",
                                        color="#FFFFFF",
                                        weight=ft.FontWeight.W_600,
                                    ),
                                ),
                                col={"xs": 12, "md": 6, "lg": 4},
                            ),
                        ],
                        spacing=15,
                        run_spacing=15,
                    ),

                    ft.Container(height=30),

                    # 3. TextStyleバリエーション
                    ft.Text("3. TextStyle（テキストスタイル）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Font Weight Variations",
                                    size=get_text_size(),
                                    weight=ft.FontWeight.W_300,
                                    color=get_text_color(),
                                ),
                                ft.Text(
                                    "Font Weight W_400 (Normal)",
                                    size=get_subsection_title_size(),
                                    weight=ft.FontWeight.W_400,
                                    color=get_text_color(),
                                ),
                                ft.Text(
                                    "Font Weight W_600 (Semi-Bold)",
                                    size=get_subsection_title_size(),
                                    weight=ft.FontWeight.W_600,
                                    color=get_text_color(),
                                ),
                                ft.Text(
                                    "Font Weight W_700 (Bold)",
                                    size=get_subsection_title_size(),
                                    weight=ft.FontWeight.W_700,
                                    color=get_text_color(),
                                ),
                                ft.Divider(height=20, color=get_border_color()),
                                ft.Text(
                                    "Large Bold Text",
                                    size=24,
                                    weight=ft.FontWeight.W_700,
                                    color="#D0BCFF" if is_dark() else "#6750A4",
                                ),
                                ft.Text(
                                    "Italic Text",
                                    size=get_subsection_title_size(),
                                    italic=True,
                                    color=get_secondary_text_color(),
                                ),
                                ft.Text(
                                    "Color Text (Primary)",
                                    size=get_subsection_title_size(),
                                    color="#D0BCFF" if is_dark() else "#6750A4",
                                ),
                                ft.Text(
                                    "Color Text (Secondary)",
                                    size=get_subsection_title_size(),
                                    color=get_secondary_text_color(),
                                ),
                                ft.Divider(height=20, color=get_border_color()),
                                ft.Text(
                                    "デフォルトフォント：これは通常のテキストです",
                                    size=get_subsection_title_size(),
                                    color=get_text_color(),
                                ),
                                ft.Text(
                                    "築豊明朝フォント：美しい日本語の明朝体です",
                                    size=get_subsection_title_size(),
                                    font_family="TsukuhouMincho",
                                    color=get_text_color(),
                                ),
                                ft.Text(
                                    "築豊明朝（大）：カスタムフォントのデモンストレーション",
                                    size=24,
                                    font_family="TsukuhouMincho",
                                    color="#D0BCFF" if is_dark() else "#6750A4",
                                    weight=ft.FontWeight.W_600,
                                ),
                                ft.Text(
                                    "築豊明朝：吾輩は猫である。名前はまだ無い。",
                                    size=18,
                                    font_family="TsukuhouMincho",
                                    color=get_secondary_text_color(),
                                ),
                            ],
                            spacing=8,
                        ),
                    ),

                ],
                spacing=0,
            ),
        )

        # ========================================
        # 11. 追加UIコンポーネント
        # ========================================
        additional_components_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "追加UIコンポーネント - スライダー・スイッチ・チェックボックスなど",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),

                    ft.Container(height=30),

                    # スライダー・スイッチ・チェックボックス
                    ft.Text("1. Slider, Switch, Checkbox", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.ResponsiveRow(
                        [
                            # スライダー
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Slider", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.Slider(
                                                min=0,
                                                max=100,
                                                value=50,
                                                label="{value}%",
                                                active_color="#D0BCFF" if is_dark() else "#6750A4",
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ),
                                col={"xs": 12, "md": 4},
                            ),
                            # スイッチ
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Switch", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.Switch(
                                                label="通知を有効化",
                                                value=False,
                                                active_color="#D0BCFF" if is_dark() else "#6750A4",
                                                label_style=ft.TextStyle(color=get_text_color()),
                                                on_change=toggle_notification,
                                            ),
                                            ft.Switch(
                                                ref=dark_mode_switch,
                                                label="ダークモード",
                                                value=is_dark(),
                                                active_color="#D0BCFF" if is_dark() else "#6750A4",
                                                on_change=toggle_theme,
                                                label_style=ft.TextStyle(color=get_text_color()),
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ),
                                col={"xs": 12, "md": 4},
                            ),
                            # チェックボックス
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Checkbox", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.Checkbox(
                                                label="オプション 1",
                                                value=True,
                                                active_color="#D0BCFF" if is_dark() else "#6750A4",
                                                label_style=ft.TextStyle(color=get_text_color()),
                                            ),
                                            ft.Checkbox(
                                                label="オプション 2",
                                                value=False,
                                                active_color="#D0BCFF" if is_dark() else "#6750A4",
                                                label_style=ft.TextStyle(color=get_text_color()),
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ),
                                col={"xs": 12, "md": 4},
                            ),
                        ],
                        spacing=15,
                        run_spacing=15,
                    ),

                    ft.Container(height=30),

                    # ラジオボタンとドロップダウン
                    ft.Text("2. Radio & Dropdown", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.ResponsiveRow(
                        [
                            # ラジオボタン
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Radio Group", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.RadioGroup(
                                                content=ft.Column([
                                                    ft.Radio(value="1", label="選択肢 1", active_color="#D0BCFF" if is_dark() else "#6750A4", label_style=ft.TextStyle(color=get_text_color())),
                                                    ft.Radio(value="2", label="選択肢 2", active_color="#D0BCFF" if is_dark() else "#6750A4", label_style=ft.TextStyle(color=get_text_color())),
                                                    ft.Radio(value="3", label="選択肢 3", active_color="#D0BCFF" if is_dark() else "#6750A4", label_style=ft.TextStyle(color=get_text_color())),
                                                ]),
                                                value="1",
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ),
                                col={"xs": 12, "md": 6},
                            ),
                            # ドロップダウン
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Dropdown", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.Dropdown(
                                                label="国を選択",
                                                value="jp",
                                                options=[
                                                    ft.dropdown.Option("jp", "日本"),
                                                    ft.dropdown.Option("us", "アメリカ"),
                                                    ft.dropdown.Option("uk", "イギリス"),
                                                    ft.dropdown.Option("fr", "フランス"),
                                                ],
                                                border_color=get_border_color(),
                                                focused_border_color="#D0BCFF" if is_dark() else "#6750A4",
                                                label_style=ft.TextStyle(color=get_secondary_text_color()),
                                                text_style=ft.TextStyle(color=get_text_color()),
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ),
                                col={"xs": 12, "md": 6},
                            ),
                        ],
                        spacing=15,
                        run_spacing=15,
                    ),

                    ft.Container(height=30),

                    # Divider（区切り線）
                    ft.Text("3. Divider & VerticalDivider", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text("水平区切り線", size=get_text_size(), color=get_text_color()),
                                ft.Divider(height=1, color="#D0BCFF" if is_dark() else "#6750A4"),
                                ft.Text("異なる色の区切り線", size=get_text_size(), color=get_text_color()),
                                ft.Divider(height=2, color="#F093FB"),
                                ft.Text("太い区切り線", size=get_text_size(), color=get_text_color()),
                                ft.Divider(height=5, color=get_border_color()),
                            ],
                            spacing=10,
                        ),
                    ),

                    ft.Container(height=30),

                    # IconButton
                    ft.Text("4. IconButton（アイコンボタン）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.Icons.HOME,
                                    icon_color="#D0BCFF" if is_dark() else "#6750A4",
                                    icon_size=30,
                                    tooltip="ホーム",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.SETTINGS,
                                    icon_color="#D0BCFF" if is_dark() else "#6750A4",
                                    icon_size=30,
                                    tooltip="設定",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.HELP,
                                    icon_color="#D0BCFF" if is_dark() else "#6750A4",
                                    icon_size=30,
                                    tooltip="ヘルプ",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.FAVORITE,
                                    icon_color="#F093FB",
                                    icon_size=30,
                                    tooltip="お気に入り",
                                ),
                            ],
                            spacing=20,
                        ),
                    ),
                ],
                spacing=0,
            ),
        )

        # ========================================
        # 12. アニメーションデモ
        # ========================================

        # アニメーション状態管理
        animated_box = ft.Ref[ft.Container]()
        fade_box = ft.Ref[ft.Container]()
        rotate_box = ft.Ref[ft.Container]()
        scale_box = ft.Ref[ft.Container]()

        # ページ遷移アニメーション用
        slide_container = ft.Ref[ft.Container]()
        slide_page_1 = ft.Ref[ft.Container]()
        slide_page_2 = ft.Ref[ft.Container]()

        # ダイアログ/ボトムシート用の関数
        dialog_ref = [None]

        def close_custom_dialog(e):
            if dialog_ref[0]:
                page.overlay.remove(dialog_ref[0])
                dialog_ref[0] = None
                page.update()

        dialog_content_ref = ft.Ref[ft.Container]()

        async def fade_in_dialog():
            await asyncio.sleep(0.05)
            if dialog_content_ref.current:
                dialog_content_ref.current.opacity = 1
                dialog_content_ref.current.update()

        def show_animated_dialog(e):
            # カスタムダイアログをContainerで作成
            dialog_content = ft.Container(
                ref=dialog_content_ref,
                width=400,
                bgcolor=get_surface_color(),
                border_radius=20,
                padding=30,
                opacity=0,
                animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
                shadow=ft.BoxShadow(
                    spread_radius=5,
                    blur_radius=30,
                    color="#00000040",
                ),
                content=ft.Column(
                    [
                        ft.Text("アニメーション付きダイアログ", size=get_section_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                        ft.Container(height=20),
                        ft.Icon(ft.Icons.CHECK_CIRCLE, color="#43E97B", size=60),
                        ft.Container(height=10),
                        ft.Text("フェードインで表示されます", size=get_subsection_title_size(), color=get_text_color(), text_align=ft.TextAlign.CENTER),
                        ft.Container(height=20),
                        ft.ElevatedButton("閉じる", on_click=close_custom_dialog, width=150),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    tight=True,
                ),
            )

            overlay = ft.Stack(
                [
                    # 背景のオーバーレイ
                    ft.Container(
                        bgcolor="#00000080",
                        expand=True,
                        on_click=close_custom_dialog,
                    ),
                    # ダイアログコンテンツ（中央配置）
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(expand=True),
                                ft.Row(
                                    [dialog_content],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Container(expand=True),
                            ],
                        ),
                        expand=True,
                    ),
                ],
            )

            dialog_ref[0] = overlay
            page.overlay.append(overlay)
            page.update()

            # フェードインアニメーションを開始（少し遅延させる）
            page.run_task(fade_in_dialog)

        def show_bottom_sheet(e):
            bs = ft.BottomSheet(
                content=ft.Container(
                    padding=30,
                    content=ft.Column(
                        [
                            ft.Text("ボトムシート", size=get_section_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                            ft.Container(height=10),
                            ft.Text("下からスライドインします", color=get_secondary_text_color()),
                            ft.Container(height=20),
                            ft.Row(
                                [
                                    ft.IconButton(ft.Icons.SHARE, bgcolor="#E8DEF8" if not is_dark() else "#4A4458"),
                                    ft.IconButton(ft.Icons.BOOKMARK, bgcolor="#E8DEF8" if not is_dark() else "#4A4458"),
                                    ft.IconButton(ft.Icons.FAVORITE, bgcolor="#E8DEF8" if not is_dark() else "#4A4458"),
                                ],
                            ),
                            ft.Container(height=10),
                            ft.ElevatedButton("閉じる", on_click=lambda _: close_bottom_sheet(bs)),
                        ],
                        tight=True,
                    ),
                ),
                open=True,
            )
            page.overlay.append(bs)
            page.update()

        def close_bottom_sheet(bs):
            bs.open = False
            page.update()

        # アニメーションカーブ比較用
        curve_linear = ft.Ref[ft.Container]()
        curve_ease = ft.Ref[ft.Container]()
        curve_bounce = ft.Ref[ft.Container]()

        def animate_curves(e):
            # すべてのボックスを右に移動
            if curve_linear.current:
                curve_linear.current.offset = ft.Offset(5, 0) if curve_linear.current.offset.x == 0 else ft.Offset(0, 0)
                curve_linear.current.update()
            if curve_ease.current:
                curve_ease.current.offset = ft.Offset(5, 0) if curve_ease.current.offset.x == 0 else ft.Offset(0, 0)
                curve_ease.current.update()
            if curve_bounce.current:
                curve_bounce.current.offset = ft.Offset(5, 0) if curve_bounce.current.offset.x == 0 else ft.Offset(0, 0)
                curve_bounce.current.update()

        # ページ遷移アニメーション関数
        def slide_to_page_2(e):
            if slide_page_1.current and slide_page_2.current:
                slide_page_1.current.offset = ft.Offset(-1, 0)
                slide_page_2.current.offset = ft.Offset(0, 0)
                slide_page_1.current.update()
                slide_page_2.current.update()

        def slide_to_page_1(e):
            if slide_page_1.current and slide_page_2.current:
                slide_page_1.current.offset = ft.Offset(0, 0)
                slide_page_2.current.offset = ft.Offset(1, 0)
                slide_page_1.current.update()
                slide_page_2.current.update()

        # スクロールアニメーション用
        scroll_items = []
        for i in range(5):
            item_ref = ft.Ref[ft.Container]()
            scroll_items.append(item_ref)

        def create_scroll_item(index, item_ref):
            # 初期状態での位置を計算（最初のアイテムが中心）
            container_height = 300
            container_center = container_height / 2
            item_height = 115
            item_center = index * item_height + 50
            distance_from_center = abs(item_center - container_center)
            max_distance = container_height / 2

            # 初期 scale と opacity を計算
            initial_scale = max(0.7, 1.2 - (distance_from_center / max_distance) * 0.5)
            initial_opacity = max(0.5, 1.0 - (distance_from_center / max_distance) * 0.5)

            return ft.Container(
                ref=item_ref,
                width=280,
                height=100,
                bgcolor=["#667EEA", "#F093FB", "#43E97B", "#FEC163", "#4FACFE"][index],
                border_radius=15,
                padding=get_container_padding(),
                opacity=initial_opacity,
                scale=initial_scale,
                animate_opacity=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
                animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
                content=ft.Column(
                    [
                        ft.Icon(
                            [ft.Icons.STAR, ft.Icons.FAVORITE, ft.Icons.THUMB_UP, ft.Icons.EMOJI_EVENTS, ft.Icons.ROCKET_LAUNCH][index],
                            color="#FFFFFF",
                            size=30,
                        ),
                        ft.Text(f"アイテム {index + 1}", color="#FFFFFF", size=get_subsection_title_size(), weight=ft.FontWeight.W_600),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )

        scroll_column_ref = ft.Ref[ft.Column]()

        def on_scroll(e):
            # スクロール位置を取得
            if e.pixels is not None:
                scroll_position = e.pixels
                container_height = 300  # コンテナの高さ
                container_center = container_height / 2  # 150px
                item_height = 115  # アイテムの高さ + spacing

                # 各アイテムの位置に応じて scale と opacity を計算
                for i, item in enumerate(scroll_items):
                    if item.current:
                        # アイテムの中心位置を計算（スクロール位置を考慮）
                        item_center = (i * item_height + 50) - scroll_position

                        # コンテナの中心からの距離を計算
                        distance_from_center = abs(item_center - container_center)

                        # 距離に基づいて scale を計算（中心に近いほど大きく）
                        # 最大 scale: 1.2, 最小 scale: 0.7
                        max_distance = container_height / 2
                        scale_factor = max(0.7, 1.2 - (distance_from_center / max_distance) * 0.5)

                        # opacity も距離に応じて調整（中心に近いほど明るく）
                        opacity_factor = max(0.5, 1.0 - (distance_from_center / max_distance) * 0.5)

                        item.current.scale = scale_factor
                        item.current.opacity = opacity_factor
                        item.current.update()

        # アニメーション制御関数
        def animate_container(e):
            if animated_box.current:
                # 現在のサイズをトグル
                current_width = animated_box.current.width
                if current_width == 100:
                    animated_box.current.width = 200
                    animated_box.current.height = 200
                    animated_box.current.bgcolor = "#F093FB"
                    animated_box.current.border_radius = 100
                else:
                    animated_box.current.width = 100
                    animated_box.current.height = 100
                    animated_box.current.bgcolor = "#6750A4" if not is_dark() else "#D0BCFF"
                    animated_box.current.border_radius = 20
                animated_box.current.update()

        def toggle_fade(e):
            if fade_box.current:
                fade_box.current.opacity = 0.0 if fade_box.current.opacity == 1.0 else 1.0
                fade_box.current.update()

        def toggle_rotate(e):
            if rotate_box.current:
                current_angle = rotate_box.current.rotate.angle if rotate_box.current.rotate else 0
                rotate_box.current.rotate = ft.Rotate(angle=current_angle + 3.14159 / 2)
                rotate_box.current.update()

        def toggle_scale(e):
            if scale_box.current:
                current_scale = scale_box.current.scale
                if current_scale == 1.0:
                    scale_box.current.scale = 1.5
                else:
                    scale_box.current.scale = 1.0
                scale_box.current.update()

        # Canvas アニメーション用の代替（プログレスバーアニメーション）
        wave_progress = ft.Ref[ft.ProgressBar]()
        wave_animating = [False]

        async def animate_wave_loop():
            wave_animating[0] = True
            for i in range(100):
                if not wave_animating[0]:
                    break
                if wave_progress.current:
                    wave_progress.current.value = i / 100.0
                    wave_progress.current.update()
                await asyncio.sleep(0.02)
            if wave_progress.current:
                wave_progress.current.value = 0.0
                wave_progress.current.update()
            wave_animating[0] = False

        def animate_wave(e):
            if not wave_animating[0]:
                page.run_task(animate_wave_loop)

        animation_section = ft.Container(
            padding=get_section_padding(),
            content=ft.Column(
                [
                    ft.Text(
                        "アニメーション機能デモ - Flet標準 & 高度なアニメーション",
                        size=get_section_title_size(),
                        weight=ft.FontWeight.W_600,
                        color=get_text_color(),
                    ),
                    ft.Container(height=20),

                    # 1. AnimatedContainer
                    ft.Text("1. AnimatedContainer（サイズ・色・角丸のトランジション）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text("クリックでアニメーション", color=get_text_color()),
                                ft.Container(height=10),
                                ft.Row(
                                    [
                                        ft.Container(
                                            ref=animated_box,
                                            width=100,
                                            height=100,
                                            bgcolor="#6750A4" if not is_dark() else "#D0BCFF",
                                            border_radius=20,
                                            animate=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
                                            on_click=animate_container,
                                            alignment=ft.alignment.center,
                                            content=ft.Icon(ft.Icons.TOUCH_APP, color="#FFFFFF", size=30),
                                        ),
                                        ft.Container(width=20),
                                        ft.Text("クリックすると\nサイズ・色・角丸が\nアニメーション", color=get_secondary_text_color(), size=get_text_size()),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 2. AnimatedOpacity, Rotation, Scale
                    ft.Text("2. Opacity（フェード）・Rotation（回転）・Scale（拡大縮小）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.ResponsiveRow(
                        [
                            # Fade
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Fade", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.Container(height=10),
                                            ft.Container(
                                                ref=fade_box,
                                                width=80,
                                                height=80,
                                                bgcolor="#43E97B",
                                                border_radius=40,
                                                opacity=1.0,
                                                animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                                                content=ft.Icon(ft.Icons.STAR, color="#FFFFFF", size=40),
                                                alignment=ft.alignment.center,
                                            ),
                                            ft.Container(height=10),
                                            ft.ElevatedButton("フェード", on_click=toggle_fade),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ),
                                col={"xs": 12, "md": 4},
                            ),
                            # Rotate
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Rotate", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.Container(height=10),
                                            ft.Container(
                                                ref=rotate_box,
                                                width=80,
                                                height=80,
                                                bgcolor="#F093FB",
                                                border_radius=15,
                                                rotate=ft.Rotate(0),
                                                animate_rotation=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                                                content=ft.Icon(ft.Icons.REFRESH, color="#FFFFFF", size=40),
                                                alignment=ft.alignment.center,
                                            ),
                                            ft.Container(height=10),
                                            ft.ElevatedButton("回転", on_click=toggle_rotate),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ),
                                col={"xs": 12, "md": 4},
                            ),
                            # Scale
                            ft.Container(
                                ft.Container(
                                    padding=get_container_padding(),
                                    bgcolor=get_container_color(),
                                    border_radius=15,
                                    content=ft.Column(
                                        [
                                            ft.Text("Scale", weight=ft.FontWeight.W_600, color=get_text_color()),
                                            ft.Container(height=10),
                                            ft.Container(
                                                ref=scale_box,
                                                width=80,
                                                height=80,
                                                bgcolor="#667EEA",
                                                border_radius=40,
                                                scale=1.0,
                                                animate_scale=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
                                                content=ft.Icon(ft.Icons.ZOOM_IN, color="#FFFFFF", size=40),
                                                alignment=ft.alignment.center,
                                            ),
                                            ft.Container(height=10),
                                            ft.ElevatedButton("拡大", on_click=toggle_scale),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ),
                                col={"xs": 12, "md": 4},
                            ),
                        ],
                        spacing=15,
                        run_spacing=15,
                    ),

                    ft.Container(height=30),

                    # 3. プログレスバーアニメーション
                    ft.Text("3. プログレスバー アニメーション", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text("プログレスバーのアニメーション", color=get_text_color()),
                                ft.Container(height=10),
                                ft.Container(
                                    width=300,
                                    padding=get_container_padding(),
                                    bgcolor=get_surface_color(),
                                    border_radius=15,
                                    border=ft.border.all(1, get_border_color()),
                                    content=ft.Column(
                                        [
                                            ft.ProgressBar(ref=wave_progress, value=0.0, color="#6750A4" if not is_dark() else "#D0BCFF", bgcolor=get_border_color()),
                                        ],
                                    ),
                                ),
                                ft.Container(height=10),
                                ft.ElevatedButton("アニメーション", on_click=animate_wave),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 4. インク波紋エフェクト
                    ft.Text("4. Ripple Effect（インク波紋エフェクト）", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text("クリックすると波紋が広がる", color=get_text_color()),
                                ft.Container(height=10),
                                ft.Row(
                                    [
                                        ft.Container(
                                            width=120,
                                            height=120,
                                            border_radius=15,
                                            ink=True,
                                            bgcolor="#E8DEF8" if not is_dark() else "#4A4458",
                                            content=ft.Column(
                                                [
                                                    ft.Icon(ft.Icons.TOUCH_APP, color="#6750A4" if not is_dark() else "#D0BCFF", size=40),
                                                    ft.Text("クリック", color=get_text_color(), size=get_text_size()),
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            ),
                                            on_click=lambda _: None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 5. ページ遷移風アニメーション
                    ft.Text("5. スライドイン・アウトアニメーション", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),

                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text("画面遷移風のアニメーション", color=get_text_color()),
                                ft.Container(height=10),
                                ft.Stack(
                                    [
                                        # ページ1
                                        ft.Container(
                                            ref=slide_page_1,
                                            width=300,
                                            height=180,
                                            bgcolor="#6750A4" if not is_dark() else "#4A4458",
                                            border_radius=15,
                                            content=ft.Column(
                                                [
                                                    ft.Icon(ft.Icons.HOME, color="#FFFFFF", size=50),
                                                    ft.Text("ページ 1", color="#FFFFFF", size=18, weight=ft.FontWeight.W_600),
                                                    ft.Container(height=10),
                                                    ft.ElevatedButton("次へ →", on_click=slide_to_page_2, bgcolor="#FFFFFF", color="#6750A4"),
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            ),
                                            offset=ft.Offset(0, 0),
                                            animate_offset=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                                        ),
                                        # ページ2
                                        ft.Container(
                                            ref=slide_page_2,
                                            width=300,
                                            height=180,
                                            bgcolor="#F093FB",
                                            border_radius=15,
                                            content=ft.Column(
                                                [
                                                    ft.Icon(ft.Icons.SETTINGS, color="#FFFFFF", size=50),
                                                    ft.Text("ページ 2", color="#FFFFFF", size=18, weight=ft.FontWeight.W_600),
                                                    ft.Container(height=10),
                                                    ft.ElevatedButton("← 戻る", on_click=slide_to_page_1, bgcolor="#FFFFFF", color="#F093FB"),
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            ),
                                            offset=ft.Offset(1, 0),
                                            animate_offset=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
                                        ),
                                    ],
                                    width=300,
                                    height=180,
                                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                ),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 6. アニメーションカーブ比較
                    ft.Text("6. アニメーションカーブ比較", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),
                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text("異なるイージング関数の比較", color=get_text_color(), size=get_text_size()),
                                ft.Container(height=10),
                                ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text("LINEAR", color=get_secondary_text_color(), size=12),
                                                ft.Container(height=5),
                                                ft.Container(
                                                    ref=curve_linear,
                                                    width=40,
                                                    height=40,
                                                    bgcolor="#667EEA",
                                                    border_radius=20,
                                                    offset=ft.Offset(0, 0),
                                                    animate_offset=ft.Animation(1000, ft.AnimationCurve.LINEAR),
                                                ),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.START,
                                        ),
                                        ft.Container(width=20),
                                        ft.Column(
                                            [
                                                ft.Text("EASE_IN_OUT", color=get_secondary_text_color(), size=12),
                                                ft.Container(height=5),
                                                ft.Container(
                                                    ref=curve_ease,
                                                    width=40,
                                                    height=40,
                                                    bgcolor="#F093FB",
                                                    border_radius=20,
                                                    offset=ft.Offset(0, 0),
                                                    animate_offset=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT),
                                                ),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.START,
                                        ),
                                        ft.Container(width=20),
                                        ft.Column(
                                            [
                                                ft.Text("BOUNCE_OUT", color=get_secondary_text_color(), size=12),
                                                ft.Container(height=5),
                                                ft.Container(
                                                    ref=curve_bounce,
                                                    width=40,
                                                    height=40,
                                                    bgcolor="#43E97B",
                                                    border_radius=20,
                                                    offset=ft.Offset(0, 0),
                                                    animate_offset=ft.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
                                                ),
                                            ],
                                            horizontal_alignment=ft.CrossAxisAlignment.START,
                                        ),
                                    ],
                                ),
                                ft.Container(height=15),
                                ft.ElevatedButton("カーブを比較", icon=ft.Icons.PLAY_ARROW, on_click=animate_curves),
                                ft.Container(height=5),
                                ft.Text("💡 3つのボックスが異なるカーブで右に移動します", color=get_secondary_text_color(), size=11, italic=True),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 7. ダイアログアニメーション
                    ft.Text("7. ダイアログ・ボトムシート アニメーション", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),

                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Row(
                            [
                                ft.ElevatedButton(
                                    "ダイアログを表示",
                                    icon=ft.Icons.OPEN_IN_NEW,
                                    on_click=show_animated_dialog,
                                ),
                                ft.Container(width=10),
                                ft.ElevatedButton(
                                    "ボトムシートを表示",
                                    icon=ft.Icons.ARROW_UPWARD,
                                    on_click=show_bottom_sheet,
                                ),
                            ],
                        ),
                    ),

                    ft.Container(height=30),

                    # 8. スクロール連動アニメーション
                    ft.Text("8. スクロール連動アニメーション", size=get_subsection_title_size(), weight=ft.FontWeight.W_600, color=get_text_color()),
                    ft.Container(height=10),

                    ft.Container(
                        padding=get_container_padding(),
                        bgcolor=get_container_color(),
                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Text("スクロールでアイテムがフェードイン＆拡大", color=get_text_color()),
                                ft.Container(height=10),
                                ft.Container(
                                    height=300,
                                    content=ft.Column(
                                        [create_scroll_item(i, scroll_items[i]) for i in range(5)],
                                        spacing=15,
                                        scroll=ft.ScrollMode.AUTO,
                                        on_scroll=on_scroll,
                                    ),
                                    border=ft.border.all(1, get_border_color()),
                                    border_radius=10,
                                    padding=10,
                                ),
                                ft.Container(height=10),
                                ft.Text(
                                    "💡 スクロールするとアイテムがアニメーションします",
                                    color=get_secondary_text_color(),
                                    size=12,
                                    italic=True,
                                ),
                            ],
                        ),
                    ),
                ],
                spacing=0,
            ),
        )

        # ========================================
        # メインコンテンツ（レスポンシブ対応）
        # ========================================
        # ヘッダーは画面端から端まで表示（パディングなし）
        # その他のコンテンツはレスポンシブパディングを適用
        main_content = ft.Column(
            [
                header,
                ft.Container(
                    content=ft.Column(
                        [
                            stats_section,
                            table_and_chart_section,
                            controls_section,
                            progress_section,
                            decoration_section,
                            styling_demo_section,
                            additional_components_section,
                            animation_section,
                            ft.Container(height=40),
                        ],
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.symmetric(horizontal=get_responsive_padding()),
                ),
            ],
            spacing=0,
        )

        page.add(main_content)

    def toggle_theme(e=None):
        is_dark_mode = page.theme_mode == ft.ThemeMode.LIGHT
        page.theme_mode = ft.ThemeMode.DARK if is_dark_mode else ft.ThemeMode.LIGHT
        page.clean()
        build_ui()

    def on_resize(e):
        """ウィンドウリサイズ時にUIを再構築"""
        page.clean()
        build_ui()

    # リサイズイベントハンドラーを設定
    page.on_resize = on_resize

    # 初回UI構築
    build_ui()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550, assets_dir="assets")
