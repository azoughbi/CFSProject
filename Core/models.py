from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import dispatcher
from django.db.models import signals
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from crum import get_current_user

main_role = ""
content_role_type = ""
content_city_type = ""
dont_send_counter = ""


class City(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


# Organization Model
class Organization(models.Model):
    # Basic Info
    enumerator_name = models.ForeignKey(
        'MyUser',
        to_field='username',
        blank=True,
        null=True,
        default=None,
    )

    interview_date = models.DateField()

    interview_location = models.ForeignKey(
        'InternalData.InterviewLocation',
        related_name="+"
    )

    first_review = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    second_review = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    person_in_charge = models.CharField(
        max_length=255
    )

    position = models.ForeignKey(
        'InternalData.Position',
        related_name="+"
    )

    # General Info

    name = models.CharField(
        max_length=255
    )

    description = models.TextField()

    name_en = models.CharField(
        max_length=255
    )

    name_i18n = models.CharField(
        max_length=255
    )

    short_name = models.CharField(
        max_length=255
    )

    director = models.CharField(
        max_length=255
    )

    executive = models.CharField(
        max_length=255
    )

    # Contact Info

    website = models.URLField()

    facebook = models.URLField()

    twitter = models.URLField()

    email = models.EmailField()

    phone = models.IntegerField()

    contact_person = models.CharField(
        max_length=255
    )

    # Office branches

    area_of_work = models.ForeignKey(
        'InternalData.AreaOfWork',
        related_name="+"
    )

    country = models.ForeignKey(
        'InternalData.Country',
        related_name="+"
    )

    province = models.ForeignKey(
        'InternalData.Province',
        related_name="+"
    )

    city = models.ForeignKey(
        'InternalData.City',
        related_name="+"
    )

    district = models.ForeignKey(
        'InternalData.District',
        related_name="+"
    )

    # Organization Structure

    found_date = models.DateField()

    found_location = models.CharField(
        max_length=255
    )

    is_registered = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    registration_country = models.ForeignKey(
        'InternalData.RegistrationCountry',
        related_name="+"
    )

    members_num = models.ForeignKey(
        'InternalData.MembersNumber',
        related_name="+"
    )

    fulltime_num = models.ForeignKey(
        'InternalData.MembersNumber',
        related_name="+"
    )

    parttime_num = models.ForeignKey(
        'InternalData.MembersNumber',
        related_name="+"
    )

    volunteer_num = models.ForeignKey(
        'InternalData.MembersNumber',
        related_name="+"
    )

    hr_challenge = models.ForeignKey(
            'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    position_training = models.IntegerField()

    org_training = models.IntegerField()

    board_check = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    board_type = models.ForeignKey(
        'InternalData.BoardType',
        related_name="+"
    )

    board_female = models.ForeignKey(
        'InternalData.MembersNumber',
        related_name="+"
    )

    bylaw_written = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    bylaw_public = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    bylaw_upload = models.FileField()

    regulation_check = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    regulation_commit = models.ForeignKey(
            'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    is_section = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    sections = models.ManyToManyField(
        'InternalData.Sections',
        related_name="+"
    )

    evaluation_method = models.ForeignKey(
        'InternalData.ChoicesEvaluation',
        related_name="+"
    )

    # Work Fields & Profession

    primary_section = models.ForeignKey(
        'InternalData.Sections',
        related_name="+"
    )

    target_audience = models.ManyToManyField(
        'InternalData.TargetAudience'
    )

    # Financial Structure

    funds_recieve = models.ForeignKey(
        'InternalData.FundTransferMethod',
        related_name="+"
    )

    fund_send = models.ForeignKey(
        'InternalData.FundTransferMethod',
        related_name="+"
    )

    finance_controller = models.ForeignKey(
        'InternalData.FundController'
    )

    finance_controlled = models.ForeignKey(
            'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    finance_planning = models.ForeignKey(
            'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    planning_period = models.ForeignKey(
        'InternalData.FinancePlanningPeriod'
    )

    finance_logs = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    funder_type = models.ForeignKey(
        'InternalData.FunderType',
        related_name="+"
    )

    finance_monitoring = models.ForeignKey(
            'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    finance_external_monitoring = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    international_fund = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    fund_recieved_check = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    fund_recieved_type = models.ForeignKey(
        'InternalData.FunderType',
        related_name="+"
    )

    funder_name = models.CharField(
        max_length=255
    )

    fund_amount = models.ForeignKey(
        'InternalData.FundAmount',
        related_name="+"
    )

    fund_challenge = models.ForeignKey(
            'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    funder_challenge = models.ForeignKey(
            'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    fund_strategies = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    # Public Relations

    local_cso_relation = models.ForeignKey(
        'InternalData.ChoicesGoodBad',
        related_name="+"
    )

    local_cso_cooperation = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    allies = models.CharField(
        max_length=255
    )

    target_audience_challenge = models.ForeignKey(
        'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    local_auth_challgenge = models.ForeignKey(
        'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    security_challenge = models.ForeignKey(
        'InternalData.ChoicesAlwaysNever',
        related_name="+"
    )

    international_partnership = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    international_conferences = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    society_impression = models.ForeignKey(
        'InternalData.ChoicesGoodBad',
        related_name="+"
    )

    # Projects

    is_programme = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    project_name = models.CharField(
        max_length=255
    )

    province = models.ForeignKey(
        'InternalData.Province',
        related_name="+"
    )

    work_field = models.ForeignKey(
        'InternalData.Sections',
        related_name="+"
    )

    project_staff = models.ForeignKey(
        'InternalData.MembersNumber',
        related_name="+"
    )

    project_duration = models.ForeignKey(
        'InternalData.ProjectDuration',
        related_name="+"
    )

    # Events

    event_type = models.ForeignKey(
        'InternalData.EventType'
    )

    event_date = models.DateField()

    event_reason = models.ForeignKey(
        'InternalData.EventReason'
    )

    event_result = models.ForeignKey(
        'InternalData.EventResult'
    )

    event_response = models.ForeignKey(
        'InternalData.EventResponse'
    )

    # Needs

    activity_needed = models.CharField(
        max_length=255
    )

    main_needs = models.CharField(
        max_length=255
    )

    training_needs = models.CharField(
        max_length=255
    )

    needs_challenge = models.CharField(
        max_length=255
    )

    # Organization Profile

    education_level = models.ForeignKey(
        'InternalData.EducationLevel'
    )

    special_skills = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    multiple_rel_eth = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    representation = models.ForeignKey(
        'InternalData.ChoicesGoodBad',
        related_name="+"
    )

    underage_employee = models.ForeignKey(
        'InternalData.ChoicesBoolean',
        related_name="+"
    )

    special_employees = models.ForeignKey(
        'InternalData.MembersNumber',
        related_name="+"
    )

    local_reputation = models.ForeignKey(
        'InternalData.ChoicesReputation',
        related_name="+"
    )

    basic_reputation = models.ForeignKey(
        'InternalData.ChoicesReputation',
        related_name="+"
    )

    strength = models.ForeignKey(
        'InternalData.ChoicesReputation',
        related_name="+"
    )

    motives = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):

        global content_role_type
        global main_role
        global content_city_type

        user = get_current_user()

        if main_role=="is_Enumerator" or main_role=="is_admin":
            self.roles_type=content_role_type
            self.city_type=content_city_type
            if self.Send=="Do not send":
                self.Send=main_role
            else:
                pass

        elif main_role=="is_AreaSupervisor" or main_role=="is_admin":
            self.roles_type==content_role_type
            self.city_type=content_city_type
            if self.Send=="Do not send":
                self.Send=main_role
            else:
                pass

        elif main_role=="is_Verification" or main_role=="is_admin":
            self.roles_type==content_role_type
            self.city_type=content_city_type
            if self.Send=="Do not send":
                self.Send=main_role
            else:
                pass

        if user and not user.pk:
            user = None
        if not self.pk:
            self.enumerator_name = user
        super(Organization, self).save(*args, **kwargs)

    # User roles

    roles_type = models.CharField(
        max_length=255,
        editable=False
    )

    city_type = models.CharField(
        max_length=255,
        editable=False
    )

    Send = models.CharField(
        max_length=50,
        choices=(
            ("send to Area Supervisor","Send to Area Supervisor"),
            ("Do not send","Do not Send")
        )
    )

    class Meta:
        permissions = (
            ('View_content', 'View Organization'),
        )

    def __init__(self, *args, **kwargs):
        global main_role
        super(Organization, self).__init__(*args, **kwargs)

        if main_role == "is_Enumerator":
            self._meta.get_field_by_name('Send')[0]._choices=(("send to Area Supervisor","Send to Area Supervisor"),("Do not send","Do not Send"))
        elif main_role=="is_AreaSupervisor":
            self._meta.get_field_by_name('Send')[0]._choices=(("send to Enumerator","Send to Enumerator"),("send to Verification","Send to Verification"),("Do not send","Do not Send"))
        elif main_role=="is_Verification":
            self._meta.get_field_by_name('Send')[0]._choices=(("send to Area Supervisor","Send to Area Supervisor"),("Do not send","Do not Send"))
        elif main_role=="is_admin":
            self._meta.get_field_by_name('Send')[0]._choices=(("send to Area Supervisor","Send to Area Supervisor"),("send to Verification","Send to Verification"),("send to Enumerator","Send to Enumerator"),("Do not send","Do not Send"))

    @classmethod
    def from_db(cls, db, field_names, values):

        global main_role
        global content_role_type
        global content_city_type

        if cls._deferred:
            instance = cls(**zip(field_names, values))
        else:

            if main_role=="is_admin":
                instance = cls(*values)
            elif main_role=="is_Enumerator":
                if cls(*values).Send=="send to Enumerator" or cls(*values).Send=="is_Enumerator":
                    if cls(*values).roles_type==content_role_type:
                        instance = cls(*values)
                    else:
                        instance = cls(values)
                else:
                    instance = cls(values)
            elif main_role=="is_AreaSupervisor":
                if cls(*values).Send=="send to Area Supervisor" or cls(*values).Send=="is_AreaSupervisor":
                    if content_city_type==cls(*values).city_type:
                        instance = cls(*values)
                    else:
                        instance = cls(values)
                else:
                    instance = cls(values)
            elif main_role=="is_Verification":
                if cls(*values).Send=="send to Verification" or cls(*values).Send=="is_Verification":
                    if content_city_type==cls(*values).city_type:
                        instance = cls(*values)
                    else:
                        instance = cls(values)
                else:
                    instance = cls(values)
        #instance._state.adding = False
        #instance._state.db = db
        # customization to store the original field values on the instance
        #instance._loaded_values = dict(zip(field_names, values))
        return instance

    def clean(self):
        global main_role

        if (main_role == "is_Enumerator" and self.Send == "send to Verification") or (main_role == "is_Enumerator" and self.Send == "send to Enumerator"):
            raise ValidationError(_('You are Enumerator Please send the request to Area Supervisor only.'))
        elif main_role == "is_AreaSupervisor" and self.Send == "send to Area Supervisor":
            raise ValidationError(_('You are Area Supervisor Please send the request to Verification and Enumerator only.'))
        elif (main_role == "is_Verification" and self.Send == "send to Verification") or (main_role == "is_Verification" and self.Send == "send to Enumerator"):
            raise ValidationError(_('You are Verification Please send the request to Area Supervisor only.'))


class MyUserManager(BaseUserManager):
    def create_user(self,username,city,password=None):
        #print "createusers"
        """
        Creates and saves a User with the given email, date ofs
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            #email=self.normalize_email(email),
            username=username,
            city_id=city,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,city,password):
        #print city
        #print "supersuers"
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
            city=city
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser,PermissionsMixin):
    #global main_role=""
    #print "Myuser"
    #MyUser.dont_send_counter=""
    username = models.CharField(
        verbose_name='UserName',
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    city=models.ForeignKey(City)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_Enumerator= models.BooleanField(default=False)
    is_AreaSupervisor= models.BooleanField(default=False)
    is_Verification= models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['city',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        global main_role
        global content_city_type
        global dont_send_counter
        global content_role_type
        content_role_type=self.email
        content_city_type=str(self.city_id)
        #print "is staff"
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        if self.is_Enumerator==True:
            dont_send_counter="enumeratordontsend"
            main_role="is_Enumerator"
            return self.is_Enumerator
        elif self.is_AreaSupervisor==True:
            dont_send_counter="areasupervisordontsend"
            main_role="is_AreaSupervisor"
            return self.is_AreaSupervisor
        elif self.is_Verification==True:
            dont_send_counter="verificationdontsend"
            main_role="is_Verification"
            return self.is_Verification
        else:
            dont_send_counter="admindontsend"
            main_role="is_admin"
            return self.is_admin
    """class Meta:
        permissions = (("can_view_article", "Can view article"),
                       ("can_add_article", "Can add article"),("can_edit_article", "Can edit article"),("can_delete_article", "Can delete article"),)"""
    """@property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_Enumerator"""

#register_custom_permissions_simple((("is_Area Supervisor", "User is Area Supervisor"),))