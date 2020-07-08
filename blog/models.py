from django.db import models

# Create your models here.title,content, image, date
class Blog(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'


"""
class Health(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'









class Education(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'





class Travel(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'






class Programming(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.title


    def snippet(self):
        return self.content[:50] + '...'






class Hardware(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'








class Networking(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'








class Politics(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title



    def snippet(self):
        return self.content[:50] + '...'







class Business(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50] + '...'







class Nutrition(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


    def snippet(self):
        return self.content[:50] + '...'






class Agriculture(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title


    def snippet(self):
        return self.content[:50] + '...'


class  lifestyle(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)
    #author

    def __str__(self):
        return self.title


    def snippet(self):
        return self.content[:50] + '...'

class   Software(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    content = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    thumb= models.ImageField(default='default.png', blank=True)
    imagesub = models.URLField(null=True)
    author = models.CharField(max_length=20, null=True)
    #author

    def __str__(self):
        return self.title


    def snippet(self):
        return self.content[:50] + '...'

class Contact(models.Model):
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=60)
    content=models.TextField()
    email=models.EmailField(max_length=254)

"""

