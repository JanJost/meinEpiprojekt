class TextWrapper:
    """
    The TextWrapper class provides a utility for breaking text into lines with automatic word wrapping.
    It takes a text string, a font, and a maximum width as input and returns a list of wrapped lines.

    Each element in the 'wrapped_lines' list represents a line of text that fits within the specified width.
    """

    def wrap_text(self, text, font, max_width):
        """
        Wrap the given 'text' into lines based on the provided 'font' and 'max_width'.

        Args:
            text (str): The input text to be wrapped.
            font (pygame.font.Font): The font used for rendering the text.
            max_width (int): The maximum width for each line.

        Returns:
            list of str: A list of wrapped lines.
        """
        paragraphs = text.split('\n')
        lines = []
        for paragraph in paragraphs:
            words = paragraph.split()
            current_line = ""
            for word in words:
                test_line = current_line + word + " "
                test_rect = font.get_rect(test_line)
                if test_rect.width <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word + " "
            lines.append(current_line)
            # Add an empty line after each paragraph
            lines.append("")
        # Remove the last empty line added after the last paragraph
        if lines[-1] == "":
            lines.pop()
        return lines
