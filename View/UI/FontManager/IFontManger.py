from abc import ABC, abstractmethod


class IFontManager(ABC):
    @abstractmethod
    def get_font_path_charissil_bold(self):
        pass

    @abstractmethod
    def get_font_path_charissil_bolditalic(self):
        pass

    @abstractmethod
    def get_font_path_font_charissil_italic(self):
        pass

    @abstractmethod
    def get_font_path_font_path_charissil_regular(self):
        pass




