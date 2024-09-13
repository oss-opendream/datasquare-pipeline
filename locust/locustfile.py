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

    data = '{"key": "value"}'  # Example data payload
    header = {'access-token': 'your_token_here'}  # Example header

    @task
    def view_get(self):
        path = "/data_request/view"
        params = {'issue_id': 5}
        self.client.get(path, data=params, headers=self.header)

    @task
    def data_request_view(self):
        path = "/data_request/view"
        params = {'issue_id': 2}
        self.client.get(path, data=self.data, params=params, headers=self.header)

    @task
    def feed(self):
        path = "/feed"
        self.client.get(path, data=self.data, headers=self.header)

    @task
    def publish(self):
        path = "/data_request/publish"
        self.client.get(path, data=self.data, headers=self.header)
        

class MyLoadTest(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(1, 2)
