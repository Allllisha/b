"""
TimePicker Section - タイムピッカーセクション（Figmaデザイン準拠）
"""
import flet as ft
from utils.constants import *


def create_timepicker_section(colors):
    """TimePickerセクション（Figmaデザインから変換）- インタラクティブ対応"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    # --- TimePicker Input States ---
    def create_timepicker_input(state="Default", value="00:00:00"):
        """TimePicker入力フィールド"""
        if state == "Default":
            bg_color = colors["neutral_white"]
            border_color = "#CCCCCC"
            text_color = "#999999"
        elif state == "Hovered":
            bg_color = "#F5F5F5"
            border_color = "#CCCCCC"
            text_color = "#999999"
        elif state == "Active":
            bg_color = colors["neutral_white"]
            border_color = "#0265dc"
            text_color = "#222222"
        elif state == "SetValue":
            bg_color = colors["neutral_white"]
            border_color = "#CCCCCC"
            text_color = "#222222"
        else:  # Disabled
            bg_color = "#F5F5F5"
            border_color = "#E0E0E0"
            text_color = "#CCCCCC"

        return ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.Text(value, size=14, color=text_color, weight=ft.FontWeight.W_400),
                    ft.Icon(ft.Icons.ACCESS_TIME, size=20, color="#0265dc" if state != "Disabled" else "#CCCCCC"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                width=168,
                height=40,
                bgcolor=bg_color,
                padding=ft.padding.symmetric(horizontal=12, vertical=8),
                border=ft.border.all(1, border_color),
                border_radius=4,
            ),
            ft.Container(height=4),
            ft.Text(state, size=10, color="#666666"),
        ], spacing=0)

    # --- TimePicker Menu States ---
    def create_timepicker_menu_item(state="Default", value="01"):
        """TimePickerメニューアイテム"""
        if state == "Default":
            bg_color = colors["neutral_white"]
            text_color = "#222222"
        elif state == "Hovered":
            bg_color = "#E0E0E0"
            text_color = "#222222"
        else:  # Active/Selected
            bg_color = "#C5DAFA"
            text_color = "#222222"

        return ft.Column([
            ft.Container(
                content=ft.Text(value, size=14, color=text_color, text_align=ft.TextAlign.CENTER),
                width=60,
                height=32,
                bgcolor=bg_color,
                border_radius=4,
                alignment=ft.alignment.center,
            ),
            ft.Container(height=4),
            ft.Text(state, size=10, color="#666666", text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0)

    # --- Interactive TimePicker ---
    selected_hour = ft.Ref[int]()
    selected_minute = ft.Ref[int]()
    selected_second = ft.Ref[int]()
    selected_hour.current = 12
    selected_minute.current = 30
    selected_second.current = 45

    time_display_text = ft.Ref[ft.Text]()
    time_menu_visible = ft.Ref[bool]()
    time_menu_visible.current = False

    hour_column = ft.Ref[ft.Column]()
    minute_column = ft.Ref[ft.Column]()
    second_column = ft.Ref[ft.Column]()
    time_menu_container = ft.Ref[ft.Container]()

    # スクロール用の状態管理
    hour_scroll_offset = ft.Ref[float]()
    minute_scroll_offset = ft.Ref[float]()
    second_scroll_offset = ft.Ref[float]()
    hour_scroll_offset.current = 0
    minute_scroll_offset.current = 0
    second_scroll_offset.current = 0

    drag_start_y = ft.Ref[float]()
    drag_start_y.current = 0

    def update_time_display():
        """時間表示を更新"""
        time_display_text.current.value = f"{selected_hour.current:02d}:{selected_minute.current:02d}:{selected_second.current:02d}"

    def on_hour_click(e, h):
        selected_hour.current = h
        update_time_display()
        update_hour_menu()
        time_display_text.current.update()
        hour_column.current.update()

    def on_minute_click(e, m):
        selected_minute.current = m
        update_time_display()
        update_minute_menu()
        time_display_text.current.update()
        minute_column.current.update()

    def on_second_click(e, s):
        selected_second.current = s
        update_time_display()
        update_second_menu()
        time_display_text.current.update()
        second_column.current.update()

    def create_time_item(value, is_selected, on_click_func):
        """時間アイテムを作成"""
        bg_color = "#C5DAFA" if is_selected else colors["neutral_white"]
        text_color = "#222222"

        return ft.Container(
            content=ft.Text(f"{value:02d}", size=14, color=text_color, text_align=ft.TextAlign.CENTER),
            width=60,
            height=32,
            bgcolor=bg_color,
            border_radius=4,
            alignment=ft.alignment.center,
            on_click=lambda e, v=value: on_click_func(e, v),
            ink=True,
        )

    def update_hour_menu():
        """時間メニューを更新"""
        items = []
        for h in range(24):
            items.append(create_time_item(h, h == selected_hour.current, on_hour_click))
        hour_column.current.controls = items

    def update_minute_menu():
        """分メニューを更新"""
        items = []
        for m in range(0, 60, 5):  # 5分刻み
            items.append(create_time_item(m, m == selected_minute.current, on_minute_click))
        minute_column.current.controls = items

    def update_second_menu():
        """秒メニューを更新"""
        items = []
        for s in range(0, 60, 5):  # 5秒刻み
            items.append(create_time_item(s, s == selected_second.current, on_second_click))
        second_column.current.controls = items

    time_display_text.current = ft.Text(f"{selected_hour.current:02d}:{selected_minute.current:02d}:{selected_second.current:02d}",
                                        size=14, color="#222222", weight=ft.FontWeight.W_400)

    hour_column.current = ft.Column([], spacing=4, scroll=ft.ScrollMode.ALWAYS, height=200, width=60)
    minute_column.current = ft.Column([], spacing=4, scroll=ft.ScrollMode.ALWAYS, height=200, width=60)
    second_column.current = ft.Column([], spacing=4, scroll=ft.ScrollMode.ALWAYS, height=200, width=60)

    time_input_container = ft.Ref[ft.Container]()

    update_hour_menu()
    update_minute_menu()
    update_second_menu()

    def toggle_time_menu(e):
        """時間メニューの表示/非表示を切り替え（拡張版）"""
        time_menu_visible.current = not time_menu_visible.current

        # メニューが開いている時は入力フィールドをActive状態（青い枠2px）に
        if time_menu_visible.current:
            time_input_container.current.border = ft.border.all(2, "#0265dc")
        else:
            time_input_container.current.border = ft.border.all(1, "#CCCCCC")

        time_menu_container.current.visible = time_menu_visible.current
        time_menu_container.current.update()
        time_input_container.current.update()

    def close_time_menu(e):
        """時間メニューを閉じる"""
        time_menu_visible.current = False
        time_input_container.current.border = ft.border.all(1, "#CCCCCC")
        time_menu_container.current.visible = False
        time_menu_container.current.update()
        time_input_container.current.update()

    interactive_timepicker = ft.Column([
        ft.Text("Interactive TimePicker（クリックして時間を選択）", size=14, weight=ft.FontWeight.BOLD, color="#222222"),
        ft.Container(height=12),
        # 入力フィールド
        ft.Container(
            ref=time_input_container,
            content=ft.Row([
                time_display_text.current,
                ft.Icon(ft.Icons.ACCESS_TIME, size=20, color="#0265dc"),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            width=168,
            height=40,
            bgcolor=colors["neutral_white"],
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border=ft.border.all(1, "#CCCCCC"),
            border_radius=4,
            on_click=toggle_time_menu,
            ink=True,
        ),
        ft.Container(height=12),
        # 時間選択メニュー
        ft.Container(
            ref=time_menu_container,
            visible=False,
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Column([
                            ft.Text("Hour", size=12, weight=ft.FontWeight.BOLD, color="#222222", text_align=ft.TextAlign.CENTER),
                            ft.Container(height=4),
                            hour_column.current,
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                        ft.Container(width=8),
                        ft.Column([
                            ft.Text("Minute", size=12, weight=ft.FontWeight.BOLD, color="#222222", text_align=ft.TextAlign.CENTER),
                            ft.Container(height=4),
                            minute_column.current,
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                        ft.Container(width=8),
                        ft.Column([
                            ft.Text("Second", size=12, weight=ft.FontWeight.BOLD, color="#222222", text_align=ft.TextAlign.CENTER),
                            ft.Container(height=4),
                            second_column.current,
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                    ], spacing=0),
                    ft.Container(height=12),
                    # 完了ボタン
                    ft.Container(
                        content=ft.Text("完了", size=14, color=colors["neutral_white"], weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        width=200,
                        height=36,
                        bgcolor=colors["success_main"],
                        border_radius=4,
                        alignment=ft.alignment.center,
                        on_click=close_time_menu,
                        ink=True,
                    ),
                ], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=colors["neutral_white"],
                padding=16,
                border_radius=8,
                border=ft.border.all(1, "#CCCCCC"),
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=8,
                    offset=ft.Offset(0, 4),
                    color="rgba(0,0,0,0.1)"
                ),
            ),
        ),
    ], spacing=0)

    return ft.Container(
        content=ft.Column([
            section_title("TimePicker (Figmaデザイン)", color=colors["primary_main"]),
            ft.Container(height=20),

            # インタラクティブなTimePicker
            interactive_timepicker,
        ], spacing=0),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
