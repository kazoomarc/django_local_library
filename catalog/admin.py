from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# register book Model using decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")
    inlines = [BooksInstanceInline]


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


# define the admin class


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = [("first_name", "last_name"), ("date_of_birth", "date_of_death")]
    inlines = [BookInline]


admin.site.register(Genre)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back", "id")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {"fields": ("book", "imprint", "id")}),
        ("Availability", {"fields": ("status", "due_back", "borrower")}),
    )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
