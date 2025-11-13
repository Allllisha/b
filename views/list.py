"""
List Section - お知らせリストセクション
"""
import flet as ft
from utils.constants import *


def section_title_local(text, color="#5258E4"):
    """ローカルセクションタイトル用のテキストコンポーネント"""
    return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=color)


def create_list_section(colors):
    """お知らせリストセクション（Figmaデザインに基づく）"""

    def create_notification_item(date, tag_label, title, description):
        """お知らせアイテムを作成（ホバー効果付き）"""

        # 日付とタグの行
        date_tag_row = ft.Row([
            ft.Text(
                date,
                size=11,
                color=colors["neutral_light"],
                weight=ft.FontWeight.NORMAL,
            ),
            ft.Container(
                content=ft.Row([
                    ft.Text(
                        tag_label,
                        size=10,
                        color="#686df4",
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(
                        ft.Icons.CLOSE,
                        size=12,
                        color="#686df4",
                    ),
                ], spacing=2),
                bgcolor="#d3d5ff",
                padding=ft.padding.symmetric(horizontal=4, vertical=2),
                border_radius=100,
                height=20,
            ),
        ], spacing=8)

        # タイトル
        title_text = ft.Text(
            title,
            size=12,
            color=colors["neutral_black"],
            weight=ft.FontWeight.NORMAL,
        )

        # 説明文
        description_text = ft.Text(
            description,
            size=10,
            color="#909090",
            weight=ft.FontWeight.NORMAL,
        )

        # コンテンツ列
        content_column = ft.Column([
            date_tag_row,
            title_text,
            description_text,
        ], spacing=4)

        # アイテム全体の行
        item_content = ft.Row([
            # 左側のアイコン
            ft.Container(
                content=ft.Icon(
                    ft.Icons.BUSINESS,
                    size=24,
                    color=colors["neutral_light"],
                ),
                padding=ft.padding.only(left=16, right=0, top=4, bottom=4),
                alignment=ft.alignment.center,
            ),
            # メインコンテンツ
            ft.Container(
                content=content_column,
                expand=True,
            ),
            # 右側の矢印
            ft.Container(
                content=ft.Icon(
                    ft.Icons.KEYBOARD_ARROW_RIGHT,
                    size=24,
                    color=colors["neutral_light"],
                ),
                padding=ft.padding.only(left=0, right=8, top=4, bottom=4),
                alignment=ft.alignment.center,
            ),
        ], spacing=8, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        # ホバー可能なコンテナ
        content_container = ft.Container(
            content=item_content,
            padding=ft.padding.symmetric(vertical=4),
            border_radius=4,
            bgcolor="transparent",
            animate=100,  # アニメーション時間（ミリ秒）
        )

        # ホバーイベントハンドラ
        def on_hover(e):
            if e.data == "true":
                content_container.bgcolor = "#e0e2ff"  # Figmaのホバー色
            else:
                content_container.bgcolor = "transparent"
            content_container.update()

        content_container.on_hover = on_hover

        # アイテムコンテナとディバイダー
        return ft.Column([
            content_container,
            ft.Divider(
                height=1,
                color="rgba(34, 34, 34, 0.1)",
            ),
        ], spacing=4)

    # お知らせリストを作成
    notification_list = ft.Column([
        # タイトル
        ft.Container(
            content=ft.Text(
                "お知らせ",
                size=16,
                color=colors["neutral_black"],
                weight=ft.FontWeight.NORMAL,
            ),
            padding=ft.padding.only(left=16, right=16, top=4, bottom=4),
        ),

        # リストアイテム
        create_notification_item(
            "2023/04/01",
            "Tag Label",
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用",
            "デザインシステムを構築する際にはデザインのガイドラインとともに、UIコンポーネントの実装が必要になります。そのUIコンポーネントをどう実装すれば良いのか？"
        ),
        create_notification_item(
            "2023/04/01",
            "Tag Label",
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用",
            "デザインシステムを構築する際にはデザインのガイドラインとともに、UIコンポーネントの実装が必要になります。そのUIコンポーネントをどう実装すれば良いのか？"
        ),
        create_notification_item(
            "2023/04/01",
            "Tag Label",
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用",
            "デザインシステムを構築する際にはデザインのガイドラインとともに、UIコンポーネントの実装が必要になります。そのUIコンポーネントをどう実装すれば良いのか？"
        ),
        create_notification_item(
            "2023/04/01",
            "Tag Label",
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用",
            "デザインシステムを構築する際にはデザインのガイドラインとともに、UIコンポーネントの実装が必要になります。そのUIコンポーネントをどう実装すれば良いのか？"
        ),
        create_notification_item(
            "2023/04/01",
            "Tag Label",
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用",
            "デザインシステムを構築する際にはデザインのガイドラインとともに、UIコンポーネントの実装が必要になります。そのUIコンポーネントをどう実装すれば良いのか？"
        ),

        # 最後の「お知らせ一覧へ」リンク
        ft.Container(
            content=ft.Row([
                ft.Text(
                    "お知らせ一覧へ",
                    size=11,
                    color=colors["success_main"],
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Icon(
                    ft.Icons.KEYBOARD_ARROW_RIGHT,
                    size=16,
                    color=colors["success_main"],
                ),
            ], spacing=0),
            alignment=ft.alignment.center_right,
            padding=ft.padding.symmetric(horizontal=16, vertical=8),
        ),
    ], spacing=4)

    # シンプルなリストアイテムを作成（List Single用）
    def create_simple_list_item(text):
        """シンプルなテキストのみのリストアイテム"""
        return ft.Column([
            ft.Container(
                content=ft.Text(
                    text,
                    size=12,
                    color="#222222",
                    weight=ft.FontWeight.NORMAL,
                    font_family="Noto Sans JP",
                ),
                padding=ft.padding.symmetric(vertical=4),
            ),
            ft.Divider(
                height=1,
                color="rgba(34, 34, 34, 0.1)",
            ),
        ], spacing=4)

    # List Single（シンプル版）
    list_single = ft.Column([
        # タイトル
        ft.Container(
            content=ft.Text(
                "お知らせ",
                size=16,
                color="#222222",
                weight=ft.FontWeight.NORMAL,
                font_family="Noto Sans JP",
            ),
            padding=ft.padding.only(top=4, bottom=4),
        ),

        # リストアイテム
        create_simple_list_item(
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用"
        ),
        create_simple_list_item(
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用"
        ),
        create_simple_list_item(
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用"
        ),
        create_simple_list_item(
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用"
        ),
        create_simple_list_item(
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用"
        ),
        create_simple_list_item(
            "【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用【デザインシステムのUIコンポーネント実装テクニック】セレクトボックスのデザイン適用"
        ),
    ], spacing=4)

    # セクション全体を構築
    list_section = ft.Container(
        content=ft.Column([
            section_title_local("List - お知らせ (Figma)", color=colors["primary_main"]),
            ft.Container(height=20),

            # 複雑なリスト（既存）
            ft.Text("複雑なリスト", size=14, weight=ft.FontWeight.BOLD, color="#666666"),
            ft.Container(height=10),
            ft.Container(
                content=notification_list,
                bgcolor="#FFFFFF",
                border_radius=8,
                border=ft.border.all(1, "#E0E0E0"),
            ),

            ft.Container(height=30),

            # List Single（シンプル版）
            ft.Text("List Single", size=14, weight=ft.FontWeight.BOLD, color="#666666"),
            ft.Container(height=10),
            ft.Container(
                content=list_single,
                bgcolor="#FFFFFF",
                border_radius=8,
                border=ft.border.all(1, "#E0E0E0"),
                padding=ft.padding.symmetric(horizontal=16, vertical=8),
            ),
        ], spacing=0),
        bgcolor="#FFFFFF",
        padding=30,
        border_radius=12,
    )

    return list_section
