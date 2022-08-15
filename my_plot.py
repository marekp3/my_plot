import PySimpleGUI as sg

class PSG_plot:
    def __init__(self, size, bottom_left, top_right, bsg_color, key, plot_type):
        self.size = size
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.bsg_color = bsg_color
        self.key = key
        self.plot_type = plot_type
        self.max_x = 0
        self.max_y = 0
        self.min_y = 0
        self.max_y = 0
        self.delta_x_ticks = 0
        self.delta_y_ticks = 0
        self.graph = sg.Graph(canvas_size = self.size, graph_bottom_left = self.bottom_left, graph_top_right = self.top_right, background_color = self.bsg_color,key = self.key)
        self.buffer = [[],[]]
    def draw_axis(self, min_x, max_x,min_y, max_y, tick_x, tick_y):
        distance = 20
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y
        resolution_px = (self.size[0] - 2*distance)/self.max_x
        resolution_py = (self.size[1] - 2*distance)/self.max_y
        self.graph.draw_line([distance,distance],[self.size[0]-distance,distance])
        self.graph.draw_line([distance,distance],[distance, self.size[1]-distance])
        for i in range(int(max_x/tick_x)):
            print(int(resolution_px*tick_x*i))
            self.graph.draw_line([int(resolution_px*tick_x*i)+ distance,distance+10], [int(resolution_px*tick_x*i) + distance,distance-10])
        for i in range(int(max_y/tick_y)):
            self.graph.draw_line([distance-10, int(resolution_py*tick_y*i)], [distance+10, int(resolution_py*tick_y*i)])
        print(resolution_px)
        pass        
    def draw_axis_desc(self):
        self.graph.draw_text('current [mA]',(self.size[0]-60, 10), color='black', angle=0)
        self.graph.draw_text('voltage [V]',(10, self.size[1]-60), color='black', angle = 90)
                

my_plot = PSG_plot((1000,700),(0,0),(1000,700),'white','graph','simple_plot')

graph = my_plot.graph
layer = [[graph]]
window = sg.Window('hej',layer,finalize = True)
my_plot.draw_axis(0,1,0,10,0.1,1)
#my_plot.draw_axis_desc()
while True:
    values, event = window.read(timeout=0.1)
    if event == sg.WIN_CLOSED:
        break
window.close()
