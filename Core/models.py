from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user


# Create your models here.
class Organization(models.Model):
    # Basic Info
    enumerator_name = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=None
    )

    interview_date = models.DateField(
    )

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
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.enumerator_name = user
        super(Organization, self).save(*args, **kwargs)

