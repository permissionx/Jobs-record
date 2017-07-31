import datetime 

class Job:
	def __init__(self, jobname, owner, proc, starttime):
		self.jobsname = jobname
		self.owner = owner
		self.proc = int(proc)
		now  = datetime.datetime.now()
		year = now.strftime('%Y-%m-%d %H:%M:%S')[:4]
		mons = {"Jua":'1',"Feb":'2',"Mar":'3',"Apr":'4',"May":'5',"Jun":'6',"Jul":'7',"Aug":'8',"Sep":'9',"Oct":'10',"Nov":'11',"Dec":'12'}
		time_str = year+'-'+mons[starttime[0]]+'-'+starttime[1]+' '+starttime[2]
		self.starttime = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
	def end(self):
		self.endtime = datetime.datetime.now()
		self.upload_to_database()
	def upload_to_database(self):

def read_jobs():
	jobs=[]
	with open('jobs.tmp','r') as file:
		lines = file.readlines()
		for line in lines:
			words = line.split()
			jobs.append_job(words[0], words[1], words[3], words[6:])
	return jobs

def read_showq(pre_jobs):
	jobs = []
	writelines = []
	with open('showq.tmp','r') as file:
		lines = file.readlines()
		for line in lines[3:]:
			if not line:
				break
			writelines.append(line)
			words = line.split()
			job = Job(words[0], words[1], words[3], words[6:])
			jobs.append(job)
	with open('jobs.tmp','w') as file:
		file.writelines(writelines)
	for pre_job in pre_jobs:
		if not pre_job.jobname in [job.jobname for job in jobs]:
			pre_job.end()





			
