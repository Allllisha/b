"""
Chart Section - チャートセクション
"""
import flet as ft
from utils.constants import *


def create_chart_section(colors):
    """チャートセクションを作成"""

    # チャート用の色
    chart_colors = {
        "stat_bg": "#1A893DE7",  # rgba(137,61,231,0.1) を16進数アルファ形式に変換
        "secondary_main": "#893de7",
        "success_green": "#49cc93",
        "data_primary_02": "#7e84fc",
        "data_secondary_04": "#cca4fd",
        "data_blue_04": "#78bbfa",
        "data_secondary_01": "#9d57f4",
        "data_primary_01": "#686df4",
        "data_red_04": "#ff9b88",
    }

    # 統計カードを作成
    def create_stat_card():
        return ft.Container(
            content=ft.Column([
                # タイトル行
                ft.Row([
                    # 左側アイテム
                    ft.Row([
                        ft.Icon(ft.Icons.FULLSCREEN, size=24, color=chart_colors["secondary_main"]),
                        ft.Text("Label", size=16, color="#222222"),
                    ], spacing=8),
                    # 右側アイテム
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.TRENDING_UP, size=10, color=chart_colors["success_green"]),
                            ft.Text("Success", size=10, color=chart_colors["success_green"]),
                        ], spacing=4),
                        bgcolor="#ffffff",
                        border=ft.border.all(1, chart_colors["success_green"]),
                        border_radius=4,
                        padding=ft.padding.only(left=4, right=4, top=2, bottom=2),
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                # 値
                ft.Column([
                    ft.Text("1,500", size=24, weight=ft.FontWeight.BOLD, color="#222222", text_align=ft.TextAlign.RIGHT),
                    ft.Text("Unit", size=16, color="#909090", text_align=ft.TextAlign.RIGHT),
                ], spacing=0, alignment=ft.CrossAxisAlignment.END, horizontal_alignment=ft.CrossAxisAlignment.END),
            ], spacing=3),
            bgcolor=chart_colors["stat_bg"],
            border_radius=8,
            padding=16,
            expand=1,
        )

    # 凡例アイテムを作成
    def create_legend_item(color, label="チャートデータ名"):
        return ft.Row([
            ft.Container(
                width=8,
                height=8,
                bgcolor=color,
                border_radius=100,
            ),
            ft.Text(label, size=10, color="#222222"),
        ], spacing=8)

    # 積み上げ棒グラフの1本を作成
    def create_stacked_bar(segments):
        """
        segments: [(height_percent, color), ...]
        bottom から top への順序で指定
        """
        bar_segments = []
        for height_percent, color in segments:
            bar_segments.append(
                ft.Container(
                    height=height_percent,
                    bgcolor=color,
                )
            )

        return ft.Container(
            content=ft.Column(
                bar_segments,
                spacing=0,
                alignment=ft.MainAxisAlignment.END,
            ),
            width=48,
            height=294,
            alignment=ft.alignment.bottom_center,
        )

    # 8本の棒グラフデータ（bottom から top、ピクセル高さ）
    # Figmaのデザインに基づいて正確な高さを設定（Y軸0-800、グラフ高さ294px）
    bars_data = [
        # 2021-01: 合計約420
        [(37, chart_colors["data_red_04"]), (43, chart_colors["data_primary_01"]), (18, chart_colors["data_secondary_01"]),
         (18, chart_colors["data_blue_04"]), (40, chart_colors["data_secondary_04"]), (18, chart_colors["data_primary_02"])],
        # 2021-02: 合計約590
        [(25, chart_colors["data_red_04"]), (80, chart_colors["data_primary_01"]), (18, chart_colors["data_secondary_01"]),
         (40, chart_colors["data_blue_04"]), (70, chart_colors["data_secondary_04"]), (35, chart_colors["data_primary_02"])],
        # 2021-03: 合計約650
        [(33, chart_colors["data_red_04"]), (75, chart_colors["data_primary_01"]), (40, chart_colors["data_secondary_01"]),
         (28, chart_colors["data_blue_04"]), (80, chart_colors["data_secondary_04"]), (35, chart_colors["data_primary_02"])],
        # 2021-04: 合計約560
        [(25, chart_colors["data_red_04"]), (80, chart_colors["data_primary_01"]), (40, chart_colors["data_secondary_01"]),
         (35, chart_colors["data_blue_04"]), (60, chart_colors["data_secondary_04"]), (40, chart_colors["data_primary_02"])],
        # 2021-05: 合計約530
        [(30, chart_colors["data_red_04"]), (65, chart_colors["data_primary_01"]), (30, chart_colors["data_secondary_01"]),
         (32, chart_colors["data_blue_04"]), (55, chart_colors["data_secondary_04"]), (35, chart_colors["data_primary_02"])],
        # 2021-06: 合計約500
        [(30, chart_colors["data_red_04"]), (95, chart_colors["data_primary_01"]), (20, chart_colors["data_secondary_01"]),
         (25, chart_colors["data_blue_04"]), (40, chart_colors["data_secondary_04"]), (25, chart_colors["data_primary_02"])],
        # 2021-07: 合計約600
        [(70, chart_colors["data_red_04"]), (50, chart_colors["data_primary_01"]), (30, chart_colors["data_secondary_01"]),
         (30, chart_colors["data_blue_04"]), (60, chart_colors["data_secondary_04"]), (55, chart_colors["data_primary_02"])],
        # 2021-08: 合計約460
        [(15, chart_colors["data_red_04"]), (110, chart_colors["data_primary_01"]), (15, chart_colors["data_secondary_01"]),
         (15, chart_colors["data_blue_04"]), (60, chart_colors["data_secondary_04"]), (10, chart_colors["data_primary_02"])],
    ]

    month_labels = ["2021-01", "2021-02", "2021-03", "2021-04", "2021-05", "2021-06", "2021-07", "2021-08"]

    chart_section = ft.Container(
        content=ft.Column([
            ft.Text("Chart", size=16, weight=ft.FontWeight.BOLD, color=colors["primary_main"]),
            ft.Container(height=40),

            # 統計カード3つ
            ft.Row([
                create_stat_card(),
                ft.Container(width=1, bgcolor="rgba(34,34,34,0.16)", expand=False),
                create_stat_card(),
                ft.Container(width=1, bgcolor="rgba(34,34,34,0.16)", expand=False),
                create_stat_card(),
            ], spacing=24),

            ft.Container(height=16),

            # チャートタイトル
            ft.Column([
                ft.Text("チャートタイトル", size=16, color="#222222"),
                ft.Text("サブタイトルがはいります。", size=11, color="#6d6d6d"),
            ], spacing=4),

            ft.Container(height=16),

            # 凡例
            ft.Row([
                create_legend_item(chart_colors["data_primary_02"]),
                create_legend_item(chart_colors["data_secondary_04"]),
                create_legend_item(chart_colors["data_blue_04"]),
                create_legend_item(chart_colors["data_secondary_01"]),
                create_legend_item(chart_colors["data_primary_01"]),
                create_legend_item(chart_colors["data_red_04"]),
            ], spacing=12, wrap=True),

            ft.Container(height=16),

            # チャート本体
            ft.Row([
                # Y軸ラベル
                ft.Column([
                    ft.Text("800", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("700", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("600", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("500", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("400", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("300", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("200", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("100", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                    ft.Text("0", size=10, color="#222222", text_align=ft.TextAlign.RIGHT, width=33),
                ], spacing=13, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                ft.Container(width=12),

                # 棒グラフ
                ft.Column([
                    ft.Row([
                        create_stacked_bar(bars_data[0]),
                        create_stacked_bar(bars_data[1]),
                        create_stacked_bar(bars_data[2]),
                        create_stacked_bar(bars_data[3]),
                        create_stacked_bar(bars_data[4]),
                        create_stacked_bar(bars_data[5]),
                        create_stacked_bar(bars_data[6]),
                        create_stacked_bar(bars_data[7]),
                    ], spacing=4, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                    ft.Container(height=4),

                    # X軸ラベル
                    ft.Row([
                        ft.Text(month_labels[0], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                        ft.Text(month_labels[1], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                        ft.Text(month_labels[2], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                        ft.Text(month_labels[3], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                        ft.Text(month_labels[4], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                        ft.Text(month_labels[5], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                        ft.Text(month_labels[6], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                        ft.Text(month_labels[7], size=10, color="#222222", text_align=ft.TextAlign.CENTER, width=48),
                    ], spacing=4, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ], spacing=0),
            ], spacing=0, alignment=ft.MainAxisAlignment.START),

            ft.Container(height=16),

            # Go To Component リンク
            ft.Row([
                ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT, size=16, color=chart_colors["secondary_main"]),
                ft.Text("Go To Component", size=11, color=chart_colors["secondary_main"]),
            ], spacing=4),
        ], spacing=0),
        bgcolor="#127B8FF4",  # rgba(123,143,244,0.07) を16進数アルファ形式に変換
        padding=ft.padding.only(left=32, right=32, top=24, bottom=24),
        border_radius=8,
    )

    return chart_section
