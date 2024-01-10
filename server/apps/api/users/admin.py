from django.contrib import admin
from .models import NewUser

@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    # Read only fields
    list_display = ('email', 'user_name', 'first_name', 'is_staff', 'is_superuser', 'is_verified', 'is_premium', 'is_logged_in')
    search_fields = ('email', 'user_name', 'first_name', 'last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = (
        'is_staff', 'is_superuser', 'is_active', 'is_logged_in', 'is_verified', 'is_premium', 'is_deleted'
    )
    fieldsets = (
        (None, 
            {'fields': 
                ('email', 'password', 'user_name', 'first_name', 'last_name',)
            }
        ),
        ('Roles', 
            {'fields': 
                ('is_staff', 'is_superuser')
            }
        ),
        ('Status', 
            {'fields': 
                ('is_active', 'is_logged_in', 'is_verified', 'is_premium', 'is_deleted')
            }
        ),
        ('Timestamps', 
            {'fields': 
                ('created_at', 'updated_at')
            }
        ),
    )