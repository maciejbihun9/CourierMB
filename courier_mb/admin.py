from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission

admin.site.register(Permission)

permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )