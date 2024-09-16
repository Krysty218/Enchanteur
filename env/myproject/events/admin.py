from django.contrib import admin
from .models import Event, Ticket, Wishlist
# Register your models here.
# Register Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time', 'location', 'hosted_by')
    search_fields = ('title', 'category', 'location')

# Register Ticket model
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'quantity')
    search_fields = ('user__username', 'event__title')

# Register Wishlist model
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    search_fields = ('user__username', 'event__title')
