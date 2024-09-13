from locust import HttpUser, task, between, TaskSet


class MyTaskSet(TaskSet):
    @task
    def test_400(self):
        self.client.get("/status/400")

    @task
    def test_404(self):
        self.client.get("/status/404")

    @task
    def test_422(self):
        self.client.get("/status/422")

    @task
    def test_500(self):
        self.client.get("/status/500")

    @task
    def test_200(self):
        self.client.get("/status/200")

    @task
    def data_request_view(self):
        self.client.get("/data_request/view")



class MyLoadTest(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(1, 2)

    