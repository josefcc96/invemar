from django.contrib import admin

from .models import Lugar, Especie, Avistamiento


class LugarAdmin(admin.ModelAdmin):
    list_display = ('ID', 'pais', 'departamento', 'nombre', 'alias')
    list_filter = ('pais', 'departamento', 'nombre', 'alias')

    def ID(self, obj):
        return '{}'.format(obj.pk)
    # ordering = ('nombre')


class AvistamientoAdmin(admin.ModelAdmin):
    list_display = ('ID', 'post_especie', 'lugar', 'latitud',
                    'longitud', 'autor', 'observación')
    # ordering = ('autor')
    search_fields = ('lugar__nombre', 'especie__n_comun', 'autor')
    list_filter = ('especie__n_comun', 'lugar__nombre', 'autor')

    def ID(self, obj):
        return '{}'.format(obj.pk)

    def post_especie(self, obj):
        return ' , '.join(
            [p.get_Esp() for p in obj.especie.all()])
    post_especie.short_description = "Especies (Nombres Comunes)"


class EspecieAdmin(admin.ModelAdmin):
    list_display = ('ID', 'n_comun', 'n_cientifico', 'familia')
    list_filter = ('n_comun', 'n_cientifico', 'familia')

    def ID(self, obj):
        return '{}'.format(obj.pk)
    # ordering = ('n_comun')


admin.site.register(Lugar, LugarAdmin)
admin.site.register(Especie, EspecieAdmin)
admin.site.register(Avistamiento, AvistamientoAdmin)
