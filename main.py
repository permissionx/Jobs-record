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
		self.deltatime = self.endtime - self.starttime
		self.upload_to_database()

	def get_date_seconds(self):
		date_seconds = dict()
		if not (self.starttime.day, self.starttime.month, self.starttime.year) == (self.endtime.day, self.endtime.month, self.endtime.year): 
			start_day_next = self.starttime+datetime.timedelta(1,0,0)
			start_day_end = datetime.datetime(start_day_next.year, start_day_next.month, start_day_next.day, 0, 0, 0, 0)
			first_day_time = (start_dat_end - self.starttime) * self.proc
			date_seconds[self.starttime] = first_day_time
			end_day_start =  datetime.datetime(end_day_next.year, end_day_next.month, end_day_next.day, 0, 0, 0, 0)
			last_day_time = (self.endtime - end_day_start) * self.proc
			date_seconds[self.endtime] = last_day_time
			inter_day = start_dat_end
			while inter_day < end_day_start :
				date_seconds[inter_day] = datetime.timedelta(1,0,0) * self.proc
				inter_day += datetime.timedelta(1,0,0)
		else:
			date_seconds[self.starttime] = self.deltatime * self.proc
		return date_seconds







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





			
