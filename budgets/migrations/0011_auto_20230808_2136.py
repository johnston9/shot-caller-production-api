# Generated by Django 3.2.15 on 2023-08-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0010_budget_fringes_taxes_development'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='armorer_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='armorer_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='armorer_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='armorer_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='armorer_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_assistants_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_assistants_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_assistants_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_assistants_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_director_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_director_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_director_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='art_director_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='artassistants_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='artdirector_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_property_master_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_property_master_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_property_master_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_property_master_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_set_decorator_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_set_decorator_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_set_decorator_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assist_set_decorator_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assistdecoratorset_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='assistpropertymaster_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='carpenters_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='carpenters_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='carpenters_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='carpenters_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='carpenters_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='constructioncoordinator_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='constructioncoordinator_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='constructioncoordinator_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='constructioncoordinator_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='constructioncoordinator_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='constructionlabour_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='decoratorset_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='designlabour_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='dressers_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='dressingbuyer_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='dressinglabour_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='graphic_artists_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='graphic_artists_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='graphic_artists_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='graphic_artists_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='graphicartists_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='head_wrangler_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='head_wrangler_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='head_wrangler_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='head_wrangler_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headcarpenter_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headcarpenter_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headcarpenter_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headcarpenter_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headcarpenter_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headpainter_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headpainter_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headpainter_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headpainter_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headpainter_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='headwrangler_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='labourers_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='labourers_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='labourers_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='labourers_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='labourers_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='lead_man_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='lead_man_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='lead_man_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='lead_man_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='leadman_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='on_set_props_person_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='on_set_props_person_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='on_set_props_person_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='on_set_props_person_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='onsetpropsperson_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_construction',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_design',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_property',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_set_dressing',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_wrangling_labour_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_wrangling_labour_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_wrangling_labour_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='other_wrangling_labour_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='otherwranglinglabour_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='painters_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='painters_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='painters_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='painters_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='painters_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_assistants_trainees_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_assistants_trainees_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_assistants_trainees_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_assistants_trainees_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_designer_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_designer_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_designer_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='production_designer_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='productionassistantstrainees_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='productiondesigner_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_buyer_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_buyer_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_buyer_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_buyer_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_master_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_master_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_master_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='property_master_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='propertybuyer_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='propertylabour_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='propertymaster_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='scenicpainters_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='scenicpainters_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='scenicpainters_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='scenicpainters_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='scenicpainters_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_decorator_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_decorator_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_decorator_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_decorator_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressers_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressers_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressers_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressers_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressing_buyer_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressing_buyer_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressing_buyer_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='set_dressing_buyer_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='swing_gang_quantity',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='swing_gang_rate',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='swing_gang_units_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='swing_gang_units_number',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='swinggang_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget',
            name='wranglerlabour_total',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]