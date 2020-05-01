from django.db import models

class speedtest_result(models.Model):
    file = models.FileField(default="",null=True,upload_to="file_uploads")
    date = models.CharField(max_length=30)
    download = models.DecimalField(decimal_places=5,max_digits=10)
    upload = models.DecimalField(decimal_places=5,max_digits=10)

    def __str__(self):              # figure out whats this do
        return self.date