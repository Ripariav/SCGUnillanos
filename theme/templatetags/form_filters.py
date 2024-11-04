from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    # Verificar si el valor es un campo de formulario
    if hasattr(field, 'field'):
        # Obtener los atributos actuales del widget
        attrs = field.field.widget.attrs.copy()
        # Añadir la nueva clase CSS
        if 'class' in attrs:
            attrs['class'] += f' {css_class}'  # Concatenar la nueva clase
        else:
            attrs['class'] = css_class
        # Devolver el widget con los nuevos atributos
        return field.as_widget(attrs=attrs)
    else:
        # Si el valor no es un campo de formulario, simplemente lo devuelve tal cual
        return field
