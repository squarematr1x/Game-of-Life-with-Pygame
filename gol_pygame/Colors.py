class Colors:

    def __init__(self):
        self.color_state = 0

        self.color0 = (90, 150, 30)
        self.color1 = (0, 50, 0)
        self.color2 = (0, 100, 0)
        self.color3 = (0, 150, 0)
        self.color4 = (75, 150, 0)

    def change_colors(self):
        self.color_state += 1

        if self.color_state == 0:
            self.set_to_green()
        elif self.color_state == 1:
            self.set_to_blue()
        elif self.color_state == 2:
            self.set_to_red()

        if self.color_state >= 2:
            self.color_state = -1

    def set_to_green(self):
        self.color0 = (90, 150, 30)
        self.color1 = (0, 50, 0)
        self.color2 = (0, 100, 0)
        self.color3 = (0, 150, 0)
        self.color4 = (75, 150, 0)

    def set_to_blue(self):
        self.color0 = (50, 50, 170)
        self.color1 = (20, 40, 90)
        self.color2 = (10, 50, 110)
        self.color3 = (0, 50, 150)
        self.color4 = (75, 70, 230)

    def set_to_red(self):
        self.color0 = (150, 30, 30)
        self.color1 = (100, 10, 20)
        self.color2 = (120, 50, 10)
        self.color3 = (190, 50, 40)
        self.color4 = (210, 20, 30)

    def get_colors(self):
        colors = [self.color0, self.color1, self.color2, self.color3, self.color4]
        return colors
