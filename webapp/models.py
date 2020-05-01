from django.db import models


class speedtest_result(models.Model):
    logfile = models.FileField(default="",null=True,upload_to="file_uploads")
    token = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30)

    def __str__(self):              # figure out whats this do
        return self.timestamp