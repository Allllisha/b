"""
共通定数定義
Figmaデザイントークンと共通設定を一元管理
"""
import flet as ft

# Figmaから取得したデザイントークン
COLORS = {
    # Success (緑系)
    "success_main": "#007a4d",

    # Primary (青系)
    "primary_main": "#5258e4",
    "primary_hovered": "#4046ca",
    "primary_selected": "#3236a8",

    # Danger (赤系)
    "danger_main": "#d31510",
    "danger_hovered": "#b40000",
    "danger_selected": "#930000",
    "danger_hovered_fade": "#ffddd6",
    "danger_selected_fade": "#ffcdc3",

    # Neutral
    "neutral_white": "#ffffff",
    "neutral_disabled_bg": "#e6e6e6",
    "neutral_disabled": "#b1b1b1",
    "neutral_light": "#6d6d6d",
    "neutral_black": "#000000",

    # White opacity variants
    "white_opacity_80": "rgba(255, 255, 255, 0.8)",
    "white_opacity_50": "rgba(255, 255, 255, 0.5)",
    "white_opacity_25": "rgba(255, 255, 255, 0.25)",
}

# デザイントークン
SPACING = 12  # spacing/60
BORDER_WIDTH = 1  # border/100
CORNER_RADIUS = 8  # corner-rounding/regular

# Figmaから取得したElevation（ドロップシャドウ）設定
# 非常に明るく薄いグレー、色味を抑えた控えめなシャドウ
ELEVATIONS = {
    "level_0": None,  # シャドウなし
    "level_1": ft.BoxShadow(
        spread_radius=0,
        blur_radius=4,
        color="rgba(230, 230, 235, 0.04)",
        offset=ft.Offset(0, 1),
    ),
    "level_2": ft.BoxShadow(
        spread_radius=0,
        blur_radius=6,
        color="rgba(230, 230, 235, 0.05)",
        offset=ft.Offset(0, 2),
    ),
    "level_3": ft.BoxShadow(
        spread_radius=0,
        blur_radius=10,
        color="rgba(230, 230, 235, 0.06)",
        offset=ft.Offset(0, 3),
    ),
    "level_4": ft.BoxShadow(
        spread_radius=1,
        blur_radius=14,
        color="rgba(230, 230, 235, 0.07)",
        offset=ft.Offset(0, 4),
    ),
    "level_5": ft.BoxShadow(
        spread_radius=2,
        blur_radius=18,
        color="rgba(230, 230, 235, 0.08)",
        offset=ft.Offset(0, 6),
    ),
}

# Figmaから取得したMaterial Design Iconsマッピング
ICONS = {
    "warning": ft.Icons.WARNING,
    "close": ft.Icons.CLOSE,
    "info": ft.Icons.INFO,
    "help": ft.Icons.HELP,
    "keyboard_arrow_down": ft.Icons.KEYBOARD_ARROW_DOWN,
    "keyboard_arrow_up": ft.Icons.KEYBOARD_ARROW_UP,
    "person": ft.Icons.PERSON,
    "keyboard_arrow_left": ft.Icons.KEYBOARD_ARROW_LEFT,
    "delete": ft.Icons.DELETE,
    "keyboard_arrow_right": ft.Icons.KEYBOARD_ARROW_RIGHT,
    "add": ft.Icons.ADD,
    "more_horiz": ft.Icons.MORE_HORIZ,
    "fullscreen": ft.Icons.FULLSCREEN,
    "settings": ft.Icons.SETTINGS,
    "trending_up": ft.Icons.TRENDING_UP,
    "trending_down": ft.Icons.TRENDING_DOWN,
    "calendar_today": ft.Icons.CALENDAR_TODAY,
    "arrow_back_ios_new": ft.Icons.ARROW_BACK_IOS_NEW,
    "arrow_forward_ios": ft.Icons.ARROW_FORWARD_IOS,
    "error": ft.Icons.ERROR,
    "arrow_back": ft.Icons.ARROW_BACK,
    "home": ft.Icons.HOME,
    "cases": ft.Icons.CASES,
    "edit": ft.Icons.EDIT,
    "attach_file": ft.Icons.ATTACH_FILE,
    "folder_open": ft.Icons.FOLDER_OPEN,
    "group": ft.Icons.GROUP,
    "manage_accounts": ft.Icons.MANAGE_ACCOUNTS,
    "admin_panel_settings": ft.Icons.ADMIN_PANEL_SETTINGS,
    "minimize": ft.Icons.MINIMIZE,
    "drag_indicator": ft.Icons.DRAG_INDICATOR,
    "arrow_drop_down": ft.Icons.ARROW_DROP_DOWN,
    "attachment": ft.Icons.ATTACHMENT,
    "help_outline": ft.Icons.HELP_OUTLINE,
    "menu": ft.Icons.MENU,
    "notifications": ft.Icons.NOTIFICATIONS,
    "file_copy": ft.Icons.FILE_COPY,
    "link": ft.Icons.LINK,
    "key": ft.Icons.KEY,
    "comment": ft.Icons.COMMENT,
    "apps": ft.Icons.APPS,
    "check_box": ft.Icons.CHECK_BOX,
    "star": ft.Icons.STAR,
    "star_border": ft.Icons.STAR_BORDER,
    "check_box_outline_blank": ft.Icons.CHECK_BOX_OUTLINE_BLANK,
    "indeterminate_check_box": ft.Icons.INDETERMINATE_CHECK_BOX,
    "search": ft.Icons.SEARCH,
    "image": ft.Icons.IMAGE,
    "lock": ft.Icons.LOCK,
    "visibility_off": ft.Icons.VISIBILITY_OFF,
    "visibility": ft.Icons.VISIBILITY,
    "download": ft.Icons.DOWNLOAD,
    "account_circle": ft.Icons.ACCOUNT_CIRCLE,
    "business": ft.Icons.BUSINESS,
    "textsms": ft.Icons.TEXTSMS,
    "cancel": ft.Icons.CANCEL,
    "check_circle": ft.Icons.CHECK_CIRCLE,
    "first_page": ft.Icons.FIRST_PAGE,
    "last_page": ft.Icons.LAST_PAGE,
    "radio_button_checked": ft.Icons.RADIO_BUTTON_CHECKED,
    "radio_button_unchecked": ft.Icons.RADIO_BUTTON_UNCHECKED,
    "filter_alt": ft.Icons.FILTER_ALT,
    "unfold_more": ft.Icons.UNFOLD_MORE,
    "remove": ft.Icons.REMOVE,
    "shortcut": ft.Icons.SHORTCUT,
    "print": ft.Icons.PRINT,
    "upload": ft.Icons.UPLOAD,
    "article": ft.Icons.ARTICLE,
    "add_circle_outline": ft.Icons.ADD_CIRCLE_OUTLINE,
    "access_time": ft.Icons.ACCESS_TIME,
    "circle": ft.Icons.CIRCLE,
}

# Figmaから取得したロゴ画像URL（7日間有効）
LOGO_IMAGES = {
    "group_main": "https://www.figma.com/api/mcp/asset/765384b0-2346-4bd9-83da-0a8aeb1049e9",
    "group_icon": "https://www.figma.com/api/mcp/asset/02375cb1-286e-4a26-a98d-0747d1af6fd6",
    "vector_accent": "https://www.figma.com/api/mcp/asset/a756fb10-ad26-44ed-8c54-96c188d25a8e",
}

# ロゴテキスト設定
LOGO_TEXT = "FDS Fixel Design System®"
LOGO_PLACEHOLDER = "Logo"

# Figmaから取得したリンクスタイル設定
LINK_STYLES = {
    "color": "#007a4d",  # Success main color
    "font_size": 12,
    "text_decoration": "underline",
    "line_height": 1.5,
}

# Figmaから取得したDivider（区切り線）の色設定
DIVIDER_COLORS = {
    "primary": "rgba(126, 132, 252, 0.16)",  # Primary color 16% opacity
    "neutral": "rgba(34, 34, 34, 0.16)",     # Neutral black 16% opacity
    "on_colored": "rgba(255, 255, 255, 0.16)",  # Static white 16% opacity (for colored backgrounds)
}
