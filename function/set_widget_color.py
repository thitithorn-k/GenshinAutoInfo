bg_color = '#111133'
fg_color = '#eeeeee'
top_header_color = '#111155'


def set_color(obj, fg=True):
    obj['bg'] = bg_color
    if fg:
        obj['fg'] = fg_color
    obj['highlightthickness'] = 0
    if hasattr(obj, 'activebackground'):
        obj['activebackground'] = bg_color
        obj['activeforeground'] = fg_color
    if hasattr(obj, 'highlightcolor'):
        obj['highlightcolor'] = bg_color