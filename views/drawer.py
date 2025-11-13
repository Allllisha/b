"""
Drawer Section - Drawerコンポーネント
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


def create_drawer_section(colors):
    """Drawerセクションを作成"""

    def create_tree_item(icon, text, has_expand=False, indent_level=0, selected=False, has_checkbox=False):
        """ツリーアイテムを作成

        Args:
            icon: アイコン（ft.Icons.xxx）
            text: テキスト
            has_expand: 展開ボタンを表示するか
            indent_level: インデントレベル（0, 1, 2）
            selected: 選択状態か
            has_checkbox: チェックボックスを表示するか
        """
        # インデントによるパディング計算
        left_padding = 16 + (indent_level * 32)

        items = []

        # チェックボックス
        if has_checkbox:
            checkbox = ft.Container(
                content=ft.Container(
                    content=ft.Icon(ft.Icons.CHECK_BOX_OUTLINE_BLANK, size=15, color="#ffffff"),
                    bgcolor="#33ffffff",
                    border_radius=2,
                    width=20,
                    height=20,
                    alignment=ft.alignment.center,
                ),
                width=20,
                height=20,
            )
            items.append(checkbox)

        # アイコン
        if icon:
            items.append(ft.Icon(icon, size=20, color="#ffffff"))

        # テキスト
        items.append(
            ft.Text(
                text,
                size=14,
                color="#ffffff",
                expand=True,
            )
        )

        # 展開ボタン
        if has_expand:
            items.append(ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, size=20, color="#ffffff"))

        return ft.Container(
            content=ft.Row(
                items,
                spacing=4,
            ),
            bgcolor="rgba(0,0,0,0.25)" if selected else "transparent",
            padding=ft.padding.only(left=left_padding, right=16, top=2, bottom=2),
            height=40,
        )

    def create_category_title(text):
        """カテゴリタイトルを作成"""
        return ft.Container(
            content=ft.Text(
                text,
                size=10,
                weight=ft.FontWeight.BOLD,
                color="#ffffff",
            ),
            padding=ft.padding.only(left=16, right=8, top=16, bottom=8),
            height=40,
        )

    # Drawerの構造
    drawer = ft.Container(
        content=ft.Column([
            # ヘッダー
            ft.Container(
                content=ft.Row([
                    # ロゴエリア（簡易版）
                    ft.Text("LOGO", size=14, weight=ft.FontWeight.BOLD, color="#ffffff"),
                    # 戻るボタン
                    ft.Icon(ft.Icons.ARROW_BACK, size=16, color="#ffffff"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=ft.padding.only(left=16, right=16, top=4, bottom=4),
                height=48,
            ),

            # 区切り線
            ft.Container(bgcolor="rgba(255,255,255,0.16)", height=1),

            # コンテンツ
            ft.Container(
                content=ft.Column([
                    # ホーム（選択状態）
                    create_tree_item(ft.Icons.HOME, "ホーム", selected=True),

                    # プロジェクト管理
                    create_category_title("プロジェクト管理"),

                    # 4Qキャンペーン（展開）
                    create_tree_item(ft.Icons.FOLDER, "4Qキャンペーン", has_expand=True),
                    create_tree_item(None, "営業キャンペーン", has_expand=True, indent_level=1),
                    create_tree_item(None, "エリア一覧", has_expand=True, indent_level=1),
                    create_tree_item(None, "首都圏エリア", indent_level=2),
                    create_tree_item(None, "関西エリア", indent_level=2),

                    # 4Q新企画（展開）
                    create_tree_item(ft.Icons.FOLDER, "4Q新企画", has_expand=True),
                    create_tree_item(ft.Icons.EDIT, "ドラフト", indent_level=1),
                    create_tree_item(ft.Icons.ATTACH_FILE, "関連資料", indent_level=1),

                    # Title
                    create_category_title("Title"),

                    # チェックボックス付きツリーアイテム
                    create_tree_item(ft.Icons.DESCRIPTION, "ツリーアイテム", has_expand=True, has_checkbox=True),
                    create_tree_item(ft.Icons.DESCRIPTION, "ツリーアイテム", has_expand=True, has_checkbox=True),
                    create_tree_item(ft.Icons.DESCRIPTION, "ツリーアイテム", has_expand=True, has_checkbox=True),
                ], spacing=0, scroll=ft.ScrollMode.AUTO),
                expand=True,
                padding=ft.padding.only(top=8, bottom=8),
            ),

            # 区切り線
            ft.Container(bgcolor="rgba(255,255,255,0.16)", height=1),

            # フッター
            ft.Container(
                content=ft.Column([
                    # 管理メニュー
                    create_category_title("管理メニュー"),

                    # グループ設定
                    create_tree_item(ft.Icons.GROUP, "グループ設定"),

                    # アカウント管理
                    create_tree_item(ft.Icons.MANAGE_ACCOUNTS, "アカウント管理", has_expand=True),

                    # 管理者メニュー
                    create_tree_item(ft.Icons.ADMIN_PANEL_SETTINGS, "管理者メニュー", has_expand=True),

                    # ユーザーアカウント
                    ft.Container(
                        content=ft.Container(
                            content=ft.Row([
                                ft.Container(
                                    content=ft.Icon(ft.Icons.PERSON, size=16, color=colors["primary_main"]),
                                    bgcolor="#ffffff",
                                    border_radius=100,
                                    width=24,
                                    height=24,
                                    alignment=ft.alignment.center,
                                ),
                                ft.Text("User Name", size=16, weight=ft.FontWeight.BOLD, color="#ffffff"),
                            ], spacing=8),
                            border=ft.border.all(1, "#ffffff"),
                            border_radius=8,
                            padding=8,
                            height=40,
                        ),
                        padding=ft.padding.only(left=8, right=8, top=16, bottom=10),
                    ),
                ], spacing=0),
                padding=ft.padding.only(bottom=24, top=8),
            ),
        ], spacing=0),
        bgcolor=colors["primary_main"],
        width=256,
        height=900,
    )

    # 閉じた状態のDrawer（色付き背景）
    drawer_closed_colored = ft.Container(
        content=ft.Column([
            # ヘッダー
            ft.Container(
                content=ft.Icon(ft.Icons.ARROW_FORWARD, size=16, color="#ffffff"),
                padding=ft.padding.only(left=28, right=28, top=16, bottom=16),
                height=48,
            ),
            # 区切り線
            ft.Container(bgcolor="rgba(255,255,255,0.16)", height=1),
            # アイコンのみのメニュー
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Icon(ft.Icons.HOME, size=20, color="#ffffff"),
                        bgcolor="rgba(0,0,0,0.25)",
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Icon(ft.Icons.FOLDER, size=20, color="#ffffff"),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Icon(ft.Icons.REMOVE, size=20, color="#ffffff"),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=0, scroll=ft.ScrollMode.AUTO),
                expand=True,
                padding=ft.padding.only(top=8, bottom=8),
            ),
            # 区切り線
            ft.Container(bgcolor="rgba(255,255,255,0.16)", height=1),
            # フッター
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Icon(ft.Icons.GROUP, size=20, color="#ffffff"),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.MANAGE_ACCOUNTS, size=20, color="#ffffff"),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS, size=20, color="#ffffff"),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Container(
                            content=ft.Icon(ft.Icons.PERSON, size=16, color=colors["primary_main"]),
                            bgcolor="#ffffff",
                            border_radius=100,
                            width=32,
                            height=32,
                            alignment=ft.alignment.center,
                        ),
                        padding=ft.padding.only(left=20, right=20, top=16, bottom=10),
                    ),
                ], spacing=0),
                padding=ft.padding.only(bottom=24, top=8),
            ),
        ], spacing=0),
        bgcolor=colors["primary_main"],
        width=72,
        height=900,
    )

    # 開いた状態のDrawer（白背景）
    def create_tree_item_white(icon, text, has_expand=False, indent_level=0, selected=False, has_checkbox=False):
        """白背景用のツリーアイテムを作成"""
        left_padding = 16 + (indent_level * 32)
        items = []

        if has_checkbox:
            checkbox = ft.Container(
                content=ft.Container(
                    content=ft.Icon(ft.Icons.CHECK_BOX_OUTLINE_BLANK, size=15, color=colors["primary_main"]),
                    bgcolor="rgba(82,88,228,0.1)",
                    border_radius=2,
                    width=20,
                    height=20,
                    alignment=ft.alignment.center,
                ),
                width=20,
                height=20,
            )
            items.append(checkbox)

        if icon:
            items.append(ft.Icon(icon, size=20, color=colors["primary_main"]))

        items.append(
            ft.Text(
                text,
                size=14,
                color="#222222",
                expand=True,
            )
        )

        if has_expand:
            items.append(ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN, size=20, color=colors["primary_main"]))

        return ft.Container(
            content=ft.Row(items, spacing=4),
            bgcolor="rgba(82,88,228,0.1)" if selected else "transparent",
            padding=ft.padding.only(left=left_padding, right=16, top=2, bottom=2),
            height=40,
        )

    def create_category_title_white(text):
        """白背景用のカテゴリタイトルを作成"""
        return ft.Container(
            content=ft.Text(
                text,
                size=10,
                weight=ft.FontWeight.BOLD,
                color="#6D6D6D",
            ),
            padding=ft.padding.only(left=16, right=8, top=16, bottom=8),
            height=40,
        )

    drawer_open_white = ft.Container(
        content=ft.Column([
            # ヘッダー
            ft.Container(
                content=ft.Row([
                    ft.Text("FDS Fleet Design System®", size=12, weight=ft.FontWeight.BOLD, color=colors["primary_main"]),
                    ft.Icon(ft.Icons.ARROW_BACK, size=16, color=colors["primary_main"]),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=ft.padding.only(left=16, right=16, top=16, bottom=16),
                bgcolor="rgba(82,88,228,0.08)",
                height=48,
            ),
            # コンテンツ
            ft.Container(
                content=ft.Column([
                    create_tree_item_white(ft.Icons.HOME, "ホーム", selected=True),
                    create_category_title_white("プロジェクト管理"),
                    create_tree_item_white(ft.Icons.FOLDER, "4Qキャンペーン", has_expand=True),
                    create_tree_item_white(None, "営業キャンペーン", has_expand=True, indent_level=1),
                    create_tree_item_white(None, "エリア一覧", has_expand=True, indent_level=1),
                    create_tree_item_white(None, "首都圏エリア", indent_level=2),
                    create_tree_item_white(None, "関西エリア", indent_level=2),
                    create_tree_item_white(ft.Icons.FOLDER, "4Q新企画", has_expand=True),
                    create_tree_item_white(ft.Icons.EDIT, "ドラフト", indent_level=1),
                    create_tree_item_white(ft.Icons.ATTACH_FILE, "関連資料", indent_level=1),
                    create_category_title_white("Title"),
                    create_tree_item_white(ft.Icons.DESCRIPTION, "ツリーアイテム", has_expand=True, has_checkbox=True),
                    create_tree_item_white(ft.Icons.DESCRIPTION, "ツリーアイテム", has_expand=True, has_checkbox=True),
                    create_tree_item_white(ft.Icons.DESCRIPTION, "ツリーアイテム", has_expand=True, has_checkbox=True),
                ], spacing=0, scroll=ft.ScrollMode.AUTO),
                expand=True,
                padding=ft.padding.only(top=8, bottom=8),
            ),
            # 区切り線
            ft.Container(bgcolor="rgba(34,34,34,0.08)", height=1),
            # フッター
            ft.Container(
                content=ft.Column([
                    create_category_title_white("管理メニュー"),
                    create_tree_item_white(ft.Icons.GROUP, "グループ設定"),
                    create_tree_item_white(ft.Icons.MANAGE_ACCOUNTS, "アカウント管理", has_expand=True),
                    create_tree_item_white(ft.Icons.ADMIN_PANEL_SETTINGS, "管理者メニュー", has_expand=True),
                    ft.Container(
                        content=ft.Container(
                            content=ft.Row([
                                ft.Container(
                                    content=ft.Icon(ft.Icons.PERSON, size=16, color="#ffffff"),
                                    bgcolor=colors["primary_main"],
                                    border_radius=100,
                                    width=24,
                                    height=24,
                                    alignment=ft.alignment.center,
                                ),
                                ft.Text("User Name", size=16, weight=ft.FontWeight.BOLD, color=colors["primary_main"]),
                            ], spacing=8),
                            border=ft.border.all(1, colors["primary_main"]),
                            border_radius=8,
                            padding=8,
                            height=40,
                        ),
                        padding=ft.padding.only(left=8, right=8, top=16, bottom=10),
                    ),
                ], spacing=0),
                padding=ft.padding.only(bottom=24, top=8),
            ),
        ], spacing=0),
        bgcolor="#FFFFFF",
        width=256,
        height=900,
    )

    # 閉じた状態のDrawer（白背景）
    drawer_closed_white = ft.Container(
        content=ft.Column([
            # ヘッダー
            ft.Container(
                content=ft.Icon(ft.Icons.ARROW_FORWARD, size=16, color=colors["primary_main"]),
                padding=ft.padding.only(left=28, right=28, top=16, bottom=16),
                bgcolor="rgba(82,88,228,0.08)",
                height=48,
            ),
            # アイコンのみのメニュー
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Icon(ft.Icons.HOME, size=20, color=colors["primary_main"]),
                        bgcolor="rgba(82,88,228,0.1)",
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Icon(ft.Icons.FOLDER, size=20, color=colors["primary_main"]),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Icon(ft.Icons.REMOVE, size=20, color=colors["primary_main"]),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                ], spacing=0, scroll=ft.ScrollMode.AUTO),
                expand=True,
                padding=ft.padding.only(top=8, bottom=8),
            ),
            # 区切り線
            ft.Container(bgcolor="rgba(34,34,34,0.08)", height=1),
            # フッター
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Icon(ft.Icons.GROUP, size=20, color=colors["primary_main"]),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.MANAGE_ACCOUNTS, size=20, color=colors["primary_main"]),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS, size=20, color=colors["primary_main"]),
                        padding=8,
                        height=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Container(
                            content=ft.Icon(ft.Icons.PERSON, size=16, color="#ffffff"),
                            bgcolor=colors["primary_main"],
                            border_radius=100,
                            width=32,
                            height=32,
                            alignment=ft.alignment.center,
                        ),
                        padding=ft.padding.only(left=20, right=20, top=16, bottom=10),
                    ),
                ], spacing=0),
                padding=ft.padding.only(bottom=24, top=8),
            ),
        ], spacing=0),
        bgcolor="#FFFFFF",
        border=ft.border.all(1, "rgba(34,34,34,0.08)"),
        width=72,
        height=900,
    )

    # セクションとして返す
    section = ft.Container(
        content=ft.Column([
            section_title("Drawer Component", color=colors["primary_main"]),
            ft.Container(height=10),

            # 色付き背景バージョン
            ft.Text("Colored Background", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Row([
                ft.Column([
                    ft.Text("Open", size=12, color="#666666"),
                    ft.Container(height=5),
                    drawer,
                ], spacing=0),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Closed", size=12, color="#666666"),
                    ft.Container(height=5),
                    drawer_closed_colored,
                ], spacing=0),
            ], spacing=0),

            ft.Container(height=20),

            # 白背景バージョン
            ft.Text("White Background", size=14, weight=ft.FontWeight.BOLD, color="#333333"),
            ft.Container(height=5),
            ft.Row([
                ft.Column([
                    ft.Text("Open", size=12, color="#666666"),
                    ft.Container(height=5),
                    drawer_open_white,
                ], spacing=0),
                ft.Container(width=20),
                ft.Column([
                    ft.Text("Closed", size=12, color="#666666"),
                    ft.Container(height=5),
                    drawer_closed_white,
                ], spacing=0),
            ], spacing=0),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return section
