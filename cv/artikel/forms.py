from django import forms

from .models import ArtikelModel

class ArtikelForm(forms.Form):
    judul = forms.CharField()

class ArtikelModelForm(forms.ModelForm):
    class Meta:
        model = ArtikelModel
        fields = ['judul', 'isi', 'image'] 


    def clean_judul(self, *args, **kwargs):
        instance = self.instance
        print(instance)
        judul = self.cleaned_data.get('judul')
        qs = ArtikelModel.objects.filter(judul__iexact=judul)
        if instance is not None: 
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Judul yang anda masukan sudah ada, silahkan masukan judul baru")
        return judul