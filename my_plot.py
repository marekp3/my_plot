import PySimpleGUI as sg

class PSG_plot:
    def __init__(self, size, bottom_left, top_right, bsg_color, key):
        self.size = size
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.bsg_color = bsg_color
        self.key = key
        self.graph = sg.Graph(canvas_size = self.size, graph_bottom_left = self.bottom_left, graph_top_right = self.top_right, background_color = self.bsg_color,key = self.key)
    def draw_axis(self):
        dist_y = 25
        dist_x = 25
        tick_space = 20
        tick_size = 3
        self.graph.draw_line((dist_x,dist_y),(self.size[0]-dist_y,dist_y),color='black', width=2)
        self.graph.draw_line((dist_x,dist_y),(dist_x,self.size[1]-dist_y),color='black', width=2)
        for i in range(dist_x + tick_space,self.size[0] - dist_x,20):
            self.graph.draw_line((i,dist_y-tick_size),(i,dist_y+tick_size),color='black', width=1)
        for i in range(dist_y + tick_space,self.size[1] - dist_y,20):
            self.graph.draw_line((dist_x-tick_size,i),(dist_x+tick_size,i),color='black', width=1)
            
    def draw_axis_desc(self):
        self.graph.draw_text('current [mA]',(self.size[0]-60, 10), color='black', angle=0)
        self.graph.draw_text('voltage [V]',(10, self.size[1]-60), color='black', angle = 90)
                

my_plot = PSG_plot((600,400),(0,0),(600,400),'white','graph')

graph = my_plot.graph
layer = [[graph]]
window = sg.Window('hej',layer,finalize = True)
my_plot.draw_axis()
my_plot.draw_axis_desc()
while True:
    values, event = window.read(timeout=0.1)
    if event == sg.WIN_CLOSED:
        break
window.close()
