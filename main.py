"""
メインアプリケーション
CLAUDE.md v1.8 準拠
"""
import flet as ft
from utils.constants import COLORS, SPACING, CORNER_RADIUS
from views import (
    create_datepicker_section,
    create_alert_section,
    create_collapse_section,
    create_interactive_section,
    create_chart_section,
    create_drawer_section,
    create_account_menu_section,
    create_footer_section,
    create_snackbar_section,
    create_switch_section,
    create_list_section,
    create_table_section,
    create_header_section,
    create_pagination_headline_section,
    create_tab_bar_variations_section,
    create_notification_section,
    create_file_upload_section,
    create_timepicker_section,
    create_avatar_badge_section,
    create_global_settings_section,
    create_paper_section,
    create_breadcrumb_section,
    create_pagination_section,
    create_tag_section,
    create_loading_section,
    create_dark_bg_loading_section,
    create_button_sizes_section,
    create_layout_templates_section,
)


def main(page: ft.Page):
    """メインアプリケーション"""
    # ページ設定
    page.title = "Figma UI Components"
    page.padding = 40
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = "#F5F5F5"

    # Figmaデザインシステムのフォント設定
    page.fonts = {
        "Noto Sans JP": "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100;300;400;500;700;900&display=swap"
    }

    # グローバルテーマ設定でデフォルトフォントを指定
    page.theme = ft.Theme(
        font_family="Noto Sans JP"
    )

    # コンテンツ作成
    content = ft.Column(
        [
            # タイトル
            ft.Text(
                "Flet UI Components Gallery",
                size=32,
                weight=ft.FontWeight.BOLD,
                color="#222222",
            ),
            ft.Divider(height=40, color="transparent"),

            # グローバル設定表示セクション
            create_global_settings_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # レイアウトテンプレートセクション
            create_layout_templates_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Paperセクション
            create_paper_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Breadcrumbセクション
            create_breadcrumb_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Paginationセクション（Basic）
            create_pagination_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Tagセクション
            create_tag_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Headerセクション
            create_header_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Pagination Headlineセクション
            create_pagination_headline_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Tab Bar Variationsセクション
            create_tab_bar_variations_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Notificationセクション
            create_notification_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # DatePickerセクション
            create_datepicker_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # File Uploadセクション
            create_file_upload_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # TimePickerセクション
            create_timepicker_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Avatar with Badgeセクション
            create_avatar_badge_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # ボタンサイズバリエーションセクション（全サイズ・全スタイル）
            create_button_sizes_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # インタラクティブボタンセクション（緑→青アニメーション）
            create_interactive_section(page, COLORS, CORNER_RADIUS, SPACING),
            ft.Divider(height=40, color="transparent"),

            # ローディングスピナーセクション
            create_loading_section(COLORS),
            ft.Divider(height=20, color="transparent"),

            # 暗い背景上のローディングボタンセクション
            create_dark_bg_loading_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Drawerセクション
            create_drawer_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # アカウントメニューセクション
            create_account_menu_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # チャートセクション
            create_chart_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # テーブルセクション
            create_table_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # フッターセクション
            create_footer_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Snackbarセクション
            create_snackbar_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # スイッチセクション
            create_switch_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # リストセクション
            create_list_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # アラートセクション
            create_alert_section(COLORS),
            ft.Divider(height=40, color="transparent"),

            # Collapseセクション
            create_collapse_section(COLORS),
        ],
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
    )

    page.add(content)


if __name__ == "__main__":
    ft.app(target=main)
