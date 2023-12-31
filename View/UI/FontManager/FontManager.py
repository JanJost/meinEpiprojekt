import os

from View.UI.FontManager.IFontManger import IFontManager


class FontManager(IFontManager):
    """
    This class manages fonts and provides paths to various CharisSIL fonts.
    """
    font_path_charisSIL_Bold = None
    font_path_charisSIL_BoldItalic = None
    font_path_charisSIL_Italic = None
    font_path_charisSIL_Regular = None

    def __init__(self):
        """
        Initializes an instance of FontManager and sets the paths to CharisSIL fonts.
        """
        font_folder = os.path.join(os.path.dirname(__file__), 'Fonts')
        self.font_path_charisSIL_Bold = os.path.join(font_folder, 'CharisSIL-Bold.ttf')
        self.font_path_charisSIL_BoldItalic = os.path.join(font_folder, 'CharisSIL-BoldItalic.ttf')
        self.font_path_charisSIL_Italic = os.path.join(font_folder, 'CharisSIL-Italic.ttf')
        self.font_path_charisSIL_Regular = os.path.join(font_folder, 'CharisSIL-Regular.ttf')

    def get_font_path_charissil_bold(self):
        """
        Returns the file path to the CharisSIL Bold font.

        Returns:
            str: File path to the CharisSIL Bold font.
        """
        return self.font_path_charisSIL_Bold

    def get_font_path_charissil_bolditalic(self):
        """
        Returns the file path to the CharisSIL Bold Italic font.

        Returns:
            str: File path to the CharisSIL Bold Italic font.
        """
        return self.font_path_charisSIL_BoldItalic

    def get_font_path_font_charissil_italic(self):
        """
        Returns the file path to the CharisSIL Italic font.

        Returns:
            str: File path to the CharisSIL Italic font.
        """
        return self.font_path_charisSIL_Italic

    def get_font_path_font_path_charissil_regular(self):
        """
        Returns the file path to the CharisSIL Regular font.

        Returns:
            str: File path to the CharisSIL Regular font.
        """
        return self.font_path_charisSIL_Regular
