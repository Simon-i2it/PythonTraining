from django.contrib import admin

from book_outlet.models import Address, Author, Book, Country


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        "author",
        "rating",
    )


# Register your models here.
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
