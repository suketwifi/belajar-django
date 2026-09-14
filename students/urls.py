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


    # =====================================================
    # ABSENSI
    # =====================================================

    path(
        'absensi/',
        login_required(views.absensi),
        name='absensi'
    ),

    path(
        'absensi/rekap/',
        login_required(views.rekap_absensi),
        name='rekap_absensi'
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

    path(
        'kelas/tambah/',
        login_required(views.tambah_kelas),
        name='tambah_kelas'
    ),

    path(
        'kelas/<int:id>/edit/',
        login_required(views.edit_kelas),
        name='edit_kelas'
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

]