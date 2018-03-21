from locust import HttpLocust, TaskSet, task

class UserLogin(TaskSet):
	@task(1)
	def get_index(self):
		self.client.get('/')

class IslUser(HttpLocust):
	task_set = UserLogin
	min_wait = 5000
	max_wait = 15000