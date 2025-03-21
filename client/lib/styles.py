from tkinter import ttk

def set_styles(config):
    """
    Defines all the styles for the application
    :param config:
    """

    style = ttk.Style()

    ########################### Frames ############################
    style.configure(
        "Main.TFrame",
        background=config['main_frame']['background_color'],
        borderwidth=config['main_frame']['border_width'],
        relief=config['main_frame']['relief'],
        bordercolor='#000000'
    )

    style.configure(
        "Components.TFrame",
        background=config['components_frame']['background_color'],
        borderwidth=config['components_frame']['border_width'],
        relief=config['components_frame']['relief'],
        bordercolor='#000000'
    )

    style.configure(
        "ReqRep.TFrame",
        background=config['req_rep_frame']['background_color'],
        borderwidth=config['req_rep_frame']['border_width'],
        relief=config['req_rep_frame']['relief'],
        bordercolor='#000000'
    )

    ########################### Labels #############################
    style.configure(
        "Title.TLabel",
        font=(config['title_label']['font'], config['title_label']['font_size'], config['title_label']['font_style']),
        background=config['main_frame']['background_color'],
        foreground=config['title_label']['text_color'],
        anchor=config['title_label']['anchor'],
        justify=config['title_label']['justify']
    )