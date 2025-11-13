"""
Interactive Section - インタラクティブボタン（色変化アニメーション）
"""
import flet as ft
from utils.constants import *


def section_title(text, color="#333333"):
    """セクションタイトル用のテキストコンポーネント"""
    return ft.Text(
        text,
        size=24,
        weight=ft.FontWeight.BOLD,
        color=color,
    )


def create_interactive_section(page, colors, corner_radius, spacing):
    """緑→青にアニメーションするインタラクティブボタンのセクション"""

    # Successボタン（緑→青）- XLサイズ
    success_btn = ft.Container(
        content=ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["neutral_white"],
        ),
        bgcolor=colors["success_main"],  # 初期状態は緑
        border_radius=corner_radius,
        padding=spacing,
        width=109,
        height=56,
        alignment=ft.alignment.center,
        animate=300,  # 300msのアニメーション
    )

    # Dangerボタン（赤→濃い赤）- XLサイズ
    danger_btn = ft.Container(
        content=ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["neutral_white"],
        ),
        bgcolor=colors["danger_main"],  # 初期状態は赤
        border_radius=corner_radius,
        padding=spacing,
        width=109,
        height=56,
        alignment=ft.alignment.center,
        animate=300,
    )

    # Success枠線ボタン（緑→青）- XLサイズ
    success_outline_btn = ft.Container(
        content=ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["success_main"],
        ),
        bgcolor="transparent",
        border=ft.border.all(1, colors["success_main"]),
        border_radius=corner_radius,
        padding=spacing,
        width=109,
        height=56,
        alignment=ft.alignment.center,
        animate=300,
    )

    # Danger枠線ボタン（赤→濃い赤）- XLサイズ
    danger_outline_btn = ft.Container(
        content=ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["danger_main"],
        ),
        bgcolor="transparent",
        border=ft.border.all(1, colors["danger_main"]),
        border_radius=corner_radius,
        padding=spacing,
        width=109,
        height=56,
        alignment=ft.alignment.center,
        animate=300,
    )

    # ホバーイベントハンドラ（塗りつぶし）
    def on_success_hover(e):
        if e.data == "true":
            success_btn.bgcolor = colors["primary_main"]  # 青に変化
        else:
            success_btn.bgcolor = colors["success_main"]  # 緑に戻る
        page.update()

    def on_danger_hover(e):
        if e.data == "true":
            danger_btn.bgcolor = colors["danger_hovered"]  # より濃い赤に変化
        else:
            danger_btn.bgcolor = colors["danger_main"]  # 赤に戻る
        page.update()

    # ホバーイベントハンドラ（枠線）
    def on_success_outline_hover(e):
        if e.data == "true":
            success_outline_btn.border = ft.border.all(1, colors["primary_main"])
            success_outline_btn.content = ft.Text(
                "Button",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=colors["primary_main"],
            )
        else:
            success_outline_btn.border = ft.border.all(1, colors["success_main"])
            success_outline_btn.content = ft.Text(
                "Button",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=colors["success_main"],
            )
        page.update()

    def on_danger_outline_hover(e):
        if e.data == "true":
            danger_outline_btn.border = ft.border.all(1, colors["danger_hovered"])
            danger_outline_btn.content = ft.Text(
                "Button",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=colors["danger_hovered"],
            )
        else:
            danger_outline_btn.border = ft.border.all(1, colors["danger_main"])
            danger_outline_btn.content = ft.Text(
                "Button",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=colors["danger_main"],
            )
        page.update()

    # クリックイベントハンドラ（塗りつぶし）
    def on_success_click(_):
        success_btn.bgcolor = colors["primary_selected"]  # クリックで濃い青
        page.update()

    def on_danger_click(_):
        danger_btn.bgcolor = colors["danger_selected"]  # さらに濃い赤
        page.update()

    # クリックイベントハンドラ（枠線）
    def on_success_outline_click(_):
        success_outline_btn.border = ft.border.all(1, colors["primary_selected"])
        success_outline_btn.content = ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["primary_selected"],
        )
        page.update()

    def on_danger_outline_click(_):
        danger_outline_btn.border = ft.border.all(1, colors["danger_selected"])
        danger_outline_btn.content = ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["danger_selected"],
        )
        page.update()

    # イベント設定
    success_btn.on_hover = on_success_hover
    success_btn.on_click = on_success_click

    danger_btn.on_hover = on_danger_hover
    danger_btn.on_click = on_danger_click

    success_outline_btn.on_hover = on_success_outline_hover
    success_outline_btn.on_click = on_success_outline_click

    danger_outline_btn.on_hover = on_danger_outline_hover
    danger_outline_btn.on_click = on_danger_outline_click

    # ===== アイコンボタン =====
    # Success アイコンボタン（緑→青）- 40x40px
    success_icon_btn = ft.Container(
        content=ft.Icon(ft.Icons.ADD, size=24, color=colors["neutral_white"]),
        bgcolor=colors["success_main"],
        border_radius=corner_radius,
        padding=8,
        width=40,
        height=40,
        alignment=ft.alignment.center,
        animate=300,
    )

    # Success アイコンボタン 枠線（緑→青）
    success_icon_outline_btn = ft.Container(
        content=ft.Icon(ft.Icons.ADD, size=24, color=colors["success_main"]),
        bgcolor="transparent",
        border=ft.border.all(1, colors["success_main"]),
        border_radius=corner_radius,
        padding=8,
        width=40,
        height=40,
        alignment=ft.alignment.center,
        animate=300,
    )

    # Danger アイコンボタン（赤→濃い赤）
    danger_icon_btn = ft.Container(
        content=ft.Icon(ft.Icons.ADD, size=24, color=colors["neutral_white"]),
        bgcolor=colors["danger_main"],
        border_radius=corner_radius,
        padding=8,
        width=40,
        height=40,
        alignment=ft.alignment.center,
        animate=300,
    )

    # Danger アイコンボタン 枠線（赤→濃い赤）
    danger_icon_outline_btn = ft.Container(
        content=ft.Icon(ft.Icons.ADD, size=24, color=colors["danger_main"]),
        bgcolor="transparent",
        border=ft.border.all(1, colors["danger_main"]),
        border_radius=corner_radius,
        padding=8,
        width=40,
        height=40,
        alignment=ft.alignment.center,
        animate=300,
    )

    # アイコンボタンのイベントハンドラ
    def on_success_icon_hover(e):
        if e.data == "true":
            success_icon_btn.bgcolor = colors["primary_main"]
        else:
            success_icon_btn.bgcolor = colors["success_main"]
        page.update()

    def on_success_icon_outline_hover(e):
        if e.data == "true":
            success_icon_outline_btn.border = ft.border.all(1, colors["primary_main"])
            success_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color=colors["primary_main"])
        else:
            success_icon_outline_btn.border = ft.border.all(1, colors["success_main"])
            success_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color=colors["success_main"])
        page.update()

    def on_danger_icon_hover(e):
        if e.data == "true":
            danger_icon_btn.bgcolor = colors["danger_hovered"]
        else:
            danger_icon_btn.bgcolor = colors["danger_main"]
        page.update()

    def on_danger_icon_outline_hover(e):
        if e.data == "true":
            danger_icon_outline_btn.border = ft.border.all(1, colors["danger_hovered"])
            danger_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color=colors["danger_hovered"])
        else:
            danger_icon_outline_btn.border = ft.border.all(1, colors["danger_main"])
            danger_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color=colors["danger_main"])
        page.update()

    def on_success_icon_click(_):
        success_icon_btn.bgcolor = colors["primary_selected"]
        page.update()

    def on_success_icon_outline_click(_):
        success_icon_outline_btn.border = ft.border.all(1, colors["primary_selected"])
        success_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color=colors["primary_selected"])
        page.update()

    def on_danger_icon_click(_):
        danger_icon_btn.bgcolor = colors["danger_selected"]
        page.update()

    def on_danger_icon_outline_click(_):
        danger_icon_outline_btn.border = ft.border.all(1, colors["danger_selected"])
        danger_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color=colors["danger_selected"])
        page.update()

    # イベント設定（アイコンボタン）
    success_icon_btn.on_hover = on_success_icon_hover
    success_icon_btn.on_click = on_success_icon_click

    success_icon_outline_btn.on_hover = on_success_icon_outline_hover
    success_icon_outline_btn.on_click = on_success_icon_outline_click

    danger_icon_btn.on_hover = on_danger_icon_hover
    danger_icon_btn.on_click = on_danger_icon_click

    danger_icon_outline_btn.on_hover = on_danger_icon_outline_hover
    danger_icon_outline_btn.on_click = on_danger_icon_outline_click

    # ===== 暗い背景上のアイコンボタン =====
    # 白アイコンボタン（白100% → 80% → 50%）
    dark_bg_icon_btn = ft.Container(
        content=ft.Icon(ft.Icons.ADD, size=24, color=colors["primary_main"]),
        bgcolor=colors["neutral_white"],
        border_radius=corner_radius,
        padding=8,
        width=40,
        height=40,
        alignment=ft.alignment.center,
        animate=300,
    )

    # 白枠線アイコンボタン（白100% → 80% → 50%）
    dark_bg_icon_outline_btn = ft.Container(
        content=ft.Icon(ft.Icons.ADD, size=24, color=colors["neutral_white"]),
        bgcolor="transparent",
        border=ft.border.all(1, colors["neutral_white"]),
        border_radius=corner_radius,
        padding=8,
        width=40,
        height=40,
        alignment=ft.alignment.center,
        animate=300,
    )

    # 暗い背景アイコンボタンのイベントハンドラ
    def on_dark_bg_icon_hover(e):
        if e.data == "true":
            dark_bg_icon_btn.bgcolor = "#E0E0E0"  # 薄いグレー
        else:
            dark_bg_icon_btn.bgcolor = colors["neutral_white"]
        page.update()

    def on_dark_bg_icon_outline_hover(e):
        if e.data == "true":
            dark_bg_icon_outline_btn.border = ft.border.all(1, "#E0E0E0")
            dark_bg_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color="#E0E0E0")
        else:
            dark_bg_icon_outline_btn.border = ft.border.all(1, colors["neutral_white"])
            dark_bg_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color=colors["neutral_white"])
        page.update()

    def on_dark_bg_icon_click(_):
        dark_bg_icon_btn.bgcolor = "#C0C0C0"  # 中間グレー
        page.update()

    def on_dark_bg_icon_outline_click(_):
        dark_bg_icon_outline_btn.border = ft.border.all(1, "#C0C0C0")
        dark_bg_icon_outline_btn.content = ft.Icon(ft.Icons.ADD, size=24, color="#C0C0C0")
        page.update()

    # イベント設定（暗い背景アイコンボタン）
    dark_bg_icon_btn.on_hover = on_dark_bg_icon_hover
    dark_bg_icon_btn.on_click = on_dark_bg_icon_click

    dark_bg_icon_outline_btn.on_hover = on_dark_bg_icon_outline_hover
    dark_bg_icon_outline_btn.on_click = on_dark_bg_icon_outline_click

    # ===== 暗い背景上のボタン =====
    # 白背景ボタン（白→80%白→50%白）
    dark_bg_btn = ft.Container(
        content=ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["primary_main"],
        ),
        bgcolor=colors["neutral_white"],
        border_radius=corner_radius,
        padding=spacing,
        width=109,
        height=56,
        alignment=ft.alignment.center,
        animate=300,
    )

    # 白枠線ボタン（白→80%白→50%白）
    dark_bg_outline_btn = ft.Container(
        content=ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=colors["neutral_white"],
        ),
        bgcolor="transparent",
        border=ft.border.all(1, colors["neutral_white"]),
        border_radius=corner_radius,
        padding=spacing,
        width=109,
        height=56,
        alignment=ft.alignment.center,
        animate=300,
    )

    # 暗い背景ボタンのイベントハンドラ
    def on_dark_bg_hover(e):
        if e.data == "true":
            dark_bg_btn.bgcolor = "#E0E0E0"  # 薄いグレー
        else:
            dark_bg_btn.bgcolor = colors["neutral_white"]
        page.update()

    def on_dark_bg_outline_hover(e):
        if e.data == "true":
            dark_bg_outline_btn.border = ft.border.all(1, "#E0E0E0")
            dark_bg_outline_btn.content = ft.Text(
                "Button",
                size=18,
                weight=ft.FontWeight.BOLD,
                color="#E0E0E0",
            )
        else:
            dark_bg_outline_btn.border = ft.border.all(1, colors["neutral_white"])
            dark_bg_outline_btn.content = ft.Text(
                "Button",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=colors["neutral_white"],
            )
        page.update()

    def on_dark_bg_click(_):
        dark_bg_btn.bgcolor = "#C0C0C0"  # 中間グレー
        page.update()

    def on_dark_bg_outline_click(_):
        dark_bg_outline_btn.border = ft.border.all(1, "#C0C0C0")
        dark_bg_outline_btn.content = ft.Text(
            "Button",
            size=18,
            weight=ft.FontWeight.BOLD,
            color="#C0C0C0",
        )
        page.update()

    # イベント設定（暗い背景ボタン）
    dark_bg_btn.on_hover = on_dark_bg_hover
    dark_bg_btn.on_click = on_dark_bg_click

    dark_bg_outline_btn.on_hover = on_dark_bg_outline_hover
    dark_bg_outline_btn.on_click = on_dark_bg_outline_click

    return ft.Column(
        [
            section_title("インタラクティブボタン（色変化アニメーション）", colors["primary_main"]),
            ft.Text(
                "ホバーで色が滑らかに変化します（300msアニメーション）",
                size=12,
                color="#666666",
                italic=True,
            ),
            ft.Divider(height=20, color="transparent"),

            ft.Column(
                [
                    ft.Text("Success（緑→青）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
                    ft.Row([success_btn, success_outline_btn], spacing=20),
                    ft.Text("塗りつぶし / 枠線：緑(Success) → 青(Primary)", size=11, color="#999999"),
                    ft.Divider(height=15, color="transparent"),

                    ft.Text("Danger（赤→濃い赤）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
                    ft.Row([danger_btn, danger_outline_btn], spacing=20),
                    ft.Text("塗りつぶし / 枠線：赤(Danger Main) → 濃い赤(Danger Hovered) → 最も濃い赤(Danger Selected)", size=11, color="#999999"),
                    ft.Divider(height=15, color="transparent"),

                    ft.Text("アイコンボタン", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
                    ft.Row([
                        ft.Column([
                            ft.Text("Success", size=12, color="#666666"),
                            ft.Row([success_icon_btn, success_icon_outline_btn], spacing=10),
                        ], spacing=5),
                        ft.Column([
                            ft.Text("Danger", size=12, color="#666666"),
                            ft.Row([danger_icon_btn, danger_icon_outline_btn], spacing=10),
                        ], spacing=5),
                    ], spacing=30),
                    ft.Divider(height=15, color="transparent"),

                    ft.Text("暗い背景上のボタン", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
                    ft.Container(
                        content=ft.Column([
                            ft.Row([dark_bg_btn, dark_bg_outline_btn], spacing=20),
                            ft.Divider(height=10, color="transparent"),
                            ft.Row([dark_bg_icon_btn, dark_bg_icon_outline_btn], spacing=20),
                        ], spacing=10),
                        bgcolor=colors["primary_main"],
                        padding=20,
                        border_radius=8,
                    ),
                    ft.Text("白(100%) → 80%白 → 50%白", size=11, color="#999999"),
                ],
                spacing=5,
            ),

            ft.Divider(height=10, color="transparent"),
            ft.Text(
                "※ マウスを乗せると色が変化、クリックでも色が変化します",
                size=11,
                color="#999999",
                italic=True,
            ),
        ],
        spacing=15,
    )
