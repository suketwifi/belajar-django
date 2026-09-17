from django.contrib import admin

from .models import (
    Student,
    Asrama,
    Kelas,
    Absensi,
    Guru,
    PresensiGuru,
    TahunAjaran,
    MataPelajaran,
    Penilaian,
)


# =========================================================
# DATA SISWA
# =========================================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'nim',
        'jk',
        'kelas',
        'asrama_master',
        'semester',
        'prodi',
        'status',
    )

    list_filter = (
        'jk',
        'kelas',
        'asrama_master',
        'semester',
        'prodi',
        'status',
    )

    search_fields = (
        'nama',
        'nim',
    )

    ordering = (
        'nama',
    )


# =========================================================
# ASRAMA
# =========================================================

@admin.register(Asrama)
class AsramaAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
    )

    search_fields = (
        'nama',
    )

    ordering = (
        'nama',
    )


# =========================================================
# KELAS
# =========================================================

@admin.register(Kelas)
class KelasAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
    )

    search_fields = (
        'nama',
    )

    ordering = (
        'nama',
    )


# =========================================================
# PRESENSI SISWA
# =========================================================

@admin.register(Absensi)
class AbsensiAdmin(admin.ModelAdmin):

    list_display = (
        'tanggal',
        'student',
        'status',
        'keterangan',
    )

    list_filter = (
        'tanggal',
        'status',
    )

    search_fields = (
        'student__nama',
        'student__nim',
    )

    ordering = (
        '-tanggal',
        'student__nama',
    )


# =========================================================
# TAHUN AJARAN
# =========================================================

@admin.register(TahunAjaran)
class TahunAjaranAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'aktif',
    )

    list_filter = (
        'aktif',
    )

    search_fields = (
        'nama',
    )

    ordering = (
        '-aktif',
        'nama',
    )


# =========================================================
# MATA PELAJARAN
# =========================================================

@admin.register(MataPelajaran)
class MataPelajaranAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'kitab',
        'tahun_ajaran',
        'daftar_kelas',
        'aktif',
    )

    list_filter = (
        'tahun_ajaran',
        'kelas',
        'aktif',
    )

    search_fields = (
        'nama',
        'kitab',
    )

    filter_horizontal = (
        'kelas',
    )

    ordering = (
        'nama',
    )

    @admin.display(description='Kelas')
    def daftar_kelas(self, obj):
        return ", ".join(
            kelas.nama
            for kelas in obj.kelas.all()
        )


# =========================================================
# PENILAIAN
# =========================================================

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
        'mata_pelajaran__nama',
    )

    ordering = (
        'student__nama',
        'mata_pelajaran__nama',
    )


# =========================================================
# DATA GURU
# =========================================================

@admin.register(Guru)
class GuruAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'jenis_kelamin',
    )

    list_filter = (
        'jenis_kelamin',
    )

    search_fields = (
        'nama',
    )

    ordering = (
        'nama',
    )


# =========================================================
# PRESENSI GURU
# =========================================================

@admin.register(PresensiGuru)
class PresensiGuruAdmin(admin.ModelAdmin):

    list_display = (
        'tanggal',
        'guru',
        'status',
        'keterangan',
    )

    list_filter = (
        'tanggal',
        'status',
    )

    search_fields = (
        'guru__nama',
    )

    ordering = (
        '-tanggal',
        'guru__nama',
    )