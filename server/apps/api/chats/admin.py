from django.contrib import admin
from .models import Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_user', 'created_at', 'updated_at')
    search_fields = ('user', 'message', 'is_user')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = (
        'user', 'message', 'is_user', 'created_at', 'updated_at'
    )
    fieldsets = (
        (None, 
            {'fields': 
                ('user', 'message', 'is_user',)
            }
        ),
        ('Timestamps', 
            {'fields': 
                ('created_at', 'updated_at')
            }
        ),
    )