from django.db import models

class Category(models.Model):
    """
    Represents the category for a payment.
    """

    title = models.CharField(
        "Category", max_length=50, null=False, blank=False
    )

    color = models.CharField(
        "Color", max_length=14, null=True, blank=True
    )

    slug = models.SlugField(
        unique=True,
        help_text="Suggested value automatically generated from title. Must be unique."
    )

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

    def __unicode__(self):
        return self.title

class Bill(models.Model):
    """
    Represents a payment transaction.
    """

    category = models.ForeignKey(
        Category, null=True, blank=True
    )

    payee = models.CharField(
        "Payee", max_length=50, null=False, blank=False
    )

    due_date = models.DateField(
        "Due Date", null=False, blank=False
    )

    amount_due = models.DecimalField(
        "Amount", null=False, blank=False, max_digits=19, decimal_places=2
    )

    notes = models.TextField(
        "Notes", null=True, blank=True
    )

    paid = models.BooleanField(
        "Paid", default=False
    )

    class Meta:
        ordering = ['-due_date']
        verbose_name_plural = "Bills"

    def __unicode__(self):
        return self.payee

    def get_absolute_url(self):
        return ('bills_entry_detail', (), {
            'year': self.due_date.strftime("%Y"),
            'month': self.due_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
        })

    get_absolute_url = models.permalink(get_absolute_url)
