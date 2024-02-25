from django import forms

class AccessForm(forms.Form):
    code = forms.CharField(label='Enter Access Code', max_length=100)

class PuzzleForm(forms.Form):
    puzzle_answer = forms.CharField(label='Solve Puzzle', max_length=100)