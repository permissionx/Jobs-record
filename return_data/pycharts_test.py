with open('out.data','r') as file:
	lines = file.readlines()
words = lines[0].split()
user = words[1:]
date = []
data = []
for line,x in zip(lines[1:],range(len(lines[1:]))):
	words = line.split()
	date.append(words[0])
	seconds = [float(word) for word in words[1:]]
	data_line = [[x,y,int(height)] for y,height in zip(range(len(seconds)),seconds)]
	data += data_line #[date, user, time]


from pyecharts import Bar3D
bar3d = Bar3D("Job Accounting", width=1200, height=1200)        
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", user, date, [[d[1], d[0], d[2]] for d in data],yaxis_name='user', is_visualmap=True,
          visual_range=[0, 10000000], visual_range_color=range_color, grid3D_width=100, grid3D_depth=200)
bar3d.show_config()
bar3d.render()