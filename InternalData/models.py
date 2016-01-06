from django.db import models


# Choices
class ChoicesBoolean(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class ChoicesAlwaysNever(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class ChoicesGoodBad(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class ChoicesEvaluation(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class ChoicesReputation(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class InterviewLocation(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class AreaOfWork(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(
        max_length=255
    )

    country = models.ForeignKey(
        Country
    )

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=255
    )

    province = models.ForeignKey(
        Province
    )

    def __unicode__(self):
        return self.name


class District(models.Model):
    name = models.CharField(
        max_length=255
    )

    city = models.ForeignKey(
        City
    )

    def __unicode__(self):
        return self.name


class RegistrationCountry(models.Model):
    name = models.CharField(
        max_length=255,
        default=None
    )

    def __unicode__(self):
        return self.name


class MembersNumber(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class BoardType(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class Sections(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class TargetAudience(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class FundTransferMethod(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class FundController(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class FinancePlanningPeriod(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class FunderType(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class FundAmount(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class ProjectDuration(models.Model):
    name = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class EventReason(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class EventResult(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class EventResponse(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


class EducationLevel(models.Model):
    name = models.CharField(
        max_length=255
    )

    def __unicode__(self):
        return self.name


