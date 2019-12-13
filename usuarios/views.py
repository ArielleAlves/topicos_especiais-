# Importa função que vai chamar as urls pelo "name" delas
from django.urls import reverse_lazy

# Importar as classes Views para inserir, alterar e excluir utilizando formulários
from django.views.generic.edit import CreateView

# Importar o modelo User e Group
from django.contrib.auth.models import User, Group

# Importar o form padrão para cadastro de usuários
from django.contrib.auth.forms import UserCreationForm

# Importar um método que da um erro 404 caso não encontre um objeto
# Ele faz a mesma coisa que: Classe.objects.get(atributo="valor")
from django.shortcuts import get_object_or_404


# Classe de criação de usuários
# Não precisa usar o model = User porque o form_class que vai definir quem são os campos desse modelo a ser inserido
class UsuarioCreate(CreateView):
    form_class = UserCreationForm
    template_name = "usuarios/form.html"
    success_url = reverse_lazy("login")

    # Método utilizado para enviar dados ao template
    def get_context_data(self, *args, **kwargs):
        context = super(UsuarioCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Usuários"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-success"
        return context

    # Iremos adicionar um grupo ao usuário cadastrado
    def form_valid(self, form):

        # Busca o grupo pelo nome "Usuario"
        # Primeiro faz a busca e depois chama o form valid para inserir o usuário normalmente
        grupo = get_object_or_404(Group, name="Usuário")

        # Executa o form_valid padrão... ele vai fazer todas as validações normais
        # Cria o objeto
        url = super().form_valid(form)

        # Se o grupo existir
        if grupo:
            # Adiciona o grupo ao usuário que foi criado nesse form
            self.object.groups.add(grupo)
            # Salva o usuário de novo
            self.object.save()

        # Retorno padrão
        return url
