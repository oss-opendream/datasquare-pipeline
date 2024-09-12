from locust import HttpUser, task, between

class WebsiteUser(HttpUser):

    wait_time = between(3, 7)  # Random wait time between 3 and 7 seconds
    data = '{"key": "value"}'  # Example data payload
    header = {'access-token': 'your_token_here'}  # Example header

    def on_start(self):
        print("Test Start")
        
    def on_stop(self):
        print("Test End")

    @task
    def code_500(self):
        path = "/data_request/view"
        params = {'issue_id': 5}
        self.client.get(path, data=self.data,params=params,  headers=self.header)
    
    @task
    def data_request_200(self):
        path = "/data_request/view"
        params = {'issue_id': 2}
        self.client.get(path, data=self.data,params=params,  headers=self.header)

    @task
    def feed(self):
        path = "/feed"
        self.client.get(path, data=self.data, headers=self.header)

    @task
    def publish(self):
        path = "/data_request/publish"
        self.client.get(path, data=self.data, headers=self.header)
    



    # @task(2)
    # def query_test(self):
    #     path = "/feed"  # Example path
    #     # params = {'total_count': 100}  # Example parameter
    #     self.client.post(path, data=self.data, headers=self.header)
    #     # self.client.post(path, data=self.data, params=params, headers=self.header)

    # @task
    # def total_count_test(self):
    #     path = "/signin"  # Example path
    #     self.client.post(path, data=self.data, headers=self.header)

    # @task
    # def total_count_test2(self):
    #     path = "/data_request/view"  # Example path
    #     params = {'issue_id': 3}  # Example parameter
    #     self.client.post(path, data=self.data, params=params, headers=self.header)

    # @task
    # def filter_test(self):
    #     path = "/profile/123123"  # Example path
    #     self.client.post(path, data=self.data, headers=self.header)
    
    # @task
    # def filter_test2(self):
    #     path = "/admin/account/create"  # Example path
        
    #     self.client.post(path, data=self.data, headers=self.header)
