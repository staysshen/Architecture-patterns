class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_user_name(self, name):
        self.model.name = name

    def set_user_email(self, email):
        self.model.email = email

    def update_view(self):
        self.view.display_user(self.model)
