from django.urls import path
from .views import (
    FuncionariosList,
    FuncionariosEdit,
    FuncionariosDelete,
    FuncionariosNovo)


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionariosEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionariosDelete.as_view(), name='delete_funcionario'),
    path('novo/', FuncionariosNovo.as_view(), name='create_funcionario'),
]
