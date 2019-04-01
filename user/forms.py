from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    # 自定义校验
    def clean_min_distance(self):
        clean_data = super().clean()
        min_distance = clean_data['min_distance']
        max_distance = clean_data['max_distance']
        if min_distance > max_distance:
            raise forms.ValidationError('最小距离不能大于最大距离')
        return min_distance

    def clean_min_age(self):
        clean_data = super().clean()
        min_age = clean_data['min_age']
        max_age = clean_data['max_age']
        if min_age > max_age:
            raise forms.ValidationError('最小年龄不能大于最大年龄')
        return min_age