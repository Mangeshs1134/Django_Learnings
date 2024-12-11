from django import template

register = template.Library()

@register.filter
def is_liked_by(recipe, user):
    """Check if a user has liked the recipe."""
    return recipe.isLiked(user)
