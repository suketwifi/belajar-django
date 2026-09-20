from django.db import models


# =========================================================
# ASRAMA
# =========================================================

class Asrama(models.Model):

    nama = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.nama


# =========================================================
# KELAS
# =========================================================

class Kelas(models.Model):

    nama = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.nama


# =========================================================
# GURU
# =========================================================

class Guru(models.Model):

    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]

    nama = models.CharField(
        max_length=150,
        unique=True
    )

    jenis_kelamin = models.CharField(
        max_length=1,
        choices=JENIS_KELAMIN_CHOICES,
        default='L'
    )

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ['nama']
        verbose_name = 'Guru'
        verbose_name_plural = 'Guru'


# =========================================================
# PRESENSI GURU
# =========================================================

class PresensiGuru(models.Model):

    STATUS_CHOICES = [
        ('Hadir', 'Hadir'),
        ('Izin', 'Izin'),
        ('Sakit', 'Sakit'),
        ('Alpa', 'Alpa'),
    ]

    guru = models.ForeignKey(
        Guru,
        on_delete=models.CASCADE,
        related_name='presensi'
    )

    tanggal = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Alpa'
    )

    keterangan = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ['-tanggal', 'guru__nama']
        constraints = [
            models.UniqueConstraint(
                fields=['guru', 'tanggal'],
                name='unique_presensi_guru_per_tanggal'
            )
        ]

    def __str__(self):
        return f'{self.guru.nama} - {self.tanggal} - {self.status}'


# =========================================================
# SISWA
# =========================================================

class Student(models.Model):

    nama = models.CharField(
        max_length=100
    )

    nama_ayah = models.CharField(
        max_length=100,
        blank=True
    )

    nim = models.CharField(
        max_length=20,
        unique=True
    )

    jk = models.CharField(
        max_length=10
    )

    tempat_lahir = models.CharField(
        max_length=100
    )

    tanggal_lahir = models.DateField()

    alamat = models.TextField()

    no_tlpn_wa = models.CharField(
        max_length=20,
        blank=True
    )

    status = models.BooleanField(
        default=True
    )

    # Asrama lama
    asrama = models.CharField(
        max_length=100,
        blank=True
    )

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

    # Tahun ajaran
    tahun_ajaran = models.ForeignKey(
        'TahunAjaran',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )

    # Program studi
    prodi = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nama


# =========================================================
# PRESENSI SISWA
# =========================================================

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
        return f'{self.student.nama} - {self.tanggal} - {self.status}'


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
# RIWAYAT KELAS SISWA
# =========================================================

class RiwayatKelasSiswa(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='riwayat_kelas'
    )

    tahun_ajaran = models.ForeignKey(
        TahunAjaran,
        on_delete=models.PROTECT,
        related_name='riwayat_kelas_siswa'
    )

    kelas = models.ForeignKey(
        Kelas,
        on_delete=models.PROTECT,
        related_name='riwayat_siswa'
    )

    semester = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    tanggal_masuk = models.DateField(
        null=True,
        blank=True
    )

    status = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Riwayat Kelas Siswa'
        verbose_name_plural = 'Riwayat Kelas Siswa'
        ordering = [
            '-tahun_ajaran',
            'kelas__nama',
            'student__nama'
        ]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'student',
                    'tahun_ajaran'
                ],
                name='unique_student_tahun_ajaran'
            )
        ]

    def __str__(self):
        return (
            f'{self.student.nama} - '
            f'{self.kelas.nama} - '
            f'{self.tahun_ajaran.nama}'
        )


# =========================================================
# MATA PELAJARAN
# =========================================================

class MataPelajaran(models.Model):

    nama = models.CharField(
        max_length=100
    )

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

    aktif = models.BooleanField(
        default=True
    )

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

    tahun_ajaran = models.ForeignKey(
        TahunAjaran,
        on_delete=models.PROTECT,
        related_name='penilaian',
        null=True,
        blank=True
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
                    'tahun_ajaran',
                    'mata_pelajaran'
                ],
                name='unique_penilaian_student_tahun_mapel'
            )
        ]

    def __str__(self):
        return (
            f'{self.student.nama} - '
            f'{self.mata_pelajaran.nama} - '
            f'{self.tahun_ajaran.nama}'
        )

