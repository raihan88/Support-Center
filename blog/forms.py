
from django import forms 
from .models import Post,Comment


STATUS = (
    (0,"Hidden"),
    (1,"Publish")
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('question' , 'author', 'answer','status')

        widgets = {
            'question':forms.TextInput(attrs={'class':'form-control','placeholder':'Write your question here...'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'userid', 'type':'hidden'}),
            'answer':forms.Textarea(attrs={'class':'form-control','placeholder':'Write the answer of the question...'}),
            # 'status':forms.CharField(label='Publish your answer', widget=forms.Select(choices=STATUS, attrs={'class':'form-control'}))
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('question', 'answer', 'status')

        widgets = {
            'question':forms.TextInput(attrs={'class':'form-control','placeholder':'Write your question here...'}),
            'answer':forms.Textarea(attrs={'class':'form-control','placeholder':'Write the answer of the question...'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Write your name or make yourself anonymous'}),
            'comment':forms.Textarea(attrs={'class':'form-control','placeholder':'Write the comment without any hesitation...'}),
        }

 
class AskForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('question', 'author')

        widgets = {
            'question':forms.Textarea(attrs={'class':'form-control','placeholder':'Write your question here...'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'userid', 'type':'hidden'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('question', 'answer', 'status')

        widgets = {
            'question':forms.TextInput(attrs={'class':'form-control','placeholder':'Write your question here...'}),
            'answer':forms.Textarea(attrs={'class':'form-control','placeholder':'Write the answer of the question...'})
        }

