from django.shortcuts import render

# Importa todas as classes do models.py
from .models import Musica, Estilo, Tipo

# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Importa o TemplateView para criação de páginas simples
from django.views.generic import TemplateView

# Importa o DetailView para ver detalhes de objetos
from django.views.generic.detail import DetailView

# Importa ListView para gerar as telas com tabelas
from django.views.generic.list import ListView

# Importa o Mixin para obrigar login
from django.contrib.auth.mixins import LoginRequiredMixin

# Biblioteca para controlar o acesso por grupo de usuário
from braces.views import GroupRequiredMixin

# Método que busca um objeto. Se não existir, da um erro 404
from django.shortcuts import get_object_or_404

# Create your views here.

#cria uma classe com herança de TemplateView para exibir um arquivo HTML (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    #nome do arquivo que vai ser utilizado para rederizar
    # - Esta pagina/metodo/classe
    template_name = "index.html"

class PartituraView(TemplateView):
    template_name = "partitura.html"

class videoAulaView(TemplateView):
    template_name = "videoAula.html"

class curriculoView(TemplateView):
    template_name = "curriculo.html"

##################### INSERIR ######################

class TipoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Tipo
    template_name = "aulas/formulario.html"
    success_url = reverse_lazy("listar-tipos")
    fields = ['descricao']

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Tipos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class EstiloCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = Estilo
    template_name = "aulas/formulario.html"
    success_url = reverse_lazy("listar-estilo")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(EstiloCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de nosvos Estilos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context


class MusicaCreate(LoginRequiredMixin, CreateView):
    model = Musica
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-musica")
    fields = ['tipo', 'estilo',
              'nome', 'autor', 'ano']

    def form_valid(self, form):

        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(MusicaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Musicas"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context



##################### EDITAR ######################

class TipoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Tipo
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-tipos")
    fields = ['descricao']

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(TipoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Tipo"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class EstiloUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = Estilo
    template_name = "aulas/formulario.html"
    success_url = reverse_lazy("listar-estilo")
    fields = ['descricao']

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Pedido, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(EstiloUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Estilos Musicais"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context


class MusicaUpdate(LoginRequiredMixin, UpdateView):
    model = Musica
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-musica")
    fields = ['tipo', 'estilo',
              'nome', 'autor', 'ano']

    # Altera a query para buscar o objeto do usuário logado
    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Musica, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(MusicaUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Musica"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-primary"
        return context

##################### Excluir ######################

class TipoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Tipo
    template_name = "aulas/formulario.html"
    success_url = reverse_lazy("listar-tipos")

    def get_context_data(self, *args, **kwargs):
        context = super(TipoDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class EstiloDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = Estilo
    template_name = "aulas/formulario.html"
    success_url = reverse_lazy("listar-estilo")

    def get_context_data(self, *args, **kwargs):
        context = super(EstiloDelete, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class MusicaDelete(LoginRequiredMixin, DeleteView):
    model = Musica
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-musica")



##################### Listar ######################

class TipoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Tipo
    template_name = "lista/list_tipo.html"

    def get_queryset(self):
        self.object_list = Pedido.objects.filter(usuario=self.request.user)
        return self.object_list     

class EstiloList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Estilo
    template_name = "lista/list_estilo.html"

class MusicaList(LoginRequiredMixin, ListView):
    model = Musica
    template_name = "aulas/lista/list_musica.html"

    # Altera a query padrão para buscar somente dados do usuário logado
    def get_queryset(self):
        # O object_list é o nome padrão para armazenar uma lista de objetos de um ListView
        self.object_list = Musica.objects.filter(usuario=self.request.user)
        return self.object_list


##################### Detalhar ######################

class MusicaDetalhes(DetailView):
    # Define a classe do objeto a ser detalhado
    model = Musica
    # Qual o template para essa tela
    template_name = "aulas/detalhe/musica.html"


    # Está comentado porque neste caso não faz sentido... #
    # Pegar somente se o animal for do usuário cadastrado
    '''
    def get_object(self, queryset=None):
        # Busca somente a Musica com a pk da URL que pertence ao usuário
        # Se o usuário tentar alguma pk diferente, vai dar página 404
        self.object = get_object_or_404(Animal, pk=self.kwargs['pk'], usuario=self.request.user,)
        # Retorna o objeto que será enviado ao template
        return self.object
    '''

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # Colocar mais coisas no context
        # Por exemplo: fazer um filtro em outra classe que utiliza o ID (pk)
        # do objeto que está sendo exibido, podemos fazer um filtro com ele...
        # context['itens'] = ItensVenda.objects.filter(venda=self.object)

        # self.object retorna o objeto da classe definida aqui no model = xxxx
        # self.kwargs['pk'] retorna a pk que está lá na URL

        return context
