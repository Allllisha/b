"""
DatePicker UI Component
Figmaデザインに基づくDatePicker（シングル・レンジ対応）
"""
import flet as ft
import calendar
import datetime
from utils.constants import *


def create_datepicker_section(colors):
    """DatePickerセクション（Figmaデザインから変換）- インタラクティブ対応"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    # level_1シャドウ
    level_1_shadow = ft.BoxShadow(
        spread_radius=0,
        blur_radius=4,
        color="rgba(150, 150, 160, 0.04)",
        offset=ft.Offset(0, 1),
    )

    def create_day_header():
        """曜日ヘッダー"""
        days = ["日", "月", "火", "水", "木", "金", "土"]
        day_colors = ["#d31510", "#222222", "#222222", "#222222", "#222222", "#222222", "#0265dc"]

        return ft.Row([
            ft.Container(
                content=ft.Text(day, size=12, weight=ft.FontWeight.BOLD, color=day_colors[i], text_align=ft.TextAlign.CENTER),
                width=32,
                height=32,
                alignment=ft.alignment.center,
            )
            for i, day in enumerate(days)
        ], spacing=4)

    # --- Single DatePicker ---
    single_year = ft.Ref[int]()
    single_month = ft.Ref[int]()
    single_selected_day = ft.Ref[int]()
    single_year.current = 2022
    single_month.current = 7
    single_selected_day.current = 14
    single_today_day = 12

    single_input_text = ft.Ref[ft.Text]()
    single_header_text = ft.Ref[ft.Text]()
    single_calendar_grid = ft.Ref[ft.Column]()
    single_calendar_container = ft.Ref[ft.Container]()
    single_input_container = ft.Ref[ft.Container]()

    def toggle_single_calendar(e):
        """シングルDatePickerのカレンダー表示/非表示を切り替え"""
        single_calendar_container.current.visible = not single_calendar_container.current.visible
        single_calendar_container.current.update()

    def update_single_calendar():
        """シングルDatePickerのカレンダー更新"""
        cal = calendar.monthcalendar(single_year.current, single_month.current)
        rows = []

        for week in cal:
            day_cells = []
            for day_idx, day in enumerate(week):
                if day == 0:
                    day_cells.append(ft.Container(width=32, height=32))
                else:
                    bg_color = "transparent"
                    text_color = "#222222"
                    border = None

                    if day_idx == 0:
                        text_color = "#d31510"
                    elif day_idx == 6:
                        text_color = "#0265dc"

                    if single_selected_day.current and day == single_selected_day.current:
                        bg_color = "#E0E0E0"

                    if day == single_today_day:
                        border = ft.border.all(2, "#0265dc")

                    def on_day_click(e, d=day):
                        single_selected_day.current = d
                        single_input_text.current.value = f"{single_year.current}/{single_month.current:02d}/{d:02d}"
                        update_single_calendar()
                        single_calendar_grid.current.update()
                        single_input_text.current.update()
                        # 日付選択後、カレンダーを閉じる
                        single_calendar_container.current.visible = False
                        single_calendar_container.current.update()

                    day_cells.append(
                        ft.Container(
                            content=ft.Text(str(day), size=12, color=text_color, text_align=ft.TextAlign.CENTER),
                            width=32,
                            height=32,
                            bgcolor=bg_color,
                            border=border,
                            border_radius=16,
                            alignment=ft.alignment.center,
                            on_click=on_day_click,
                            ink=True,
                        )
                    )

            rows.append(ft.Row(day_cells, spacing=4))

        single_calendar_grid.current.controls = rows
        single_header_text.current.value = f"{single_year.current}/{single_month.current:02d}"

    def on_single_prev_month(e):
        if single_month.current == 1:
            single_month.current = 12
            single_year.current -= 1
        else:
            single_month.current -= 1
        update_single_calendar()
        single_calendar_grid.current.update()
        single_header_text.current.update()

    def on_single_next_month(e):
        if single_month.current == 12:
            single_month.current = 1
            single_year.current += 1
        else:
            single_month.current += 1
        update_single_calendar()
        single_calendar_grid.current.update()
        single_header_text.current.update()

    single_input_text.current = ft.Text(f"{single_year.current}/{single_month.current:02d}/{single_selected_day.current:02d}", size=14, color="#222222")
    single_header_text.current = ft.Text(f"{single_year.current}/{single_month.current:02d}", size=14, weight=ft.FontWeight.BOLD, color="#222222", text_align=ft.TextAlign.CENTER, expand=True)
    single_calendar_grid.current = ft.Column([], spacing=4)
    update_single_calendar()

    single_input_container.current = ft.Container(
        content=ft.Row([
            single_input_text.current,
            ft.Icon(ft.Icons.CALENDAR_TODAY, size=20, color="#222222"),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        width=168,
        height=40,
        bgcolor=colors["neutral_white"],
        padding=ft.padding.symmetric(horizontal=12, vertical=8),
        border=ft.border.all(1, "#CCCCCC"),
        border_radius=4,
        on_click=toggle_single_calendar,
        ink=True,
    )

    single_calendar_container.current = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.CHEVRON_LEFT, icon_size=20, icon_color="#222222", padding=0, on_click=on_single_prev_month),
                single_header_text.current,
                ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, icon_size=20, icon_color="#222222", padding=0, on_click=on_single_next_month),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Container(height=8),
            create_day_header(),
            ft.Container(height=4),
            single_calendar_grid.current,
        ], spacing=0),
        width=272,
        bgcolor=colors["neutral_white"],
        padding=20,
        border_radius=8,
        shadow=level_1_shadow,
        visible=False,
    )

    single_datepicker = ft.Column([
        single_input_container.current,
        ft.Container(height=8),
        single_calendar_container.current,
    ], spacing=0)

    # --- Range DatePicker ---
    range_start_year = ft.Ref[int]()
    range_start_month = ft.Ref[int]()
    range_end_year = ft.Ref[int]()
    range_end_month = ft.Ref[int]()
    range_start_day = ft.Ref[int]()
    range_end_day = ft.Ref[int]()

    range_start_year.current = 2022
    range_start_month.current = 7
    range_end_year.current = 2022
    range_end_month.current = 8
    range_start_day.current = 20
    range_end_day.current = 6

    range_left_header = ft.Ref[ft.Text]()
    range_right_header = ft.Ref[ft.Text]()
    range_left_grid = ft.Ref[ft.Column]()
    range_right_grid = ft.Ref[ft.Column]()
    range_start_input = ft.Ref[ft.Text]()
    range_end_input = ft.Ref[ft.Text]()
    range_start_calendar_container = ft.Ref[ft.Container]()
    range_end_calendar_container = ft.Ref[ft.Container]()
    range_start_input_container = ft.Ref[ft.Container]()
    range_end_input_container = ft.Ref[ft.Container]()

    def toggle_start_calendar(e):
        """開始日のカレンダー表示/非表示を切り替え"""
        range_start_calendar_container.current.visible = not range_start_calendar_container.current.visible
        range_start_calendar_container.current.update()

    def toggle_end_calendar(e):
        """終了日のカレンダー表示/非表示を切り替え"""
        range_end_calendar_container.current.visible = not range_end_calendar_container.current.visible
        range_end_calendar_container.current.update()

    def on_range_start_day_click(e, d):
        """開始日の日付クリック"""
        range_start_day.current = d
        update_range_calendar()
        range_start_input.current.update()
        range_left_grid.current.update()
        range_right_grid.current.update()

    def on_range_end_day_click(e, d):
        """終了日の日付クリック"""
        range_end_day.current = d
        update_range_calendar()
        range_end_input.current.update()
        range_left_grid.current.update()
        range_right_grid.current.update()

    def update_range_calendar():
        """レンジDatePickerのカレンダー更新"""
        # 開始日と終了日のdatetimeオブジェクトを作成
        start_date = datetime.datetime(range_start_year.current, range_start_month.current, range_start_day.current)
        end_date = datetime.datetime(range_end_year.current, range_end_month.current, range_end_day.current)

        # 左カレンダー
        cal_left = calendar.monthcalendar(range_start_year.current, range_start_month.current)
        rows_left = []

        for week in cal_left:
            day_cells = []
            for day_idx, day in enumerate(week):
                if day == 0:
                    day_cells.append(ft.Container(width=32, height=32))
                else:
                    bg_color = "transparent"
                    text_color = "#222222"

                    if day_idx == 0:
                        text_color = "#d31510"
                    elif day_idx == 6:
                        text_color = "#0265dc"

                    # 現在の日付を作成
                    current_date = datetime.datetime(range_start_year.current, range_start_month.current, day)

                    # 開始日から終了日の間なら薄い緑
                    if start_date <= current_date <= end_date:
                        bg_color = "#B3D9D3"

                    # 開始日そのものなら濃い緑
                    if day == range_start_day.current:
                        bg_color = colors["success_main"]
                        text_color = colors["neutral_white"]

                    day_cells.append(
                        ft.Container(
                            content=ft.Text(str(day), size=12, color=text_color, text_align=ft.TextAlign.CENTER),
                            width=32,
                            height=32,
                            bgcolor=bg_color,
                            border_radius=16,
                            alignment=ft.alignment.center,
                            on_click=lambda e, d=day: on_range_start_day_click(e, d),
                            ink=True,
                        )
                    )

            rows_left.append(ft.Row(day_cells, spacing=4))

        # 右カレンダー
        cal_right = calendar.monthcalendar(range_end_year.current, range_end_month.current)
        rows_right = []

        for week in cal_right:
            day_cells = []
            for day_idx, day in enumerate(week):
                if day == 0:
                    day_cells.append(ft.Container(width=32, height=32))
                else:
                    bg_color = "transparent"
                    text_color = "#222222"

                    if day_idx == 0:
                        text_color = "#d31510"
                    elif day_idx == 6:
                        text_color = "#0265dc"

                    # 現在の日付を作成
                    current_date = datetime.datetime(range_end_year.current, range_end_month.current, day)

                    # 開始日から終了日の間なら薄い緑
                    if start_date <= current_date <= end_date:
                        bg_color = "#B3D9D3"

                    # 終了日そのものなら濃い緑
                    if day == range_end_day.current:
                        bg_color = colors["success_main"]
                        text_color = colors["neutral_white"]

                    day_cells.append(
                        ft.Container(
                            content=ft.Text(str(day), size=12, color=text_color, text_align=ft.TextAlign.CENTER),
                            width=32,
                            height=32,
                            bgcolor=bg_color,
                            border_radius=16,
                            alignment=ft.alignment.center,
                            on_click=lambda e, d=day: on_range_end_day_click(e, d),
                            ink=True,
                        )
                    )

            rows_right.append(ft.Row(day_cells, spacing=4))

        range_left_grid.current.controls = rows_left
        range_right_grid.current.controls = rows_right
        range_left_header.current.value = f"{range_start_year.current}/{range_start_month.current:02d}"
        range_right_header.current.value = f"{range_end_year.current}/{range_end_month.current:02d}"
        range_start_input.current.value = f"{range_start_year.current}/{range_start_month.current:02d}/{range_start_day.current:02d}"
        range_end_input.current.value = f"{range_end_year.current}/{range_end_month.current:02d}/{range_end_day.current:02d}"

    def on_range_left_prev(e):
        if range_start_month.current == 1:
            range_start_month.current = 12
            range_start_year.current -= 1
        else:
            range_start_month.current -= 1
        update_range_calendar()
        range_left_grid.current.update()
        range_left_header.current.update()

    def on_range_left_next(e):
        if range_start_month.current == 12:
            range_start_month.current = 1
            range_start_year.current += 1
        else:
            range_start_month.current += 1
        update_range_calendar()
        range_left_grid.current.update()
        range_left_header.current.update()

    def on_range_right_prev(e):
        if range_end_month.current == 1:
            range_end_month.current = 12
            range_end_year.current -= 1
        else:
            range_end_month.current -= 1
        update_range_calendar()
        range_right_grid.current.update()
        range_right_header.current.update()

    def on_range_right_next(e):
        if range_end_month.current == 12:
            range_end_month.current = 1
            range_end_year.current += 1
        else:
            range_end_month.current += 1
        update_range_calendar()
        range_right_grid.current.update()
        range_right_header.current.update()

    range_left_header.current = ft.Text(f"{range_start_year.current}/{range_start_month.current:02d}", size=14, weight=ft.FontWeight.BOLD, color="#222222", text_align=ft.TextAlign.CENTER, expand=True)
    range_right_header.current = ft.Text(f"{range_end_year.current}/{range_end_month.current:02d}", size=14, weight=ft.FontWeight.BOLD, color="#222222", text_align=ft.TextAlign.CENTER, expand=True)
    range_left_grid.current = ft.Column([], spacing=4)
    range_right_grid.current = ft.Column([], spacing=4)
    range_start_input.current = ft.Text(f"{range_start_year.current}/{range_start_month.current:02d}/{range_start_day.current:02d}", size=14, color="#222222")
    range_end_input.current = ft.Text(f"{range_end_year.current}/{range_end_month.current:02d}/{range_end_day.current:02d}", size=14, color="#222222")

    update_range_calendar()

    range_start_input_container.current = ft.Container(
        content=ft.Row([
            range_start_input.current,
            ft.Icon(ft.Icons.CALENDAR_TODAY, size=20, color="#222222"),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        width=168,
        height=40,
        bgcolor=colors["neutral_white"],
        padding=ft.padding.symmetric(horizontal=12, vertical=8),
        border=ft.border.all(1, "#CCCCCC"),
        border_radius=4,
        on_click=toggle_start_calendar,
        ink=True,
    )

    range_end_input_container.current = ft.Container(
        content=ft.Row([
            range_end_input.current,
            ft.Icon(ft.Icons.CALENDAR_TODAY, size=20, color="#222222"),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        width=168,
        height=40,
        bgcolor=colors["neutral_white"],
        padding=ft.padding.symmetric(horizontal=12, vertical=8),
        border=ft.border.all(1, "#CCCCCC"),
        border_radius=4,
        on_click=toggle_end_calendar,
        ink=True,
    )

    range_start_calendar_container.current = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.CHEVRON_LEFT, icon_size=20, icon_color="#222222", padding=0, on_click=on_range_left_prev),
                range_left_header.current,
                ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, icon_size=20, icon_color="#222222", padding=0, on_click=on_range_left_next),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Container(height=8),
            create_day_header(),
            ft.Container(height=4),
            range_left_grid.current,
        ], spacing=0),
        width=272,
        bgcolor=colors["neutral_white"],
        padding=20,
        border_radius=8,
        shadow=level_1_shadow,
        visible=False,
    )

    range_end_calendar_container.current = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.CHEVRON_LEFT, icon_size=20, icon_color="#222222", padding=0, on_click=on_range_right_prev),
                range_right_header.current,
                ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, icon_size=20, icon_color="#222222", padding=0, on_click=on_range_right_next),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Container(height=8),
            create_day_header(),
            ft.Container(height=4),
            range_right_grid.current,
        ], spacing=0),
        width=272,
        bgcolor=colors["neutral_white"],
        padding=20,
        border_radius=8,
        shadow=level_1_shadow,
        visible=False,
    )

    range_datepicker = ft.Column([
        ft.Row([
            range_start_input_container.current,
            ft.Text("~", size=14, color="#222222"),
            range_end_input_container.current,
        ], spacing=8),
        ft.Container(height=8),
        ft.Stack([
            range_start_calendar_container.current,
            range_end_calendar_container.current,
        ]),
    ], spacing=0)

    return ft.Container(
        content=ft.Column([
            section_title("DatePicker (LV2 - Figmaデザイン)", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Text("type=Single（月の移動、日付選択が可能）", size=12, color="#222222"),
            ft.Container(height=10),
            single_datepicker,
            ft.Container(height=40),

            ft.Text("type=Range（月の移動が可能）", size=12, color="#222222"),
            ft.Container(height=10),
            range_datepicker,
        ], spacing=0),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
