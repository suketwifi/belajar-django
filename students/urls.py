from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

    # =====================================================
    # LOGIN
    # =====================================================

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='students/login.html'
        ),
        name='login'
    ),

    # =====================================================
    # LOGOUT
    # =====================================================

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # =====================================================
    # DASHBOARD
    # =====================================================

    path(
        '',
        login_required(views.dashboard),
        name='dashboard'
    ),

    path(
        'tahun-ajaran/pilih/',
        views.pilih_tahun_ajaran,
        name='pilih_tahun_ajaran'
    ),

    # =====================================================
    # DATA SISWA
    # =====================================================

    path(
        'students/',
        login_required(views.student_list),
        name='student_list'
    ),

    path(
        'students/tambah/',
        login_required(views.student_create),
        name='student_create'
    ),

    path(
        'students/import/',
        login_required(views.import_siswa),
        name='import_siswa'
    ),

    path(
        'students/export/',
        login_required(views.export_siswa),
        name='export_siswa'
    ),

    path(
        'students/download-format/',
        login_required(views.download_format_siswa),
        name='download_format_siswa'
    ),

    path(
        'students/<int:id>/',
        login_required(views.student_detail),
        name='student_detail'
    ),

    path(
        'students/<int:id>/edit/',
        login_required(views.student_edit),
        name='student_edit'
    ),

    path(
        'students/<int:id>/delete/',
        login_required(views.student_delete),
        name='student_delete'
    ),

    path(
        'students/<int:id>/histori/<int:riwayat_id>/delete/',
        login_required(views.hapus_histori_pendidikan),
        name='hapus_histori_pendidikan'
    ),

    # =====================================================
    # PRESENSI SISWA
    # =====================================================

    path(
        'presensi-siswa/',
        views.absensi,
        name='presensi_siswa'
    ),

    path(
        'presensi-siswa/rekap/',
        views.rekap_absensi,
        name='rekap_presensi_siswa'
    ),

    path(
        'absensi/rekap/cetak/',
        login_required(views.cetak_rekap_absensi),
        name='cetak_rekap_absensi'
    ),

    # =====================================================
    # KELAS
    # =====================================================

    path(
        'kelas/',
        login_required(views.data_kelas),
        name='data_kelas'
    ),

    # =====================================================
    # ASRAMA
    # =====================================================

    path(
        "asrama/",
        views.data_asrama,
        name="data_asrama"
    ),


    # =====================================================
    # MATA PELAJARAN
    # =====================================================

    path(
        'mata-pelajaran/',
        login_required(views.data_mata_pelajaran),
        name='data_mata_pelajaran'
    ),

    path(
        'mata-pelajaran/tambah/',
        login_required(views.tambah_mata_pelajaran),
        name='tambah_mata_pelajaran'
    ),

    path(
        'mata-pelajaran/<int:id>/edit/',
        login_required(views.edit_mata_pelajaran),
        name='edit_mata_pelajaran'
    ),

    path(
        'mata-pelajaran/salin/',
        login_required(views.salin_mata_pelajaran),
        name='salin_mata_pelajaran'
    ),

    # =====================================================
    # PENILAIAN
    # =====================================================

    path(
        'penilaian/',
        login_required(views.penilaian),
        name='penilaian'
    ),

    # =====================================================
    # RAPOT
    # =====================================================

    path(
        'rapot/',
        login_required(views.rapot),
        name='rapot'
    ),

    path(
        'rapot/cetak/<int:id>/',
        login_required(views.cetak_rapot_siswa),
        name='cetak_rapot_siswa'
    ),

    # =====================================================
    # DATA GURU
    # =====================================================

    path(
        'guru/',
        login_required(views.data_guru),
        name='data_guru'
    ),

    # =====================================================
    # PRESENSI GURU
    # =====================================================

    path(
        'presensi-guru/',
        login_required(views.presensi_guru),
        name='presensi_guru'
    ),

    path(
        'presensi-guru/rekap/',
        login_required(views.rekap_presensi_guru),
        name='rekap_presensi_guru'
    ),

    path(
        'presensi-guru/rekap/cetak/',
        login_required(views.cetak_rekap_presensi_guru),
        name='cetak_rekap_presensi_guru'
    ),

    # =====================================================
    # KENAIKAN SISWA
    # =====================================================

    path(
        'kenaikan-siswa/',
        login_required(views.kenaikan_siswa),
        name='kenaikan_siswa'
    ),

    # =====================================================
    # TAHUN AJARAN
    # =====================================================

    path(
        'tahun-ajaran/',
        login_required(views.tahun_ajaran),
        name='tahun_ajaran'
    ),
]