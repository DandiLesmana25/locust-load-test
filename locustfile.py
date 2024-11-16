from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def load_test(self):
        self.client.get("/")