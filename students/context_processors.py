from .models import TahunAjaran


def tahun_ajaran_global(request):

    tahun_ajaran_aktif = None

    tahun_ajarans = (
        TahunAjaran.objects
        .all()
        .order_by('-id')
    )

    if request.user.is_authenticated:

        tahun_ajaran_id = request.session.get(
            'tahun_ajaran_id'
        )

        if tahun_ajaran_id:

            tahun_ajaran_aktif = (
                TahunAjaran.objects.filter(
                    id=tahun_ajaran_id
                ).first()
            )

        if tahun_ajaran_aktif is None:

            tahun_ajaran_aktif = (
                TahunAjaran.objects.filter(
                    aktif=True
                ).first()
            )

    return {
        'tahun_ajaran_aktif': tahun_ajaran_aktif,
        'tahun_ajarans': tahun_ajarans,
    }