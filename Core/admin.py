from django.contrib import admin
from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'area_of_work',
        'country',
        'province',
        'city',
        'district',
    )

    fieldsets = (
        (
            'Basic Info', {
                'fields': (
                    'enumerator_name',
                    'interview_location',
                    'interview_date',
                    'person_in_charge',
                    'position',
                )
            }
        ),
        (
            'General Info', {
                'fields': (
                    'description',
                    'name',
                    'name_en',
                    'name_i18n',
                    'short_name',
                    'director',
                    'executive',
                )
            }
        ),
        (
            'Contact Info', {
                'fields': (
                    'website',
                    'facebook',
                    'twitter',
                    'email',
                    'phone',
                    'contact_person',
                )
            }
        ),
        (
            'Office branches', {
                'fields': (
                    'area_of_work',
                    'country',
                    'province',
                    'city',
                    'district',
                )
            }
        ),
        (
            'Organization Structure', {
                'fields': (
                    'found_date',
                    'found_location',
                    'is_registered',
                    'registration_country',
                    'members_num',
                    'fulltime_num',
                    'parttime_num',
                    'volunteer_num',
                    'hr_challenge',
                    'position_training',
                    'org_training',
                    'board_check',
                    'board_type',
                    'board_female',
                    'bylaw_written',
                    'bylaw_public',
                    'bylaw_upload',
                    'regulation_check',
                    'regulation_commit',
                    'is_section',
                    'sections',
                    'evaluation_method',
                )
            }
        ),
        (
            'Work Fields & Profession', {
                'fields': (
                    'primary_section',
                    'target_audience',
                )
            }
        ),
        (
            'Financial Structure', {
                'fields': (
                    'funds_recieve',
                    'fund_send',
                    'finance_controller',
                    'finance_controlled',
                    'finance_planning',
                    'planning_period',
                    'finance_logs',
                    'funder_type',
                    'finance_monitoring',
                    'finance_external_monitoring',
                    'international_fund',
                    'fund_recieved_check',
                    'fund_recieved_type',
                    'funder_name',
                    'fund_amount',
                    'fund_challenge',
                    'funder_challenge',
                    'fund_strategies',
                )
            }
        ),
        (
            'Public Relation', {
                'fields': (
                    'local_cso_relation',
                    'local_cso_cooperation',
                    'allies',
                    'target_audience_challenge',
                    'local_auth_challgenge',
                    'security_challenge',
                    'international_partnership',
                    'international_conferences',
                    'society_impression',
                )
            }
        ),
        (
            'Projects', {
                'fields': (
                    'is_programme',
                    'project_name',
                    'province',
                    'work_field',
                    'project_staff',
                    'project_duration',
                )
            }
        ),
        (
            'Events', {
                'fields': (
                    'event_type',
                    'event_date',
                    'event_reason',
                    'event_result',
                    'event_response',
                )
            }
        ),
        (
            'Needs', {
                'fields': (
                    'activity_needed',
                    'main_needs',
                    'training_needs',
                    'needs_challenge',
                )
            }
        ),
        (
            'Organization Profile', {
                'fields': (
                    'education_level',
                    'special_skills',
                    'multiple_rel_eth',
                    'representation',
                    'underage_employee',
                    'special_employees',
                    'local_reputation',
                    'basic_reputation',
                    'strength',
                    'motives',
                )
            }
        ),
    )

admin.site.register(Organization, OrganizationAdmin)