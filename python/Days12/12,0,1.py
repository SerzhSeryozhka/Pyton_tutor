# def print_in_box(text, width, height):
#     if len(text) > width - 2:
#         text = text[:width - 2]
#     else:
#         text = text + " " * (width - 2 - len(text))
#     horizontal_border = "#" * width
#     vertical_border = "#" + " " * (width - 2) + "#"
#     top_padding = (height - 3) // 2
#     bottom_padding = height - 3 - top_padding
#     print(horizontal_border)
#     for i in range(top_padding):
#         print(vertical_border)
#     print("#" + " " * ((width - 2 - len(text)) // 2) + text + " " * ((width - 2 - len(text) + 1) // 2) + "#")
#     for i in range(bottom_padding):
#         print(vertical_border)
#     print(horizontal_border)
# print_in_box("Hello", 4,3)
def print_in_box(text, width, height):
    if len(text) > width - 2:
        text_lines = []
        split_text = text.split()
        current_line = ""
        for word in split_text:
            if len(current_line) + len(word) + 1 < width - 2:
                if current_line == "":
                    current_line = word
                else:
                    current_line += " " + word
            else:
                text_lines.append(current_line)
                current_line = word
        text_lines.append(current_line)
        
        if len(text_lines) > height - 2:
            print("Текст не помещается в рамки")
            return
        
        top_padding = (height - 3 - len(text_lines)) // 2
        bottom_padding = height - 3 - len(text_lines) - top_padding
        horizontal_border = "#" * width
        vertical_border = "#" + " " * (width - 2) + "#"
        
        print(horizontal_border)
        for i in range(top_padding):
            print(vertical_border)
        for line in text_lines:
            line = line + " " * (width - 2 - len(line))
            print("#" + " " * ((width - 2 - len(line)) // 2) + line + " " * ((width - 2 - len(line) + 1) // 2) + "#")
        for i in range(bottom_padding):
            print(vertical_border)
        print(horizontal_border)
    else:
        text = text + " " * (width - 2 - (len(text)*2))
        horizontal_border = "#" * width
        vertical_border = "#" + " " * (width - 2) + "#"
        top_padding = (height - 3) // 2
        bottom_padding = height - 3 - top_padding
        print(horizontal_border)
        for i in range(top_padding):
            print(vertical_border)
        print("#" + " " * ((width - 2 - len(text)) // 2) + text + " " * ((width - 2 - len(text) + 1) // 2) + "#")
        for i in range(bottom_padding):
            print(vertical_border)
        print(horizontal_border)

# Пример использования:
print_in_box("Hello, World!This is a long text that needs to be wrapped onto multiple lines" , 25, 10) 
