"""
Switch Section - スイッチセクション
"""
import flet as ft
from utils.constants import *


def section_title_local(text, color="#5258E4"):
    """ローカルセクションタイトル用のテキストコンポーネント"""
    return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)


def create_switch_section(colors):
    """スイッチセクション（Figmaデザインに基づく）"""

    # スイッチの状態管理
    def create_switch_item(label_text="Switch item", initial_value=False, label_position="left", on_colored=False):
        """カスタムスイッチアイテムを作成"""
        switch_ref = ft.Ref[ft.Switch]()

        # スイッチのカスタムスタイル
        if on_colored:
            # 白背景用
            track_color = {
                ft.ControlState.DEFAULT: "rgba(255, 255, 255, 0.5)",
                ft.ControlState.SELECTED: "rgba(255, 255, 255, 0.5)",
            }
            thumb_color = colors["neutral_white"]
            label_color = colors["neutral_white"]
        else:
            # 通常背景用
            track_color = {
                ft.ControlState.DEFAULT: "#909090",
                ft.ControlState.SELECTED: colors["primary_main"],
            }
            thumb_color = colors["neutral_white"]
            label_color = colors["neutral_black"]

        switch = ft.Switch(
            ref=switch_ref,
            value=initial_value,
            active_color=track_color[ft.ControlState.SELECTED],
            inactive_thumb_color=thumb_color,
            active_track_color=track_color[ft.ControlState.SELECTED],
            inactive_track_color=track_color[ft.ControlState.DEFAULT],
            width=32,
            height=20,
        )

        label = ft.Text(
            label_text,
            size=14,
            color=label_color,
            weight=ft.FontWeight.NORMAL,
        )

        if label_position == "left":
            return ft.Row(
                [switch, label],
                spacing=4,
                alignment=ft.MainAxisAlignment.START,
            )
        else:  # right
            return ft.Row(
                [label, switch],
                spacing=4,
                alignment=ft.MainAxisAlignment.START,
            )

    # 通常背景のスイッチグループ
    normal_bg_group = ft.Container(
        content=ft.Column([
            ft.Text("Normal Background", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
            ft.Container(height=10),

            # オフ状態、ラベル左
            create_switch_item("Switch item", False, "left", False),
            ft.Container(height=8),

            # オン状態、ラベル左
            create_switch_item("Switch item", True, "left", False),
            ft.Container(height=8),

            # オフ状態、ラベル右
            create_switch_item("Switch item", False, "right", False),
            ft.Container(height=8),

            # オン状態、ラベル右
            create_switch_item("Switch item", True, "right", False),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=20,
        border_radius=8,
        border=ft.border.all(1, "#E0E0E0"),
    )

    # 白背景用（colored）のスイッチグループ
    colored_bg_group = ft.Container(
        content=ft.Column([
            ft.Text("On Colored Background", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            ft.Container(height=10),

            # オフ状態、ラベル左
            create_switch_item("Switch item", False, "left", True),
            ft.Container(height=8),

            # オン状態、ラベル左
            create_switch_item("Switch item", True, "left", True),
            ft.Container(height=8),

            # オフ状態、ラベル右
            create_switch_item("Switch item", False, "right", True),
            ft.Container(height=8),

            # オン状態、ラベル右
            create_switch_item("Switch item", True, "right", True),
        ], spacing=0),
        bgcolor=colors["primary_main"],
        padding=20,
        border_radius=8,
    )

    # セクション全体を構築
    switch_section = ft.Container(
        content=ft.Column([
            section_title_local("Switch (Figma)", color=colors["primary_main"]),
            ft.Container(height=20),

            normal_bg_group,
            ft.Container(height=20),

            colored_bg_group,
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return switch_section
