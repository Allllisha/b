"""
Pagination Headline Section - ページネーション付きヘッドラインセクション（Figmaデザイン準拠）
"""
import flet as ft
from utils.constants import *


def create_pagination_headline_section(colors):
    """ページネーション付きヘッドラインセクション（Figmaデザインから変換）"""

    def section_title(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_pagination_headline():
        """LV2 / Headline コンポーネント"""
        neutral_main_opacity_25 = "rgba(34,34,34,0.25)"
        neutral_main_opacity_16 = "rgba(34,34,34,0.16)"

        # State management
        current_page_num = [1]
        total_items = 30
        items_per_page_num = [10]

        page_info_ref = ft.Ref[ft.Text]()
        page_input_text_ref = ft.Ref[ft.Text]()
        page_numbers_ref = ft.Ref[ft.Row]()

        def create_page_button(page_num):
            is_active = page_num == current_page_num[0]
            return ft.Container(
                content=ft.Text(str(page_num), size=16, color="#FFFFFF" if is_active else colors["neutral_black"]),
                width=40, height=40,
                bgcolor="#7e84fc" if is_active else colors["neutral_white"],
                border=None if is_active else ft.border.all(1, neutral_main_opacity_25),
                border_radius=8 if is_active else 6,
                alignment=ft.alignment.center,
                on_click=lambda _, p=page_num: go_to_page(p),
                ink=True,
            )

        def update_display():
            start = (current_page_num[0] - 1) * items_per_page_num[0] + 1
            end = min(current_page_num[0] * items_per_page_num[0], total_items)
            max_pages = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]

            page_info_ref.current.value = f"{start}〜{end}件（全{total_items}件中）"
            page_input_text_ref.current.value = str(current_page_num[0])

            # Create page number buttons dynamically based on max_pages
            page_buttons = []
            for page_num in range(1, min(max_pages + 1, 6)):  # Show up to 5 pages
                page_buttons.append(create_page_button(page_num))

            # Update page buttons dynamically
            page_numbers_ref.current.controls = [
                ft.Container(
                    content=ft.Icon(ft.Icons.FIRST_PAGE, size=20, color=colors["neutral_disabled"] if current_page_num[0] == 1 else colors["neutral_light"]),
                    width=40, height=40, alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(1),
                    ink=True,
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.KEYBOARD_ARROW_LEFT, size=20, color=colors["neutral_disabled"] if current_page_num[0] == 1 else colors["neutral_light"]),
                    width=40, height=40, alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] - 1),
                    ink=True,
                ),
            ] + page_buttons + [
                ft.Container(
                    content=ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT, size=20, color=colors["neutral_disabled"] if current_page_num[0] >= max_pages else colors["neutral_light"]),
                    width=40, height=40, alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] + 1),
                    ink=True,
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.LAST_PAGE, size=20, color=colors["neutral_disabled"] if current_page_num[0] >= max_pages else colors["neutral_light"]),
                    width=40, height=40, alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(max_pages),
                    ink=True,
                ),
            ]

            page_info_ref.current.update()
            page_input_text_ref.current.update()
            page_numbers_ref.current.update()

        def go_to_page(page_num):
            max_pages = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]
            if 1 <= page_num <= max_pages:
                current_page_num[0] = page_num
                update_display()

        title = ft.Container(
            content=ft.Text("メインタイトルが入ります", size=24, weight=ft.FontWeight.W_400, color=colors["neutral_black"]),
            padding=ft.padding.only(top=16, bottom=8),
        )

        page_info = ft.Row([
            ft.Text(ref=page_info_ref, value="1〜10件（全30件中）", size=12, color=colors["neutral_light"]),
            ft.Container(
                content=ft.Row([
                    ft.Text("10", size=14, color=colors["neutral_black"]),
                    ft.Icon(ft.Icons.ARROW_DROP_DOWN, size=20, color=colors["neutral_light"]),
                ], spacing=4),
                height=40, padding=ft.padding.symmetric(horizontal=8, vertical=8),
                border=ft.border.all(1, colors["neutral_light"]), border_radius=8, bgcolor=colors["neutral_white"],
            ),
            ft.Text("件表示", size=12, color=colors["neutral_black"]),
        ], spacing=4)

        # Calculate initial max pages
        max_pages_init = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]

        # Create initial page buttons
        initial_page_buttons = []
        for page_num in range(1, min(max_pages_init + 1, 6)):
            initial_page_buttons.append(create_page_button(page_num))

        # Page numbers - initialize with initial state
        page_numbers = ft.Row([
            ft.Container(
                content=ft.Icon(ft.Icons.FIRST_PAGE, size=20, color=colors["neutral_disabled"]),
                width=40, height=40, alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(1),
                ink=True,
            ),
            ft.Container(
                content=ft.Icon(ft.Icons.KEYBOARD_ARROW_LEFT, size=20, color=colors["neutral_disabled"]),
                width=40, height=40, alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] - 1),
                ink=True,
            ),
        ] + initial_page_buttons + [
            ft.Container(
                content=ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT, size=20, color=colors["neutral_disabled"] if current_page_num[0] >= max_pages_init else colors["neutral_light"]),
                width=40, height=40, alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] + 1),
                ink=True,
            ),
            ft.Container(
                content=ft.Icon(ft.Icons.LAST_PAGE, size=20, color=colors["neutral_disabled"] if current_page_num[0] >= max_pages_init else colors["neutral_light"]),
                width=40, height=40, alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(max_pages_init),
                ink=True,
            ),
        ], spacing=4, ref=page_numbers_ref)

        page_input = ft.Row([
            ft.Container(
                content=ft.Text(ref=page_input_text_ref, value="1", size=14, color=colors["neutral_black"]),
                width=50, height=40, padding=ft.padding.symmetric(horizontal=12),
                border=ft.border.all(1, colors["neutral_light"]), border_radius=8,
                bgcolor=colors["neutral_white"], alignment=ft.alignment.center_left
            ),
            ft.Text("ページ", size=12, color=colors["neutral_black"]),
        ], spacing=4)

        pagination = ft.Row([page_info, page_numbers, page_input], spacing=16)

        search_area = ft.Row([
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.SEARCH, size=16, color=colors["neutral_light"]),
                    ft.Text("placeholder", size=12, color="#909090"),
                ], spacing=4),
                width=168, height=32, padding=ft.padding.symmetric(horizontal=12),
                border=ft.border.all(1, colors["neutral_light"]), border_radius=6,
                bgcolor=colors["neutral_white"], alignment=ft.alignment.center_left,
            ),
            ft.Container(
                content=ft.Text("検索", size=14, weight=ft.FontWeight.BOLD, color=colors["neutral_white"]),
                height=32, padding=ft.padding.symmetric(horizontal=12, vertical=4),
                bgcolor=colors["success_main"], border_radius=8, alignment=ft.alignment.center,
            ),
        ], spacing=16, alignment=ft.MainAxisAlignment.END)

        toolbar = ft.Container(
            content=ft.Row([pagination, search_area], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, expand=True),
            padding=ft.padding.symmetric(vertical=8),
        )

        tabs = []
        for i in range(5):
            is_selected = i == 0
            tab = ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.LABEL, size=16, color=colors["neutral_black"] if is_selected else colors["neutral_light"]),
                    ft.Text("Label", size=12, weight=ft.FontWeight.BOLD, color=colors["neutral_black"] if is_selected else colors["neutral_light"]),
                ], spacing=8),
                height=40, padding=ft.padding.symmetric(horizontal=16, vertical=8),
                border=ft.border.only(bottom=ft.BorderSide(2 if is_selected else 1, colors["neutral_black"] if is_selected else neutral_main_opacity_16)),
            )
            tabs.append(tab)

        tab_bar = ft.Container(
            content=ft.Row(tabs, spacing=0),
            border=ft.border.only(bottom=ft.BorderSide(1, colors["neutral_light"])),
            margin=ft.margin.only(top=16),
        )

        return ft.Column([title, toolbar, tab_bar], spacing=0, expand=True)

    return ft.Container(
        content=ft.Column([
            section_title("Pagination Headline (LV2 - Figmaデザイン)", color=colors["primary_main"]),
            ft.Container(height=10),
            create_pagination_headline(),
        ], spacing=0),
        bgcolor="#FFFFFF", padding=30, border_radius=12,
    )
