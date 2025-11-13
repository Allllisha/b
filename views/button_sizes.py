"""
Button Sizes Section - ボタンサイズバリエーション（Figmaデザイン準拠）
5列×12行 = 60個のボタン
- 5スタイル: Filled, Outlined, Text, Outlined2, Disabled
- 4サイズ: Large, Medium, Small, XSmall
- 3タイプ: テキストボタン、アイコンボタン（+のみ）、ローディングボタン
"""
import flet as ft
from utils.constants import *


def create_button_sizes_section(colors):
    """ボタンサイズセクション（Figmaデザイン準拠）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    # === Large Buttons (16px H / 12px V padding) ===
    def create_large_filled_text():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_filled_icon():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=20, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=12,
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_filled_loading():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=20, height=20, stroke_width=2, color=colors["neutral_white"]),
                ft.Container(width=8),
                ft.Text("Loading...", size=14, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            ], spacing=0, tight=True),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_outlined_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_outlined_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=20, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=12,
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_outlined_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=20, height=20, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=14, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=8), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_text_text():
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            text_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            text_ref.current.update()
        text_ref.current = ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=text_ref.current,
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )

    def create_large_text_icon():
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            icon_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            icon_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=20, color=colors["success_main"])
        return ft.Container(
            content=icon_ref.current,
            bgcolor="transparent",
            padding=12,
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )

    def create_large_text_loading():
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=20, height=20, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=14, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=8), text_ref.current], spacing=0, tight=True),
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )

    def create_large_outlined2_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_outlined2_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=20, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=12,
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_outlined2_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=20, height=20, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=14, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=8), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_large_disabled_text():
        return ft.Container(
            content=ft.Text("Button", size=14, weight=ft.FontWeight.BOLD, color="#999999"),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
        )

    def create_large_disabled_icon():
        return ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=20, color="#999999"),
            bgcolor="#F5F5F5",
            padding=12,
            border_radius=6,
        )

    def create_large_disabled_loading():
        return ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=20, height=20, stroke_width=2, color="#999999"),
                ft.Container(width=8),
                ft.Text("Loading...", size=14, weight=ft.FontWeight.BOLD, color="#999999"),
            ], spacing=0, tight=True),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=16, vertical=12),
            border_radius=6,
        )

    # === Medium Buttons (12px H / 8px V padding) ===
    def create_medium_filled_text():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Text("Button", size=12, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_filled_icon():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=16, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=8,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_filled_loading():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=16, height=16, stroke_width=2, color=colors["neutral_white"]),
                ft.Container(width=6),
                ft.Text("Loading...", size=12, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            ], spacing=0, tight=True),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_outlined_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=12, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_outlined_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=16, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=8,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_outlined_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=16, height=16, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=12, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=6), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_text_text():
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            text_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            text_ref.current.update()
        text_ref.current = ft.Text("Button", size=12, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=text_ref.current,
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )

    def create_medium_text_icon():
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            icon_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            icon_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=16, color=colors["success_main"])
        return ft.Container(
            content=icon_ref.current,
            bgcolor="transparent",
            padding=8,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )

    def create_medium_text_loading():
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=16, height=16, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=12, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=6), text_ref.current], spacing=0, tight=True),
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )

    def create_medium_outlined2_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=12, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_outlined2_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=16, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=8,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_outlined2_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=16, height=16, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=12, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=6), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_medium_disabled_text():
        return ft.Container(
            content=ft.Text("Button", size=12, weight=ft.FontWeight.BOLD, color="#999999"),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
        )

    def create_medium_disabled_icon():
        return ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=16, color="#999999"),
            bgcolor="#F5F5F5",
            padding=8,
            border_radius=4,
        )

    def create_medium_disabled_loading():
        return ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=16, height=16, stroke_width=2, color="#999999"),
                ft.Container(width=6),
                ft.Text("Loading...", size=12, weight=ft.FontWeight.BOLD, color="#999999"),
            ], spacing=0, tight=True),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=4,
        )

    # === Small Buttons (10px H / 6px V padding) ===
    def create_small_filled_text():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Text("Button", size=11, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_filled_icon():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=14, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=6,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_filled_loading():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=14, height=14, stroke_width=2, color=colors["neutral_white"]),
                ft.Container(width=5),
                ft.Text("Loading...", size=11, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            ], spacing=0, tight=True),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_outlined_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=11, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_outlined_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=14, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=6,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_outlined_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=14, height=14, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=11, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=5), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_text_text():
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            text_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            text_ref.current.update()
        text_ref.current = ft.Text("Button", size=11, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=text_ref.current,
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )

    def create_small_text_icon():
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            icon_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            icon_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=14, color=colors["success_main"])
        return ft.Container(
            content=icon_ref.current,
            bgcolor="transparent",
            padding=6,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )

    def create_small_text_loading():
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=14, height=14, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=11, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=5), text_ref.current], spacing=0, tight=True),
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )

    def create_small_outlined2_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=11, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_outlined2_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=14, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=6,
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_outlined2_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=14, height=14, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=11, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=5), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_small_disabled_text():
        return ft.Container(
            content=ft.Text("Button", size=11, weight=ft.FontWeight.BOLD, color="#999999"),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
        )

    def create_small_disabled_icon():
        return ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=14, color="#999999"),
            bgcolor="#F5F5F5",
            padding=6,
            border_radius=4,
        )

    def create_small_disabled_loading():
        return ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=14, height=14, stroke_width=2, color="#999999"),
                ft.Container(width=5),
                ft.Text("Loading...", size=11, weight=ft.FontWeight.BOLD, color="#999999"),
            ], spacing=0, tight=True),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=10, vertical=6),
            border_radius=4,
        )

    # === XSmall Buttons (8px H / 4px V padding) ===
    def create_xsmall_filled_text():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Text("Button", size=10, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_filled_icon():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=12, color=colors["neutral_white"]),
            bgcolor=colors["success_main"],
            padding=4,
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_filled_loading():
        btn_ref = ft.Ref[ft.Container]()
        def on_hover(e):
            btn_ref.current.bgcolor = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.update()
        btn_ref.current = ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=12, height=12, stroke_width=2, color=colors["neutral_white"]),
                ft.Container(width=4),
                ft.Text("Loading...", size=10, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
            ], spacing=0, tight=True),
            bgcolor=colors["success_main"],
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_outlined_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=10, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_outlined_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=12, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=4,
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_outlined_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=12, height=12, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=10, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=4), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_text_text():
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            text_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            text_ref.current.update()
        text_ref.current = ft.Text("Button", size=10, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=text_ref.current,
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )

    def create_xsmall_text_icon():
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            icon_ref.current.color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            icon_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=12, color=colors["success_main"])
        return ft.Container(
            content=icon_ref.current,
            bgcolor="transparent",
            padding=4,
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )

    def create_xsmall_text_loading():
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=12, height=12, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=10, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        return ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=4), text_ref.current], spacing=0, tight=True),
            bgcolor="transparent",
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )

    def create_xsmall_outlined2_text():
        btn_ref = ft.Ref[ft.Container]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            text_ref.current.color = new_color
            text_ref.current.update()
            btn_ref.current.update()
        text_ref.current = ft.Text("Button", size=10, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=text_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_outlined2_icon():
        btn_ref = ft.Ref[ft.Container]()
        icon_ref = ft.Ref[ft.Icon]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            icon_ref.current.color = new_color
            icon_ref.current.update()
            btn_ref.current.update()
        icon_ref.current = ft.Icon(ft.Icons.ADD, size=12, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=icon_ref.current,
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=4,
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_outlined2_loading():
        btn_ref = ft.Ref[ft.Container]()
        ring_ref = ft.Ref[ft.ProgressRing]()
        text_ref = ft.Ref[ft.Text]()
        def on_hover(e):
            new_color = colors["primary_main"] if e.data == "true" else colors["success_main"]
            btn_ref.current.border = ft.border.all(1, new_color)
            ring_ref.current.color = new_color
            text_ref.current.color = new_color
            ring_ref.current.update()
            text_ref.current.update()
            btn_ref.current.update()
        ring_ref.current = ft.ProgressRing(width=12, height=12, stroke_width=2, color=colors["success_main"])
        text_ref.current = ft.Text("Loading...", size=10, weight=ft.FontWeight.BOLD, color=colors["success_main"])
        btn_ref.current = ft.Container(
            content=ft.Row([ring_ref.current, ft.Container(width=4), text_ref.current], spacing=0, tight=True),
            bgcolor=colors["neutral_white"],
            border=ft.border.all(1, colors["success_main"]),
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
            on_hover=on_hover,
            ink=True,
        )
        return btn_ref.current

    def create_xsmall_disabled_text():
        return ft.Container(
            content=ft.Text("Button", size=10, weight=ft.FontWeight.BOLD, color="#999999"),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
        )

    def create_xsmall_disabled_icon():
        return ft.Container(
            content=ft.Icon(ft.Icons.ADD, size=12, color="#999999"),
            bgcolor="#F5F5F5",
            padding=4,
            border_radius=3,
        )

    def create_xsmall_disabled_loading():
        return ft.Container(
            content=ft.Row([
                ft.ProgressRing(width=12, height=12, stroke_width=2, color="#999999"),
                ft.Container(width=4),
                ft.Text("Loading...", size=10, weight=ft.FontWeight.BOLD, color="#999999"),
            ], spacing=0, tight=True),
            bgcolor="#F5F5F5",
            padding=ft.padding.symmetric(horizontal=8, vertical=4),
            border_radius=3,
        )

    # レイアウト構築
    return ft.Container(
        content=ft.Column([
            section_title("Button Sizes (Figma Design)", color=colors["primary_main"]),
            ft.Container(height=20),

            # Large Buttons
            ft.Text("Large Buttons", size=16, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=10),
            ft.Row([
                ft.Column([
                    ft.Text("Filled", size=12, color="#666"),
                    create_large_filled_text(),
                    create_large_filled_icon(),
                    create_large_filled_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined", size=12, color="#666"),
                    create_large_outlined_text(),
                    create_large_outlined_icon(),
                    create_large_outlined_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Text", size=12, color="#666"),
                    create_large_text_text(),
                    create_large_text_icon(),
                    create_large_text_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined2", size=12, color="#666"),
                    create_large_outlined2_text(),
                    create_large_outlined2_icon(),
                    create_large_outlined2_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Disabled", size=12, color="#666"),
                    create_large_disabled_text(),
                    create_large_disabled_icon(),
                    create_large_disabled_loading(),
                ], spacing=8),
            ], spacing=0, scroll=ft.ScrollMode.AUTO),

            ft.Container(height=30),

            # Medium Buttons
            ft.Text("Medium Buttons", size=16, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=10),
            ft.Row([
                ft.Column([
                    ft.Text("Filled", size=12, color="#666"),
                    create_medium_filled_text(),
                    create_medium_filled_icon(),
                    create_medium_filled_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined", size=12, color="#666"),
                    create_medium_outlined_text(),
                    create_medium_outlined_icon(),
                    create_medium_outlined_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Text", size=12, color="#666"),
                    create_medium_text_text(),
                    create_medium_text_icon(),
                    create_medium_text_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined2", size=12, color="#666"),
                    create_medium_outlined2_text(),
                    create_medium_outlined2_icon(),
                    create_medium_outlined2_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Disabled", size=12, color="#666"),
                    create_medium_disabled_text(),
                    create_medium_disabled_icon(),
                    create_medium_disabled_loading(),
                ], spacing=8),
            ], spacing=0, scroll=ft.ScrollMode.AUTO),

            ft.Container(height=30),

            # Small Buttons
            ft.Text("Small Buttons", size=16, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=10),
            ft.Row([
                ft.Column([
                    ft.Text("Filled", size=12, color="#666"),
                    create_small_filled_text(),
                    create_small_filled_icon(),
                    create_small_filled_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined", size=12, color="#666"),
                    create_small_outlined_text(),
                    create_small_outlined_icon(),
                    create_small_outlined_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Text", size=12, color="#666"),
                    create_small_text_text(),
                    create_small_text_icon(),
                    create_small_text_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined2", size=12, color="#666"),
                    create_small_outlined2_text(),
                    create_small_outlined2_icon(),
                    create_small_outlined2_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Disabled", size=12, color="#666"),
                    create_small_disabled_text(),
                    create_small_disabled_icon(),
                    create_small_disabled_loading(),
                ], spacing=8),
            ], spacing=0, scroll=ft.ScrollMode.AUTO),

            ft.Container(height=30),

            # XSmall Buttons
            ft.Text("XSmall Buttons", size=16, weight=ft.FontWeight.BOLD, color="#222222"),
            ft.Container(height=10),
            ft.Row([
                ft.Column([
                    ft.Text("Filled", size=12, color="#666"),
                    create_xsmall_filled_text(),
                    create_xsmall_filled_icon(),
                    create_xsmall_filled_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined", size=12, color="#666"),
                    create_xsmall_outlined_text(),
                    create_xsmall_outlined_icon(),
                    create_xsmall_outlined_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Text", size=12, color="#666"),
                    create_xsmall_text_text(),
                    create_xsmall_text_icon(),
                    create_xsmall_text_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Outlined2", size=12, color="#666"),
                    create_xsmall_outlined2_text(),
                    create_xsmall_outlined2_icon(),
                    create_xsmall_outlined2_loading(),
                ], spacing=8),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Disabled", size=12, color="#666"),
                    create_xsmall_disabled_text(),
                    create_xsmall_disabled_icon(),
                    create_xsmall_disabled_loading(),
                ], spacing=8),
            ], spacing=0, scroll=ft.ScrollMode.AUTO),

        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )
