from workspace.models import Rol

def user_role(request):
    """
    Context processor para añadir el rol del usuario al contexto de todas las plantillas.
    """
    if request.user.is_authenticated:
        # Obtén el rol del usuario si está autenticado
        rol = Rol.objects.filter(usuario=request.user).first()
        return {'rol': rol}
    
    # Si el usuario no está autenticado, devolvemos un rol nulo
    return {'rol': None}
