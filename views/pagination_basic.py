"""
Pagination Section - Paginationコンポーネント（Figmaデザインに基づく）
"""
import flet as ft
from utils.constants import *


def create_pagination_section(colors):
    """Paginationコンポーネント（Figmaデザインに基づく）"""

    def section_title_local(text, color="#5258E4"):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)

    def create_pagination_large():
        """Large size pagination (40px height) - Interactive"""
        # State management
        current_page_num = [1]  # Use list to allow modification in nested functions
        total_items = 30
        items_per_page_num = [10]

        items_per_page_ref = ft.Ref[ft.Text]()
        page_input_ref = ft.Ref[ft.TextField]()
        pagination_row_ref = ft.Ref[ft.Row]()
        pagination_basic_ref = ft.Ref[ft.Row]()

        def create_page_button(page_num):
            is_active = page_num == current_page_num[0]
            return ft.Container(
                content=ft.Text(str(page_num), size=16, color="#FFFFFF" if is_active else "#222222"),
                bgcolor="#7e84fc" if is_active else "#FFFFFF",
                border=None if is_active else ft.border.all(1, "rgba(34, 34, 34, 0.25)"),
                border_radius=8 if is_active else 6,
                width=40,
                height=40,
                alignment=ft.alignment.center,
                on_click=lambda _, p=page_num: go_to_page(p),
                ink=True,
            )

        def update_display():
            """Update pagination display based on current state"""
            start = (current_page_num[0] - 1) * items_per_page_num[0] + 1
            end = min(current_page_num[0] * items_per_page_num[0], total_items)
            max_pages = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]

            items_per_page_ref.current.value = f"{start}〜{end}件（全{total_items}件中）"
            page_input_ref.current.value = str(current_page_num[0])

            # Create page number buttons dynamically based on max_pages
            page_buttons = []
            for page_num in range(1, min(max_pages + 1, 6)):  # Show up to 5 pages
                page_buttons.append(create_page_button(page_num))

            # Update page buttons
            pagination_basic_ref.current.controls = [
                # First page
                ft.Container(
                    content=ft.Icon(name="first_page", size=20, color="#B1B1B1" if current_page_num[0] == 1 else "#6D6D6D"),
                    width=40,
                    height=40,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(1),
                    ink=True,
                ),
                # Previous
                ft.Container(
                    content=ft.Icon(name="keyboard_arrow_left", size=20, color="#B1B1B1" if current_page_num[0] == 1 else "#6D6D6D"),
                    width=40,
                    height=40,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] - 1),
                    ink=True,
                ),
            ] + page_buttons + [
                # Next
                ft.Container(
                    content=ft.Icon(name="keyboard_arrow_right", size=20, color="#B1B1B1" if current_page_num[0] >= max_pages else "#6D6D6D"),
                    width=40,
                    height=40,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] + 1),
                    ink=True,
                ),
                # Last page
                ft.Container(
                    content=ft.Icon(name="last_page", size=20, color="#B1B1B1" if current_page_num[0] >= max_pages else "#6D6D6D"),
                    width=40,
                    height=40,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(max_pages),
                    ink=True,
                ),
            ]

            items_per_page_ref.current.update()
            page_input_ref.current.update()
            pagination_basic_ref.current.update()

        def go_to_page(page_num):
            """Navigate to specific page"""
            max_pages = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]
            if 1 <= page_num <= max_pages:
                current_page_num[0] = page_num
                update_display()

        def on_dropdown_change(e):
            """Handle items per page dropdown change"""
            items_per_page_num[0] = int(e.control.value)
            current_page_num[0] = 1  # Reset to first page
            update_display()

        def on_page_input_submit(e):
            """Handle page input submission"""
            try:
                page_num = int(e.control.value)
                go_to_page(page_num)
            except ValueError:
                page_input_ref.current.value = str(current_page_num[0])
                page_input_ref.current.update()

        # Page control left with interactive dropdown
        page_control_left = ft.Row([
            # Label
            ft.Container(
                content=ft.Text(
                    ref=items_per_page_ref,
                    value="1〜10件（全30件中）",
                    size=12,
                    color="#6D6D6D",
                ),
                padding=ft.padding.only(top=2, bottom=2),
            ),
            # Interactive Dropdown
            ft.Dropdown(
                value="10",
                options=[
                    ft.dropdown.Option("5"),
                    ft.dropdown.Option("10"),
                    ft.dropdown.Option("20"),
                    ft.dropdown.Option("50"),
                    ft.dropdown.Option("100"),
                ],
                width=80,
                text_size=14,
                color="#222222",
                border_radius=8,
                border_color="#6D6D6D",
                bgcolor="#FFFFFF",
                on_change=on_dropdown_change,
            ),
            ft.Text("件表示", size=12, color="#222222"),
        ], spacing=4, alignment=ft.MainAxisAlignment.START)

        # Calculate initial max pages
        max_pages_init = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]

        # Create initial page buttons
        initial_page_buttons = []
        for page_num in range(1, min(max_pages_init + 1, 6)):
            initial_page_buttons.append(create_page_button(page_num))

        # Pagination basic - initialize with initial controls
        pagination_basic = ft.Row([
            # First page
            ft.Container(
                content=ft.Icon(name="first_page", size=20, color="#B1B1B1"),
                width=40,
                height=40,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(1),
                ink=True,
            ),
            # Previous
            ft.Container(
                content=ft.Icon(name="keyboard_arrow_left", size=20, color="#B1B1B1"),
                width=40,
                height=40,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] - 1),
                ink=True,
            ),
        ] + initial_page_buttons + [
            # Next
            ft.Container(
                content=ft.Icon(name="keyboard_arrow_right", size=20, color="#B1B1B1" if current_page_num[0] >= max_pages_init else "#6D6D6D"),
                width=40,
                height=40,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] + 1),
                ink=True,
            ),
            # Last page
            ft.Container(
                content=ft.Icon(name="last_page", size=20, color="#B1B1B1" if current_page_num[0] >= max_pages_init else "#6D6D6D"),
                width=40,
                height=40,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(max_pages_init),
                ink=True,
            ),
        ], spacing=4, ref=pagination_basic_ref)

        # Page control right with interactive text field
        page_control_right = ft.Row([
            ft.TextField(
                ref=page_input_ref,
                value="1",
                text_align=ft.TextAlign.CENTER,
                width=80,
                height=40,
                text_size=14,
                color="#222222",
                border_radius=8,
                border_color="#6D6D6D",
                bgcolor="#FFFFFF",
                content_padding=ft.padding.only(left=12, right=12, top=10, bottom=10),
                on_submit=on_page_input_submit,
            ),
            ft.Text("ページ", size=12, color="#222222"),
        ], spacing=4)

        result = ft.Row([
            page_control_left,
            pagination_basic,
            page_control_right,
        ], spacing=16, alignment=ft.MainAxisAlignment.END, ref=pagination_row_ref)

        return result

    def create_pagination_medium():
        """Medium size pagination (32px height) - Interactive"""
        # State management
        current_page_num = [1]
        total_items = 30
        items_per_page_num = [10]

        items_per_page_ref = ft.Ref[ft.Text]()
        page_input_ref = ft.Ref[ft.TextField]()
        pagination_row_ref = ft.Ref[ft.Row]()
        pagination_basic_ref = ft.Ref[ft.Row]()

        def create_page_button(page_num):
            is_active = page_num == current_page_num[0]
            return ft.Container(
                content=ft.Text(str(page_num), size=14, color="#FFFFFF" if is_active else "#222222"),
                bgcolor="#7e84fc" if is_active else "#FFFFFF",
                border=None if is_active else ft.border.all(1, "rgba(34, 34, 34, 0.25)"),
                border_radius=8 if is_active else 6,
                width=32,
                height=32,
                alignment=ft.alignment.center,
                on_click=lambda _, p=page_num: go_to_page(p),
                ink=True,
            )

        def update_display():
            start = (current_page_num[0] - 1) * items_per_page_num[0] + 1
            end = min(current_page_num[0] * items_per_page_num[0], total_items)
            items_per_page_ref.current.value = f"{start}〜{end}件（全{total_items}件中）"
            page_input_ref.current.value = str(current_page_num[0])

            # Update page buttons
            pagination_basic_ref.current.controls = [
                # First page
                ft.Container(
                    content=ft.Icon(name="first_page", size=20, color="#B1B1B1" if current_page_num[0] == 1 else "#6D6D6D"),
                    width=32,
                    height=32,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(1),
                    ink=True,
                ),
                # Previous
                ft.Container(
                    content=ft.Icon(name="keyboard_arrow_left", size=20, color="#B1B1B1" if current_page_num[0] == 1 else "#6D6D6D"),
                    width=32,
                    height=32,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] - 1),
                    ink=True,
                ),
                # Page buttons 1-5
                create_page_button(1),
                create_page_button(2),
                create_page_button(3),
                create_page_button(4),
                create_page_button(5),
                # Next
                ft.Container(
                    content=ft.Icon(name="keyboard_arrow_right", size=20, color="#6D6D6D"),
                    width=32,
                    height=32,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] + 1),
                    ink=True,
                ),
                # Last page
                ft.Container(
                    content=ft.Icon(name="last_page", size=20, color="#6D6D6D"),
                    width=32,
                    height=32,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page((total_items + items_per_page_num[0] - 1) // items_per_page_num[0]),
                    ink=True,
                ),
            ]

            items_per_page_ref.current.update()
            page_input_ref.current.update()
            pagination_basic_ref.current.update()

        def go_to_page(page_num):
            max_pages = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]
            if 1 <= page_num <= max_pages:
                current_page_num[0] = page_num
                update_display()

        def on_dropdown_change(e):
            items_per_page_num[0] = int(e.control.value)
            current_page_num[0] = 1
            update_display()

        def on_page_input_submit(e):
            try:
                page_num = int(e.control.value)
                go_to_page(page_num)
            except ValueError:
                page_input_ref.current.value = str(current_page_num[0])
                page_input_ref.current.update()

        # Page control left
        page_control_left = ft.Row([
            # Label
            ft.Container(
                content=ft.Text(
                    ref=items_per_page_ref,
                    value="1〜10件（全30件中）",
                    size=11,
                    color="#6D6D6D",
                ),
                padding=ft.padding.only(top=2, bottom=2),
            ),
            # Interactive Dropdown
            ft.Dropdown(
                value="10",
                options=[
                    ft.dropdown.Option("5"),
                    ft.dropdown.Option("10"),
                    ft.dropdown.Option("20"),
                    ft.dropdown.Option("50"),
                    ft.dropdown.Option("100"),
                ],
                width=80,
                text_size=13,
                color="#222222",
                border_radius=6,
                border_color="#6D6D6D",
                bgcolor="#FFFFFF",
                on_change=on_dropdown_change,
            ),
            ft.Text("件表示", size=11, color="#222222"),
        ], spacing=4, alignment=ft.MainAxisAlignment.START)

        # Pagination basic - initialize with initial controls
        pagination_basic = ft.Row([
            # First page
            ft.Container(
                content=ft.Icon(name="first_page", size=20, color="#B1B1B1"),
                width=32,
                height=32,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(1),
                ink=True,
            ),
            # Previous
            ft.Container(
                content=ft.Icon(name="keyboard_arrow_left", size=20, color="#B1B1B1"),
                width=32,
                height=32,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] - 1),
                ink=True,
            ),
            # Page buttons 1-5
            create_page_button(1),
            create_page_button(2),
            create_page_button(3),
            create_page_button(4),
            create_page_button(5),
            # Next
            ft.Container(
                content=ft.Icon(name="keyboard_arrow_right", size=20, color="#6D6D6D"),
                width=32,
                height=32,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] + 1),
                ink=True,
            ),
            # Last page
            ft.Container(
                content=ft.Icon(name="last_page", size=20, color="#6D6D6D"),
                width=32,
                height=32,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page((total_items + items_per_page_num[0] - 1) // items_per_page_num[0]),
                ink=True,
            ),
        ], spacing=4, ref=pagination_basic_ref)

        # Page control right with interactive text field
        page_control_right = ft.Row([
            ft.TextField(
                ref=page_input_ref,
                value="1",
                text_align=ft.TextAlign.CENTER,
                width=80,
                text_size=13,
                color="#222222",
                border_radius=6,
                border_color="#6D6D6D",
                bgcolor="#FFFFFF",
                content_padding=ft.padding.only(left=12, right=12, top=8, bottom=8),
                on_submit=on_page_input_submit,
            ),
            ft.Text("ページ", size=11, color="#222222"),
        ], spacing=4)

        result = ft.Row([
            page_control_left,
            pagination_basic,
            page_control_right,
        ], spacing=16, alignment=ft.MainAxisAlignment.END, ref=pagination_row_ref)

        return result

    def create_pagination_small():
        """Small size pagination (24px height) - Interactive"""
        # State management
        current_page_num = [1]
        total_items = 30
        items_per_page_num = [10]

        items_per_page_ref = ft.Ref[ft.Text]()
        page_input_ref = ft.Ref[ft.TextField]()
        pagination_row_ref = ft.Ref[ft.Row]()
        pagination_basic_ref = ft.Ref[ft.Row]()

        def create_page_button(page_num):
            is_active = page_num == current_page_num[0]
            return ft.Container(
                content=ft.Text(str(page_num), size=12, color="#FFFFFF" if is_active else "#222222"),
                bgcolor="#7e84fc" if is_active else "#FFFFFF",
                border=None if is_active else ft.border.all(1, "rgba(34, 34, 34, 0.25)"),
                border_radius=8 if is_active else 4,
                width=24,
                height=24,
                alignment=ft.alignment.center,
                on_click=lambda _, p=page_num: go_to_page(p),
                ink=True,
            )

        def update_display():
            start = (current_page_num[0] - 1) * items_per_page_num[0] + 1
            end = min(current_page_num[0] * items_per_page_num[0], total_items)
            items_per_page_ref.current.value = f"{start}〜{end}件（全{total_items}件中）"
            page_input_ref.current.value = str(current_page_num[0])

            # Update page buttons
            pagination_basic_ref.current.controls = [
                # First page
                ft.Container(
                    content=ft.Icon(name="first_page", size=16, color="#B1B1B1" if current_page_num[0] == 1 else "#6D6D6D"),
                    width=24,
                    height=24,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(1),
                    ink=True,
                ),
                # Previous
                ft.Container(
                    content=ft.Icon(name="keyboard_arrow_left", size=16, color="#B1B1B1" if current_page_num[0] == 1 else "#6D6D6D"),
                    width=24,
                    height=24,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] - 1),
                    ink=True,
                ),
                # Page buttons 1-5
                create_page_button(1),
                create_page_button(2),
                create_page_button(3),
                create_page_button(4),
                create_page_button(5),
                # Next
                ft.Container(
                    content=ft.Icon(name="keyboard_arrow_right", size=16, color="#6D6D6D"),
                    width=24,
                    height=24,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page(current_page_num[0] + 1),
                    ink=True,
                ),
                # Last page
                ft.Container(
                    content=ft.Icon(name="last_page", size=16, color="#6D6D6D"),
                    width=24,
                    height=24,
                    alignment=ft.alignment.center,
                    on_click=lambda _: go_to_page((total_items + items_per_page_num[0] - 1) // items_per_page_num[0]),
                    ink=True,
                ),
            ]

            items_per_page_ref.current.update()
            page_input_ref.current.update()
            pagination_basic_ref.current.update()

        def go_to_page(page_num):
            max_pages = (total_items + items_per_page_num[0] - 1) // items_per_page_num[0]
            if 1 <= page_num <= max_pages:
                current_page_num[0] = page_num
                update_display()

        def on_dropdown_change(e):
            items_per_page_num[0] = int(e.control.value)
            current_page_num[0] = 1
            update_display()

        def on_page_input_submit(e):
            try:
                page_num = int(e.control.value)
                go_to_page(page_num)
            except ValueError:
                page_input_ref.current.value = str(current_page_num[0])
                page_input_ref.current.update()

        # Page control left
        page_control_left = ft.Row([
            # Label
            ft.Container(
                content=ft.Text(
                    ref=items_per_page_ref,
                    value="1〜10件（全30件中）",
                    size=10,
                    color="#6D6D6D",
                ),
                padding=ft.padding.only(top=2, bottom=2),
            ),
            # Interactive Dropdown
            ft.Dropdown(
                value="10",
                options=[
                    ft.dropdown.Option("5"),
                    ft.dropdown.Option("10"),
                    ft.dropdown.Option("20"),
                    ft.dropdown.Option("50"),
                    ft.dropdown.Option("100"),
                ],
                width=80,
                text_size=12,
                color="#222222",
                border_radius=4,
                border_color="#6D6D6D",
                bgcolor="#FFFFFF",
                on_change=on_dropdown_change,
            ),
            ft.Text("件表示", size=10, color="#222222"),
        ], spacing=4, alignment=ft.MainAxisAlignment.START)

        # Pagination basic - initialize with initial controls
        pagination_basic = ft.Row([
            # First page
            ft.Container(
                content=ft.Icon(name="first_page", size=16, color="#B1B1B1"),
                width=24,
                height=24,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(1),
                ink=True,
            ),
            # Previous
            ft.Container(
                content=ft.Icon(name="keyboard_arrow_left", size=16, color="#B1B1B1"),
                width=24,
                height=24,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] - 1),
                ink=True,
            ),
            # Page buttons 1-5
            create_page_button(1),
            create_page_button(2),
            create_page_button(3),
            create_page_button(4),
            create_page_button(5),
            # Next
            ft.Container(
                content=ft.Icon(name="keyboard_arrow_right", size=16, color="#6D6D6D"),
                width=24,
                height=24,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page(current_page_num[0] + 1),
                ink=True,
            ),
            # Last page
            ft.Container(
                content=ft.Icon(name="last_page", size=16, color="#6D6D6D"),
                width=24,
                height=24,
                alignment=ft.alignment.center,
                on_click=lambda _: go_to_page((total_items + items_per_page_num[0] - 1) // items_per_page_num[0]),
                ink=True,
            ),
        ], spacing=4, ref=pagination_basic_ref)

        # Page control right with interactive text field
        page_control_right = ft.Row([
            ft.TextField(
                ref=page_input_ref,
                value="1",
                text_align=ft.TextAlign.CENTER,
                width=80,
                text_size=12,
                color="#222222",
                border_radius=4,
                border_color="#6D6D6D",
                bgcolor="#FFFFFF",
                content_padding=ft.padding.only(left=12, right=12, top=4, bottom=4),
                on_submit=on_page_input_submit,
            ),
            ft.Text("ページ", size=10, color="#222222"),
        ], spacing=4)

        result = ft.Row([
            page_control_left,
            pagination_basic,
            page_control_right,
        ], spacing=16, alignment=ft.MainAxisAlignment.END, ref=pagination_row_ref)

        return result

    return ft.Container(
        content=ft.Column([
            section_title_local("PAGINATION コンポーネント", color=colors["primary_main"]),
            ft.Container(height=20),

            ft.Text(
                "Figmaデザインシステムから取得したPagination（ページネーション）",
                size=14,
                color="#666666",
            ),
            ft.Container(height=30),

            # Large size
            ft.Text("Large（高さ40px）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            create_pagination_large(),
            ft.Container(height=30),

            # Medium size
            ft.Text("Medium（高さ32px）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            create_pagination_medium(),
            ft.Container(height=30),

            # Small size
            ft.Text("Small（高さ24px）", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=10),
            create_pagination_small(),
        ], spacing=5),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

