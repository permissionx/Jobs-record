import datetime 
import pymysql
import os


class Job:

	def __init__(self, jobname, owner, proc, starttime):
		self.jobname = jobname
		self.owner = owner
		self.proc = int(proc)
		now  = datetime.datetime.now()
		year = now.strftime('%Y-%m-%d %H:%M:%S')[:4]
		mons = {"Jua":'1',"Feb":'2',"Mar":'3',"Apr":'4',"May":'5',"Jun":'6',"Jul":'7',"Aug":'8',"Sep":'9',"Oct":'10',"Nov":'11',"Dec":'12'}
		time_str = year+'-'+mons[starttime[0]]+'-'+starttime[1]+' '+starttime[2]
		self.starttime = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

	def end(self, endtime):
		self.endtime = endtime
		self.deltatime = self.endtime - self.starttime
		self.upload_to_database()

	def get_date_seconds(self):
		date_seconds = []
		if not (self.starttime.day, self.starttime.month, self.starttime.year) == (self.endtime.day, self.endtime.month, self.endtime.year): 
			start_day_next = self.starttime+datetime.timedelta(1,0,0)
			start_day_end = datetime.datetime(start_day_next.year, start_day_next.month, start_day_next.day, 0, 0, 0, 0)
			first_day_time = (start_day_end - self.starttime) * self.proc
			end_day_start =  datetime.datetime(self.endtime.year, self.endtime.month, self.endtime.day, 0, 0, 0, 0)
			last_day_time = (self.endtime - end_day_start) * self.proc
			inter_day = start_day_end
			date_seconds.append((self.starttime, first_day_time)) 
			while inter_day < end_day_start :
				date_seconds.append((inter_day, datetime.timedelta(1,0,0) * self.proc)) 
				inter_day += datetime.timedelta(1,0,0)
			date_seconds.append((self.endtime, last_day_time)) 
		else:
			date_seconds.append((self.starttime, self.deltatime * self.proc ))
		self.date_seconds = date_seconds

	def upload_to_database(self):
		self.get_date_seconds()
		upload(self.owner, self.date_seconds)


def upload(owner, date_seconds):
	db = pymysql.connect(host = "localhost", port = 8701, user = "root", db = 'job_record' )
	cursor = db.cursor()
	for a_data in date_seconds:
		sql = 'insert into jobs(day) select \'{0}\' from dual where not exists (select day from jobs where day =  \'{0}\')'.format(str(a_data[0].date()))
		cursor.execute(sql)
		sql = 'update jobs set {0}={0}+{1} where day=\'{2}\''.format(owner, a_data[1].total_seconds(), str(a_data[0].date()))
		cursor.execute(sql)
	db.commit()
	db.close()


def read_pre_jobs():
	jobs=[]
	with open('pre-jobs.tmp','r') as file:
		lines = file.readlines()
		for line in lines:
			words = line.split()
			if words[0] != 'TIME:':
				jobs.append(Job(words[0], words[1], words[3], words[6:]))
			else:
				time = datetime.datetime.strptime(line[6:-1],'%Y-%m-%d %H:%M:%S')
	return (jobs, time)


def read_showq():
	jobs = []
	writelines = []
	with open('showq.tmp','r') as file:
		lines = file.readlines()
		for line in lines[3:]:
			if len(line) < 2:
				break
			writelines.append(line)
			words = line.split()
			job = Job(words[0], words[1], words[3], words[6:])
			jobs.append(job)
	with open('pre-jobs.tmp','w') as file:
		file.writelines(writelines)
		nowstr = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
		file.write('TIME: '+nowstr+'\n')
	return jobs


def main():
	(pre_jobs, pre_time) = read_pre_jobs()
	jobs = read_showq()
	for pre_job in pre_jobs:
		if not pre_job.jobname in [job.jobname for job in jobs]:
			pre_job.end(pre_time)

if __name__ == '__main__':
	main()



			
