from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    # 自定义校验
    def clean_max_distance(self):
        print('自定义校验距离')
        clean_data = super().clean()
        print(clean_data)
        min_distance = clean_data['min_distance']
        max_distance = clean_data['max_distance']
        if min_distance > max_distance:
            raise forms.ValidationError('最小距离不能大于最大距离')
        return max_distance

    def clean_max_dating_age(self):
        print('自定义校验年龄')
        clean_data = super().clean()
        print(clean_data)
        min_dating_age = clean_data['min_dating_age']
        max_dating_age = clean_data['max_dating_age']
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('最小年龄不能大于最大年龄')
        return max_dating_age
