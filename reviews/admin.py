from django.contrib import admin
from django.contrib.admin import AdminSite
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class BookrAdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'

