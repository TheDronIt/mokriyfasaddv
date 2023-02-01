from django.db import models

class Category(models.Model):
	class Meta:
		verbose_name = 'Категории'
		verbose_name_plural = 'Категории'

	Visibility_list = [
		("Отображать", "Отображать"),
		("Не отображать", "Не отображать")
	]

	Name = models.CharField(verbose_name="Название", max_length=50)
	Visibility = models.CharField(max_length=50, choices=Visibility_list,default="Отображать", verbose_name="Отображение")

	def __str__(self):
		return str(self.Name)


class ServiceImage(models.Model):
	class Meta:
		verbose_name = 'Изображения услуги'
		verbose_name_plural = 'Изображения услуги'
	Image = models.ImageField(upload_to='service/images/', blank=True)

	def __str__(self):
		return str(self.Image)


class Service(models.Model):
	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуга'

	Visibility_list = [
		("Отображать", "Отображать"),
		("Не отображать", "Не отображать")
	]

	Name = models.CharField(verbose_name="Название", max_length=50)
	Image = models.ImageField(verbose_name="Изображение", upload_to='service/')
	Images = models.ManyToManyField(ServiceImage, verbose_name="Изображения услуги", blank=True)
	Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,related_name='category_service', verbose_name="Категория")
	Description = models.TextField(blank=True, verbose_name="Описание")
	Price = models.IntegerField(verbose_name="Цена")
	Visibility = models.CharField(max_length=50, choices=Visibility_list, default="Отображать", verbose_name="Отображение")

	def __str__(self):
		return str(self.Name)


class Certificate(models.Model): 
	class Meta:
		verbose_name = 'Сертификаты'
		verbose_name_plural = 'Сертификаты'

	Visibility_list = [
		("Отображать", "Отображать"),
		("Не отображать", "Не отображать")
	]

	Name = models.CharField(verbose_name="Название", max_length=50)
	Image = models.ImageField(verbose_name="Изображение", upload_to='certificate/image/')
	File = models.FileField(upload_to='certificate/file/',null=True, verbose_name="Фаил")
	Visibility = models.CharField(max_length=50, choices=Visibility_list, default="Отображать", verbose_name="Отображение")

	def __str__(self):
		return str(self.Name)


class PortfolioImage(models.Model):
	class Meta:
		verbose_name = 'Изображения портфолио'
		verbose_name_plural = 'Изображения портфолио'
	Image = models.ImageField(upload_to='portfolio/images/', blank=True)

	def __str__(self):
		return str(self.Image)


class Portfolio(models.Model):
	class Meta:
		verbose_name = 'Портфолио'
		verbose_name_plural = 'Портфолио'

	Visibility_list = [
		("Отображать", "Отображать"),
		("Не отображать", "Не отображать")
	]

	Name = models.CharField(verbose_name="Название", max_length=50)
	Image = models.ImageField(verbose_name="Изображение", upload_to='portfolio/')
	Images = models.ManyToManyField(PortfolioImage, verbose_name="Изображения портфолио", blank=True)
	Description = models.TextField(blank=True, verbose_name="Описание")
	Wasted_time = models.CharField(blank=True, max_length=50, verbose_name="Сроки выполения")
	Price = models.IntegerField(verbose_name="Цена")
	Visibility = models.CharField(max_length=50, choices=Visibility_list, default="Отображать", verbose_name="Отображение")

	def __str__(self):
		return str(self.Name)


class Jobs(models.Model):
	class Meta:
		verbose_name = 'Вакансии'
		verbose_name_plural = 'Вакансии'

	Name = models.CharField(verbose_name="Название вакансии", max_length=50)
	Description = models.TextField(blank=True, verbose_name="Описание")
	Salary = models.IntegerField(verbose_name="Цена")

	def __str__(self):
		return str(self.Name)