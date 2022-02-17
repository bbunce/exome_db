from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.json import DataContains
from multiselectfield import MultiSelectField

patient_sex = (('female', 'Female'),
              ('male', 'Male'),
              ('unknown', 'Unknown'))

patient_gender = (('female', 'Female'),
              ('male', 'Male'),
              ('unknown', 'Unknown'))

#add to family table
patient_status = (('active', 'Active'),
                ('on_hold', 'On hold'),
                ('complete', 'Complete'))

test_type = (('trio', 'Trio'),
            ('singleton', 'Singleton'),
            ('virtual', 'Virutal'))

test_status = (('logged', 'Logged'),
            ('active', 'Active'),
            ('hold', 'Hold'),
            ('complete', 'Complete'),
            ('failed', 'Failed'),
            ('analysis_complete', 'Analysis Complete'),
            ('re_analysis', 'Re-Analysis'))

test_result = (('diag', 'Diagnosis'),
            ('likely', 'Likely diagnosis'),
            ('possible', 'Possible diagnosis'),
            ('no_diag', 'No diagnosis'))

build = (('37', 'GRCh37'),('38', 'GRCh38'))

var_type = (('miss', 'Missense'),
            ('non', 'Nonsense'),
            ('syn', 'Synonymous'),
            ('del', 'Deletion in-frame'),
            ('del_fs', 'Deletion frameshift'),
            ('dup', 'Duplication in-frame'),
            ('dup_fs', 'Duplication frameshift'),
            ('part_del', 'Partial gene deletion'),
            ('whole_del', 'Whole gene deletion'),
            ('part_dup', 'Partial gene duplication'),
            ('whole_dup', 'Whole gene duplication'),
            ('splicing', 'Splicing'),
            ('regulatory', 'Regulatory'))


class Panel(models.Model):
    panel_name = models.CharField(max_length=50)
    date_added = models.DateField()
    submitter = models.CharField(max_length=20)
    on_panelapp = models.BooleanField()

    def __str__(self):
        return f"{self.panel_name}. On panelapp: {self.on_panelapp}"

class Test(models.Model):
    panel_id = models.ForeignKey(Panel, on_delete=models.PROTECT)
    test_type = MultiSelectField(choices=test_type, default=False)
    additional_seqeuncing = models.BooleanField(default=False)

    def __str__(self):
        return self.workbatch_id

class Family(models.Model):
    family_id = models.CharField(max_length=10, unique=True)
    priority = models.BooleanField()
    urgent = models.BooleanField()
    scientist_1 = models.CharField(max_length=20, blank=False)
    scientist_2 = models.CharField(max_length=20, blank=True)
    one_hundred_k_project = models.BooleanField(default=False)
    ddd_project = models.BooleanField(default=False)
    nhse = models.BooleanField(default=False)
    nbt = models.BooleanField(default=False)
    referral_reason = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.family_id

class Family_Test(models.Model):
    workbatch_id = models.CharField(max_length=10, unique=True)
    family_id = models.ForeignKey(Family, on_delete=models.PROTECT)
    test_id = models.ForeignKey(Test, on_delete=models.PROTECT)
    test_activation_date = models.DateTimeField(blank=True)
    library_prep_date = models.DateTimeField(blank=True)
    sample_sent_date = models.DateTimeField(blank=True)
    sample_received_date = models.DateTimeField(blank=True)
    test_status = MultiSelectField(choices=test_status, default=False) 
    analysis_completion_date = models.DateTimeField(blank=True)
    analysis_time = models.TimeField(blank=True)
    average_read_depth = models.IntegerField(blank=True)
    coverage_20x = models.IntegerField(blank=True)
    variant_detected_probability = models.FloatField(blank=True)
    re_analysis_required = models.BooleanField(default=False, blank=True)
    diagnosis_after_reanalysis = models.BooleanField(default=False, blank=True) #move to families table?

    
class Patient(models.Model):
    family_id = models.ForeignKey(Family, to_field='family_id', on_delete=models.PROTECT)
    starlims_id = models.CharField(max_length=9, unique=True)
    surname = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    sex = MultiSelectField(choices=patient_sex)
    gender = MultiSelectField(choices=patient_gender)
    dob = models.DateField()
    proband = models.BooleanField(blank=False)
    nhs_number = models.IntegerField(default=0)
    exome_id = models.CharField(max_length=10, blank=True) #varchar //different from family number?
    status = MultiSelectField(choices=patient_status) #varchar // ?check active/hold or proband
    no_affected_foetuses = models.IntegerField
    currently_pregnant = models.BooleanField

    def __str__(self):
        return self.starlims_id


class Contact_Log(models.Model):
    starlims_id = models.ForeignKey(Patient, to_field='starlims_id', on_delete=models.PROTECT)
    log_date = models.DateTimeField(blank=False)
    submitter = models.CharField(max_length=10, blank=False) 
    log = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.starlims_id} - {self.log_date}"


class Variant(models.Model):
    build = MultiSelectField(choices=build, default='37', null=True)
    chromosome = models.CharField(max_length=2, blank=True, null=True)
    gene = models.CharField(max_length=100, blank=True, null=True)
    transcript = models.CharField(max_length=100, blank=True, null=True)
    genomic = models.CharField(max_length=100, blank=True, null=True)
    dna = models.CharField(max_length=100, blank=True, null=True)
    protein = models.CharField(max_length=100, blank=True, null=True)
    zygosity = models.CharField(max_length=100, blank=True, null=True)
    vus_wip = models.BooleanField(default=False)
    pubmed_ref = models.IntegerField()
    gene_matcher = models.BooleanField(default=False)
    var_prev_reported = models.CharField(max_length=100, blank=True, null=True)
    var_type = MultiSelectField(choices=var_type, blank=True, null=True)
    primary_additinal_var = models.CharField(max_length=100, blank=True, null=True)


class Clinician(models.Model):
    surname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.firstname[0]}.{self.surname} - {self.email}"    

class Clinician_Family(models.Model):
    family_id = models.ForeignKey(Family, on_delete=models.PROTECT)
    clinician_id = models.ForeignKey(Clinician, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.family_id} - {self.clinician_id}"


class Variant_Test(models.Model):
    variant_id = models.ForeignKey(Variant, on_delete=models.PROTECT)
    family_test_id = models.ForeignKey(Family_Test, on_delete=models.PROTECT)


 
