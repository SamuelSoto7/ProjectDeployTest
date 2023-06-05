from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self,email, name, idType, numID, role,  password=None, profilePicture=None, **extra_fields):
       
        
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            idType=idType,
            numID=numID,
            role=role,
            profilePicture=profilePicture,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, idType, numID, role, password,profilePicture=None,  **kwargs):
        user = self.create_user(
        email= self.normalize_email(email),
        name=name,
        idType=idType,
        numID=numID,
        role=5,
        profilePicture=profilePicture,
        password=password,
        is_superuser=True,
        **kwargs
        )
        user.is_staff= True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    def has_module_perms(self, app_label):
       return self.is_superuser
    def has_perm(self, perm, obj=None):
       return self.is_superuser
    
