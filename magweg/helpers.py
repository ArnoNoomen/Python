windows = """
WindowManager:
    Login:
    Info:
    Articlelist:
    Dock:
    Article:
"""
paul = """
MDNavigationDrawer:
    id: nav_drawer
"""
toolbar_demo = """
MDToolbar:
    id: toolbar_demo
    title: 'Demo Application'
    left_action_items: [["menu", lambda x: app.root.navigation_draw()]]
    pos_hint: {'top': 1}
    elevation:5
"""
username_input = """
MDTextField:
    id: username
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "account"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width: 500
    font_size: 48
"""
password_input = """
MDTextField:
    id: password
    icon_left: "key-variant"
    hint_text: "Password"
    helper_text: "or click on forgot password"
    helper_text_mode: "on_focus"
    icon_right: "form-textbox-password"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.4}
    size_hint_x: None
    width: 200
    password: True
    font_size: 24  
"""
dock_input = """
MDTextField:
    hint_text: "Enter dock"
    helper_text: "or click on forgot dock"
    helper_text_mode: "on_focus"
    icon_right: "dock-window"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.4}
    size_hint_x:None
    width: 200
    font_size: 24  
"""
article_input = """
MDTextField:
    hint_text: "Enter article"
    helper_text: "or click on forgot article"
    helper_text_mode: "on_focus"
    icon_right: "amazon"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width: 200
    font_size: 24  
"""
receive_input = """
MDTextField:
    hint_text: "Enter receive number"
    helper_text: "or click on forgot receive"
    helper_text_mode: "on_focus"
    icon_right: "receipt"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    width: 200
    font_size: 24  
"""
button_icon = """
MDIconButton:
    icon: "language-python"
    orientation: "horizontal"
    icon_size: "128sp"
    pos_hint: { 'bottom': 1, 'left': 1}
"""
button_ok = """
MDFillRoundFlatButton:
    icon: "page-next"
    text: "Ok" 
    orientation: 'horizontal'
    pos_hint: { 'bottom': 1, 'left': 1}
    size_hint: ( 0.35 , 0.10)    
"""
button_cancel = """ 
MDFillRoundFlatButton:
    icon: "cancel"
    text: "Cancel" 
    orientation: 'horizontal'
    pos_hint: { 'bottom': 1, 'right': 1}
    size_hint: ( 0.35 , 0.10)    
"""
KV = """
<Content>
    adaptive_height: True

    TwoLineIconListItem:
        text: "(050)-123-45-67"
        secondary_text: "Mobile"

        IconLeftWidget:
            icon: 'phone'


ScrollView:

    MDGridLayout:
        id: box
        cols: 1
        adaptive_height: False
        height: 50
"""