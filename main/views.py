from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406432425',
        'nama' : 'Jarred Muhammad Radithya',
        'kelas' : 'PBP D',
        'nama_produk' : 'Adizero Evo SL',
        'harga' : 2700000,
        'kategori': 'Sepatu Running',
        'deskripsi': 'Sepatu yang ringan dan nyaman jika digunakan untuk lari'
    }

    return render(request, "main.html", context)

# Create your views here.
