"""
Layout Templates - Figmaデザインシステムに準拠したレイアウトテンプレート
"""
import flet as ft
from utils.constants import COLORS


def create_placeholder_container(text="Container", height=None):
    """プレースホルダーコンテナ - コンテンツ配置エリアの視覚化"""
    return ft.Container(
        content=ft.Text(
            text,
            size=12,
            color="#EA3829",
            text_align=ft.TextAlign.CENTER,
        ),
        bgcolor="rgba(234, 56, 41, 0.1)",
        border=ft.border.all(1, "#F75C46"),
        border_radius=2,
        padding=ft.padding.symmetric(horizontal=16, vertical=8),
        alignment=ft.alignment.center,
        expand=True if height is None else False,
        height=height,
    )


def create_layout_header(colors):
    """共通ヘッダーコンポーネント"""
    return ft.Container(
        content=ft.Row([
            # Left: Logo
            ft.Container(
                content=ft.Text(
                    "FIXEL",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=COLORS["neutral_white"],
                ),
                expand=True,
            ),
            # Right: Icons + Login
            ft.Row([
                ft.IconButton(
                    icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                    icon_color=COLORS["neutral_white"],
                    icon_size=20,
                ),
                ft.IconButton(
                    icon=ft.Icons.HELP_OUTLINE,
                    icon_color=COLORS["neutral_white"],
                    icon_size=20,
                ),
                ft.IconButton(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    icon_color=COLORS["neutral_white"],
                    icon_size=20,
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Icon(ft.Icons.PERSON_OUTLINE, size=20, color=COLORS["neutral_white"]),
                        ft.Text("ログイン", size=16, weight=ft.FontWeight.BOLD, color=COLORS["neutral_white"]),
                    ], spacing=8),
                    border=ft.border.all(1, COLORS["neutral_white"]),
                    border_radius=8,
                    padding=8,
                ),
            ], spacing=16),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        bgcolor=COLORS["primary_main"],
        padding=ft.padding.symmetric(horizontal=32, vertical=0),
        height=48,
    )


def create_layout_footer(colors):
    """共通フッターコンポーネント"""
    return ft.Container(
        content=ft.Text(
            "Fixel Inc.",
            size=12,
            color=COLORS["neutral_white"],
            text_align=ft.TextAlign.CENTER,
        ),
        bgcolor=COLORS["primary_main"],
        padding=8,
        alignment=ft.alignment.center,
    )


def create_breadcrumb(colors):
    """パンくずリストコンポーネント"""
    items = []
    pages = ["HOME", "Page", "Page", "Page", "Page", "Page"]

    for i, page in enumerate(pages):
        is_last = i == len(pages) - 1
        color = COLORS["neutral_light"] if is_last else COLORS["primary_main"]

        items.append(ft.Text(page, size=12, weight=ft.FontWeight.BOLD, color=color))

        if not is_last:
            items.append(ft.Icon(ft.Icons.KEYBOARD_ARROW_RIGHT, size=16, color=COLORS["neutral_light"]))

    return ft.Container(
        content=ft.Row(items, spacing=8),
        padding=ft.padding.only(top=16, bottom=4, left=32, right=32),
    )


def create_foot_buttons(colors):
    """フッターボタングループコンポーネント"""
    return ft.Container(
        content=ft.Row([
            # Left: Delete button
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.DELETE_OUTLINE, size=24, color=COLORS["neutral_white"]),
                    ft.Text("削除", size=16, weight=ft.FontWeight.BOLD, color=COLORS["neutral_white"]),
                ], spacing=8),
                bgcolor=COLORS["danger_main"],
                padding=8,
                border_radius=8,
                height=40,
            ),
            # Right: Cancel + Save buttons
            ft.Row([
                ft.Container(
                    content=ft.Text("キャンセル", size=16, weight=ft.FontWeight.BOLD, color=COLORS["success_main"]),
                    border=ft.border.all(1, COLORS["success_main"]),
                    padding=8,
                    border_radius=8,
                    height=40,
                ),
                ft.Container(
                    content=ft.Text("保存", size=16, weight=ft.FontWeight.BOLD, color=COLORS["neutral_white"]),
                    bgcolor=COLORS["success_main"],
                    padding=8,
                    border_radius=8,
                    height=40,
                ),
            ], spacing=4),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        bgcolor=COLORS["neutral_white"],
        border=ft.border.only(top=ft.BorderSide(1, "rgba(34, 34, 34, 0.1)")),
        padding=ft.padding.symmetric(horizontal=32, vertical=8),
    )


# ========================================
# Stacked Layout (ヘッダー + コンテンツ + フッター)
# ========================================

def create_stacked_layout_1col(colors):
    """Stacked Layout - 1 Column"""
    return ft.Column([
        create_layout_header(colors),

        # Content Area - Stackを使用して絶対配置を実現
        ft.Container(
            content=ft.Stack([
                # メインコンテンツ
                ft.Column([
                    create_breadcrumb(colors),
                    ft.Container(
                        content=create_placeholder_container("Container"),
                        padding=32,
                        expand=True,
                    ),
                ], spacing=0, expand=True),

                # Foot Buttons - 絶対配置で下部に固定
                ft.Container(
                    content=create_foot_buttons(colors),
                    bottom=0,
                    left=0,
                    right=0,
                ),
            ]),
            expand=True,
        ),

        create_layout_footer(colors),
    ], spacing=0, expand=True)


# ========================================
# Light Sidebar + Nav Bar Layout
# ========================================

def create_light_sidebar_layout_1col(colors):
    """Light Sidebar with Nav Bar - 1 Column"""

    # Light Sidebar (Left)
    sidebar = ft.Container(
        content=ft.Column([
            # Header
            ft.Container(
                content=ft.Icon(ft.Icons.MENU, size=16, color=COLORS["primary_main"]),
                padding=ft.padding.symmetric(horizontal=16, vertical=4),
                height=48,
            ),
            ft.Divider(height=1, color="rgba(34, 34, 34, 0.1)"),

            # Navigation Items
            ft.Container(
                content=ft.Column([
                    # Active Item
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.HOME, size=20, color="#7E84FC"),
                            ft.Text("ホーム", size=14, color=COLORS["neutral_black"]),
                        ], spacing=4),
                        bgcolor="#D3D5FF",
                        padding=ft.padding.symmetric(horizontal=16, vertical=2),
                        height=40,
                    ),

                    # Category Title
                    ft.Container(
                        content=ft.Text("プロジェクト管理", size=10, weight=ft.FontWeight.BOLD, color=COLORS["neutral_black"]),
                        padding=ft.padding.only(left=16, right=8, top=16, bottom=8),
                    ),

                    # Tree Items
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.FOLDER_OUTLINED, size=20, color="#7E84FC"),
                            ft.Text("4Qキャンペーン", size=14, color=COLORS["neutral_black"]),
                            ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, size=20, color="#7E84FC"),
                        ], spacing=4),
                        padding=ft.padding.symmetric(horizontal=16, vertical=2),
                        height=40,
                    ),
                ], spacing=0),
                expand=True,
                padding=ft.padding.symmetric(vertical=8),
            ),

            ft.Divider(height=1, color="rgba(34, 34, 34, 0.1)"),

            # Footer - User Account
            ft.Container(
                content=ft.Row([
                    ft.CircleAvatar(radius=12, bgcolor="#7E84FC"),
                    ft.Text("User Name", size=16, weight=ft.FontWeight.BOLD, color=COLORS["success_main"]),
                ], spacing=8),
                border=ft.border.all(1, COLORS["success_main"]),
                padding=8,
                border_radius=8,
                margin=ft.margin.all(8),
                height=40,
            ),
        ], spacing=0),
        width=256,
        bgcolor="#FDFDFD",
    )

    # Main Content (Right) - Stackを使用して絶対配置を実現
    main_content = ft.Container(
        content=ft.Stack([
            # メインコンテンツ
            ft.Container(
                content=ft.Column([
                    create_breadcrumb(colors),
                    # Container Area
                    ft.Container(
                        content=create_placeholder_container("Container"),
                        padding=ft.padding.only(left=0, right=32, top=0, bottom=0),
                        expand=True,
                    ),
                ], spacing=0, expand=True),
                padding=ft.padding.only(top=16, bottom=24),
                expand=True,
            ),

            # Foot Buttons - 絶対配置で下部に固定
            ft.Container(
                content=create_foot_buttons(colors),
                bottom=0,
                left=0,
                right=0,
            ),
        ]),
        expand=True,
    )

    return ft.Column([
        create_layout_header(colors),

        # Sidebar + Main Content
        ft.Row([
            sidebar,
            main_content,
        ], spacing=24, expand=True),

        create_layout_footer(colors),
    ], spacing=0, expand=True)


# ========================================
# Primary Sidebar + Nav Bar Layout
# ========================================

def create_primary_sidebar_layout_1col(colors):
    """Primary Sidebar with Nav Bar - 1 Column"""

    # Primary Sidebar (Left) - 紫背景
    sidebar = ft.Container(
        content=ft.Column([
            # Header
            ft.Container(
                content=ft.Icon(ft.Icons.MENU, size=16, color=COLORS["neutral_white"]),
                padding=ft.padding.symmetric(horizontal=16, vertical=4),
                height=48,
            ),
            ft.Divider(height=1, color="rgba(255, 255, 255, 0.16)"),

            # Navigation Items
            ft.Container(
                content=ft.Column([
                    # Active Item
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.HOME, size=20, color=COLORS["neutral_white"]),
                            ft.Text("ホーム", size=14, color=COLORS["neutral_white"]),
                        ], spacing=4),
                        bgcolor="rgba(0, 0, 0, 0.25)",
                        padding=ft.padding.symmetric(horizontal=16, vertical=2),
                        height=40,
                    ),

                    # Category Title
                    ft.Container(
                        content=ft.Text("プロジェクト管理", size=10, weight=ft.FontWeight.BOLD, color=COLORS["neutral_white"]),
                        padding=ft.padding.only(left=16, right=8, top=16, bottom=8),
                    ),

                    # Tree Items
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(ft.Icons.FOLDER_OUTLINED, size=20, color=COLORS["neutral_white"]),
                            ft.Text("4Qキャンペーン", size=14, color=COLORS["neutral_white"]),
                            ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, size=20, color=COLORS["neutral_white"]),
                        ], spacing=4),
                        padding=ft.padding.symmetric(horizontal=16, vertical=2),
                        height=40,
                    ),
                ], spacing=0),
                expand=True,
                padding=ft.padding.symmetric(vertical=8),
            ),

            ft.Divider(height=1, color="rgba(255, 255, 255, 0.16)"),

            # Footer - User Account
            ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.CircleAvatar(radius=12, bgcolor="#7E84FC"),
                        border=ft.border.all(1, COLORS["neutral_white"]),
                        border_radius=100,
                        padding=0,
                    ),
                    ft.Text("User Name", size=16, weight=ft.FontWeight.BOLD, color=COLORS["neutral_white"]),
                ], spacing=8),
                border=ft.border.all(1, COLORS["neutral_white"]),
                padding=8,
                border_radius=8,
                margin=ft.margin.all(8),
                height=40,
            ),
        ], spacing=0),
        width=256,
        bgcolor=COLORS["primary_main"],
    )

    # Main Content (Right) - Stackを使用して絶対配置を実現
    main_content = ft.Container(
        content=ft.Stack([
            # メインコンテンツ
            ft.Container(
                content=ft.Column([
                    create_breadcrumb(colors),
                    # Container Area
                    ft.Container(
                        content=create_placeholder_container("Container"),
                        padding=ft.padding.only(left=0, right=32, top=0, bottom=0),
                        expand=True,
                    ),
                ], spacing=0, expand=True),
                padding=ft.padding.only(top=16, bottom=24),
                expand=True,
            ),

            # Foot Buttons - 絶対配置で下部に固定
            ft.Container(
                content=create_foot_buttons(colors),
                bottom=0,
                left=0,
                right=0,
            ),
        ]),
        expand=True,
    )

    return ft.Column([
        create_layout_header(colors),

        # Sidebar + Main Content
        ft.Row([
            sidebar,
            main_content,
        ], spacing=24, expand=True),

        create_layout_footer(colors),
    ], spacing=0, expand=True)


# ========================================
# Gallery Section
# ========================================

def create_layout_templates_section(colors):
    """レイアウトテンプレートギャラリーセクション"""

    def section_title(text):
        return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=colors["primary_main"])

    return ft.Container(
        content=ft.Column([
            section_title("Layout Templates (Figma Design System)"),
            ft.Container(height=20),

            # Stacked Layout
            ft.Container(
                content=ft.Column([
                    ft.Text("1. Stacked Layout (1 Column)", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
                    ft.Container(height=10),
                    ft.Container(
                        content=create_stacked_layout_1col(colors),
                        height=600,
                        border=ft.border.all(2, colors["neutral_light"]),
                        border_radius=8,
                    ),
                ], spacing=0),
            ),

            ft.Container(height=40),

            # Light Sidebar Layout
            ft.Container(
                content=ft.Column([
                    ft.Text("2. Light Sidebar + Nav Bar (1 Column)", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
                    ft.Container(height=10),
                    ft.Container(
                        content=create_light_sidebar_layout_1col(colors),
                        height=600,
                        border=ft.border.all(2, colors["neutral_light"]),
                        border_radius=8,
                    ),
                ], spacing=0),
            ),

            ft.Container(height=40),

            # Primary Sidebar Layout
            ft.Container(
                content=ft.Column([
                    ft.Text("3. Primary Sidebar + Nav Bar (1 Column)", size=16, weight=ft.FontWeight.BOLD, color=colors["neutral_black"]),
                    ft.Container(height=10),
                    ft.Container(
                        content=create_primary_sidebar_layout_1col(colors),
                        height=600,
                        border=ft.border.all(2, colors["neutral_light"]),
                        border_radius=8,
                    ),
                ], spacing=0),
            ),

        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )
