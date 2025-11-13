"""
Tag Section - Tagコンポーネント（Figmaデザインに基づく）
"""
import flet as ft
from utils.constants import *


def create_tag_section(colors):
    """Tagコンポーネント（Figmaデザインに基づく）"""

    def section_title_local(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_tag(label, text_color, bg_color=None, border_color=None, icon_name="cancel", border_style=None):
        """Tagを作成（Figma仕様準拠：外側4px padding、spacing 0px）"""
        content_items = []

        # Add iconの場合はアイコンが先
        if label == "Add":
            content_items.append(
                ft.Icon(
                    name=icon_name,
                    size=12,
                    color=text_color,
                )
            )

        # テキスト（Wrapper付き：パディング調整）
        text_wrapper = ft.Container(
            content=ft.Text(
                label,
                size=10,
                weight=ft.FontWeight.BOLD,
                color=text_color,
            ),
            padding=ft.padding.symmetric(horizontal=4, vertical=2),
        )
        content_items.append(text_wrapper)

        # Tag Labelの場合はキャンセルアイコンが後
        if label == "Tag Label":
            content_items.append(
                ft.Icon(
                    name=icon_name,
                    size=12,
                    color=text_color,
                )
            )

        container_props = {
            "content": ft.Row(
                content_items,
                spacing=2,  # Wrapper内は2px gap
                alignment=ft.MainAxisAlignment.CENTER,
                tight=True,  # コンテンツの幅に合わせる
            ),
            "padding": ft.padding.symmetric(horizontal=4, vertical=2),  # 調整: 上下2px追加
            "border_radius": 100,
            "expand": False,  # 横幅いっぱいに広がらないようにする
        }

        if bg_color:
            container_props["bgcolor"] = bg_color

        if border_color:
            if border_style == "dashed":
                container_props["border"] = ft.border.all(1, border_color)
                # Fletではborder-styleを直接指定できないため、実線で代用
            else:
                container_props["border"] = ft.border.all(1, border_color)

        return ft.Container(**container_props)

    # Tag colors定義
    tag_colors = {
        "primary": {"text": "#686df4", "bg": "#d3d5ff"},
        "secondary": {"text": "#9d57f4", "bg": "#e6d0ff"},
        "teal": {"text": "#008f5d", "bg": "#89ecbc"},
        "magenta": {"text": "#de3d82", "bg": "#ffcadd"},
        "blue": {"text": "#147af3", "bg": "#b5deff"},
        "red": {"text": "#ea3829", "bg": "#ffcdc3"},
    }

    # Contained type tags
    contained_tags = ft.Row([
        create_tag("Tag Label", tag_colors["primary"]["text"], bg_color=tag_colors["primary"]["bg"]),
        create_tag("Tag Label", tag_colors["secondary"]["text"], bg_color=tag_colors["secondary"]["bg"]),
        create_tag("Tag Label", tag_colors["teal"]["text"], bg_color=tag_colors["teal"]["bg"]),
        create_tag("Tag Label", tag_colors["magenta"]["text"], bg_color=tag_colors["magenta"]["bg"]),
        create_tag("Tag Label", tag_colors["blue"]["text"], bg_color=tag_colors["blue"]["bg"]),
        create_tag("Tag Label", tag_colors["red"]["text"], bg_color=tag_colors["red"]["bg"]),
    ], spacing=8, wrap=True)

    # Ghost type tags
    ghost_tags = ft.Row([
        create_tag("Tag Label", tag_colors["primary"]["text"], border_color=tag_colors["primary"]["text"]),
        create_tag("Tag Label", tag_colors["secondary"]["text"], border_color=tag_colors["secondary"]["text"]),
        create_tag("Tag Label", tag_colors["teal"]["text"], border_color=tag_colors["teal"]["text"]),
        create_tag("Tag Label", tag_colors["magenta"]["text"], border_color=tag_colors["magenta"]["text"]),
        create_tag("Tag Label", tag_colors["blue"]["text"], border_color=tag_colors["blue"]["text"]),
        create_tag("Tag Label", tag_colors["red"]["text"], border_color=tag_colors["red"]["text"]),
    ], spacing=8, wrap=True)

    # Add New type tags
    add_new_tags = ft.Row([
        create_tag("Add", tag_colors["primary"]["text"], border_color=tag_colors["primary"]["text"],
                  icon_name="add_circle_outline", border_style="dashed"),
        create_tag("Add", tag_colors["secondary"]["text"], border_color=tag_colors["secondary"]["text"],
                  icon_name="add_circle_outline", border_style="dashed"),
        create_tag("Add", tag_colors["teal"]["text"], border_color=tag_colors["teal"]["text"],
                  icon_name="add_circle_outline", border_style="dashed"),
        create_tag("Add", tag_colors["magenta"]["text"], border_color=tag_colors["magenta"]["text"],
                  icon_name="add_circle_outline", border_style="dashed"),
        create_tag("Add", tag_colors["blue"]["text"], border_color=tag_colors["blue"]["text"],
                  icon_name="add_circle_outline", border_style="dashed"),
        create_tag("Add", tag_colors["red"]["text"], border_color=tag_colors["red"]["text"],
                  icon_name="add_circle_outline", border_style="dashed"),
    ], spacing=8, wrap=True)

    return ft.Container(
        content=ft.Column([
            section_title_local("TAG コンポーネント", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Text(
                "Figmaデザインシステムから取得したTag（タグ）",
                size=14,
                color="#666666",
            ),
            ft.Container(height=30),

            # Contained type
            ft.Text("Type: Contained（背景色あり）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            contained_tags,
            ft.Container(height=30),

            # Ghost type
            ft.Text("Type: Ghost（ボーダーのみ）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            ghost_tags,
            ft.Container(height=30),

            # Add New type
            ft.Text("Type: Add New（点線ボーダー）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            add_new_tags,
        ], spacing=5),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

