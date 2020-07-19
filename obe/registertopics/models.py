from django.db import models


class Topic(models.Model):
	id = models.AutoField(primary_key=True)
	topic = models.CharField(max_length=30)
	SUBJECT = (
		('QuantumElectronics', 'Quantum Electronics'),
		('VLSICircuitDesignandDeviceModeling', 'VLSI Circuit Design and Device Modeling'),
		('ModernCommunicationSystems', 'Modern Communication Systems'),
		('MicrowaveElectronics', 'Microwave Electronics')
		)
	author_name = models.CharField(max_length=60, default='Pawan Kumar Mishra')
	topic_subject = models.CharField(max_length=50, choices=SUBJECT)
	keyWords = models.TextField()
	description = models.TextField()
	last_modified = models.DateTimeField(auto_now_add = True)
	image1 = models.ImageField(upload_to = "images/", blank=True)
	image2 = models.ImageField(upload_to = "images/", blank=True)
	image3 = models.ImageField(upload_to = "images/", blank=True)
	image4 = models.ImageField(upload_to = "images/", blank=True)

