from django.contrib import admin
from .models import *

#class BookAdmin(admin.ModelAdmin):
#            list_display = ('title', 'publisher','publication_date')
#                    list_filter = ('publication_date',)
#                            date_hierarchy = 'publication_date'
#                                    ordering = ('-publication_date',)
#                                            filter_horizontal = ('authors',)
#                                            

class DomandaInLine(admin.TabularInline):
    model=Domanda
    extra=1


class GaraAdmin(admin.ModelAdmin):
    list_display=('titolo','inizio','durata','num_domande','tipo','stato')
    ordering=('-inizio',)
    inlines=[DomandaInLine,]

class StudenteAdmin(admin.ModelAdmin):
    list_display=('get_username','get_name','squadra')
    def get_username(self,obj):
        return obj.user.username
    get_username.short_description='Username'
    def get_name(self,obj):
        return "{} {}".format(obj.user.last_name,obj.user.first_name)
    get_name.short_description='Nome'
#    ordering=('-inizio',)
#    inlines=[DomandaInLine,]


# Register your models here.

admin.site.register(Squadra)
admin.site.register(Gara,GaraAdmin)
admin.site.register(Studente, StudenteAdmin)
