from django.db import models


class Asrama(models.Model):
    nama = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama


class Kelas(models.Model):
    nama = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nama


class Student(models.Model):
    nama = models.CharField(max_length=100)
    nama_ayah = models.CharField(max_length=100, blank=True)
    nim = models.CharField(max_length=20, unique=True)
    jk = models.CharField(max_length=10)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.TextField()
    no_tlpn_wa = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)

    # Asrama lama
    asrama = models.CharField(max_length=100, blank=True)

    # Asrama master
    asrama_master = models.ForeignKey(
        Asrama,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Semester
    semester = models.PositiveIntegerField()

    # Kelas master
    kelas = models.ForeignKey(
        Kelas,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    tahun_ajaran = models.ForeignKey(
        'TahunAjaran',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )

    # Program studi
    prodi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Absensi(models.Model):
    STATUS_CHOICES = [
        ('Hadir', 'Hadir'),
        ('Izin', 'Izin'),
        ('Sakit', 'Sakit'),
        ('Alpa', 'Alpa'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='absensi'
    )

    tanggal = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Hadir'
    )

    keterangan = models.CharField(
        max_length=255,
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'tanggal'],
                name='unique_absensi_student_tanggal'
            )
        ]
        ordering = ['-tanggal']

    def __str__(self):
        return f"{self.student.nama} - {self.tanggal} - {self.status}"

# =========================================================
# TAHUN AJARAN
# =========================================================

class TahunAjaran(models.Model):
    nama = models.CharField(
        max_length=20,
        unique=True
    )

    aktif = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.nama


# =========================================================
# MATA PELAJARAN
# =========================================================

class MataPelajaran(models.Model):
    nama = models.CharField(max_length=100)

    kitab = models.CharField(
        max_length=150,
        blank=True
    )

    tahun_ajaran = models.ForeignKey(
        TahunAjaran,
        on_delete=models.CASCADE,
        related_name='mata_pelajaran'
    )

    kelas = models.ManyToManyField(
        Kelas,
        related_name='mata_pelajaran',
        blank=True
    )

    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.nama


# =========================================================
# PENILAIAN
# =========================================================

class Penilaian(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='penilaian'
    )

    mata_pelajaran = models.ForeignKey(
        MataPelajaran,
        on_delete=models.CASCADE,
        related_name='penilaian'
    )

    nilai_harian = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    nilai_ujian = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    nilai_akhir = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'student',
                    'mata_pelajaran'
                ],
                name='unique_penilaian_student_mapel'
            )
        ]

    def __str__(self):
        return (
            f"{self.student.nama} - "
            f"{self.mata_pelajaran.nama}"
        )