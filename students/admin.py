from django.contrib import admin

from .models import (
    Student,
    Asrama,
    Kelas,
    Absensi,
    TahunAjaran,
    MataPelajaran,
    Penilaian,
)


@admin.register(TahunAjaran)
class TahunAjaranAdmin(admin.ModelAdmin):
    list_display = (
        'nama',
        'aktif',
    )

    list_filter = (
        'aktif',
    )


@admin.register(MataPelajaran)
class MataPelajaranAdmin(admin.ModelAdmin):
    list_display = (
        'nama',
        'kitab',
        'tahun_ajaran',
        'daftar_kelas',
        'aktif'
    )

    list_filter = (
        'tahun_ajaran',
        'kelas',
        'aktif',
    )

    search_fields = (
        'nama',
    )

    filter_horizontal = (
        'kelas',
    )

    def daftar_kelas(self, obj):
        return ", ".join(
            kelas.nama
            for kelas in obj.kelas.all()
        )

    daftar_kelas.short_description = 'Kelas'


@admin.register(Penilaian)
class PenilaianAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'mata_pelajaran',
        'nilai_harian',
        'nilai_ujian',
        'nilai_akhir',
    )

    list_filter = (
        'mata_pelajaran__tahun_ajaran',
        'mata_pelajaran',
    )

    search_fields = (
        'student__nama',
        'student__nim',
    )


# Model yang sudah ada
admin.site.register(Student)
admin.site.register(Asrama)
admin.site.register(Kelas)
admin.site.register(Absensi)