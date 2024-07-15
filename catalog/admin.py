from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# register book Model using decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")

# admin.site.register(Book, BookAdmin)


# define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

# admin.site.register(BookInstance, BookInstanceAdmin)

admin.site.register(Language)
