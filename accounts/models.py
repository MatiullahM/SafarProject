from django.db import models
from geography.models import Provinces,Terminals
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(unique=True, max_length=15, blank=True, null=True)
    password_changed_at = models.DateTimeField(blank=True, null=True)
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE, db_column='province_id', blank=True, null=True)
    terminal = models.ForeignKey(Terminals,on_delete=models.CASCADE,db_column='terminal_id', blank=True, null=True)
    account_status = models.CharField(max_length=20, choices=(
        ('active', 'Active'),
    ), default='active')
    last_login = models.DateTimeField(blank=True, null=True)
    failed_login_count = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('self', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    approved_by = models.ForeignKey('self', models.DO_NOTHING, db_column='approved_by', related_name='users_approved_by_set', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    deleted_by = models.ForeignKey('self', models.DO_NOTHING, db_column='deleted_by', related_name='users_deleted_by_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = "users"
    
    def __str__(self):
        return self.first_name + " " + self.last_name


# class Users(models.Model):
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     password_changed_at = models.DateTimeField(blank=True, null=True)
#     province = models.ForeignKey(Provinces, on_delete=models.SET_NULL, null=True, blank=True)
#     terminal = models.ForeignKey(Terminals, on_delete=models.SET_NULL, null=True, blank=True)
#     failed_login_count = models.IntegerField(blank=True, null=True)
#     created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_users')
#     approved_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_users')
#     deleted_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='deleted_users' )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted = models.BooleanField(default=False)
#     deleted_at = models.DateTimeField(blank=True, null=True)

    
#     class Meta:
#         managed = False
#         db_table = "users"



# class Modules(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.CharField(unique=True, max_length=100)
#     description = models.TextField(blank=True, null=True)
#     is_active = models.BooleanField(blank=True, null=True)
#     created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='modules_updated_by_set', blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted = models.BooleanField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     deleted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deleted_by', related_name='modules_deleted_by_set', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'modules'
    
#     def __str__(self):
#         return self.name



# class PermissionGroups(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     module = models.ForeignKey(Modules, models.DO_NOTHING)
#     is_active = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted = models.BooleanField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     deleted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'permission_groups'
    
#     def __str__(self):
#         return self.name


# class Permissions(models.Model):
#     name = models.CharField(max_length=100)
#     action = models.CharField(max_length=100)
#     slug = models.CharField(unique=True, max_length=150)
#     group = models.ForeignKey(PermissionGroups, models.DO_NOTHING)
#     is_active = models.BooleanField(blank=True, null=True)
#     created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='permissions_updated_by_set', blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted = models.BooleanField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     deleted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deleted_by', related_name='permissions_deleted_by_set', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'permissions'

#     def __str__(self):
#         return f"{self.group.module.name} - {self.group.name} - {self.name} ({self.action})"




# class RolePermissions(models.Model):
#     role = models.ForeignKey('Roles', models.DO_NOTHING)
#     permission = models.ForeignKey(Permissions, models.DO_NOTHING)
#     effect = models.TextField()  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'role_permissions'
#         unique_together = (('role', 'permission'),)
    
#     def __str__(self):
#         return f"{self.role.name} - {self.permission.name} ({self.effect})"


# class Roles(models.Model):
#     SCOPE_CHOICES = [
#     ('global', 'Global'),
#     ('province', 'Province'),
#     ('terminal', 'Terminal'),
# ]
#     name = models.CharField(max_length=100)
#     slug = models.CharField(unique=True, max_length=100)
#     scope = models.CharField(max_length=20, choices=SCOPE_CHOICES)  # This field type is a guess.
#     province_id = models.ForeignKey(Provinces, on_delete=models.CASCADE, db_column='province_id', blank=True, null=True)
#     is_active = models.BooleanField(blank=True, null=True)
#     created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', related_name='roles_updated_by_set', blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted = models.BooleanField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     deleted_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='deleted_by', related_name='roles_deleted_by_set', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'roles'

#     def __str__(self):
#         return self.name

# class UserPermissions(models.Model):
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#     permission = models.ForeignKey(Permissions, models.DO_NOTHING)
#     effect = models.TextField()  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'user_permissions'
#         unique_together = (('user', 'permission'),)

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name} - {self.permission.name} ({self.effect})"

# class UserRoles(models.Model):
#     user = models.ForeignKey(Users, models.DO_NOTHING)
#     role = models.ForeignKey(Roles, models.DO_NOTHING)
#     assigned_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='assigned_by', related_name='userroles_assigned_by_set', blank=True, null=True)
#     is_active = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user_roles'
#         unique_together = (('user', 'role'),)
    
#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name} - {self.role.name} ({'Active' if self.is_active else 'Inactive'})"






















