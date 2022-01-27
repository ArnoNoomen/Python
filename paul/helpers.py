windows = """
WindowManager:
    Login:
    Info:
    Articlelist:
    Dock:
    Article:
"""
paul = """
FloatLayout:
    MDCard:
        id: card
        size_hint: None, None
        size: 300, 450
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 65
        spacing: 35
        orientation: 'vertical'
"""
toolbar_demo = """
MDToolbar:
    id: toolbar_demo
    title: 'Demo Application'
    left_action_items: [["menu", lambda x: app.root.navigation_draw()]]
    # left_action_items: [['menu', lambda x: app.root.nav_drawer.toggle_nav_drawer()]]
    pos_hint: {'top': 1}
    elevation:5
"""
usericon = """
MDIcon:
    icon: 'account'
    icon_color: 0 ,0 ,0 ,0
    halign: 'center'
    pos_hint:{'center_x': 0.5, 'center_y': 0.7}
    font_size: 180
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
    size_hint: 0.9 , 0.1
    width: 200
    height: 28
    font_size: 32
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
    size_hint: 0.9 , 0.1
    width: 200
    height: 36
    password: True
    font_size: 32  
"""
dock_input = """
MDTextField:
    hint_text: "Enter dock"
    helper_text: "or click on forgot dock"
    helper_text_mode: "on_focus"
    icon_right: "dock-window"
    icon_right_color: app.theme_cls.primary_color
    # pos_hint:{'center_x': 0.5, 'center_y': 0.05 }
    pos_hint:{'top': 1}
    size_hint: 0.9 , 0.1
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
    size_hint: 0.9 , 0.1
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
    pos_hint:{'center_x': 0.5, 'center_y': 0.8}
    
    size_hint: 0.9 , 0.1
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
box = """
BoxLayout:
    id: box
    orientation: 'vertical'
    pos_hint: { 'bottom': 1, 'left': 1}
"""
button_ok = """
MDFillRoundFlatButton:
    icon: "Ok"
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
