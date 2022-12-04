import cv2
import pydantic, typing


class Point(pydantic.BaseModel):
    x: int
    y: int


class ClickAndSetPoint:
    points: typing.List[Point] = []
    font = cv2.FONT_HERSHEY_SIMPLEX
    look_for_points_in_radius = 7

    def tk_on_delete_key_press(self, event):
        if event.char == 'c':
            self.points.clear()
        

    def tk_mouse_callback(self, event):
        new_point = Point(x=event.x, y=event.y)
        if new_point not in self.points:
            self.points.append(new_point)

    def draw_all_points(self, img):
        id = 0
        while id < len(self.points):
            p = self.points[id]
            # cv2.putText(img, 'Point ' + str(id) + ': ' + str(p.x) + ', ' + str(p.y), (p.x, p.y), self.font, 0.5 , (255,0,0), 2 )
            cv2.rectangle(img, (p.x - 3,p.y - 3), (p.x + 3,p.y + 3), (255,0,0), 1)
            id += 1


    def get_points(self):
        return self.points
