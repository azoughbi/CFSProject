from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Organization, MyUser, City


class CityAdmin(admin.ModelAdmin):
    main_role = ""

    def has_add_permission(self, request, obj=None):
        if request.user.is_admin is True:
            return True

        elif request.user.is_Enumerator is True:
            return False

        elif request.user.is_AreaSupervisor is True:
            return False

        elif request.user.is_Verification is True:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_admin is True:
            return True

        elif request.user.is_Enumerator is True:
            return False

        elif request.user.is_AreaSupervisor is True:
            return False

        elif request.user.is_Verification is True:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_admin is True:
            return True

        elif request.user.is_Enumerator is True:
            return False

        elif request.user.is_AreaSupervisor is True:
            return False

        elif request.user.is_Verification is True:
            return False


class OrganizationAdmin(admin.ModelAdmin):

    main_role = ""

    def has_add_permission(self, request, obj=None):
        if request.user.is_admin is True:
            return True
        elif request.user.is_Enumerator is True:
            return True
        elif request.user.is_AreaSupervisor is True:
            return False
        elif request.user.is_Verification is True:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_admin is True:
            return True
        elif request.user.is_Enumerator is True:
            return True
        elif request.user.is_AreaSupervisor is True:
            return False
        elif request.user.is_Verification is True:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_admin is True:
            return True
        elif request.user.is_Enumerator is True:
            return True
        elif request.user.is_AreaSupervisor is True:
            return True
        elif request.user.is_Verification is True:
            return True

    list_display = (
        'name',
        'area_of_work',
        'country',
        'province',
        'city',
        'district',
    )


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'city',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords doesn't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = (
            'username',
            'email',
            'city',
            'password',
            'is_active',
            'is_admin',
            'is_Enumerator',
            'is_AreaSupervisor',
            'is_Verification'
        )

    def clean_password(self):
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username','email','is_admin','is_Enumerator','is_AreaSupervisor','is_Verification')

    list_filter = ('is_admin','is_Enumerator','is_AreaSupervisor','is_Verification')

    fieldsets = (
        (
            None, {
                'fields': (
                    'username',
                    'email',
                    'password'
                )
            }
        ),
        (
            'Personal Info', {
                'fields': (
                    'city',
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'is_admin',
                    'is_Enumerator',
                    'is_AreaSupervisor',
                    'is_Verification',
                    'groups',
                    'user_permissions'
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'username',
                    'email',
                    'city',
                    'password1',
                    'password2'
                )
            }
        ),
        (
            'Permissions', {
                'fields': (
                    'groups',
                    'user_permissions',
                )
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def has_add_permission(self, request, obj=None):
        if request.user.is_admin is True:
           return True
        elif request.user.is_Enumerator is True:
            return False
        elif request.user.is_AreaSupervisor is True:
            return False
        elif request.user.is_Verification is True:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_admin is True:
           return True
        elif request.user.is_Enumerator is True:
            return False
        elif request.user.is_AreaSupervisor is True:
            return False
        elif request.user.is_Verification is True:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_admin is True:
           return True
        elif request.user.is_Enumerator is True:
            return False
        elif request.user.is_AreaSupervisor is True:
            return False
        elif request.user.is_Verification is True:
            return False


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(City, CityAdmin)
admin.site.unregister(Group)