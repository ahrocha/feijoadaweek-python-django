from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, default='')
    imagem = models.CharField(max_length=500, null=True, blank=True)
    enable_comments = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    @property
    def has_html_content(self):
        content = self.content or ''
        return content != strip_tags(content)


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'ip_address')
        indexes = [
            models.Index(fields=['post', 'ip_address']),
            models.Index(fields=['post', 'created_at']),
        ]

    def __str__(self):
        return f"Like on {self.post.title} from {self.ip_address}"

class Local(Post):
    # 1. O endereço completo que a API do Google Maps vai "ler" ou "retornar"
    endereco_completo = models.CharField(
        max_length=255, 
        help_text="Ex: Av. Paulista, 900 - Bela Vista, São Paulo - SP, 01310-100"
    )
    
    # 2. Coordenadas exatas (Essenciais! O mapa se move baseado nelas, não no texto)
    # Usamos DecimalField em vez de FloatField para maior precisão geográfica
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # 3. Google Place ID (Altamente recomendado para Google Maps)
    # O Google gera um ID único para cada estabelecimento. Salvar isso evita que você
    # gaste dinheiro re-buscando o local na API toda vez que o usuário abrir a página.
    place_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
    
    # 4. Componentes separados (Facilita se você quiser filtrar locais por Cidade ou Estado depois)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=50, blank=True) # Ou um CharField menor para a sigla (ex: max_length=2)
    pais = models.CharField(max_length=100, default="Brasil")

    def __str__(self):
        return f"{self.title} ({self.cidade} - {self.estado})"
