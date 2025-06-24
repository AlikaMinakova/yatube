from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        # На основе какой модели создаётся класс формы
        model = Post
        # Укажем, какие поля будут в форме
        fields = ('text', 'group', 'image')

    # Метод-валидатор для прооверки поля text
    def clean_text(self):
        data = self.cleaned_data['text']

        # Если пользователь не поблагодарил администратора - считаем это ошибкой
        if data == '':
            raise forms.ValidationError('Пост обязательно должен содержать текст!')

        # Метод-валидатор обязательно должен вернуть очищенные данные,
        # даже если не изменил их
        return data


class CommentForm(forms.ModelForm):
    class Meta:
        # На основе какой модели создаётся класс формы
        model = Comment
        # Укажем, какие поля будут в форме
        fields = ('text',)

    # Метод-валидатор для прооверки поля text
    def clean_text(self):
        data = self.cleaned_data['text']

        # Если пользователь не поблагодарил администратора - считаем это ошибкой
        if data == '':
            raise forms.ValidationError('Пост обязательно должен содержать текст!')

        # Метод-валидатор обязательно должен вернуть очищенные данные,
        # даже если не изменил их
        return data
