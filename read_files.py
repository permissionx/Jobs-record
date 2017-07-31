import datetime 

class Job:
	def __init__(self, jobname, proc, starttime):
		self.jobsname = jobname
		self.proc = int(proc)
		now  = datetime.datetime.now()
		year = now.strftime('%Y-%m-%d %H:%M:%S')[:4]
		mons = {"Jua":'1',"Feb":'2',"Mar":'3',"Apr":'4',"May":'5',"Jun":'6',"Jul":'7',"Aug":'8',"Sep":'9',"Oct":'10',"Nov":'11',"Dec":'12'}
		time_str = year+'-'+mons[starttime[0]]+'-'+starttime[1]+' '+starttime[2]
		self.starttime = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
	def compute_dtime(self):
		now  = datetime.datetime.now()
		self.dtime = now - self.starttime


class User:
	def __init__(self, name):
		self.name = name
		self.jobs = []
	def append_job(self, jobname, proc, starttime):
		job = Job(jobname, proc, starttime)
		self.jobs.append(job)


def read_tasks():
	users = {}
	with open('jobs.tmp','r') as file:
		lines = file.readlines()
		for line in lines:
			words = line.split()
			name = words[1]
			if not name in users.keys():
				users[name] = User(name)
			users[name].append_job(words[0], words[3], words[6:])
	return users

def read_showq(users):
	jobs = []
	writelines = []
	with open('showq.tmp','r') as file:
		lines = file.readlines()
		for line in lines[3:]:
			if not line:
				break
			writelines.append(line)
			words = line.split()
			job = Job(words[0], words[3], words[6:])
			jobs.append(job)
	with open('jobs.tmp','w') as file:
		file.writelines(writelines)
	for username, user in users.item():
		for job in user.jobs:
			if not job in jobs:
				job.compute_dtime()
				job.upload_to_database(username)




			
